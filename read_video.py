import cv2

#vid = cv2.VideoCapture(0)
vid = cv2.VideoCapture("AnthonyShkraba.mp4")

if( vid.isOpened() == False):
     print("Unable to read....")


height = int( vid.get( cv2.CAP_PROP_FRAME_HEIGHT) )
width = int(vid.get(cv2.CAP_PROP_FRAME_WIDTH))
fps = int(vid.get(cv2.CAP_PROP_FPS))
print( height , width , fps)

#cv2.VideoWriter(filename, fourcc, fps, frameSize, isColor)
out = cv2.VideoWriter("boxing.mp4", cv2.VideoWriter_fourcc(*'DIVX') , 30 , (width,height) )

while(True):
     #read() method returns a tuple of two elements - boolean & video frame
     ret , frame = vid.read()
     cv2.imshow("my boxing class" , frame )
     
     out.write(frame )
     if( cv2.waitKey(25) == 32):
          break

vid.release()
out.release()
cv2.destroyAllWindows()