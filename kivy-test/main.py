from kivy.app import App
from kivy.uix.widget import Widget

from kivy.uix.camera import Camera

from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition

from kivy.core.image import Image as CoreImage #for saving image data file

import cv2
import numpy

import os
from kivy.cache import Cache

Builder.load_string('''
<DisplayPhoto>
    GridLayout:
        rows: 2
        cols: 1
        id: displayGrid

        Image:
            id: displayImageOld
            source: 'faceImg/grayImg.png'
        GridLayout:
            rows: 1
            cols: 2
            size_hint_y: None
            height: '48dp'
            Button:
                text: 'Back to V.A.T.S.'
                on_release:
                    root.DeleteSavedFace()
                    root.manager.transition.direction = 'left'
                    root.manager.current = 'camera'

            Button:
                text: 'Home'
                on_release:
                    root.DeleteSavedFace()
                    root.manager.transition.direction = 'down'
                    root.manager.current = 'menu'
''')

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
		self.ids.displayImage.source = ''
		camera = self.ids['camera'] #get camera obj from .kv file

		#freeze the image
		capturedImg = camera.export_to_png("faceImg/IMG.png")
		print("captured")

		#process gray image, using 0 param
		img = cv2.imread("faceImg/IMG.png")

		os.remove("faceImg/IMG.png")
		body_cascade = cv2.CascadeClassifier("../haarcascades/haarcascade_frontalface_default.xml");

		items = body_cascade.detectMultiScale(img, 1.1, 2)
		print("Faces Found ", len(items))

		for (x,y,w,h) in items:
			cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
			#cv2.imshow('face_gray', img)

		cv2.imwrite("faceImg/grayImg.png", img)
		
		#img.save("./grayImg.png")
		#sm.current = 'display'
		self.ids.displayImage.source = 'faceImg/grayImg.png'
		self.ids.displayImage.reload()

	def DeleteCamera(self):
		self.remove_widget(self.ids.camera)

class DisplayPhoto(Screen):

	def DeleteSavedFace(self):
		self.ids.displayImage.source = ''
		imToRemove = CoreImage('faceImg/grayImg.png')
		imToRemove.remove_from_cache()

		os.rename("faceImg/grayImg.png", "faceImg/grayImgTemp.png")

		Cache.remove("kv.image")
		Cache.remove("kv.textur")

		self.remove_widget(self.ids.displayImage)
		os.rename("faceImg/grayImgTemp.png", "faceImg/grayImg.png")

		self.ids.displayImage.source = 'faceImg/grayImg.png'

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