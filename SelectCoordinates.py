import cv2
import math
# Lists to store the points

circumference=[]
def drawCircle(action, x, y, flags, userdata):
  # Referencing global variables 
  global mouseX,mouseY,circumference
  # Action to be taken when left mouse button is pressed
  if action==cv2.EVENT_LBUTTONDOWN:
    # Mark the center
    cv2.circle(source, (x,y), 10, (255,255,0), 2, cv2.LINE_AA )
    mouseX,mouseY = x,y

source = cv2.imread("NewThinned.png",1)
print(source[114,25],source[114,25])
# Make a dummy image, will be useful to clear the drawing
dummy = source.copy()
cv2.namedWindow("Window")
# highgui function called when mouse events occur
cv2.setMouseCallback("Window", drawCircle)
k = 0
# loop until escape character is pressed



while k!=27 :
  
  cv2.imshow("Window", source)
  cv2.putText(source,"Choose center, and drag, Press ESC to exit and c to clear" ,(10,30), cv2.FONT_HERSHEY_SIMPLEX, 0.7,(255,255,255), 2 );
  k = cv2.waitKey(20) & 0xFF
  # Another way of cloning
  if k==99:
    source= dummy.copy()
  elif k == ord('a'):
    print(mouseX,mouseY,source[mouseY,mouseX])
  
cv2.destroyAllWindows()
