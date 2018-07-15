from kivy.app import App
from kivy.uix.widget import Widget

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

#Create the screen manager

class PipBoyApp(App):

	def build(self):
		sm = ScreenManager()
		sm.add_widget(MenuScreen(name='menu'))
		sm.add_widget(SettingsScreen(name='settings'))
		return sm


if __name__ == '__main__':
  PipBoyApp().run()