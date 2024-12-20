import math
import os
import sys

import glm
import moderngl
import pygame
import numpy as np
from objloader import Obj
from PIL import Image

os.environ['SDL_WINDOWS_DPI_AWARENESS'] = 'permonitorv2'

pygame.init()
pygame.display.set_mode((800, 800), flags=pygame.OPENGL | pygame.DOUBLEBUF, vsync=True)


class ImageTexture:
    def __init__(self, path):
        self.ctx = moderngl.get_context()

        img = Image.open(path).convert('RGBA')
        img = img.resize((512, 512))
        self.texture = self.ctx.texture(img.size, 4, img.tobytes())
        self.sampler = self.ctx.sampler(texture=self.texture)
        self.texture.repeat_x = True
        self.texture.repeat_y = True


    def use(self):
        self.sampler.use()


class ModelGeometry:
    def __init__(self, path):
        self.ctx = moderngl.get_context()

        obj = Obj.open(path)
        self.vbo = self.ctx.buffer(obj.pack('vx vy vz nx ny nz tx ty'))

    def vertex_array(self, program):
        return self.ctx.vertex_array(program, [(self.vbo, '3f 12x 2f', 'in_vertex', 'in_uv')])


class Mesh:
    def __init__(self, program, geometry, texture=None):
        self.ctx = moderngl.get_context()
        self.vao = geometry.vertex_array(program)
        self.texture = texture

    def render(self, position, color, scale):
        self.vao.program['use_texture'] = False

        if self.texture:
            self.vao.program['use_texture'] = True
            self.texture.use()

        self.vao.program['position'] = position
        self.vao.program['color'] = color
        self.vao.program['scale'] = scale
        self.vao.render()


class Scene:
    def __init__(self):
        self.ctx = moderngl.get_context()

        self.program = self.ctx.program(
            vertex_shader='''
                #version 330 core

                uniform mat4 camera;
                uniform vec3 position;
                uniform float scale;
                uniform mat2 uv_transform; // Matriz para transformar las coordenadas UV

                layout (location = 0) in vec3 in_vertex;
                layout (location = 1) in vec3 in_normal;
                layout (location = 2) in vec2 in_uv;

                out vec3 v_vertex;
                out vec3 v_normal;
                out vec2 v_uv;

                void main() {
                    v_vertex = position + in_vertex * scale;
                    v_normal = in_normal;
                    v_uv = uv_transform * in_uv; // Aplicar transformación
                    gl_Position = camera * vec4(v_vertex, 1.0);
                }

            ''',
            fragment_shader='''
                #version 330 core

                uniform sampler2D Texture;
                uniform bool use_texture;
                uniform vec3 color;

                in vec3 v_vertex;
                in vec3 v_normal;
                in vec2 v_uv;

                layout (location = 0) out vec4 out_color;

                void main() {
                    out_color = vec4(color, 1.0);
                    if (use_texture) {
                        out_color *= texture(Texture, v_uv);
                    }
                }
            ''',
        )

        self.texture = ImageTexture('tecLogo.jpg')

        self.car_geometry = ModelGeometry('lowpoly_toy_car.obj')
        self.car = Mesh(self.program, self.car_geometry)

        self.crate_geometry = ModelGeometry('crate.obj')
        self.crate = Mesh(self.program, self.crate_geometry, self.texture)

    def camera_matrix(self):
        now = pygame.time.get_ticks() / 1000.0
        eye = (math.cos(now), math.sin(now), 0.5)
        proj = glm.perspective(45.0, 1.0, 0.1, 1000.0)
        look = glm.lookAt(eye, (0.0, 0.0, 0.0), (0.0, 0.0, 1.0))
        return proj * look

    def render(self):
        camera = self.camera_matrix()

        self.ctx.clear()
        self.ctx.enable(self.ctx.DEPTH_TEST)

        self.program['camera'].write(camera)

        self.car.render((-0.4, 0.0, 0.0), (1.0, 0.0, 0.0), 0.2)
        self.crate.render((0.0, 0.0, 0.0), (1.0, 1.0, 1.0), 0.2)
        self.car.render((0.4, 0.0, 0.0), (0.0, 0.0, 1.0), 0.2)

scene = Scene()

# Rotar la textura 180 grados
angle = np.radians(180)
cos_a, sin_a = np.cos(angle), np.sin(angle)
uv_transform = np.array([
    [cos_a, -sin_a],
    [sin_a, cos_a]
], dtype='f4')

scene.program['uv_transform'].write(uv_transform)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    scene.render()

    pygame.display.flip()
