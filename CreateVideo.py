import os
import cv2


path = "Images"

images = []


for file in os.listdir(path):
    name, ext = os.path.splitext(file)

    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        file_name = path+"/"+file

        print(file_name)
               
        images.append(file_name)
        
print(len(images))
count = len(images)

frames = cv2.imread(images[0])

height,width,channels = frames.shape
size = (width,height)
print(size)



out = cv2.VideoWriter('project1.mp4',cv2.VideoWriter_fourcc(*'m','p','4','v'), 5, size)

for i in range(0,count-1):

    frames = cv2.imread(images[i])
    out.write(frames)
out.release()
print("done")

