import os
import cv2

path="Image"
images=[]
Images=os.listdir(path)

for x in Images:
    name, ext=os.path.splitext(x)
    if ext in ['.gif','.png','.jpg']:
        file_name=path+'/'+x
    images.append(file_name)
count=len(images)
print(count)
print(images[0])
frame=cv2.imread(images[0])
shape=frame.shape
width=shape[0]
height=shape[1]
Channel=shape[2]

size=(width,height)

out=cv2.VideoWriter('Project.avi',cv2.VideoWriter_fourcc(*'DIVX'),0.8,size)

for i in range(0,count-1):
    print(images[i])
    video=cv2.imread(images[i])
    out.write(video)
out.release()