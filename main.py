import pygame as pg
import moderngl as mgl
import sys

from model import *
from camera import Camera


class GraphicEngine: # 2 50
	def __init__(self, win_size=(1280, 720)):
		pg.init()
		self.WIN_SIZE = win_size
		pg.display.gl_set_attribute(pg.GL_CONTEXT_MAJOR_VERSION, 3)
		pg.display.gl_set_attribute(pg.GL_CONTEXT_MINOR_VERSION, 3)
		pg.display.gl_set_attribute(pg.GL_CONTEXT_PROFILE_MASK, pg.GL_CONTEXT_PROFILE_CORE)
		pg.display.set_mode(self.WIN_SIZE, flags=pg.OPENGL | pg.DOUBLEBUF)
		self.ctx = mgl.create_context()
		self.clock = pg.time.Clock()
		# Scene
		self.camera = Camera(self)
		self.scene = Cube(self)

	def quit(self):
		self.scene.destroy()
		pg.quit()
		sys.exit()

	def check_events(self):
		for event in pg.event.get():
			if event.type == pg.QUIT:
				self.quit()
			elif event.type == pg.KEYDOWN:
				if event.key == pg.K_ESCAPE:
					self.quit()

	def render(self):
		self.ctx.clear(color=(0.08, 0.16, 0.18))
		self.scene.render()
		pg.display.flip()
	
	def run(self):
		while True:
			self.check_events()
			self.render()
			self.clock.tick(60)


if __name__ == '__main__':
	app = GraphicEngine()
	app.run()
