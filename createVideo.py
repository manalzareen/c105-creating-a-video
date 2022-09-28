import cv2
import os 

path = "Images"
images = []

for file in os.listdir(path):
    name,ext = os.path.splitext(file)
    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        file_name = path+"/"+file  #Images/110.jpg
        images.append(file_name)

count = len(images) 
frame = cv2.imread(images[0]) 

#shape property values are returned as tuple of (rows,cols, channels)
height,width,channels = frame.shape
size= (width,height)    

out = cv2.VideoWriter("sunrise.mp4",cv2.VideoWriter_fourcc(*"DIVX"),5 , size )

for i in range(count-1,0,-1):
    frame = cv2.imread(images[i])
    out.write(frame)
    
out.release()
print("done")