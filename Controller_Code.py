from tkinter import *
import tkinter.font
import cv2
import numpy as np
import torch
import torch.nn.functional as F
import yaml
from PIL import ExifTags, Image, ImageOps
from torch.utils.data import Dataset
from tqdm import tqdm
import serial
import time
import datetime
from datetime import datetime
from datetime import timedelta

model = torch.hub.load('ultralytics/yolov5', 'custom', path='TANAMAN.pt')  # or yolov5m, yolov5l, yolov5x, custom
ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1)
img = 'https://ultralytics.com/images/zidane.jpg'  # or file, Path, PIL, OpenCV, numpy, list

#G-Code Declaration
# G-CODE REAL
# DEPAN   = "G1 X121 F4000\n" 
# RESET   = "N1 G91\n"
# KANAN   = "G1 Y67 F4000\n"
# KIRI    = "G1 Y-67 F4000\n"
# BAWAH   = "G1 Z170 F4000\n"
# ATAS    = "G1 Z-170 F4000\n"
# SIRAM   = ["M3\n","M5\n"]
# OFF     = ""
# NOT     = "Tanaman tidak membutuhkan pupuk"

#TEST
DEPAN   = "G1 X121 F4000\n" 
RESET   = "N1 G91\n"
KANAN   = "G1 Y67 F4000\n"
KIRI    = "G1 Y-67 F4000\n"
BAWAH   = "G1 Z170 F4000\n"
ATAS    = "G1 Z-170 F4000\n"
SIRAM   = ["M3\n","M5\n"]
OFF     = ""
NOT     = "Tanaman tidak membutuhkan pupuk"

def shower1():
    reset()
    time.sleep(2)
    for s in SIRAM:
            print (SIRAM)
            ser.write(s.encode('utf-8'))
            print (elapsed_time1)
            time.sleep(0.1)

def shower2():
    reset()
    time.sleep(2)
    for s in SIRAM:
            print (SIRAM)
            ser.write(s.encode('utf-8'))
            print (elapsed_time1)
            time.sleep(0.5)

def shower3():
    reset()
    time.sleep(2)
    for s in SIRAM:
            print (SIRAM)
            ser.write(s.encode('utf-8'))
            print (elapsed_time1)
            time.sleep(1.5)

def down():
    print (BAWAH)
    ser.write(BAWAH.encode('utf-8'))
    print (elapsed_time1)
    time.sleep(21)

def up():
    print (ATAS)
    ser.write(ATAS.encode('utf-8'))
    print (elapsed_time1)

def reset():
    print (RESET)
    ser.write(RESET.encode('utf-8'))

def function1():
    if flag1 == 0:
        reset()

def function2():
    if flag2 == 0:
        print (DEPAN)
        ser.write(DEPAN.encode('utf-8'))
        print (elapsed_time2)

def function3():
    if flag3 == 0:
        print (RESET)
        ser.write(RESET.encode('utf-8'))
        print (elapsed_time3)
    
def function4():
    if flag4 == 0:
        print (KANAN)
        ser.write(KANAN.encode('utf-8'))
        print (elapsed_time4)

def function5():
    if flag5 == 0:
        print (RESET)
        ser.write(RESET.encode('utf-8'))
        print (elapsed_time5)

def function6():
    for i in range (1):
        if flag6 == 0:
            if 'Cabai Mentah' in listt:
                print (elapsed_time6)
                print (listt)
                down()
                shower1()
                break              
                
            elif 'Cabai Set-Matang' in listt:
                print (elapsed_time6)
                print (listt)
                down()
                shower2()
                break
                
            elif 'Cabai Matang' in listt:
                print (elapsed_time6)
                print (listt)
                down()
                shower3()
                break
                
            elif 'Cabai Busuk' in listt:
                print (elapsed_time6)
                print (listt)
                down()
                reset()
                break             

            else:
                down()
                break

def function7():
    if flag7 == 0:
        reset()
        print (elapsed_time7)

def function8():
    if flag8 == 0:
        print (ATAS)
        ser.write(ATAS.encode('utf-8'))
        print (elapsed_time8)

def function9():
    if flag9 == 0:
        reset()
        print (elapsed_time9)

def function10():
    if flag10 == 0:
        print (KANAN)
        ser.write(KANAN.encode('utf-8'))
        print (elapsed_time10)

def function11():
    if flag11 == 0:
        print (RESET)
        ser.write(RESET.encode('utf-8'))
        print (elapsed_time11)

def function12():
    for i in range (1):
        if flag12 == 0:
            if 'Cabai Mentah' in listt:
                print (elapsed_time12)
                print (listt)
                down()
                shower1() 
                break             
                
            elif 'Cabai Set-Matang' in listt:
                print (elapsed_time12)
                print (listt)
                down()
                shower2()
                break
                
            elif 'Cabai Matang' in listt:
                print (elapsed_time12)
                print (listt)
                down()
                shower3()
                break
                
            elif 'Cabai Busuk' in listt:
                print (elapsed_time12)
                print (listt)
                down()
                reset()
                break              

            else:
                 down()
                 break

def function13():
    if flag13 == 0:
        reset()
        print (elapsed_time13)

def function14():
    if flag14 == 0:
        print (ATAS)
        ser.write(ATAS.encode('utf-8'))
        print (elapsed_time14)

def function15():
    if flag15 == 0:
        reset()
        print (elapsed_time15)

def function16():
    if flag16 == 0:
        print (KANAN)
        ser.write(KANAN.encode('utf-8'))
        print (elapsed_time16)

def function17():
    if flag17 == 0:
        reset()
        print (elapsed_time17)
        
def function18():
    for i in range (1):
        if flag18 == 0:
            if 'Cabai Mentah' in listt:
                print (elapsed_time18)
                print (listt)
                down()
                shower1() 
                break             
                
            elif 'Cabai Set-Matang' in listt:
                print (elapsed_time18)
                print (listt)
                down()
                shower2()
                break
                
            elif 'Cabai Matang' in listt:
                print (elapsed_time18)
                print (listt)
                down()
                shower3()
                break
                
            elif 'Cabai Busuk' in listt:
                print (elapsed_time18)
                print (listt)
                down()
                reset()
                break              

            else:
                 down()
                 break

def function19():
    if flag19 == 0:
        reset()
        print (elapsed_time19)

def function20():
    if flag20 == 0:
        print (ATAS)
        ser.write(ATAS.encode('utf-8'))
        print (elapsed_time20)

def function21():
    if flag21 == 0:
        reset()
        print (elapsed_time21)
    
def function22():
    if flag22 == 0:
        print (KANAN)
        ser.write(KANAN.encode('utf-8'))
        print (elapsed_time22)

def function23():
    if flag23 == 0:
        reset()
        print (elapsed_time23)
    
def function24():
    for i in range (1):
        if flag24 == 0:
            if 'Cabai Mentah' in listt:
                print (elapsed_time24)
                print (listt)
                down()
                shower1() 
                break             
                
            elif 'Cabai Set-Matang' in listt:
                print (elapsed_time24)
                print (listt)
                down()
                shower2()
                break
                
            elif 'Cabai Matang' in listt:
                print (elapsed_time24)
                print (listt)
                down()
                shower3()
                break
                
            elif 'Cabai Busuk' in listt:
                print (elapsed_time24)
                print (listt)
                down()
                reset()
                break              

            else:
                 down()
                 break

def function25():
    if flag25 == 0:
        reset()
        print (elapsed_time25)

def function26():
    if flag26 == 0:
        print (ATAS)
        ser.write(ATAS.encode('utf-8'))
        print (elapsed_time26)

def function27():
    if flag27 == 0:
        reset()
        print (elapsed_time27)
    
def function28():
    if flag28 == 0:
        print (KANAN)
        ser.write(KANAN.encode('utf-8'))
        print (elapsed_time28)

def function29():
    if flag29 == 0:
        reset()
        print (elapsed_time29)
    
def function30():
    for i in range (1):
        if flag30 == 0:
            if 'Cabai Mentah' in listt:
                print (elapsed_time30)
                print (listt)
                down()
                shower1() 
                break             
                
            elif 'Cabai Set-Matang' in listt:
                print (elapsed_time30)
                print (listt)
                down()
                shower2()
                break
                
            elif 'Cabai Matang' in listt:
                print (elapsed_time30)
                print (listt)
                down()
                shower3()
                break

            elif 'Cabai Busuk' in listt:
                print (elapsed_time30)
                print (listt)
                down()
                reset()
                break              

            else:
                 down()
                 break

def function31():
    if flag31 == 0:
        reset()
        print (elapsed_time31)

def function32():
    if flag32 == 0:
        print (ATAS)
        ser.write(ATAS.encode('utf-8'))
        print (elapsed_time32)

def function33():
    if flag33 == 0:
        reset()
        print (elapsed_time33)
    
def function34():
    if flag34 == 0:
        print (KANAN)
        ser.write(KANAN.encode('utf-8'))
        print (elapsed_time34)

def function35():
    if flag35 == 0:
        reset()
        print (elapsed_time35)

#KANAN-1

def function36():
    if flag36 == 0:
        print (DEPAN)
        ser.write(DEPAN.encode('utf-8'))
        print (elapsed_time36)

def function37():
    if flag37 == 0:
        print (RESET)
        ser.write(RESET.encode('utf-8'))
        print (elapsed_time37)
    
def function38():
    if flag38 == 0:
        print (KIRI)
        ser.write(KIRI.encode('utf-8'))
        print (elapsed_time38)

def function39():
    if flag39 == 0:
        print (RESET)
        ser.write(RESET.encode('utf-8'))
        print (elapsed_time39)

def function40():
    for i in range (1):
        if flag40 == 0:
            if 'Cabai Mentah' in listt:
                print (elapsed_time40)
                print (listt)
                down()
                shower1()
                break              
                
            elif 'Cabai Set-Matang' in listt:
                print (elapsed_time40)
                print (listt)
                down()
                shower2()
                break
                
            elif 'Cabai Matang' in listt:
                print (elapsed_time40)
                print (listt)
                down()
                shower3()
                break
                
            elif 'Cabai Busuk' in listt:
                print (elapsed_time40)
                print (listt)
                down()
                reset()
                break              

            else: 
                down()
                break

def function41():
    if flag41 == 0:
        reset()
        print (elapsed_time41)

def function42():
    if flag42 == 0:
        print (ATAS)
        ser.write(ATAS.encode('utf-8'))
        print (elapsed_time42)

def function43():
    if flag43 == 0:
        reset()
        print (elapsed_time43)

def function44():
    if flag44 == 0:
        print (KIRI)
        ser.write(KIRI.encode('utf-8'))
        print (elapsed_time44)

def function45():
    if flag45 == 0:
        print (RESET)
        ser.write(RESET.encode('utf-8'))
        print (elapsed_time45)

def function46():
    for i in range (1):
        if flag46 == 0:
            if 'Cabai Mentah' in listt:
                print (elapsed_time46)
                print (listt)
                down()
                shower1() 
                break             
                
            elif 'Cabai Set-Matang' in listt:
                print (elapsed_time46)
                print (listt)
                down()
                shower2()
                break
                
            elif 'Cabai Matang' in listt:
                print (elapsed_time46)
                print (listt)
                down()
                shower3()
                break
                
            elif 'Cabai Busuk' in listt:
                print (elapsed_time46)
                print (listt)
                down()
                reset()
                break              

            else:
                 down()
                 break

def function47():
    if flag47 == 0:
        reset()
        print (elapsed_time47)

def function48():
    if flag48 == 0:
        print (ATAS)
        ser.write(ATAS.encode('utf-8'))
        print (elapsed_time48)

def function49():
    if flag49 == 0:
        reset()
        print (elapsed_time49)

def function50():
    if flag50 == 0:
        print (KIRI)
        ser.write(KIRI.encode('utf-8'))
        print (elapsed_time50)

def function51():
    if flag51 == 0:
        reset()
        print (elapsed_time51)
        
def function52():
    for i in range (1):
        if flag52 == 0:
            if 'Cabai Mentah' in listt:
                print (elapsed_time52)
                print (listt)
                down()
                shower1() 
                break             
                
            elif 'Cabai Set-Matang' in listt:
                print (elapsed_time52)
                print (listt)
                down()
                shower2()
                break
                
            elif 'Cabai Matang' in listt:
                print (elapsed_time52)
                print (listt)
                down()
                shower3()
                break
                
            elif 'Cabai Busuk' in listt:
                print (elapsed_time52)
                print (listt)
                down()
                reset()
                break              

            else:
                 down()
                 break

def function53():
    if flag53 == 0:
        reset()
        print (elapsed_time53)

def function54():
    if flag54 == 0:
        print (ATAS)
        ser.write(ATAS.encode('utf-8'))
        print (elapsed_time54)

def function55():
    if flag55 == 0:
        reset()
        print (elapsed_time55)
    
def function56():
    if flag56 == 0:
        print (KIRI)
        ser.write(KIRI.encode('utf-8'))
        print (elapsed_time56)

def function57():
    if flag57 == 0:
        reset()
        print (elapsed_time57)
    
def function58():
    for i in range (1):
        if flag58 == 0:
            if 'Cabai Mentah' in listt:
                print (elapsed_time58)
                print (listt)
                down()
                shower1() 
                break             
                
            elif 'Cabai Set-Matang' in listt:
                print (elapsed_time58)
                print (listt)
                down()
                shower2()
                break
                
            elif 'Cabai Matang' in listt:
                print (elapsed_time58)
                print (listt)
                down()
                shower3()
                break
                
            elif 'Cabai Busuk' in listt:
                print (elapsed_time58)
                print (listt)
                down()
                reset()
                break              

            else:
                 down()
                 break

def function59():
    if flag59 == 0:
        reset()
        print (elapsed_time59)

def function60():
    if flag60 == 0:
        print (ATAS)
        ser.write(ATAS.encode('utf-8'))
        print (elapsed_time60)

def function61():
    if flag61 == 0:
        reset()
        print (elapsed_time61)
    
def function62():
    if flag62 == 0:
        print (KIRI)
        ser.write(KIRI.encode('utf-8'))
        print (elapsed_time62)

def function63():
    if flag63 == 0:
        reset()
        print (elapsed_time63)
    
def function64():
    for i in range (1):
        if flag64 == 0:
            if 'Cabai Mentah' in listt:
                print (elapsed_time64)
                print (listt)
                down()
                shower1() 
                break             
                
            elif 'Cabai Set-Matang' in listt:
                print (elapsed_time64)
                print (listt)
                down()
                shower2()
                break
                
            elif 'Cabai Matang' in listt:
                print (elapsed_time64)
                print (listt)
                down()
                shower3()
                break
                
            elif 'Cabai Busuk' in listt:
                print (elapsed_time64)
                print (listt)
                down()
                reset()
                break              

            else:
                 down()
                 break

def function65():
    if flag65 == 0:
        reset()
        print (elapsed_time65)

def function66():
    if flag66 == 0:
        print (ATAS)
        ser.write(ATAS.encode('utf-8'))
        print (elapsed_time66)

def function67():
    if flag67 == 0:
        reset()
        print (elapsed_time67)
    
def function68():
    if flag68 == 0:
        print (KIRI)
        ser.write(KIRI.encode('utf-8'))
        print (elapsed_time68)

def function69():
    if flag69 == 0:
        reset()
        print (elapsed_time69)

#KIRI-1

def function70():
    if flag70 == 0:
        print (DEPAN)
        ser.write(DEPAN.encode('utf-8'))
        print (elapsed_time70)

def function71():
    if flag71 == 0:
        print (RESET)
        ser.write(RESET.encode('utf-8'))
        print (elapsed_time71)
    
def function72():
    if flag72 == 0:
        print (KANAN)
        ser.write(KANAN.encode('utf-8'))
        print (elapsed_time72)

def function73():
    if flag73 == 0:
        print (RESET)
        ser.write(RESET.encode('utf-8'))
        print (elapsed_time73)

def function74():
    for i in range (1):
        if flag74 == 0:
            if 'Cabai Mentah' in listt:
                print (elapsed_time74)
                print (listt)
                down()
                shower1()
                break              
                
            elif 'Cabai Set-Matang' in listt:
                print (elapsed_time74)
                print (listt)
                down()
                shower2()
                break
                
            elif 'Cabai Matang' in listt:
                print (elapsed_time74)
                print (listt)
                down()
                shower3()
                break
                
            elif 'Cabai Busuk' in listt:
                print (elapsed_time74)
                print (listt)
                down()
                reset()
                break

            else:
                 down()
                 break

def function75():
    if flag75 == 0:
        reset()
        print (elapsed_time75)

def function76():
    if flag76 == 0:
        print (ATAS)
        ser.write(ATAS.encode('utf-8'))
        print (elapsed_time76)

def function77():
    if flag77 == 0:
        reset()
        print (elapsed_time77)

def function78():
    if flag78 == 0:
        print (KANAN)
        ser.write(KANAN.encode('utf-8'))
        print (elapsed_time78)

def function79():
    if flag79 == 0:
        print (RESET)
        ser.write(RESET.encode('utf-8'))
        print (elapsed_time79)

def function80():
    for i in range (1):
        if flag80 == 0:
            if 'Cabai Mentah' in listt:
                print (elapsed_time80)
                print (listt)
                down()
                shower1() 
                break             
                
            elif 'Cabai Set-Matang' in listt:
                print (elapsed_time80)
                print (listt)
                down()
                shower2()
                break
                
            elif 'Cabai Matang' in listt:
                print (elapsed_time80)
                print (listt)
                down()
                shower3()
                break
                
            elif 'Cabai Busuk' in listt:
                print (elapsed_time80)
                print (listt)
                down()
                reset()
                break

            else:
                 down()
                 break

def function81():
    if flag81 == 0:
        reset()
        print (elapsed_time81)

def function82():
    if flag82 == 0:
        print (ATAS)
        ser.write(ATAS.encode('utf-8'))
        print (elapsed_time82)

def function83():
    if flag83 == 0:
        reset()
        print (elapsed_time83)

def function84():
    if flag84 == 0:
        print (KANAN)
        ser.write(KANAN.encode('utf-8'))
        print (elapsed_time84)

def function85():
    if flag85 == 0:
        reset()
        print (elapsed_time85)
        
def function86():
    for i in range (1):
        if flag86 == 0:
            if 'Cabai Mentah' in listt:
                print (elapsed_time86)
                print (listt)
                down()
                shower1() 
                break             
                
            elif 'Cabai Set-Matang' in listt:
                print (elapsed_time86)
                print (listt)
                down()
                shower2()
                break
                
            elif 'Cabai Matang' in listt:
                print (elapsed_time86)
                print (listt)
                down()
                shower3()
                break
                
            elif 'Cabai Busuk' in listt:
                print (elapsed_time86)
                print (listt)
                down()
                reset()
                break

            else:
                 down()
                 break

def function87():
    if flag87 == 0:
        reset()
        print (elapsed_time87)

def function88():
    if flag88 == 0:
        print (ATAS)
        ser.write(ATAS.encode('utf-8'))
        print (elapsed_time88)

def function89():
    if flag89 == 0:
        reset()
        print (elapsed_time89)
    
def function90():
    if flag90 == 0:
        print (KANAN)
        ser.write(KANAN.encode('utf-8'))
        print (elapsed_time90)

def function91():
    if flag91 == 0:
        reset()
        print (elapsed_time91)
    
def function92():
    for i in range (1):
        if flag92 == 0:
            if 'Cabai Mentah' in listt:
                print (elapsed_time92)
                print (listt)
                down()
                shower1() 
                break             
                
            elif 'Cabai Set-Matang' in listt:
                print (elapsed_time92)
                print (listt)
                down()
                shower2()
                break
                
            elif 'Cabai Matang' in listt:
                print (elapsed_time92)
                print (listt)
                down()
                shower3()
                break
                
            elif 'Cabai Busuk' in listt:
                print (elapsed_time92)
                print (listt)
                down()
                reset()
                break

            else:
                 down()
                 break

def function93():
    if flag93 == 0:
        reset()
        print (elapsed_time93)

def function94():
    if flag94 == 0:
        print (ATAS)
        ser.write(ATAS.encode('utf-8'))
        print (elapsed_time94)

def function95():
    if flag95 == 0:
        reset()
        print (elapsed_time95)
    
def function96():
    if flag96 == 0:
        print (KANAN)
        ser.write(KANAN.encode('utf-8'))
        print (elapsed_time96)

def function97():
    if flag97 == 0:
        reset()
        print (elapsed_time97)
    
def function98():
    for i in range (1):
        if flag98 == 0:
            if 'Cabai Mentah' in listt:
                print (elapsed_time98)
                print (listt)
                down()
                shower1() 
                break             
                
            elif 'Cabai Set-Matang' in listt:
                print (elapsed_time98)
                print (listt)
                down()
                shower2()
                break
                
            elif 'Cabai Matang' in listt:
                print (elapsed_time98)
                print (listt)
                down()
                shower3()
                break
                
            elif 'Cabai Busuk' in listt:
                print (elapsed_time98)
                print (listt)
                down()
                reset()
                break

            else:
                 down()
                 break

def function99():
    if flag99 == 0:
        reset()
        print (elapsed_time99)

def function100():
    if flag100 == 0:
        print (ATAS)
        ser.write(ATAS.encode('utf-8'))
        print (elapsed_time100)

def function101():
    if flag101 == 0:
        reset()
        print (elapsed_time101)
    
def function102():
    if flag102 == 0:
        print (KANAN)
        ser.write(KANAN.encode('utf-8'))
        print (elapsed_time102)

def function103():
    if flag103 == 0:
        reset()
        print (elapsed_time103)

#KANAN-2

def function104():
    if flag104 == 0:
        print (DEPAN)
        ser.write(DEPAN.encode('utf-8'))
        print (elapsed_time104)

def function105():
    if flag105 == 0:
        print (RESET)
        ser.write(RESET.encode('utf-8'))
        print (elapsed_time105)
    
def function106():
    if flag106 == 0:
        print (KIRI)
        ser.write(KIRI.encode('utf-8'))
        print (elapsed_time106)

def function107():
    if flag107 == 0:
        print (RESET)
        ser.write(RESET.encode('utf-8'))
        print (elapsed_time107)

def function108():
    for i in range (1):
        if flag108 == 0:
            if 'Cabai Mentah' in listt:
                print (elapsed_time108)
                print (listt)
                down()
                shower1()
                break              
                
            elif 'Cabai Set-Matang' in listt:
                print (elapsed_time108)
                print (listt)
                down()
                shower2()
                break
                
            elif 'Cabai Matang' in listt:
                print (elapsed_time108)
                print (listt)
                down()
                shower3()
                break
                
            elif 'Cabai Busuk' in listt:
                print (elapsed_time108)
                print (listt)
                down()
                reset()
                break

            else:
                 down()
                 break

def function109():
    if flag109 == 0:
        reset()
        print (elapsed_time109)

def function110():
    if flag110 == 0:
        print (ATAS)
        ser.write(ATAS.encode('utf-8'))
        print (elapsed_time110)

def function111():
    if flag111 == 0:
        reset()
        print (elapsed_time111)

def function112():
    if flag112 == 0:
        print (KIRI)
        ser.write(KIRI.encode('utf-8'))
        print (elapsed_time112)

def function113():
    if flag113 == 0:
        print (RESET)
        ser.write(RESET.encode('utf-8'))
        print (elapsed_time113)

def function114():
    for i in range (1):
        if flag114 == 0:
            if 'Cabai Mentah' in listt:
                print (elapsed_time114)
                print (listt)
                down()
                shower1() 
                break             
                
            elif 'Cabai Set-Matang' in listt:
                print (elapsed_time114)
                print (listt)
                down()
                shower2()
                break
                
            elif 'Cabai Matang' in listt:
                print (elapsed_time114)
                print (listt)
                down()
                shower3()
                break
                
            elif 'Cabai Busuk' in listt:
                print (elapsed_time114)
                print (listt)
                down()
                reset()
                break

            else:
                 down()
                 break

def function115():
    if flag115 == 0:
        reset()
        print (elapsed_time115)

def function116():
    if flag116 == 0:
        print (ATAS)
        ser.write(ATAS.encode('utf-8'))
        print (elapsed_time116)

def function117():
    if flag117 == 0:
        reset()
        print (elapsed_time117)

def function118():
    if flag118 == 0:
        print (KIRI)
        ser.write(KIRI.encode('utf-8'))
        print (elapsed_time118)

def function119():
    if flag119 == 0:
        reset()
        print (elapsed_time119)
        
def function120():
    for i in range (1):
        if flag120 == 0:
            if 'Cabai Mentah' in listt:
                print (elapsed_time120)
                print (listt)
                down()
                shower1() 
                break             
                
            elif 'Cabai Set-Matang' in listt:
                print (elapsed_time120)
                print (listt)
                down()
                shower2()
                break
                
            elif 'Cabai Matang' in listt:
                print (elapsed_time120)
                print (listt)
                down()
                shower3()
                break
                
            elif 'Cabai Busuk' in listt:
                print (elapsed_time120)
                print (listt)
                down()
                reset()
                break

            else:
                 down()
                 break

def function121():
    if flag121 == 0:
        reset()
        print (elapsed_time121)

def function122():
    if flag122 == 0:
        print (ATAS)
        ser.write(ATAS.encode('utf-8'))
        print (elapsed_time122)

def function123():
    if flag123 == 0:
        reset()
        print (elapsed_time123)
    
def function124():
    if flag124 == 0:
        print (KIRI)
        ser.write(KIRI.encode('utf-8'))
        print (elapsed_time124)

def function125():
    if flag125 == 0:
        reset()
        print (elapsed_time125)
    
def function126():
    for i in range (1):
        if flag126 == 0:
            if 'Cabai Mentah' in listt:
                print (elapsed_time126)
                print (listt)
                down()
                shower1() 
                break             
                
            elif 'Cabai Set-Matang' in listt:
                print (elapsed_time126)
                print (listt)
                down()
                shower2()
                break
                
            elif 'Cabai Matang' in listt:
                print (elapsed_time126)
                print (listt)
                down()
                shower3()
                break
                
            elif 'Cabai Busuk' in listt:
                print (elapsed_time126)
                print (listt)
                down()
                reset()
                break
            else:
                 down()
                 break

def function127():
    if flag127 == 0:
        reset()
        print (elapsed_time127)

def function128():
    if flag128 == 0:
        print (ATAS)
        ser.write(ATAS.encode('utf-8'))
        print (elapsed_time128)

def function129():
    if flag129 == 0:
        reset()
        print (elapsed_time129)
    
def function130():
    if flag130 == 0:
        print (KIRI)
        ser.write(KIRI.encode('utf-8'))
        print (elapsed_time130)

def function131():
    if flag131 == 0:
        reset()
        print (elapsed_time131)
    
def function132():
    for i in range (1):
        if flag132 == 0:
            if 'Cabai Mentah' in listt:
                print (elapsed_time132)
                print (listt)
                down()
                shower1() 
                break             
                
            elif 'Cabai Set-Matang' in listt:
                print (elapsed_time132)
                print (listt)
                down()
                shower2()
                break
                
            elif 'Cabai Matang' in listt:
                print (elapsed_time132)
                print (listt)
                down()
                shower3()
                break
                
            elif 'Cabai Busuk' in listt:
                print (elapsed_time132)
                print (listt)
                down()
                reset()
                break
            else:
                 down()
                 break

def function133():
    if flag133 == 0:
        reset()
        print (elapsed_time133)

def function134():
    if flag134 == 0:
        print (ATAS)
        ser.write(ATAS.encode('utf-8'))
        print (elapsed_time134)

def function135():
    if flag135 == 0:
        reset()
        print (elapsed_time135)
    
def function136():
    if flag136 == 0:
        print (KIRI)
        ser.write(KIRI.encode('utf-8'))
        print (elapsed_time136)

def function137():
    if flag137 == 0:
        reset()
        print (elapsed_time137)
    
#KIRI-2

def function138():
    if flag138 == 0:
        print (DEPAN)
        ser.write(DEPAN.encode('utf-8'))
        print (elapsed_time138)

def function139():
    if flag139 == 0:
        print (RESET)
        ser.write(RESET.encode('utf-8'))
        print (elapsed_time139)
    
def function140():
    if flag140 == 0:
        print (KANAN)
        ser.write(KANAN.encode('utf-8'))
        print (elapsed_time140)

def function141():
    if flag141 == 0:
        print (RESET)
        ser.write(RESET.encode('utf-8'))
        print (elapsed_time141)

def function142():
    for i in range (1):
        if flag142 == 0:
            if 'Cabai Mentah' in listt:
                print (elapsed_time142)
                print (listt)
                down()
                shower1()
                break              
                
            elif 'Cabai Set-Matang' in listt:
                print (elapsed_time142)
                print (listt)
                down()
                shower2()
                break
                
            elif 'Cabai Matang' in listt:
                print (elapsed_time142)
                print (listt)
                down()
                shower3()
                break
                
            elif 'Cabai Busuk' in listt:
                print (elapsed_time142)
                print (listt)
                down()
                reset()
                break

            else:
                 down()
                 break

def function143():
    if flag143 == 0:
        reset()
        print (elapsed_time143)

def function144():
    if flag144 == 0:
        print (ATAS)
        ser.write(ATAS.encode('utf-8'))
        print (elapsed_time144)

def function145():
    if flag145 == 0:
        reset()
        print (elapsed_time145)

def function146():
    if flag146 == 0:
        print (KANAN)
        ser.write(KANAN.encode('utf-8'))
        print (elapsed_time146)

def function147():
    if flag147 == 0:
        print (RESET)
        ser.write(RESET.encode('utf-8'))
        print (elapsed_time147)

def function148():
    for i in range (1):
        if flag148 == 0:
            if 'Cabai Mentah' in listt:
                print (elapsed_time148)
                print (listt)
                down()
                shower1() 
                break             
                
            elif 'Cabai Set-Matang' in listt:
                print (elapsed_time148)
                print (listt)
                down()
                shower2()
                break
                
            elif 'Cabai Matang' in listt:
                print (elapsed_time148)
                print (listt)
                down()
                shower3()
                break
                
            elif 'Cabai Busuk' in listt:
                print (elapsed_time148)
                print (listt)
                down()
                reset()
                break

            else:
                 down()
                 break

def function149():
    if flag149 == 0:
        reset()
        print (elapsed_time149)

def function150():
    if flag150 == 0:
        print (ATAS)
        ser.write(ATAS.encode('utf-8'))
        print (elapsed_time150)

def function151():
    if flag151 == 0:
        reset()
        print (elapsed_time151)

def function152():
    if flag152 == 0:
        print (KANAN)
        ser.write(KANAN.encode('utf-8'))
        print (elapsed_time152)

def function153():
    if flag153 == 0:
        reset()
        print (elapsed_time153)
        
def function154():
    for i in range (1):
        if flag154 == 0:
            if 'Cabai Mentah' in listt:
                print (elapsed_time154)
                print (listt)
                down()
                shower1() 
                break             
                
            elif 'Cabai Set-Matang' in listt:
                print (elapsed_time154)
                print (listt)
                down()
                shower2()
                break
                
            elif 'Cabai Matang' in listt:
                print (elapsed_time154)
                print (listt)
                down()
                shower3()
                break
                
            elif 'Cabai Busuk' in listt:
                print (elapsed_time154)
                print (listt)
                down()
                reset()
                break

            else:
                 down()
                 break

def function155():
    if flag155 == 0:
        reset()
        print (elapsed_time155)

def function156():
    if flag156 == 0:
        print (ATAS)
        ser.write(ATAS.encode('utf-8'))
        print (elapsed_time156)

def function157():
    if flag157 == 0:
        reset()
        print (elapsed_time157)
    
def function158():
    if flag158 == 0:
        print (KANAN)
        ser.write(KANAN.encode('utf-8'))
        print (elapsed_time158)

def function159():
    if flag159 == 0:
        reset()
        print (elapsed_time159)
    
def function160():
    for i in range (1):
        if flag160 == 0:
            if 'Cabai Mentah' in listt:
                print (elapsed_time160)
                print (listt)
                down()
                shower1() 
                break             
                
            elif 'Cabai Set-Matang' in listt:
                print (elapsed_time160)
                print (listt)
                down()
                shower2()
                break
                
            elif 'Cabai Matang' in listt:
                print (elapsed_time160)
                print (listt)
                down()
                shower3()
                break
                
            elif 'Cabai Busuk' in listt:
                print (elapsed_time160)
                print (listt)
                down()
                reset()
                break

            else:
                 down()
                 break

def function161():
    if flag161 == 0:
        reset()
        print (elapsed_time161)

def function162():
    if flag162 == 0:
        print (ATAS)
        ser.write(ATAS.encode('utf-8'))
        print (elapsed_time162)

def function163():
    if flag163 == 0:
        reset()
        print (elapsed_time163)
    
def function164():
    if flag164 == 0:
        print (KANAN)
        ser.write(KANAN.encode('utf-8'))
        print (elapsed_time164)

def function165():
    if flag165 == 0:
        reset()
        print (elapsed_time165)
    
def function166():
    for i in range (1):
        if flag166 == 0:
            if 'Cabai Mentah' in listt:
                print (elapsed_time166)
                print (listt)
                down()
                shower1() 
                break             
                
            elif 'Cabai Set-Matang' in listt:
                print (elapsed_time166)
                print (listt)
                down()
                shower2()
                break
                
            elif 'Cabai Matang' in listt:
                print (elapsed_time166)
                print (listt)
                down()
                shower3()
                break
                
            elif 'Cabai Busuk' in listt:
                print (elapsed_time166)
                print (listt)
                down()
                reset()
                break

            else:
                 down()
                 break

def function167():
    if flag167 == 0:
        reset()
        print (elapsed_time167)

def function168():
    if flag168 == 0:
        print (ATAS)
        ser.write(ATAS.encode('utf-8'))
        print (elapsed_time168)

def function169():
    if flag169 == 0:
        reset()
        print (elapsed_time169)
    
def function170():
    if flag170 == 0:
        print (KANAN)
        ser.write(KANAN.encode('utf-8'))
        print (elapsed_time170)

def function171():
    if flag171 == 0:
        reset()
        print (elapsed_time171)

#KANAN-3

def function172():
    if flag172 == 0:
        print (DEPAN)
        ser.write(DEPAN.encode('utf-8'))
        print (elapsed_time172)

def function173():
    if flag173 == 0:
        print (RESET)
        ser.write(RESET.encode('utf-8'))
        print (elapsed_time173)
    
def function174():
    if flag174 == 0:
        print (KIRI)
        ser.write(KIRI.encode('utf-8'))
        print (elapsed_time174)

def function175():
    if flag175 == 0:
        print (RESET)
        ser.write(RESET.encode('utf-8'))
        print (elapsed_time175)

def function176():
    for i in range (1):
        if flag176 == 0:
            if 'Cabai Mentah' in listt:
                print (elapsed_time176)
                print (listt)
                down()
                shower1()
                break              
                
            elif 'Cabai Set-Matang' in listt:
                print (elapsed_time176)
                print (listt)
                down()
                shower2()
                break
                
            elif 'Cabai Matang' in listt:
                print (elapsed_time176)
                print (listt)
                down()
                shower3()
                break
                
            elif 'Cabai Busuk' in listt:
                print (elapsed_time176)
                print (listt)
                down()
                reset()
                break

            else:
                 down()
                 break

def function177():
    if flag177 == 0:
        reset()
        print (elapsed_time177)

def function178():
    if flag178 == 0:
        print (ATAS)
        ser.write(ATAS.encode('utf-8'))
        print (elapsed_time178)

def function179():
    if flag179 == 0:
        reset()
        print (elapsed_time179)

def function180():
    if flag180 == 0:
        print (KIRI)
        ser.write(KIRI.encode('utf-8'))
        print (elapsed_time180)

def function181():
    if flag181 == 0:
        print (RESET)
        ser.write(RESET.encode('utf-8'))
        print (elapsed_time181)

def function182():
    for i in range (1):
        if flag182 == 0:
            if 'Cabai Mentah' in listt:
                print (elapsed_time182)
                print (listt)
                down()
                shower1() 
                break             
                
            elif 'Cabai Set-Matang' in listt:
                print (elapsed_time182)
                print (listt)
                down()
                shower2()
                break
                
            elif 'Cabai Matang' in listt:
                print (elapsed_time182)
                print (listt)
                down()
                shower3()
                break
                
            elif 'Cabai Busuk' in listt:
                print (elapsed_time182)
                print (listt)
                down()
                reset()
                break

            else:
                 down()
                 break

def function183():
    if flag183 == 0:
        reset()
        print (elapsed_time183)

def function184():
    if flag184 == 0:
        print (ATAS)
        ser.write(ATAS.encode('utf-8'))
        print (elapsed_time184)

def function185():
    if flag185 == 0:
        reset()
        print (elapsed_time185)

def function186():
    if flag186 == 0:
        print (KIRI)
        ser.write(KIRI.encode('utf-8'))
        print (elapsed_time186)

def function187():
    if flag187 == 0:
        reset()
        print (elapsed_time187)
        
def function188():
    for i in range (1):
        if flag188 == 0:
            if 'Cabai Mentah' in listt:
                print (elapsed_time188)
                print (listt)
                down()
                shower1() 
                break             
                
            elif 'Cabai Set-Matang' in listt:
                print (elapsed_time188)
                print (listt)
                down()
                shower2()
                break
                
            elif 'Cabai Matang' in listt:
                print (elapsed_time188)
                print (listt)
                down()
                shower3()
                break
                
            elif 'Cabai Busuk' in listt:
                print (elapsed_time188)
                print (listt)
                down()
                reset()
                break

            else:
                 down()
                 break

def function189():
    if flag189 == 0:
        reset()
        print (elapsed_time189)

def function190():
    if flag190 == 0:
        print (ATAS)
        ser.write(ATAS.encode('utf-8'))
        print (elapsed_time190)

def function191():
    if flag191 == 0:
        reset()
        print (elapsed_time191)
    
def function192():
    if flag192 == 0:
        print (KIRI)
        ser.write(KIRI.encode('utf-8'))
        print (elapsed_time192)

def function193():
    if flag193 == 0:
        reset()
        print (elapsed_time193)
    
def function194():
    for i in range (1):
        if flag194 == 0:
            if 'Cabai Mentah' in listt:
                print (elapsed_time194)
                print (listt)
                down()
                shower1() 
                break             
                
            elif 'Cabai Set-Matang' in listt:
                print (elapsed_time194)
                print (listt)
                down()
                shower2()
                break
                
            elif 'Cabai Matang' in listt:
                print (elapsed_time194)
                print (listt)
                down()
                shower3()
                break
                
            elif 'Cabai Busuk' in listt:
                print (elapsed_time194)
                print (listt)
                down()
                reset()
                break

            else:
                 down()
                 break

def function195():
    if flag195 == 0:
        reset()
        print (elapsed_time195)

def function196():
    if flag196 == 0:
        print (ATAS)
        ser.write(ATAS.encode('utf-8'))
        print (elapsed_time196)

def function197():
    if flag197 == 0:
        reset()
        print (elapsed_time197)
    
def function198():
    if flag198 == 0:
        print (KIRI)
        ser.write(KIRI.encode('utf-8'))
        print (elapsed_time198)

def function199():
    if flag199 == 0:
        reset()
        print (elapsed_time199)
    
def function200():
    for i in range (1):
        if flag200 == 0:
            if 'Cabai Mentah' in listt:
                print (elapsed_time200)
                print (listt)
                down()
                shower1() 
                break             
                
            elif 'Cabai Set-Matang' in listt:
                print (elapsed_time200)
                print (listt)
                down()
                shower2()
                break
                
            elif 'Cabai Matang' in listt:
                print (elapsed_time200)
                print (listt)
                down()
                shower3()
                break
                
            elif 'Cabai Busuk' in listt:
                print (elapsed_time200)
                print (listt)
                down()
                reset()
                break

            else:
                 down()
                 break
        
def function201():
    if flag201 == 0:
        reset()
        print (elapsed_time201)

def function202():
    if flag202 == 0:
        print (ATAS)
        ser.write(ATAS.encode('utf-8'))
        print (elapsed_time202)

def function203():
    if flag203 == 0:
        reset()
        print (elapsed_time203)
    
def function204():
    if flag204 == 0:
        print (KIRI)
        ser.write(KIRI.encode('utf-8'))
        print (elapsed_time204)

def function205():
    if flag205 == 0:
        reset()
        print (elapsed_time205)
    
#KIRI-3

####

#DELTA-T
#KANAN-1
#DELTA-T
d1     = 2000
d2     = 7000#RES 10
d3     = 23000#F 16
d4     = 25000#RES 2
d5     = 35000#R 10
d6     = 50000#RES 2
d7     = 77000#DS 27
d8     = 79000#RES 2
d9     = 100000#U 21
d10    = 102000#RES 2
d11    = 112000#R 10
d12    = 122000#RES 2
d13    = 149000#DS 25
d14    = 151000#RES
d15    = 172000#U
d16    = 174000#
d17    = 184000#K
d18    = 194000#R
d19    = 221000#d
d20    = 223000#r
d21    = 244000#U
d22    = 246000
d23    = 256000
d24    = 266000
d25    = 293000
d26    = 295000
d27    = 316000
d28    = 318000
d29    = 328000
d30    = 338000
d31    = 365000
d32    = 367000
d33    = 388000
d34    = 390000
d35    = 400000

#KIRI-1

d36    = 402000
d37    = 418000#f
d38    = 420000
d39    = 430000
d40    = 440000
d41    = 467000#d
d42    = 469000
d43    = 490000
d44    = 492000
d45    = 502000#l
d46    = 512000
d47    = 539000
d48    = 541000
d49    = 562000
d50    = 564000
d51    = 574000
d52    = 584000
d53    = 611000
d54    = 613000
d55    = 634000
d56    = 636000
d57    = 646000
d58    = 656000
d59    = 683000
d60    = 685000
d61    = 706000
d62    = 708000
d63    = 718000
d64    = 728000
d65    = 755000
d66    = 757000
d67    = 778000
d68    = 780000
d69    = 790000

#KANAN-2
d70    = 792000
d71    = 808000
d72    = 810000
d73    = 820000
d74    = 830000
d75    = 857000
d76    = 859000
d77    = 880000
d78    = 882000
d79    = 892000
d80    = 902000
d81    = 929000
d82    = 931000
d83    = 952000
d84    = 954000
d85    = 964000
d86    = 974000
d87    = 1001000
d88    = 1003000
d89    = 1024000
d90    = 1026000
d91    = 1036000
d92    = 1046000
d93    = 1073000
d94    = 1075000
d95    = 1096000
d96    = 1098000
d97    = 1108000
d98    = 1118000
d99    = 1145000
d100   = 1157000
d101   = 1178000
d102   = 1180000
d103   = 1190000

#KIRI
d104   = 1192000
d105   = 1208000
d106   = 1210000
d107   = 1220000
d108   = 1230000
d109   = 1257000
d110   = 1259000
d111   = 1280000
d112   = 1282000
d113   = 1292000
d114   = 1302000
d115   = 1329000
d116   = 1331000
d117   = 1352000
d118   = 1354000
d119   = 1364000
d120   = 1374000
d121   = 1401000
d122   = 1403000
d123   = 1425000
d124   = 1427000
d125   = 1437000
d126   = 1447000
d127   = 1474000
d128   = 1476000
d129   = 1497000
d130   = 1499000
d131   = 1509000
d132   = 1519000
d133   = 1546000
d134   = 1548000
d135   = 1569000
d136   = 1571000
d137   = 1581000


d138   = 1583000
d139   = 1599000
d140   = 1601000
d141   = 1611000
d142   = 1621000
d143   = 1648000
d144   = 1650000
d145   = 1671000
d146   = 1673000
d147   = 1683000
d148   = 1693000
d149   = 1720000
d150   = 1722000
d151   = 1743000
d152   = 1745000
d153   = 1755000
d154   = 1765000
d155   = 1792000
d156   = 1794000
d157   = 1815000
d158   = 1817000
d159   = 1827000
d160   = 1837000
d161   = 1864000
d162   = 1866000
d163   = 1887000
d164   = 1889000
d165   = 1899000
d166   = 1909000
d167   = 1936000
d168   = 1938000
d169   = 1959000
d170   = 1961000
d171   = 1971000


d172   = 1973000
d173   = 1989000
d174   = 1991000
d175   = 2001000
d176   = 2011000
d177   = 2038000
d178   = 2040000
d179   = 2061000
d180   = 2063000
d181   = 2073000
d182   = 2083000
d183   = 2110000
d184   = 2112000
d185   = 2133000
d186   = 2135000
d187   = 2145000
d188   = 2155000
d189   = 2182000
d190   = 2184000
d191   = 2205000
d192   = 2207000
d193   = 2217000
d194   = 2227000
d195   = 2254000
d196   = 2256000
d197   = 2277000
d198   = 2279000
d199   = 2289000
d200   = 2299000
d201   = 2326000
d202   = 2329000
d203   = 2350000
d204   = 2352000
d205   = 2362000

#Results
spot = 0
cap = cv2.VideoCapture(-1)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640) # 1cm / 32 pixel
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480) # 1cm / 24 pixel
fps = cap.get(cv2.CAP_PROP_FPS)
fps_start_time = 0
fps = 0

def millis():
    return int(time.perf_counter_ns() // 1000000) 

start = millis()

flags     = 0
flag1     = 0
flag2     = 0
flag3     = 0
flag4     = 0
flag5     = 0
flag6     = 0
flag7     = 0
flag8     = 0
flag9     = 0
flag10    = 0
flag11    = 0
flag12    = 0
flag13    = 0
flag14    = 0
flag15    = 0
flag16    = 0
flag17    = 0
flag18    = 0
flag19    = 0
flag20    = 0
flag21    = 0
flag22    = 0
flag23    = 0
flag24    = 0
flag25    = 0
flag26    = 0
flag27    = 0
flag28    = 0
flag29    = 0
flag30    = 0
flag31    = 0
flag32    = 0
flag33    = 0
flag34    = 0
flag35    = 0
flag36    = 0
flag37    = 0
flag38    = 0
flag39    = 0
flag40    = 0
flag41    = 0
flag42    = 0
flag43    = 0
flag44    = 0
flag45    = 0
flag46    = 0
flag47    = 0
flag48    = 0
flag49    = 0
flag50    = 0
flag51    = 0
flag52    = 0
flag53    = 0
flag54    = 0
flag55    = 0
flag56    = 0
flag57    = 0
flag58    = 0
flag59    = 0
flag60    = 0
flag61    = 0
flag62    = 0
flag63    = 0
flag64    = 0
flag65    = 0
flag66    = 0
flag67    = 0
flag68    = 0
flag69    = 0
flag70    = 0
flag71    = 0
flag72    = 0
flag73    = 0
flag74    = 0
flag75    = 0
flag76    = 0
flag77    = 0
flag78    = 0
flag79    = 0
flag80    = 0
flag81    = 0
flag82    = 0
flag83    = 0
flag84    = 0
flag85    = 0
flag86    = 0
flag87    = 0
flag88    = 0
flag89    = 0
flag90    = 0
flag91    = 0
flag92    = 0
flag93    = 0
flag94    = 0
flag95    = 0
flag96    = 0
flag97    = 0
flag98    = 0
flag99    = 0
flag100   = 0
flag101   = 0
flag102   = 0
flag103   = 0
flag104   = 0
flag105   = 0
flag106   = 0
flag107   = 0
flag108   = 0
flag109   = 0
flag110   = 0
flag111   = 0
flag112   = 0
flag113   = 0
flag114   = 0
flag115   = 0
flag116   = 0
flag117   = 0
flag118   = 0
flag119   = 0
flag120   = 0
flag121   = 0
flag122   = 0
flag123   = 0
flag124   = 0
flag125   = 0
flag126   = 0
flag127   = 0
flag128   = 0
flag129   = 0
flag130   = 0
flag131   = 0
flag132   = 0
flag133   = 0
flag134   = 0
flag135   = 0
flag136   = 0
flag137   = 0
flag138   = 0
flag139   = 0
flag140   = 0
flag141   = 0
flag142   = 0
flag143   = 0
flag144   = 0
flag145   = 0
flag146   = 0
flag147   = 0
flag148   = 0
flag149   = 0
flag150   = 0
flag151   = 0
flag152   = 0
flag153   = 0
flag154   = 0
flag155   = 0
flag156   = 0
flag157   = 0
flag158   = 0
flag159   = 0
flag160   = 0
flag161   = 0
flag162   = 0
flag163   = 0
flag164   = 0
flag165   = 0
flag166   = 0
flag167   = 0
flag168   = 0
flag169   = 0
flag170   = 0
flag171   = 0
flag172   = 0
flag173   = 0
flag174   = 0
flag175   = 0
flag176   = 0
flag177   = 0
flag178   = 0
flag179   = 0
flag180   = 0
flag181   = 0
flag182   = 0
flag183   = 0
flag184   = 0
flag185   = 0
flag186   = 0
flag187   = 0
flag188   = 0
flag189   = 0
flag190   = 0
flag191   = 0
flag192   = 0
flag193   = 0
flag194   = 0
flag195   = 0
flag196   = 0
flag197   = 0
flag198   = 0
flag199   = 0
flag200   = 0
flag201   = 0
flag202   = 0
flag203   = 0
flag204   = 0
flag205   = 0

last_execute_tS      = start
last_execute_t1      = start
last_execute_t2      = start
last_execute_t3      = start
last_execute_t4      = start
last_execute_t5      = start
last_execute_t6      = start
last_execute_t7      = start
last_execute_t8      = start
last_execute_t9      = start
last_execute_t10     = start
last_execute_t11     = start
last_execute_t12     = start
last_execute_t13     = start
last_execute_t14     = start
last_execute_t15     = start
last_execute_t16     = start
last_execute_t17     = start
last_execute_t18     = start
last_execute_t19     = start
last_execute_t20     = start
last_execute_t21     = start
last_execute_t22     = start
last_execute_t23     = start
last_execute_t24     = start
last_execute_t25     = start
last_execute_t26     = start
last_execute_t27     = start
last_execute_t28     = start
last_execute_t29     = start
last_execute_t30     = start
last_execute_t31     = start
last_execute_t32     = start
last_execute_t33     = start
last_execute_t34     = start
last_execute_t35     = start
last_execute_t36     = start
last_execute_t37     = start
last_execute_t38     = start
last_execute_t39     = start
last_execute_t40     = start
last_execute_t41     = start
last_execute_t42     = start
last_execute_t43     = start
last_execute_t44     = start
last_execute_t45     = start
last_execute_t46     = start
last_execute_t47     = start
last_execute_t48     = start
last_execute_t49     = start
last_execute_t50     = start
last_execute_t51     = start
last_execute_t52     = start
last_execute_t53     = start
last_execute_t54     = start
last_execute_t55     = start
last_execute_t56     = start
last_execute_t57     = start
last_execute_t58     = start
last_execute_t59     = start
last_execute_t60     = start
last_execute_t61     = start
last_execute_t62     = start
last_execute_t63     = start
last_execute_t64     = start
last_execute_t65     = start
last_execute_t66     = start
last_execute_t67     = start
last_execute_t68     = start
last_execute_t69     = start
last_execute_t70     = start
last_execute_t71     = start
last_execute_t72     = start
last_execute_t73     = start
last_execute_t74     = start
last_execute_t75     = start
last_execute_t76     = start
last_execute_t77     = start
last_execute_t78     = start
last_execute_t79     = start
last_execute_t80     = start
last_execute_t81     = start
last_execute_t82     = start
last_execute_t83     = start
last_execute_t84     = start
last_execute_t85     = start
last_execute_t86     = start
last_execute_t87     = start
last_execute_t88     = start
last_execute_t89     = start
last_execute_t90     = start
last_execute_t91     = start
last_execute_t92     = start
last_execute_t93     = start
last_execute_t94     = start
last_execute_t95     = start
last_execute_t96     = start
last_execute_t97     = start
last_execute_t98     = start
last_execute_t99     = start
last_execute_t100    = start
last_execute_t101    = start
last_execute_t102    = start
last_execute_t103    = start
last_execute_t104    = start
last_execute_t105    = start
last_execute_t106    = start
last_execute_t107    = start
last_execute_t108    = start
last_execute_t109    = start
last_execute_t110    = start
last_execute_t111    = start
last_execute_t112    = start
last_execute_t113    = start
last_execute_t114    = start
last_execute_t115    = start
last_execute_t116    = start
last_execute_t117    = start
last_execute_t118    = start
last_execute_t119    = start
last_execute_t120    = start
last_execute_t121    = start
last_execute_t122    = start
last_execute_t123    = start
last_execute_t124    = start
last_execute_t125    = start
last_execute_t126    = start
last_execute_t127    = start
last_execute_t128    = start
last_execute_t129    = start
last_execute_t130    = start
last_execute_t131    = start
last_execute_t132    = start
last_execute_t133    = start
last_execute_t134    = start
last_execute_t135    = start
last_execute_t136    = start
last_execute_t137    = start
last_execute_t138    = start
last_execute_t139    = start
last_execute_t140    = start
last_execute_t141    = start
last_execute_t142    = start
last_execute_t143    = start
last_execute_t144    = start
last_execute_t145    = start
last_execute_t146    = start
last_execute_t147    = start
last_execute_t148    = start
last_execute_t149    = start
last_execute_t150    = start
last_execute_t151    = start
last_execute_t152    = start
last_execute_t153    = start
last_execute_t154    = start
last_execute_t155    = start
last_execute_t156    = start
last_execute_t157    = start
last_execute_t158    = start
last_execute_t159    = start
last_execute_t160    = start
last_execute_t161    = start
last_execute_t162    = start
last_execute_t163    = start
last_execute_t164    = start
last_execute_t165    = start
last_execute_t166    = start
last_execute_t167    = start
last_execute_t168    = start
last_execute_t169    = start
last_execute_t170    = start
last_execute_t171    = start
last_execute_t172    = start
last_execute_t173    = start
last_execute_t174    = start
last_execute_t175    = start
last_execute_t176    = start
last_execute_t177    = start
last_execute_t178    = start
last_execute_t179    = start
last_execute_t180    = start
last_execute_t181    = start
last_execute_t182    = start
last_execute_t183    = start
last_execute_t184    = start
last_execute_t185    = start
last_execute_t186    = start
last_execute_t187    = start
last_execute_t188    = start
last_execute_t189    = start
last_execute_t190    = start
last_execute_t191    = start
last_execute_t192    = start
last_execute_t193    = start
last_execute_t194    = start
last_execute_t195    = start
last_execute_t196    = start
last_execute_t197    = start
last_execute_t198    = start
last_execute_t199    = start
last_execute_t200    = start
last_execute_t201    = start
last_execute_t202    = start
last_execute_t203    = start
last_execute_t204    = start
last_execute_t205    = start

ser.flush()
while cap.isOpened() & ser.is_open:

    ret, frame = cap.read()
    fps_end_time = time.time()
    fps_diff = fps_end_time - fps_start_time
    fps = 1/(fps_diff)
    fps_start_time = fps_end_time
    
    fps_text = "FPS: {:.2f}".format(fps)
    
    cv2.putText(frame, fps_text, (5,30), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 255), 1)
    results = model(frame)
    results.xyxy[0]
    listt = results.pandas().xyxy[0]['name'].tolist()
    list2 = results.pandas().xyxy[0]
    info2 = results.pandas().xyxy[0].to_dict(orient = "records")

    cv2.imshow('Cam', np.squeeze(results.render()))
    
    current_time = millis()
    elapsed_timeS      = current_time - last_execute_tS
    elapsed_time1      = current_time - last_execute_t1
    elapsed_time2      = current_time - last_execute_t2
    elapsed_time3      = current_time - last_execute_t3
    elapsed_time4      = current_time - last_execute_t4
    elapsed_time5      = current_time - last_execute_t5
    elapsed_time6      = current_time - last_execute_t6
    elapsed_time7      = current_time - last_execute_t7
    elapsed_time8      = current_time - last_execute_t8
    elapsed_time9      = current_time - last_execute_t9
    elapsed_time10     = current_time - last_execute_t10
    elapsed_time11     = current_time - last_execute_t11
    elapsed_time12     = current_time - last_execute_t12
    elapsed_time13     = current_time - last_execute_t13
    elapsed_time14     = current_time - last_execute_t14
    elapsed_time15     = current_time - last_execute_t15
    elapsed_time16     = current_time - last_execute_t16
    elapsed_time17     = current_time - last_execute_t17
    elapsed_time18     = current_time - last_execute_t18
    elapsed_time19     = current_time - last_execute_t19
    elapsed_time20     = current_time - last_execute_t20
    elapsed_time21     = current_time - last_execute_t21
    elapsed_time22     = current_time - last_execute_t22
    elapsed_time23     = current_time - last_execute_t23
    elapsed_time24     = current_time - last_execute_t24
    elapsed_time25     = current_time - last_execute_t25
    elapsed_time26     = current_time - last_execute_t26
    elapsed_time27     = current_time - last_execute_t27
    elapsed_time28     = current_time - last_execute_t28
    elapsed_time29     = current_time - last_execute_t29
    elapsed_time30     = current_time - last_execute_t30
    elapsed_time31     = current_time - last_execute_t31
    elapsed_time32     = current_time - last_execute_t32
    elapsed_time33     = current_time - last_execute_t33
    elapsed_time34     = current_time - last_execute_t34
    elapsed_time35     = current_time - last_execute_t35
    elapsed_time36     = current_time - last_execute_t36
    elapsed_time37     = current_time - last_execute_t37
    elapsed_time38     = current_time - last_execute_t38
    elapsed_time39     = current_time - last_execute_t39
    elapsed_time40     = current_time - last_execute_t40
    elapsed_time41     = current_time - last_execute_t41
    elapsed_time42     = current_time - last_execute_t42
    elapsed_time43     = current_time - last_execute_t43
    elapsed_time44     = current_time - last_execute_t44
    elapsed_time45     = current_time - last_execute_t45
    elapsed_time46     = current_time - last_execute_t46
    elapsed_time47     = current_time - last_execute_t47
    elapsed_time48     = current_time - last_execute_t48
    elapsed_time49     = current_time - last_execute_t49
    elapsed_time50     = current_time - last_execute_t50
    elapsed_time51     = current_time - last_execute_t51
    elapsed_time52     = current_time - last_execute_t52
    elapsed_time53     = current_time - last_execute_t53
    elapsed_time54     = current_time - last_execute_t54
    elapsed_time55     = current_time - last_execute_t55
    elapsed_time56     = current_time - last_execute_t56
    elapsed_time57     = current_time - last_execute_t57
    elapsed_time58     = current_time - last_execute_t58
    elapsed_time59     = current_time - last_execute_t59
    elapsed_time60     = current_time - last_execute_t60
    elapsed_time61     = current_time - last_execute_t61
    elapsed_time62     = current_time - last_execute_t62
    elapsed_time63     = current_time - last_execute_t63
    elapsed_time64     = current_time - last_execute_t64
    elapsed_time65     = current_time - last_execute_t65
    elapsed_time66     = current_time - last_execute_t66
    elapsed_time67     = current_time - last_execute_t67
    elapsed_time68     = current_time - last_execute_t68
    elapsed_time69     = current_time - last_execute_t69
    elapsed_time70     = current_time - last_execute_t70
    elapsed_time71     = current_time - last_execute_t71
    elapsed_time72     = current_time - last_execute_t72
    elapsed_time73     = current_time - last_execute_t73
    elapsed_time74     = current_time - last_execute_t74
    elapsed_time75     = current_time - last_execute_t75
    elapsed_time76     = current_time - last_execute_t76
    elapsed_time77     = current_time - last_execute_t77
    elapsed_time78     = current_time - last_execute_t78
    elapsed_time79     = current_time - last_execute_t79
    elapsed_time80     = current_time - last_execute_t80
    elapsed_time81     = current_time - last_execute_t81
    elapsed_time82     = current_time - last_execute_t82
    elapsed_time83     = current_time - last_execute_t83
    elapsed_time84     = current_time - last_execute_t84
    elapsed_time85     = current_time - last_execute_t85
    elapsed_time86     = current_time - last_execute_t86
    elapsed_time87     = current_time - last_execute_t87
    elapsed_time88     = current_time - last_execute_t88
    elapsed_time89     = current_time - last_execute_t89
    elapsed_time90     = current_time - last_execute_t90
    elapsed_time91     = current_time - last_execute_t91
    elapsed_time92     = current_time - last_execute_t92
    elapsed_time93     = current_time - last_execute_t93
    elapsed_time94     = current_time - last_execute_t94
    elapsed_time95     = current_time - last_execute_t95
    elapsed_time96     = current_time - last_execute_t96
    elapsed_time97     = current_time - last_execute_t97
    elapsed_time98     = current_time - last_execute_t98
    elapsed_time99     = current_time - last_execute_t99
    elapsed_time100    = current_time - last_execute_t100
    elapsed_time101    = current_time - last_execute_t101
    elapsed_time102    = current_time - last_execute_t102
    elapsed_time103    = current_time - last_execute_t103
    elapsed_time104    = current_time - last_execute_t104
    elapsed_time105    = current_time - last_execute_t105
    elapsed_time106    = current_time - last_execute_t106
    elapsed_time107    = current_time - last_execute_t107
    elapsed_time108    = current_time - last_execute_t108
    elapsed_time109    = current_time - last_execute_t109
    elapsed_time110    = current_time - last_execute_t110
    elapsed_time111    = current_time - last_execute_t111
    elapsed_time112    = current_time - last_execute_t112
    elapsed_time113    = current_time - last_execute_t113
    elapsed_time114    = current_time - last_execute_t114
    elapsed_time115    = current_time - last_execute_t115
    elapsed_time116    = current_time - last_execute_t116
    elapsed_time117    = current_time - last_execute_t117
    elapsed_time118    = current_time - last_execute_t118
    elapsed_time119    = current_time - last_execute_t119
    elapsed_time120    = current_time - last_execute_t120
    elapsed_time121    = current_time - last_execute_t121
    elapsed_time122    = current_time - last_execute_t122
    elapsed_time123    = current_time - last_execute_t123
    elapsed_time124    = current_time - last_execute_t124
    elapsed_time125    = current_time - last_execute_t125
    elapsed_time126    = current_time - last_execute_t126
    elapsed_time127    = current_time - last_execute_t127
    elapsed_time128    = current_time - last_execute_t128
    elapsed_time129    = current_time - last_execute_t129
    elapsed_time130    = current_time - last_execute_t130
    elapsed_time131    = current_time - last_execute_t131
    elapsed_time132    = current_time - last_execute_t132
    elapsed_time133    = current_time - last_execute_t133
    elapsed_time134    = current_time - last_execute_t134
    elapsed_time135    = current_time - last_execute_t135
    elapsed_time136    = current_time - last_execute_t136
    elapsed_time137    = current_time - last_execute_t137
    elapsed_time138    = current_time - last_execute_t138
    elapsed_time139    = current_time - last_execute_t139
    elapsed_time140    = current_time - last_execute_t140
    elapsed_time141    = current_time - last_execute_t141
    elapsed_time142    = current_time - last_execute_t142
    elapsed_time143    = current_time - last_execute_t143
    elapsed_time144    = current_time - last_execute_t144
    elapsed_time145    = current_time - last_execute_t145
    elapsed_time146    = current_time - last_execute_t146
    elapsed_time147    = current_time - last_execute_t147
    elapsed_time148    = current_time - last_execute_t148
    elapsed_time149    = current_time - last_execute_t149
    elapsed_time150    = current_time - last_execute_t150
    elapsed_time151    = current_time - last_execute_t151
    elapsed_time152    = current_time - last_execute_t152
    elapsed_time153    = current_time - last_execute_t153
    elapsed_time154    = current_time - last_execute_t154
    elapsed_time155    = current_time - last_execute_t155
    elapsed_time156    = current_time - last_execute_t156
    elapsed_time157    = current_time - last_execute_t157
    elapsed_time158    = current_time - last_execute_t158
    elapsed_time159    = current_time - last_execute_t159
    elapsed_time160    = current_time - last_execute_t160
    elapsed_time161    = current_time - last_execute_t161
    elapsed_time162    = current_time - last_execute_t162
    elapsed_time163    = current_time - last_execute_t163
    elapsed_time164    = current_time - last_execute_t164
    elapsed_time165    = current_time - last_execute_t165
    elapsed_time166    = current_time - last_execute_t166
    elapsed_time167    = current_time - last_execute_t167
    elapsed_time168    = current_time - last_execute_t168
    elapsed_time169    = current_time - last_execute_t169
    elapsed_time170    = current_time - last_execute_t170
    elapsed_time171    = current_time - last_execute_t171
    elapsed_time172    = current_time - last_execute_t172
    elapsed_time173    = current_time - last_execute_t173
    elapsed_time174    = current_time - last_execute_t174
    elapsed_time175    = current_time - last_execute_t175
    elapsed_time176    = current_time - last_execute_t176
    elapsed_time177    = current_time - last_execute_t177
    elapsed_time178    = current_time - last_execute_t178
    elapsed_time179    = current_time - last_execute_t179
    elapsed_time180    = current_time - last_execute_t180
    elapsed_time181    = current_time - last_execute_t181
    elapsed_time182    = current_time - last_execute_t182
    elapsed_time183    = current_time - last_execute_t183
    elapsed_time184    = current_time - last_execute_t184
    elapsed_time185    = current_time - last_execute_t185
    elapsed_time186    = current_time - last_execute_t186
    elapsed_time187    = current_time - last_execute_t187
    elapsed_time188    = current_time - last_execute_t188
    elapsed_time189    = current_time - last_execute_t189
    elapsed_time190    = current_time - last_execute_t190
    elapsed_time191    = current_time - last_execute_t191
    elapsed_time192    = current_time - last_execute_t192
    elapsed_time193    = current_time - last_execute_t193
    elapsed_time194    = current_time - last_execute_t194
    elapsed_time195    = current_time - last_execute_t195
    elapsed_time196    = current_time - last_execute_t196
    elapsed_time197    = current_time - last_execute_t197
    elapsed_time198    = current_time - last_execute_t198
    elapsed_time199    = current_time - last_execute_t199
    elapsed_time200    = current_time - last_execute_t200
    elapsed_time201    = current_time - last_execute_t201
    elapsed_time202    = current_time - last_execute_t202
    elapsed_time203    = current_time - last_execute_t203
    elapsed_time204    = current_time - last_execute_t204
    elapsed_time205    = current_time - last_execute_t205

    print(elapsed_time1)         

    for i in range (1):
            if  elapsed_time1 >= d1:
                function1()
                if elapsed_time1 >= d1:
                    flag1 = 1
                    break
                last_execute_t1 = current_time          
            break
    
    for i in range (1):
            if  elapsed_time2 >= d2:
                function2()                
                if elapsed_time2 >= d2:
                    flag2 = 1
                    break
                last_execute_t2 = current_time
            break
    
    for i in range (1):
            if  elapsed_time3 >= d3:
                function3()
                if elapsed_time3 >= d3:
                    flag3 = 1
                    break
                last_execute_t3 = current_time
            break
    
    for i in range (1):
            if  elapsed_time4 >= d4:
                function4()
                if elapsed_time4 >= d4:
                    flag4 = 1
                    break
                last_execute_t4 = current_time          
            break
    
    for i in range (1):
            if  elapsed_time5 >= d5:
                function5()                
                if elapsed_time5 >= d5:
                    flag5 = 1
                    break
                last_execute_t5 = current_time
            break
    
    for i in range (1):
            if  elapsed_time6 >= d6:
                function6()
                if elapsed_time6 >= d6:
                    flag6 = 1
                    break
                last_execute_t6 = current_time
            break
    
    for i in range (1):
            if  elapsed_time7 >= d7:
                function7()                
                if elapsed_time7 >= d7:
                    flag7 = 1
                    break
                last_execute_t7 = current_time
            break
    
    for i in range (1):
            if  elapsed_time8 >= d8:
                function8()
                if elapsed_time8 >= d8:
                    flag8 = 1
                    break
                last_execute_t8 = current_time
            break
    
    for i in range (1):
            if  elapsed_time9 >= d9:
                function9()
                if elapsed_time9 >= d9:
                    flag9 = 1
                    break
                last_execute_t9 = current_time          
            break
    
    for i in range (1):
            if  elapsed_time10 >= d10:
                function10()                
                if elapsed_time10 >= d10:
                    flag10 = 1
                    break
                last_execute_t10 = current_time
            break
    #10
    for i in range (1):
            if  elapsed_time11 >= d11:
                function11()
                if elapsed_time11 >= d11:
                    flag11 = 1
                    break
                last_execute_t11 = current_time          
            break
    
    for i in range (1):
            if  elapsed_time12 >= d12:
                function12()                
                if elapsed_time12 >= d12:
                    flag12 = 1
                    break
                last_execute_t12 = current_time
            break
    
    for i in range (1):
            if  elapsed_time13 >= d13:
                function13()
                if elapsed_time13 >= d13:
                    flag13 = 1
                    break
                last_execute_t13 = current_time
            break
    
    for i in range (1):
            if  elapsed_time14 >= d14:
                function14()
                if elapsed_time14 >= d14:
                    flag14 = 1
                    break
                last_execute_t14 = current_time          
            break
    
    for i in range (1):
            if  elapsed_time15 >= d15:
                function15()                
                if elapsed_time15 >= d15:
                    flag15 = 1
                    break
                last_execute_t15 = current_time
            break
    
    for i in range (1):
            if  elapsed_time16 >= d16:
                function16()
                if elapsed_time16 >= d16:
                    flag16 = 1
                    break
                last_execute_t16 = current_time
            break
    
    for i in range (1):
            if  elapsed_time17 >= d17:
                function17()                
                if elapsed_time17 >= d17:
                    flag17 = 1
                    break
                last_execute_t17 = current_time
            break
    
    for i in range (1):
            if  elapsed_time18 >= d18:
                function18()
                if elapsed_time18 >= d18:
                    flag18 = 1
                    break
                last_execute_t18 = current_time
            break
    
    for i in range (1):
            if  elapsed_time19 >= d19:
                function19()
                if elapsed_time19 >= d19:
                    flag19 = 1
                    break
                last_execute_t19 = current_time          
            break
    
    for i in range (1):
            if  elapsed_time20 >= d20:
                function20()                
                if elapsed_time20 >= d20:
                    flag20 = 1
                    break
                last_execute_t20 = current_time
            break
    #20
    for i in range (1):
            if  elapsed_time21 >= d21:
                function21()
                if elapsed_time21 >= d21:
                    flag21 = 1
                    break
                last_execute_t21 = current_time          
            break
    
    for i in range (1):
            if  elapsed_time22 >= d22:
                function22()                
                if elapsed_time22 >= d22:
                    flag22 = 1
                    break
                last_execute_t22 = current_time
            break
    
    for i in range (1):
            if  elapsed_time23 >= d23:
                function23()
                if elapsed_time23 >= d23:
                    flag23 = 1
                    break
                last_execute_t23 = current_time
            break
    
    for i in range (1):
            if  elapsed_time24 >= d24:
                function24()
                if elapsed_time24 >= d24:
                    flag24 = 1
                    break
                last_execute_t24 = current_time          
            break
    
    for i in range (1):
            if  elapsed_time25 >= d25:
                function25()                
                if elapsed_time25 >= d25:
                    flag25 = 1
                    break
                last_execute_t25 = current_time
            break
    
    for i in range (1):
            if  elapsed_time26 >= d26:
                function26()
                if elapsed_time26 >= d26:
                    flag26 = 1
                    break
                last_execute_t26 = current_time
            break
    
    for i in range (1):
            if  elapsed_time27 >= d27:
                function27()                
                if elapsed_time27 >= d27:
                    flag27 = 1
                    break
                last_execute_t27 = current_time
            break
    
    for i in range (1):
            if  elapsed_time28 >= d28:
                function28()
                if elapsed_time28 >= d28:
                    flag28 = 1
                    break
                last_execute_t28 = current_time
            break
    
    for i in range (1):
            if  elapsed_time29 >= d29:
                function29()
                if elapsed_time29 >= d29:
                    flag29 = 1
                    break
                last_execute_t29 = current_time          
            break
    
    for i in range (1):
            if  elapsed_time30 >= d30:
                function30()                
                if elapsed_time30 >= d30:
                    flag30 = 1
                    break
                last_execute_t30 = current_time
            break
    #30
    for i in range (1):
            if  elapsed_time31 >= d31:
                function31()
                if elapsed_time31 >= d31:
                    flag31 = 1
                    break
                last_execute_t31 = current_time          
            break
    
    for i in range (1):
            if  elapsed_time32 >= d32:
                function32()                
                if elapsed_time32 >= d32:
                    flag32 = 1
                    break
                last_execute_t32 = current_time
            break
    
    for i in range (1):
            if  elapsed_time33 >= d33:
                function33()
                if elapsed_time33 >= d33:
                    flag33 = 1
                    break
                last_execute_t33 = current_time
            break
    
    for i in range (1):
            if  elapsed_time34 >= d34:
                function34()
                if elapsed_time34 >= d34:
                    flag34 = 1
                    break
                last_execute_t34 = current_time          
            break
    
    for i in range (1):
            if  elapsed_time35 >= d35:
                function35()                
                if elapsed_time35 >= d35:
                    flag35 = 1
                    break
                last_execute_t35 = current_time
            break
    
    for i in range (1):
            if  elapsed_time36 >= d36:
                function36()
                if elapsed_time36 >= d36:
                    flag36 = 1
                    break
                last_execute_t36 = current_time
            break
    
    for i in range (1):
            if  elapsed_time37 >= d37:
                function37()                
                if elapsed_time37 >= d37:
                    flag37 = 1
                    break
                last_execute_t37 = current_time
            break
    
    for i in range (1):
            if  elapsed_time38 >= d38:
                function38()
                if elapsed_time38 >= d38:
                    flag38 = 1
                    break
                last_execute_t38 = current_time
            break
    
    for i in range (1):
            if  elapsed_time39 >= d39:
                function39()
                if elapsed_time39 >= d39:
                    flag39 = 1
                    break
                last_execute_t39 = current_time          
            break
    
    for i in range (1):
            if  elapsed_time40 >= d40:
                function40()                
                if elapsed_time40 >= d40:
                    flag40 = 1
                    break
                last_execute_t40 = current_time
            break
    #40
    for i in range (1):
            if  elapsed_time41 >= d41:
                function41()
                if elapsed_time41 >= d41:
                    flag41 = 1
                    break
                last_execute_t41 = current_time          
            break
    
    for i in range (1):
            if  elapsed_time42 >= d42:
                function42()                
                if elapsed_time42 >= d42:
                    flag42 = 1
                    break
                last_execute_t42 = current_time
            break
    
    for i in range (1):
            if  elapsed_time43 >= d43:
                function43()
                if elapsed_time43 >= d43:
                    flag43 = 1
                    break
                last_execute_t43 = current_time
            break
    
    for i in range (1):
            if  elapsed_time44 >= d44:
                function44()
                if elapsed_time44 >= d44:
                    flag44 = 1
                    break
                last_execute_t44 = current_time          
            break
    
    for i in range (1):
            if  elapsed_time45 >= d45:
                function45()                
                if elapsed_time45 >= d45:
                    flag45 = 1
                    break
                last_execute_t45 = current_time
            break
    
    for i in range (1):
            if  elapsed_time46 >= d46:
                function46()
                if elapsed_time46 >= d46:
                    flag46 = 1
                    break
                last_execute_t46 = current_time
            break
    
    for i in range (1):
            if  elapsed_time47 >= d47:
                function47()                
                if elapsed_time47 >= d47:
                    flag47 = 1
                    break
                last_execute_t47 = current_time
            break
    
    for i in range (1):
            if  elapsed_time48 >= d48:
                function48()
                if elapsed_time48 >= d48:
                    flag48 = 1
                    break
                last_execute_t48 = current_time
            break
    
    for i in range (1):
            if  elapsed_time49 >= d49:
                function49()
                if elapsed_time49 >= d49:
                    flag49 = 1
                    break
                last_execute_t49 = current_time          
            break
    
    for i in range (1):
            if  elapsed_time50 >= d50:
                function50()                
                if elapsed_time50 >= d50:
                    flag50 = 1
                    break
                last_execute_t50 = current_time
            break
    #50
    for i in range (1):
            if  elapsed_time51 >= d51:
                function51()
                if elapsed_time51 >= d51:
                    flag51 = 1
                    break
                last_execute_t51 = current_time          
            break
    
    for i in range (1):
            if  elapsed_time52 >= d52:
                function52()                
                if elapsed_time52 >= d52:
                    flag52 = 1
                    break
                last_execute_t52 = current_time
            break
    
    for i in range (1):
            if  elapsed_time53 >= d53:
                function53()
                if elapsed_time53 >= d53:
                    flag53 = 1
                    break
                last_execute_t53 = current_time
            break
    
    for i in range (1):
            if  elapsed_time54 >= d54:
                function54()
                if elapsed_time54 >= d54:
                    flag54 = 1
                    break
                last_execute_t54 = current_time          
            break
    
    for i in range (1):
            if  elapsed_time55 >= d55:
                function55()                
                if elapsed_time55 >= d55:
                    flag55 = 1
                    break
                last_execute_t55 = current_time
            break
    
    for i in range (1):
            if  elapsed_time56 >= d56:
                function56()
                if elapsed_time56 >= d56:
                    flag56 = 1
                    break
                last_execute_t56 = current_time
            break
    
    for i in range (1):
            if  elapsed_time57 >= d57:
                function57()                
                if elapsed_time57 >= d57:
                    flag57 = 1
                    break
                last_execute_t57 = current_time
            break
    
    for i in range (1):
            if  elapsed_time58 >= d58:
                function58()
                if elapsed_time58 >= d58:
                    flag58 = 1
                    break
                last_execute_t58 = current_time
            break
    
    for i in range (1):
            if  elapsed_time59 >= d59:
                function59()
                if elapsed_time59 >= d59:
                    flag59 = 1
                    break
                last_execute_t59 = current_time          
            break
    
    for i in range (1):
            if  elapsed_time60 >= d60:
                function60()                
                if elapsed_time60 >= d60:
                    flag60 = 1
                    break
                last_execute_t60 = current_time
            break
    #60
    for i in range (1):
            if  elapsed_time61 >= d61:
                function61()
                if elapsed_time61 >= d61:
                    flag61 = 1
                    break
                last_execute_t61 = current_time          
            break
    
    for i in range (1):
            if  elapsed_time62 >= d62:
                function62()                
                if elapsed_time62 >= d62:
                    flag62 = 1
                    break
                last_execute_t62 = current_time
            break
    
    for i in range (1):
            if  elapsed_time63 >= d63:
                function63()
                if elapsed_time63 >= d63:
                    flag63 = 1
                    break
                last_execute_t63 = current_time
            break
    
    for i in range (1):
            if  elapsed_time64 >= d64:
                function64()
                if elapsed_time64 >= d64:
                    flag64 = 1
                    break
                last_execute_t64 = current_time          
            break
    
    for i in range (1):
            if  elapsed_time65 >= d65:
                function65()                
                if elapsed_time65 >= d65:
                    flag65 = 1
                    break
                last_execute_t65 = current_time
            break
    
    for i in range (1):
            if  elapsed_time66 >= d66:
                function66()
                if elapsed_time66 >= d66:
                    flag66 = 1
                    break
                last_execute_t66 = current_time
            break
    
    for i in range (1):
            if  elapsed_time67 >= d67:
                function67()                
                if elapsed_time67 >= d67:
                    flag67 = 1
                    break
                last_execute_t67 = current_time
            break
    
    for i in range (1):
            if  elapsed_time68 >= d68:
                function68()
                if elapsed_time68 >= d68:
                    flag68 = 1
                    break
                last_execute_t68 = current_time
            break
    
    for i in range (1):
            if  elapsed_time69 >= d69:
                function69()
                if elapsed_time69 >= d69:
                    flag69 = 1
                    break
                last_execute_t69 = current_time          
            break
    
    for i in range (1):
            if  elapsed_time70 >= d70:
                function70()                
                if elapsed_time70 >= d70:
                    flag70 = 1
                    break
                last_execute_t70 = current_time
            break
    #70
    for i in range (1):
            if  elapsed_time71 >= d71:
                function71()
                if elapsed_time71 >= d71:
                    flag71 = 1
                    break
                last_execute_t71 = current_time          
            break
    
    for i in range (1):
            if  elapsed_time72 >= d72:
                function72()                
                if elapsed_time72 >= d72:
                    flag72 = 1
                    break
                last_execute_t72 = current_time
            break
    
    for i in range (1):
            if  elapsed_time73 >= d73:
                function73()
                if elapsed_time73 >= d73:
                    flag73 = 1
                    break
                last_execute_t73 = current_time
            break
    
    for i in range (1):
            if  elapsed_time74 >= d74:
                function74()
                if elapsed_time74 >= d74:
                    flag74 = 1
                    break
                last_execute_t74 = current_time          
            break
    
    for i in range (1):
            if  elapsed_time75 >= d75:
                function75()                
                if elapsed_time75 >= d75:
                    flag75 = 1
                    break
                last_execute_t75 = current_time
            break
    
    for i in range (1):
            if  elapsed_time76 >= d76:
                function76()
                if elapsed_time76 >= d76:
                    flag76 = 1
                    break
                last_execute_t76 = current_time
            break
    
    for i in range (1):
            if  elapsed_time77 >= d77:
                function77()                
                if elapsed_time77 >= d77:
                    flag77 = 1
                    break
                last_execute_t77 = current_time
            break
    
    for i in range (1):
            if  elapsed_time78 >= d78:
                function78()
                if elapsed_time78 >= d78:
                    flag78 = 1
                    break
                last_execute_t78 = current_time
            break
    
    for i in range (1):
            if  elapsed_time79 >= d79:
                function79()
                if elapsed_time79 >= d79:
                    flag79 = 1
                    break
                last_execute_t79 = current_time          
            break
    
    for i in range (1):
            if  elapsed_time80 >= d80:
                function80()                
                if elapsed_time80 >= d80:
                    flag80 = 1
                    break
                last_execute_t80 = current_time
            break
    #80
    for i in range (1):
            if  elapsed_time81 >= d81:
                function81()
                if elapsed_time81 >= d81:
                    flag81 = 1
                    break
                last_execute_t81 = current_time          
            break
    
    for i in range (1):
            if  elapsed_time82 >= d82:
                function82()                
                if elapsed_time82 >= d82:
                    flag82 = 1
                    break
                last_execute_t82 = current_time
            break
    
    for i in range (1):
            if  elapsed_time83 >= d83:
                function83()
                if elapsed_time83 >= d83:
                    flag83 = 1
                    break
                last_execute_t83 = current_time
            break
    
    for i in range (1):
            if  elapsed_time84 >= d84:
                function84()
                if elapsed_time84 >= d84:
                    flag84 = 1
                    break
                last_execute_t84 = current_time          
            break
    
    for i in range (1):
            if  elapsed_time85 >= d85:
                function85()                
                if elapsed_time85 >= d85:
                    flag85 = 1
                    break
                last_execute_t85 = current_time
            break
    
    for i in range (1):
            if  elapsed_time86 >= d86:
                function86()
                if elapsed_time86 >= d86:
                    flag86 = 1
                    break
                last_execute_t86 = current_time
            break
    
    for i in range (1):
            if  elapsed_time87 >= d87:
                function87()                
                if elapsed_time87 >= d87:
                    flag87 = 1
                    break
                last_execute_t87 = current_time
            break
    
    for i in range (1):
            if  elapsed_time88 >= d88:
                function88()
                if elapsed_time88 >= d88:
                    flag88 = 1
                    break
                last_execute_t88 = current_time
            break
    
    for i in range (1):
            if  elapsed_time89 >= d89:
                function89()
                if elapsed_time89 >= d89:
                    flag89 = 1
                    break
                last_execute_t89 = current_time          
            break
    
    for i in range (1):
            if  elapsed_time90 >= d90:
                function90()                
                if elapsed_time90 >= d90:
                    flag90 = 1
                    break
                last_execute_t90 = current_time
            break
    #90
    for i in range (1):
            if  elapsed_time91 >= d91:
                function91()
                if elapsed_time91 >= d91:
                    flag91 = 1
                    break
                last_execute_t91 = current_time          
            break
    
    for i in range (1):
            if  elapsed_time92 >= d92:
                function92()                
                if elapsed_time92 >= d92:
                    flag92 = 1
                    break
                last_execute_t92 = current_time
            break
    
    for i in range (1):
            if  elapsed_time93 >= d93:
                function93()
                if elapsed_time93 >= d93:
                    flag93 = 1
                    break
                last_execute_t93 = current_time
            break
    
    for i in range (1):
            if  elapsed_time94 >= d94:
                function94()
                if elapsed_time94 >= d94:
                    flag94 = 1
                    break
                last_execute_t94 = current_time          
            break
    
    for i in range (1):
            if  elapsed_time95 >= d95:
                function95()                
                if elapsed_time95 >= d95:
                    flag95 = 1
                    break
                last_execute_t95 = current_time
            break
    
    for i in range (1):
            if  elapsed_time96 >= d96:
                function96()
                if elapsed_time96 >= d96:
                    flag96 = 1
                    break
                last_execute_t96 = current_time
            break
    
    for i in range (1):
            if  elapsed_time97 >= d97:
                function97()                
                if elapsed_time97 >= d97:
                    flag97 = 1
                    break
                last_execute_t97 = current_time
            break
    
    for i in range (1):
            if  elapsed_time98 >= d98:
                function98()
                if elapsed_time98 >= d98:
                    flag98 = 1
                    break
                last_execute_t98 = current_time
            break
    
    for i in range (1):
            if  elapsed_time99 >= d99:
                function99()
                if elapsed_time99 >= d99:
                    flag99 = 1
                    break
                last_execute_t99 = current_time          
            break
    
    for i in range (1):
            if  elapsed_time100 >= d100:
                function100()                
                if elapsed_time100 >= d100:
                    flag100 = 1
                    break
                last_execute_t100 = current_time
            break
    #100
    for i in range (1):
            if  elapsed_time101 >= d101:
                function101()
                if elapsed_time101 >= d101:
                    flag101 = 1
                    break
                last_execute_t101 = current_time          
            break
    
    for i in range (1):
            if  elapsed_time102 >= d102:
                function102()                
                if elapsed_time102 >= d102:
                    flag102 = 1
                    break
                last_execute_t102 = current_time
            break
    
    for i in range (1):
            if  elapsed_time103 >= d103:
                function103()
                if elapsed_time103 >= d103:
                    flag103 = 1
                    break
                last_execute_t103 = current_time
            break
    
    for i in range (1):
            if  elapsed_time104 >= d104:
                function104()
                if elapsed_time104 >= d104:
                    flag104 = 1
                    break
                last_execute_t104 = current_time          
            break
    
    for i in range (1):
            if  elapsed_time105 >= d105:
                function105()                
                if elapsed_time105 >= d105:
                    flag105 = 1
                    break
                last_execute_t105 = current_time
            break
    
    for i in range (1):
            if  elapsed_time106 >= d106:
                function106()
                if elapsed_time106 >= d106:
                    flag106 = 1
                    break
                last_execute_t106 = current_time
            break
    
    for i in range (1):
            if  elapsed_time107 >= d107:
                function107()                
                if elapsed_time107 >= d107:
                    flag107 = 1
                    break
                last_execute_t107 = current_time
            break
    
    for i in range (1):
            if  elapsed_time108 >= d108:
                function108()
                if elapsed_time108 >= d108:
                    flag108 = 1
                    break
                last_execute_t108 = current_time
            break
    
    for i in range (1):
            if  elapsed_time109 >= d109:
                function109()
                if elapsed_time109 >= d109:
                    flag109 = 1
                    break
                last_execute_t109 = current_time          
            break
    
    for i in range (1):
            if  elapsed_time110 >= d110:
                function110()                
                if elapsed_time110 >= d110:
                    flag110 = 1
                    break
                last_execute_t110 = current_time
            break
    #110
    for i in range (1):
            if  elapsed_time111 >= d111:
                function111()
                if elapsed_time111 >= d111:
                    flag111 = 1
                    break
                last_execute_t111 = current_time          
            break
    
    for i in range (1):
            if  elapsed_time112 >= d112:
                function112()                
                if elapsed_time112 >= d112:
                    flag112 = 1
                    break
                last_execute_t112 = current_time
            break
    
    for i in range (1):
            if  elapsed_time113 >= d113:
                function113()
                if elapsed_time113 >= d113:
                    flag113 = 1
                    break
                last_execute_t113 = current_time
            break
    
    for i in range (1):
            if  elapsed_time114 >= d114:
                function114()
                if elapsed_time114 >= d114:
                    flag114 = 1
                    break
                last_execute_t114 = current_time          
            break
    
    for i in range (1):
            if  elapsed_time115 >= d115:
                function115()                
                if elapsed_time115 >= d115:
                    flag115 = 1
                    break
                last_execute_t115 = current_time
            break
    
    for i in range (1):
            if  elapsed_time116 >= d116:
                function116()
                if elapsed_time116 >= d116:
                    flag116 = 1
                    break
                last_execute_t116 = current_time
            break
    
    for i in range (1):
            if  elapsed_time117 >= d117:
                function117()                
                if elapsed_time117 >= d117:
                    flag117 = 1
                    break
                last_execute_t117 = current_time
            break
    
    for i in range (1):
            if  elapsed_time118 >= d118:
                function118()
                if elapsed_time118 >= d118:
                    flag118 = 1
                    break
                last_execute_t118 = current_time
            break
    
    for i in range (1):
            if  elapsed_time119 >= d119:
                function119()
                if elapsed_time119 >= d119:
                    flag119 = 1
                    break
                last_execute_t119 = current_time          
            break
    
    for i in range (1):
            if  elapsed_time120 >= d120:
                function120()                
                if elapsed_time120 >= d120:
                    flag120 = 1
                    break
                last_execute_t120 = current_time
            break
    #120
    for i in range (1):
            if  elapsed_time121 >= d121:
                function121()
                if elapsed_time121 >= d121:
                    flag121 = 1
                    break
                last_execute_t121 = current_time          
            break
    
    for i in range (1):
            if  elapsed_time122 >= d122:
                function122()                
                if elapsed_time122 >= d122:
                    flag122 = 1
                    break
                last_execute_t122 = current_time
            break
    
    for i in range (1):
            if  elapsed_time123 >= d123:
                function123()
                if elapsed_time123 >= d123:
                    flag123 = 1
                    break
                last_execute_t123 = current_time
            break
    
    for i in range (1):
            if  elapsed_time124 >= d124:
                function124()
                if elapsed_time124 >= d124:
                    flag124 = 1
                    break
                last_execute_t124 = current_time          
            break
    
    for i in range (1):
            if  elapsed_time125 >= d125:
                function125()                
                if elapsed_time125 >= d125:
                    flag125 = 1
                    break
                last_execute_t125 = current_time
            break
    
    for i in range (1):
            if  elapsed_time126 >= d126:
                function126()
                if elapsed_time126 >= d126:
                    flag126 = 1
                    break
                last_execute_t126 = current_time
            break
    
    for i in range (1):
            if  elapsed_time127 >= d127:
                function127()                
                if elapsed_time127 >= d127:
                    flag127 = 1
                    break
                last_execute_t127 = current_time
            break
    
    for i in range (1):
            if  elapsed_time128 >= d128:
                function128()
                if elapsed_time128 >= d128:
                    flag128 = 1
                    break
                last_execute_t128 = current_time
            break
    
    for i in range (1):
            if  elapsed_time129 >= d129:
                function129()
                if elapsed_time129 >= d129:
                    flag129 = 1
                    break
                last_execute_t129 = current_time          
            break
    
    for i in range (1):
            if  elapsed_time130 >= d130:
                function130()                
                if elapsed_time130 >= d130:
                    flag130 = 1
                    break
                last_execute_t130 = current_time
            break
    #130
    for i in range (1):
            if  elapsed_time131 >= d131:
                function131()
                if elapsed_time131 >= d131:
                    flag131 = 1
                    break
                last_execute_t131 = current_time          
            break
    
    for i in range (1):
            if  elapsed_time132 >= d132:
                function132()                
                if elapsed_time132 >= d132:
                    flag132 = 1
                    break
                last_execute_t132 = current_time
            break
    
    for i in range (1):
            if  elapsed_time133 >= d133:
                function133()
                if elapsed_time133 >= d133:
                    flag133 = 1
                    break
                last_execute_t133 = current_time
            break
    
    for i in range (1):
            if  elapsed_time134 >= d134:
                function134()
                if elapsed_time134 >= d134:
                    flag134 = 1
                    break
                last_execute_t134 = current_time          
            break
    
    for i in range (1):
            if  elapsed_time135 >= d135:
                function135()                
                if elapsed_time135 >= d135:
                    flag135 = 1
                    break
                last_execute_t135 = current_time
            break
    
    for i in range (1):
            if  elapsed_time136 >= d136:
                function136()
                if elapsed_time136 >= d136:
                    flag136 = 1
                    break
                last_execute_t136 = current_time
            break
    
    for i in range (1):
            if  elapsed_time137 >= d137:
                function137()                
                if elapsed_time137 >= d137:
                    flag137 = 1
                    break
                last_execute_t137 = current_time
            break
    
    for i in range (1):
            if  elapsed_time138 >= d138:
                function138()
                if elapsed_time138 >= d138:
                    flag138 = 1
                    break
                last_execute_t138 = current_time
            break
    
    for i in range (1):
            if  elapsed_time139 >= d139:
                function139()
                if elapsed_time139 >= d139:
                    flag139 = 1
                    break
                last_execute_t139 = current_time          
            break
    
    for i in range (1):
            if  elapsed_time140 >= d140:
                function140()                
                if elapsed_time140 >= d140:
                    flag140 = 1
                    break
                last_execute_t140 = current_time
            break
    #140
    for i in range (1):
            if  elapsed_time141 >= d141:
                function141()
                if elapsed_time141 >= d141:
                    flag141 = 1
                    break
                last_execute_t141 = current_time          
            break
    
    for i in range (1):
            if  elapsed_time142 >= d142:
                function142()                
                if elapsed_time142 >= d142:
                    flag142 = 1
                    break
                last_execute_t142 = current_time
            break
    
    for i in range (1):
            if  elapsed_time143 >= d143:
                function143()
                if elapsed_time143 >= d143:
                    flag143 = 1
                    break
                last_execute_t143 = current_time
            break
    
    for i in range (1):
            if  elapsed_time144 >= d144:
                function144()
                if elapsed_time144 >= d144:
                    flag144 = 1
                    break
                last_execute_t144 = current_time          
            break
    
    for i in range (1):
            if  elapsed_time145 >= d145:
                function145()                
                if elapsed_time145 >= d145:
                    flag145 = 1
                    break
                last_execute_t145 = current_time
            break
    
    for i in range (1):
            if  elapsed_time146 >= d146:
                function146()
                if elapsed_time146 >= d146:
                    flag146 = 1
                    break
                last_execute_t146 = current_time
            break
    
    for i in range (1):
            if  elapsed_time147 >= d147:
                function147()                
                if elapsed_time147 >= d147:
                    flag147 = 1
                    break
                last_execute_t147 = current_time
            break
    
    for i in range (1):
            if  elapsed_time148 >= d148:
                function148()
                if elapsed_time148 >= d148:
                    flag148 = 1
                    break
                last_execute_t148 = current_time
            break
    
    for i in range (1):
            if  elapsed_time149 >= d149:
                function149()
                if elapsed_time149 >= d149:
                    flag149 = 1
                    break
                last_execute_t149 = current_time          
            break
    
    for i in range (1):
            if  elapsed_time150 >= d150:
                function150()                
                if elapsed_time150 >= d150:
                    flag150 = 1
                    break
                last_execute_t150 = current_time
            break
    #150
    for i in range (1):
            if  elapsed_time151 >= d151:
                function151()
                if elapsed_time151 >= d151:
                    flag151 = 1
                    break
                last_execute_t151 = current_time          
            break
    
    for i in range (1):
            if  elapsed_time152 >= d152:
                function152()                
                if elapsed_time152 >= d152:
                    flag152 = 1
                    break
                last_execute_t152 = current_time
            break
    
    for i in range (1):
            if  elapsed_time153 >= d153:
                function153()
                if elapsed_time153 >= d153:
                    flag153 = 1
                    break
                last_execute_t153 = current_time
            break
    
    for i in range (1):
            if  elapsed_time154 >= d154:
                function154()
                if elapsed_time154 >= d154:
                    flag154 = 1
                    break
                last_execute_t154 = current_time          
            break
    
    for i in range (1):
            if  elapsed_time155 >= d155:
                function155()                
                if elapsed_time155 >= d155:
                    flag155 = 1
                    break
                last_execute_t155 = current_time
            break
    
    for i in range (1):
            if  elapsed_time156 >= d156:
                function156()
                if elapsed_time156 >= d156:
                    flag156 = 1
                    break
                last_execute_t156 = current_time
            break
    
    for i in range (1):
            if  elapsed_time157 >= d157:
                function157()                
                if elapsed_time157 >= d157:
                    flag157 = 1
                    break
                last_execute_t157 = current_time
            break
    
    for i in range (1):
            if  elapsed_time158 >= d158:
                function158()
                if elapsed_time158 >= d158:
                    flag158 = 1
                    break
                last_execute_t158 = current_time
            break
    
    for i in range (1):
            if  elapsed_time159 >= d159:
                function159()
                if elapsed_time159 >= d159:
                    flag159 = 1
                    break
                last_execute_t159 = current_time          
            break
    
    for i in range (1):
            if  elapsed_time160 >= d160:
                function160()                
                if elapsed_time160 >= d160:
                    flag160 = 1
                    break
                last_execute_t160 = current_time
            break
    #160
    for i in range (1):
            if  elapsed_time161 >= d161:
                function161()
                if elapsed_time161 >= d161:
                    flag161 = 1
                    break
                last_execute_t161 = current_time          
            break
    
    for i in range (1):
            if  elapsed_time162 >= d162:
                function162()                
                if elapsed_time162 >= d162:
                    flag162 = 1
                    break
                last_execute_t162 = current_time
            break
    
    for i in range (1):
            if  elapsed_time163 >= d163:
                function163()
                if elapsed_time163 >= d163:
                    flag163 = 1
                    break
                last_execute_t163 = current_time
            break
    
    for i in range (1):
            if  elapsed_time164 >= d164:
                function164()
                if elapsed_time164 >= d164:
                    flag164 = 1
                    break
                last_execute_t164 = current_time          
            break
    
    for i in range (1):
            if  elapsed_time165 >= d165:
                function165()                
                if elapsed_time165 >= d165:
                    flag165 = 1
                    break
                last_execute_t165 = current_time
            break
    
    for i in range (1):
            if  elapsed_time166 >= d166:
                function166()
                if elapsed_time166 >= d166:
                    flag166 = 1
                    break
                last_execute_t166 = current_time
            break
    
    for i in range (1):
            if  elapsed_time167 >= d167:
                function167()                
                if elapsed_time167 >= d167:
                    flag167 = 1
                    break
                last_execute_t167 = current_time
            break
    
    for i in range (1):
            if  elapsed_time168 >= d168:
                function168()
                if elapsed_time168 >= d168:
                    flag168 = 1
                    break
                last_execute_t168 = current_time
            break
    
    for i in range (1):
            if  elapsed_time169 >= d169:
                function169()
                if elapsed_time169 >= d169:
                    flag169 = 1
                    break
                last_execute_t169 = current_time          
            break
    
    for i in range (1):
            if  elapsed_time170 >= d170:
                function170()                
                if elapsed_time170 >= d170:
                    flag170 = 1
                    break
                last_execute_t170 = current_time
            break
    #170
    for i in range (1):
            if  elapsed_time171 >= d171:
                function171()
                if elapsed_time171 >= d171:
                    flag171 = 1
                    break
                last_execute_t171 = current_time          
            break
    
    for i in range (1):
            if  elapsed_time172 >= d172:
                function172()                
                if elapsed_time172 >= d172:
                    flag172 = 1
                    break
                last_execute_t172 = current_time
            break
    
    for i in range (1):
            if  elapsed_time173 >= d173:
                function173()
                if elapsed_time173 >= d173:
                    flag173 = 1
                    break
                last_execute_t173 = current_time
            break
    
    for i in range (1):
            if  elapsed_time174 >= d174:
                function174()
                if elapsed_time174 >= d174:
                    flag174 = 1
                    break
                last_execute_t174 = current_time          
            break
    
    for i in range (1):
            if  elapsed_time175 >= d175:
                function175()                
                if elapsed_time175 >= d175:
                    flag175 = 1
                    break
                last_execute_t175 = current_time
            break
    
    for i in range (1):
            if  elapsed_time176 >= d176:
                function176()
                if elapsed_time176 >= d176:
                    flag176 = 1
                    break
                last_execute_t176 = current_time
            break
    
    for i in range (1):
            if  elapsed_time177 >= d177:
                function177()                
                if elapsed_time177 >= d177:
                    flag177 = 1
                    break
                last_execute_t177 = current_time
            break
    
    for i in range (1):
            if  elapsed_time178 >= d178:
                function178()
                if elapsed_time178 >= d178:
                    flag178 = 1
                    break
                last_execute_t178 = current_time
            break
    
    for i in range (1):
            if  elapsed_time179 >= d179:
                function179()
                if elapsed_time179 >= d179:
                    flag179 = 1
                    break
                last_execute_t179 = current_time          
            break
    
    for i in range (1):
            if  elapsed_time180 >= d180:
                function180()                
                if elapsed_time180 >= d180:
                    flag180 = 1
                    break
                last_execute_t180 = current_time
            break
    #180
    for i in range (1):
            if  elapsed_time181 >= d181:
                function181()
                if elapsed_time181 >= d181:
                    flag181 = 1
                    break
                last_execute_t181 = current_time          
            break
    
    for i in range (1):
            if  elapsed_time182 >= d182:
                function182()                
                if elapsed_time182 >= d182:
                    flag182 = 1
                    break
                last_execute_t182 = current_time
            break
    
    for i in range (1):
            if  elapsed_time183 >= d183:
                function183()
                if elapsed_time183 >= d183:
                    flag183 = 1
                    break
                last_execute_t183 = current_time
            break
    
    for i in range (1):
            if  elapsed_time184 >= d184:
                function184()
                if elapsed_time184 >= d184:
                    flag184 = 1
                    break
                last_execute_t184 = current_time          
            break
    
    for i in range (1):
            if  elapsed_time185 >= d185:
                function185()                
                if elapsed_time185 >= d185:
                    flag185 = 1
                    break
                last_execute_t185 = current_time
            break
    
    for i in range (1):
            if  elapsed_time186 >= d186:
                function186()
                if elapsed_time186 >= d186:
                    flag186 = 1
                    break
                last_execute_t186 = current_time
            break
    
    for i in range (1):
            if  elapsed_time187 >= d187:
                function187()                
                if elapsed_time187 >= d187:
                    flag187 = 1
                    break
                last_execute_t187 = current_time
            break
    
    for i in range (1):
            if  elapsed_time188 >= d188:
                function188()
                if elapsed_time188 >= d188:
                    flag188 = 1
                    break
                last_execute_t188 = current_time
            break
    
    for i in range (1):
            if  elapsed_time189 >= d189:
                function189()
                if elapsed_time189 >= d189:
                    flag189 = 1
                    break
                last_execute_t189 = current_time          
            break
    
    for i in range (1):
            if  elapsed_time190 >= d190:
                function190()                
                if elapsed_time190 >= d190:
                    flag190 = 1
                    break
                last_execute_t190 = current_time
            break
    #190
    for i in range (1):
            if  elapsed_time191 >= d191:
                function191()
                if elapsed_time191 >= d191:
                    flag191 = 1
                    break
                last_execute_t191 = current_time          
            break
    
    for i in range (1):
            if  elapsed_time192 >= d192:
                function192()                
                if elapsed_time192 >= d192:
                    flag192 = 1
                    break
                last_execute_t192 = current_time
            break
    
    for i in range (1):
            if  elapsed_time193 >= d193:
                function193()
                if elapsed_time193 >= d193:
                    flag193 = 1
                    break
                last_execute_t193 = current_time
            break
    
    for i in range (1):
            if  elapsed_time194 >= d194:
                function194()
                if elapsed_time194 >= d194:
                    flag194 = 1
                    break
                last_execute_t194 = current_time          
            break
    
    for i in range (1):
            if  elapsed_time195 >= d195:
                function195()                
                if elapsed_time195 >= d195:
                    flag195 = 1
                    break
                last_execute_t195 = current_time
            break
    
    for i in range (1):
            if  elapsed_time196 >= d196:
                function196()
                if elapsed_time196 >= d196:
                    flag196 = 1
                    break
                last_execute_t196 = current_time
            break
    
    for i in range (1):
            if  elapsed_time197 >= d197:
                function197()                
                if elapsed_time197 >= d197:
                    flag197 = 1
                    break
                last_execute_t197 = current_time
            break
    
    for i in range (1):
            if  elapsed_time198 >= d198:
                function198()
                if elapsed_time198 >= d198:
                    flag198 = 1
                    break
                last_execute_t198 = current_time
            break
    
    for i in range (1):
            if  elapsed_time199 >= d199:
                function199()
                if elapsed_time199 >= d199:
                    flag199 = 1
                    break
                last_execute_t199 = current_time          
            break
    
    for i in range (1):
            if  elapsed_time200 >= d200:
                function200()                
                if elapsed_time200 >= d200:
                    flag200 = 1
                    break
                last_execute_t200 = current_time
            break
    #200
    for i in range (1):
            if  elapsed_time201 >= d201:
                function201()
                if elapsed_time201 >= d201:
                    flag201 = 1
                    break
                last_execute_t201 = current_time          
            break
    
    for i in range (1):
            if  elapsed_time202 >= d202:
                function202()                
                if elapsed_time202 >= d202:
                    flag202 = 1
                    break
                last_execute_t202 = current_time
            break
    
    for i in range (1):
            if  elapsed_time203 >= d203:
                function203()
                if elapsed_time203 >= d203:
                    flag203 = 1
                    break
                last_execute_t203 = current_time
            break
    
    for i in range (1):
            if  elapsed_time204 >= d204:
                function204()
                if elapsed_time204 >= d204:
                    flag204 = 1
                    break
                last_execute_t204 = current_time          
            break
    
    for i in range (1):
            if  elapsed_time205 >= d205:
                function205()                
                if elapsed_time205 >= d205:
                    flag205 = 1
                    break
                last_execute_t205 = current_time
            break
    #205
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

# stop_function()
cap.release()
cv2.destroyAllWindows()
