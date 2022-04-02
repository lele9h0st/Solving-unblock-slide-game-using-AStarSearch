import keyboard
import mss
import cv2
import numpy as np
from time import time,sleep
import pyautogui
from Node import Node
from AStarSearch import AStarSearch
print("press s to play")
print("once started press q to quit")
keyboard.wait('s')
x = 1360
y = 275
sct = mss.mss()
dimensions = {
        'left': 1360,
        'top': 275,
        'width': 480,
        'height': 600
    }

while True:
    scr = np.array(sct.grab(dimensions))
    scr_copy=np.copy(scr)
    scr_copy[:,1*80-4:1*80-3,:]=255
    scr_copy[:,2*80-3:2*80-2,:]=255
    scr_copy[:,3*80-2:3*80-1,:]=255
    scr_copy[:,4*80-1:4*80,:]=255
    scr_copy[:,5*80:5*80+1,:]=255

    scr_copy[1*80-1:1*80,:,:]=255
    scr_copy[2*80:2*80+1,:,:]=255
    scr_copy[3*80+1:3*80+2,:,:]=255
    scr_copy[4*80+2:4*80+3,:,:]=255


    a=[[0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0]]
    h_block_count=10
    v_block_count=0

    redX=0
    redY=0
    for j in range(6):
        for i in range(5):
            if scr[j*80+40,(i+1)*80+(i-4),1]>100 and scr[j*80+40,(i+1)*80+(i-4),1]<250:
                if a[j][i] ==0 and a[j][i+1]==0:
                    v_block_count+=1
                    a[j][i]=v_block_count
                    a[j][i+1]=v_block_count
                elif a[j][i] >0 and a[j][i] <10 and i<4:
                    a[j][i+1]=a[j][i]
            if scr[j*80+40,(i+1)*80+(i-4),1]>0 and scr[j*80+40,(i+1)*80+(i-4),1]<10 :
                print(str(i)+"  "+str(j))
                a[j][i]=100
                a[j][i+1]=100
                redX=j*80+40
                redY=(i+1)*80+(i-4)

    for j in range(6):
        for i in range(5):
            if scr[(i+1)*80+(i-1),j*80+40,1]>100 and scr[(i+1)*80+(i-1),j*80+40,1]<250:
                if a[i][j] ==0 and a[i+1][j]==0:
                    h_block_count+=1
                    a[i][j]=h_block_count
                    a[i+1][j]=h_block_count
                elif a[i][j] >10 and a[i][j] <25 and i<4:
                    a[i+1][j]=a[i][j]
    cv2.imshow('Screen Shot', scr_copy)
    cv2.waitKey(1)
    b=np.array(a)
    print(b)
    print("press c to continue")
    keyboard.wait('c')
    print("processing")
    astar=AStarSearch()

    root = Node(a,0,0)
    astar.execute(root)
    hStep=astar.hstep
    wStep=astar.wstep

    print(hStep)
    print(wStep)
    # print("press c to continue")
    # keyboard.wait('c')
    for i in range(len(hStep)-1,-1,-1):
        h=list(hStep[i])
        w=list(wStep[i])
        pyautogui.moveTo(x+int(w[2])*80+40,y+int(h[2])*80+40)
        pyautogui.dragTo(x+int(w[0])*80+40, y+int(h[0])*80+40, duration=0.5)
    
    
    for i in range(5):
        if scr[200,(i+1)*80+(i-4),1]>0 and scr[200,(i+1)*80+(i-4),1]<10 :
            redX=(i+1)*80+(i-4)
            redY=200
            break
    pyautogui.moveTo(x+redX,y+redY)
    pyautogui.dragTo(x+480+redX, y+redY, duration=0.5)
    
    
    sleep(.25)
    if keyboard.is_pressed('q'):
        break


# [[ 12  36  91 255]
#  [ 15  42  99 255]] blcack

# [[ 92 163 229 255]
#  [ 94 167 229 255]] brown

# [[  1   5 186 255]
#  [  1   5 182 255]] red

