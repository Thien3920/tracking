import cv2
import sys
import os
import os.path
import numpy as np
from os import makedirs, path, write
import PySimpleGUI as sg

TimeOut_1=10
TimeOut_2=10
n=50 # số  lượng frame tối thiểu trong một clip

import MyLibrary as ml
while True:
    event, values = sg.Window('Get filename example', [[sg.Text('Filename')], [sg.Input(), sg.FileBrowse()], [sg.OK(), sg.Cancel()] ]).read(close=True)
    print(values[0])
    file_name=values[0].split("/")
    file_name=file_name[-1].split(".")[0]
    #file_name=file_name[0]

    print(file_name)

    # Tao doi tuong tracking
    my_track_method = cv2.legacy.TrackerMOSSE_create()
    my_track_metho_2=cv2.legacy.TrackerMOSSE_create()

    # Doc file video

    cap=cv2.VideoCapture(values[0])


    
    
   
    
    j=-1 # khởi tạo chỉ số video  video_1 video_2
    i=0 # khởi tạo chỉ số frame  frame1_1 frame_2
    
    while True:
        ok,frame=cap.read()
        k=cv2.waitKey(TimeOut_1)&0xff
        if not ok:
            
            print(" k tim thay frame")
            print("j=",j)
            ml.delete(j,file_name,n)
            sys.exit()
        cv2.imshow("frame",frame)

        if k==ord("s"):
            
            
            j+=1
            i=0

            # Doc frame dau tien de nguoi dung chon doi truong can track
            ret , frame = cap.read()
            if not ret:
                print('Khong tim thay file video') 
                print("j=",j)
                sys.exit()
            select_box = cv2.selectROI(frame, showCrosshair=True)
            select_box_2=cv2.selectROI(frame,showCrosshair=True)
            my_track_method.init(frame, select_box)
            my_track_metho_2.init(frame,select_box_2)    
            
            ml.video_x(j,file_name) 
            while True:
                # Read a new frame
                ok,frame =cap.read()
                frame_copy=np.copy(frame)
                
                if not ok:
                    # Neu khong doc duoc tiep thi out
                    print("3")
                    print("j=",j)
                    break

                # Update tracker
                ret, select_box = my_track_method.update(frame)
                ret_2,select_box_2=my_track_metho_2.update(frame)

                if ret or ret_2 :
                    # Neu nhu tracking duoc thanh cong
                    tl, br  = (int(select_box[0]), int(select_box[1])) , (int(select_box[0] + select_box[2]), int(select_box[1] + select_box[3]))
                    tl_2,br_2=(int(select_box_2[0]), int(select_box_2[1])) , (int(select_box_2[0] + select_box_2[2]), int(select_box_2[1] + select_box_2[3]))
                    cv2.rectangle(frame_copy, tl, br, (0, 255, 0), 2, 2)
                    cv2.rectangle(frame_copy,tl_2,br_2,(255,0,0),2,2)
                    i+=1 

                    cx_1,cy_1,w_1,h_1 =ml.thongso(select_box,frame)
                    cx_2,cy_2,w_2,h_2 =ml.thongso(select_box_2,frame)
                    if ret and ret_2:
                        thongso="0"+" "+ cx_1+" "+cy_1+" "+w_1+" "+h_1+"\n"+"1 "+cx_2+" "+cy_2+" "+w_2+" "+h_2
                    elif not ret_2:
                        thongso ="0"+" "+ cx_1+" "+cy_1+" "+w_1+" "+h_1
                    else:
                        thongso="1 "+cx_2+" "+cy_2+" "+w_2+" "+h_2
                    ml.write(i,j,thongso,frame,file_name)

                    print("frame.shape=",frame.shape)
                    print("select_box=",select_box)
                    print(thongso)
                    
                else:
                    # Neu nhu khong tim thay doi tuong
                    cv2.putText(frame_copy, "Object can not be tracked!", (80, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)


                
                # Hien thi thong tin va video
                cv2.putText(frame_copy, "MiAI Demo Object Tracking", (80, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2);
                cv2.imshow("Video", frame_copy)



                # Nhan dien thao tac nhan phim
            
                key=cv2.waitKey(TimeOut_2)&0xff

                
                if key==ord("p"):
                    while True:
                        key_2=cv2.waitKey(10)&0xff
                        if key_2==ord("c"):
                            break    
                
                # Neu nhan q thi thoat  
                if key == ord('q'):
                    break
                if key == ord('s'):
                    # Select lai ROI moi  
                    j+=1
                    i=0
                    ml.video_x(j,file_name)
                    

                    select_box = cv2.selectROI(frame, showCrosshair=True)
                    my_track_method.clear()
                    my_track_method = cv2.legacy.TrackerMOSSE_create()
                    my_track_method.init(frame, select_box)

                    select_box_2=cv2.selectROI(frame,showCrosshair=True)
                    my_track_metho_2.clear()
                    my_track_metho_2=cv2.legacy.TrackerMOSSE_create()
                    my_track_metho_2.init(frame,select_box_2)
            
            
        if k==ord("p"):
                while True:
                    k_2=cv2.waitKey(10)&0xff
                    if k_2==ord("c"):
                        break
        if k==ord("q"):
            break
    print("5 ---j=",j)
    ml.delete(j,file_name,n)
    """
    print(file_name)
    for i in range(j+1):
        print(i)
        ml.delete_folder(i,file_name)
    """

            
            
    