import numpy as np
import cv2

VATS_DEFAULT_COLOR = (0, 255, 0)

'''
Adds the provied text to the current frame centered around
the provided x and y coordinates
frame = the frame to add the text too
text = the text to add
positionX = the center x position for the text
positionY =  the center y position for the text
verticalOffset = how far the text should be vertically set away from positionY
'''
def add_text(frame, text, positionX, positionY, verticalOffset):
  fontStyle = cv2.FONT_HERSHEY_SIMPLEX
  fontScale = .5
  fontThickness = 1
  textSize = cv2.getTextSize(text, fontStyle, fontScale, fontThickness)
  textWidth = textSize[0][0]
  cv2.putText(frame, text, (positionX - (textWidth / 2), positionY + verticalOffset),
    fontStyle, fontScale, VATS_DEFAULT_COLOR, fontThickness, cv2.LINE_AA)

'''
Adds the mysterious status bar / line to the current frame
frame = the frame to add the status bar to
length = the length of the line
positionX = the X position to center the line between
positionY = the Y position to center the line between
verticalOffset = how far the text should be vertically set away from positionY
'''
def add_status_bar(frame, length, positionX, positionY, verticalOffset):
  halfLength = length/2
  cv2.line(frame, (positionX-halfLength, positionY+verticalOffset), 
    (positionX+halfLength, positionY+verticalOffset), VATS_DEFAULT_COLOR, 4)

'''
Draws the identifing box above the given x, y coordinates.
frame = the frame to draw the box onto
x = the center x position of the obj that the id box is identifying
y = the center y position tf the obj that the ID box is identifying
w = the total width of the obj that the ID box is identifying
h = the total height of the obj that the ID box is identfying
'''
def draw_identifier_box(frame, x, y, w, h):
  descriptionHeightAbove = 25
  descriptionHeightBelow = 45
  descriptionWidth = 40

  #draw describer above head
  descriptionYOffset = int(h * .75)
  centerX = (x + x+w) / 2
  centerY = (y + y+h) / 2 - descriptionYOffset

  leftVector = (centerX-descriptionWidth, centerY-descriptionHeightAbove)
  rightVector = (centerX+descriptionWidth, centerY+descriptionHeightBelow)
  cv2.rectangle(frame, 
    leftVector, rightVector,
     VATS_DEFAULT_COLOR, 2)

  #font = cv2.FONT_HERSHEY_SIMPLEX
  add_text(frame, "Head", centerX, centerY, 0)

  add_status_bar(frame, descriptionWidth-10, centerX, centerY, 12)

  #Add identifer number
  add_text(frame, "40%", centerX, centerY, 30)

'''
Applies frontalface cascadeclassifier to an open video stream. Then adds rectangles for the
dected face and an identifier above it.
'''
if __name__ == '__main__':
  body_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')

  cap = cv2.VideoCapture(0)

  #setup 480p res
  cap.set(3, 640)
  cap.set(4, 480)

  while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    itemsOfInterest = body_cascade.detectMultiScale(
      gray,
      1.3,
      5
    )

    for (x,y,w,h) in itemsOfInterest:
      cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
      draw_identifier_box(frame, x, y, w, h)
      
    # Display the resulting frame
    cv2.imshow('frame',frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
      break

  # When everything done, release the capture
  cap.release()
  cv2.destroyAllWindows()
