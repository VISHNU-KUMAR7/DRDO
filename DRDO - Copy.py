import tkinter as tk
import time
import serial
import threading
import continuous_threading
'''link_YouTube:- https://www.youtube.com/watch?v=0V-6pu1Gyp8'''
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter import *
import numpy as np
import serial as sr
import random
import tkinter
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure

"""'''ser = serial.Serial('COM10',9600)
val1 = 0

index = []'''

def readserial():
    global val1
    ser_bytes = ser.readline()
    ser_bytes = ser_bytes.decode("utf-8")
    print(ser_bytes.rstrip())
    val1 = ser_bytes
    index.append(val1)
    
    if len(index) == 1:
        display1 = tk.Label(root,text=index[0]).place(x=50,y=10)
    elif len(index) == 2:
        #display1 = tk.Label(root,text=index[0]).place(x=10,y=10)
        display2 = tk.Label(root,text=index[1]).place(x=50,y=40)

        
    if len(index) == 2:
        #print("Done")
        index.clear()
    
    time.sleep(0.5)

t1 = continuous_threading.PeriodicThread(0.5, readserial)"""
ser = serial.Serial('COM9', 9600)
time.sleep(3)


#---------global variables1-------
data_1 = np.array([])
list_data = list()
def plot_data_1():
    global data_1,list_data
    
    if (True):
        '''a = s.readline()
        a.decode()])'''

        #------reading the data once from the Arduino Serial-----#
        data = ser.readline()
        bin_data = data.decode()
        str_data = bin_data.rstrip()
        list_data = str_data.split(",")
        #------compeletd the reading the data from the arduion -----#

        #print(list_data, end = "\n")


        
        a = round(random.uniform(-50.0, 8.5),4)
        if(len(data_1)<100):
            data_1 = np.append(data_1, a)
        else:
            data_1[0:99] = data_1[1:100]
            data_1[99] = a
            
        lines.set_xdata(np.arange(0,len(data_1)))
        lines.set_ydata(data_1)
        
        canvas.draw()

        try:
            display1 = tk.Label(root,text=list_data[0],bg= 'black',fg = "red").place(x=245,y=160)
            display2 = tk.Label(root,text=list_data[1],bg= 'black',fg = "red").place(x=245,y=210)
            display3 = tk.Label(root,text=list_data[2],bg= 'black',fg = "red").place(x=245,y=260)
        except:
            pass
                
    root.after(1,plot_data_1)
    
    
#---------global variables2-------
data_2 = np.array([])
a_2=0
def plot_data_2():
    global data_2,a_2
    
    if (True):
        '''a = s.readline()
        a.decode()])'''
        a_2 = round(random.uniform(-50.0, 8.5),4)
        if(len(data_2)<100):
            data_2 = np.append(data_2, a_2)
        else:
            data_2[0:99] = data_2[1:100]
            data_2[99] = a_2
            
        lines_2.set_xdata(np.arange(0,len(data_2)))
        lines_2.set_ydata(data_2)
        
        canvas_2.draw()

        try:
            print(list_data[3] , end = "\n")  
            display1 = tk.Label(root,text=list_data[3],fg = "red",bg= 'black').place(x=760,y=160)
            display2 = tk.Label(root,text=list_data[4],fg = "red",bg= 'black').place(x=760,y=210)
            display3 = tk.Label(root,text=list_data[5],fg = "red",bg= 'black').place(x=760,y=260)
        except:
            pass
        
                
    root.after(1,plot_data_2)
    
#---------global variables3-------
data_3 = np.array([])
a_3 =0
def plot_data_3():
    global data_3,a_3
    #print(list_data, end = "\n")
      
    if (True):
        '''a = s.readline()
        a.decode()])'''
        a_3 = round(random.uniform(-50.0, 8.5),4)
        if(len(data_3)<100):
            data_3 = np.append(data_3, a_3)
        else:
            data_3[0:99] = data_3[1:100]
            data_3[99] = a_3
            
        lines_3.set_xdata(np.arange(0,len(data_3)))
        lines_3.set_ydata(data_3)
        
        canvas_3.draw()

        try:
            display1 = tk.Label(root,text=list_data[6],bg= 'black',fg = "red").place(x=1250,y=160)
            display2 = tk.Label(root,text=list_data[7],bg= 'black',fg = "red").place(x=1250,y=210)
            display3 = tk.Label(root,text=list_data[8],bg= 'black',fg = "red").place(x=1250,y=260)
        except:
            pass
        
                
    root.after(1,plot_data_3)

root = tk.Tk()
root.title("DRDO")
root.configure(background = "black")
root.iconbitmap(r'C:\Users\Lenovo\Desktop\DRDO\vishnu\drdo\favicon.ico')
root.geometry("1920x1080")


#-----------Top_Mission_Heading_----------
Heading = tk.Label(root,text=" Rocket ",font=('Arial Italic', 28, 'bold'),fg = "red",bg= 'black').place(x=760,y=60)

ssw1 = tk.Label(root,text="Acc_X",font=('Arial', 24, 'bold'),fg = "red",bg= 'black').place(x=140,y=150)
w2 = tk.Label(root,text="Acc_Y",font=('Arial', 24, 'bold'),fg = "red",bg= 'black').place(x=140,y=200)
w3 = tk.Label(root,text="Acc_Z",font=('Arial', 24, 'bold'),fg = "red",bg= 'black').place(x=140,y=250)

#display1 = tk.Label(root,text="Reading_the_data1",bg= 'black',fg = "red").place(x=245,y=160)
#display2 = tk.Label(root,text="Reading_the_data2",bg= 'black',fg = "red").place(x=245,y=210)
#display3 = tk.Label(root,text="Reading_the_data3",bg= 'black',fg = "red").place(x=245,y=260)

w1 = tk.Label(root,text="Gyro_X",font=('Arial', 24, 'bold'),fg = "red",bg= 'black').place(x=640,y=150)
w2 = tk.Label(root,text="Gyro_Y",font=('Arial', 24, 'bold'),fg = "red",bg= 'black').place(x=640,y=200)
w3 = tk.Label(root,text="Gyro_Z",font=('Arial', 24, 'bold'),fg = "red",bg= 'black').place(x=640,y=250)

#display1 = tk.Label(root,text="Reading_the_data1",fg = "red",bg= 'black').place(x=760,y=160)
#display2 = tk.Label(root,text="Reading_the_data2",fg = "red",bg= 'black').place(x=760,y=210)
#display3 = tk.Label(root,text="Reading_the_data3",fg = "red",bg= 'black').place(x=760,y=260)

w1 = tk.Label(root,text="Mag_X",font=('Arial', 24, 'bold'),fg = "red",bg= 'black').place(x=1140,y=150)
w2 = tk.Label(root,text="Mag_Y",font=('Arial', 24, 'bold'),fg = "red",bg= 'black').place(x=1140,y=200)
w3 = tk.Label(root,text="Mag_Z",font=('Arial', 24, 'bold'),fg = "red",bg= 'black').place(x=1140,y=250)

#display1 = tk.Label(root,text="Reading_the_data1",bg= 'black',fg = "red").place(x=1250,y=160)
#display2 = tk.Label(root,text="Reading_the_data2",bg= 'black',fg = "red").place(x=1250,y=210)
#display3 = tk.Label(root,text="Reading_the_data3",bg= 'black',fg = "red").place(x=1250,y=260)




#-------create Plot object on GUI_1-------
#add figure canvas
fig = Figure();
ax = fig.add_subplot(111)

#ax = plt.axes(xlim=(0,100), ylim(0,120));  #displaying only 100 sam
ax.set_title('accelerometer ');
ax.set_xlabel('X_label')
ax.set_ylabel('Y_label')
ax.set_xlim(0,100)
ax.set_ylim(-50,10)
lines = ax.plot([],[])[0]

canvas  = FigureCanvasTkAgg(fig, master= root)  #A  tk.DrawingArea.
canvas.get_tk_widget().place(x=10, y= 400, width = 600, height = 400)
canvas.draw()

#th = continuous_threading.ContinuousThread(target=plot_data_3)
#th.start()


#-------create Plot object on GUI_2-------
#add figure canvas
fig_2 = Figure();
ax_2 = fig_2.add_subplot(111)

#ax = plt.axes(xlim=(0,100), ylim(0,120));  #displaying only 100 sam
ax_2.set_title('gyrometer ');
ax_2.set_xlabel('X_label')
ax_2.set_ylabel('Y_label')
ax_2.set_xlim(0,100)
ax_2.set_ylim(-50,10)
lines_2 = ax_2.plot([],[])[0]

canvas_2  = FigureCanvasTkAgg(fig_2, master= root)  #A  tk.DrawingArea.
canvas_2.get_tk_widget().place(x=550, y= 400, width = 600, height = 400)
canvas_2.draw()




#-------create Plot object on GUI_3-------
#add figure canvas
fig_3 = Figure();
ax_3 = fig_3.add_subplot(111)

#ax = plt.axes(xlim=(0,100), ylim(0,120));  #displaying only 100 sam
ax_3.set_title('magnetometer ');
ax_3.set_xlabel('X_label')
ax_3.set_ylabel('Y_label')
ax_3.set_xlim(0,100)
ax_3.set_ylim(-50,10)
lines_3 = ax_3.plot([],[])[0]

canvas_3  = FigureCanvasTkAgg(fig_3, master= root)  #A  tk.DrawingArea.
canvas_3.get_tk_widget().place(x=1050, y= 400, width = 600, height = 400)
canvas_3.draw()


#------Right side image------------/
photo = PhotoImage(file=r'C:\Users\Lenovo\Desktop\DRDO\vishnu\drdo\photos\drdo-official-logo2.png')
labelphoto = Label(root, image = photo).place(x=1380,y=0)

#t1.start()
#t1.join()

root.after(1,plot_data_1)
root.after(1,plot_data_2)
root.after(1,plot_data_3)

root.mainloop()
