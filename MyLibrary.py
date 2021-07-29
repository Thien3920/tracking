import os
import shutil
import cv2
import zipfile
def thongso(select_box,frame):
    h,w=frame.shape[:2]
    width,height=select_box[2],select_box[3]
    center_x,center_y=(select_box[0]+width/2)/w,(select_box[1]+height/2)/h
    width,height=width/w,height/h
    """
    if width <0:
        width=abs(width)
    if height <0:
        height=abs(height)
    if center_x <0:
        center_x=abs(center_x)
    if center_y<0:
        center_y=abs(center_y)
    """
    cx="%.6f"%center_x
    cy="%.6f"%center_y
    w="%.6f"%width
    h="%.6f"%height
    return cx,cy,w,h

    

def video_x(j,file_name):
    path="outputs/"+file_name+"_"+str(j)+"/annotations"
    path2="outputs/"+file_name+"_"+str(j)+"/obj_train_data"
    path3= "outputs/"+file_name+"_"+str(j)+"/annotations/obj_train_data"

    os.makedirs(path)
    os.makedirs(path2)
    os.makedirs(path3)

    f1=open(path+"/obj.data","w")
    f1.write("classes = 2 \ntrain = train.txt \nnames = obj.names \nbackup = backup/")
    f1.close()
    f2=open(path+"/obj.names","w")
    f2.write("Ban_Hang_Rong \nKhong_Ban_Hang_Rong")
    f2.close()
def write(i,j,thongso,frame,file_name):
    n=6-len(str(i))
    f1=open("outputs/"+file_name+"_"+str(j)+"/annotations/obj_train_data/frame_"+"0"*n+str(i)+".txt","w")
    f1.write(thongso)
    f1.close()

    f2=open("outputs/"+file_name+"_"+str(j)+"/annotations/train.txt","a+")
    f2.write("obj_train_data/frame_"+"0"*n+str(i)+".jpg\n")
    f2.close()

    cv2.imwrite("outputs/"+file_name+"_"+str(j)+"/obj_train_data/frame_"+"0"*n+str(i)+".jpg",frame)
def delete_folder(j,file_name,n):
    path="/home/thien/Desktop/thien/tracking/outputs/"+file_name+"_"+str(j)+"/obj_train_data"
    path_2="/home/thien/Desktop/thien/tracking/outputs/"+file_name+"_"+str(j)
    if os.path.isdir(path_2) and len(os.listdir(path)) <n:
        shutil.rmtree(path_2)
def delete(j,file_name,n):
    for i in range(j+1):
        delete_folder(i,file_name,n)
