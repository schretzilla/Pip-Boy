from kivy.app import App
from kivy.uix.widget import Widget

from kivy.uix.camera import Camera

from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition

class SplashScreen(Widget):
	#when loading is complete switch to menu
  pass

class MenuScreen(Screen):
	pass

class AnotherScreen(Screen):
	pass

class ScreenManagement(ScreenManager):
	pass

class SettingsScreen(Screen):
	pass

class CameraMode(Screen):
	#camera = Camera(play=True, index=1, resolution=(399, 299))
	def FindFace(self):
		print()

class PipBoyApp(App):

	def build(self):
		#Create the screen manager
		sm = ScreenManager()
		sm.add_widget(MenuScreen(name='menu'))
		sm.add_widget(SettingsScreen(name='settings'))
		sm.add_widget(CameraMode(name='camera'))
		return sm


if __name__ == '__main__':
  PipBoyApp().run()