from kivy.app import App
from kivy.uix.widget import Widget

from kivy.uix.camera import Camera

from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition

import cv2
import numpy

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
		camera = self.ids['camera'] #get camera obj from .kv file

		#freeze the image
		capturedImg = camera.export_to_png("./IMG_1.png")
		print("captured")

		#process gray image, using 0 param
		img = cv2.imread("IMG_1.png", 0)

		body_cascade = cv2.CascadeClassifier("../haarcascades/haarcascade_frontalface_default.xml");

		items = body_cascade.detectMultiScale(img, 1.1, 2)
		print("Faces Found ", len(items))

		for (x,y,w,h) in items:
			cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
			#cv2.imshow('face_gray', img)

		sm.current = 'display'

class DisplayPhoto(Screen):
	pass

sm = ScreenManager()

class PipBoyApp(App):

	def build(self):
		#Create the screen manager
		sm.add_widget(MenuScreen(name='menu'))
		sm.add_widget(SettingsScreen(name='settings'))
		sm.add_widget(CameraMode(name='camera'))
		sm.add_widget(DisplayPhoto(name='display'))
		return sm


if __name__ == '__main__':
  PipBoyApp().run()