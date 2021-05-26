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



#---------global variables1-------
data_1 = np.array([])
data_b_1 = np.array([]) 
a_1 =0
b_1 =0
def plot_data_1():
    global data_1,a_1,b_1,data_b_1
      
    if (True):
        '''a = s.readline()
        a.decode()])'''
        a_1 = round(random.uniform(-50.0, 8.5),4)
        b_1 = random.random()
        if(len(data_1)<100):
            data_1 = np.append(data_1, a_1)
            data_b_1 = np.append(data_b_1, b_1)
        else:
            data_1[0:99] = data_1[1:100]
            data_1[99] = a_1
            data_b_1[0:99] = data_b_1[1:100]
            data_b_1[99] = b_1
            
        lines.set_xdata(np.arange(0,len(data_1)))
        lines.set_ydata(data_1)
        lines.set_3d_properties(data_b_1)
        
        canvas.draw()
                
    root.after(1,plot_data_1)
    
    
#---------global variables2-------
data_2 = np.array([])
data_b_2 = np.array([]) 
a_2=0
b_2=0
def plot_data_2():
    global data_2,a_2,b_2,data_b_2
      
    if (True):
        '''a = s.readline()
        a.decode()])'''
        a_2 = round(random.uniform(-50.0, 8.5),4)
        b_2 = random.random()
        if(len(data_2)<100):
            data_2 = np.append(data_2, a_2)
            data_b_2 = np.append(data_b_2, b_2)
        else:
            data_2[0:99] = data_2[1:100]
            data_2[99] = a_2
            data_b_2[0:99] = data_b_2[1:100]
            data_b_2[99] = b_2
            
        lines_2.set_xdata(np.arange(0,len(data_2)))
        lines_2.set_ydata(data_2)
        lines_2.set_3d_properties(data_b_2)
        
        canvas_2.draw()
                
    root.after(1,plot_data_2)
    
#---------global variables3-------
data_3 = np.array([])
data_b_3 = np.array([]) 
a_3 =0
b_3 =0
def plot_data_3():
    global data_3,a_3,b_3,data_b_3
    global data_b_3,data_3,a_3,b_3
    if (True):
        '''a = s.readline()
        a.decode()])'''
        a_3 = round(random.uniform(-50.0, 8.5),4)
        b_3 = random.random()
        if(len(data_3)<100):
            data_3 = np.append(data_3, a_3)
            data_b_3 = np.append(data_b_3, b_3)
        else:
            data_3[0:99] = data_3[1:100]
            data_3[99] = a_3
            data_b_3[0:99] = data_b_3[1:100]
            data_b_3[99] = b_3
            
        lines_3.set_xdata(np.arange(0,len(data_3)))
        lines_3.set_ydata(data_3)
        lines_3.set_3d_properties(data_b_3)
        
        canvas_3.draw()
                
    root.after(1,plot_data_3)

    
    
def main():

    global root
    root = tk.Tk()
    root.title("DRDO")
    root.configure(background = "black")
    root.iconbitmap(r'F:\Maskottchen\drdo\favicon.ico')
    root.geometry("1920x1080")


    #-----------Top_Mission_Heading_----------
    Heading = tk.Label(root,text="Wireless Rocket").place(x=420,y=60)

    w1 = tk.Label(root,text="Data_1_X").place(x=140,y=150)
    w2 = tk.Label(root,text="Data_2_Y").place(x=140,y=180)
    w3 = tk.Label(root,text="Data_3_Z").place(x=140,y=210)

    display1 = tk.Label(root,text="Reading_the_data1").place(x=220,y=150)
    display2 = tk.Label(root,text="Reading_the_data2").place(x=220,y=180)
    display3 = tk.Label(root,text="Reading_the_data3").place(x=220,y=210)

    w1 = tk.Label(root,text="Data_1_X").place(x=640,y=150)
    w2 = tk.Label(root,text="Data_2_Y").place(x=640,y=180)
    w3 = tk.Label(root,text="Data_3_Z").place(x=640,y=210)

    display1 = tk.Label(root,text="Reading_the_data1").place(x=720,y=150)
    display2 = tk.Label(root,text="Reading_the_data2").place(x=720,y=180)
    display3 = tk.Label(root,text="Reading_the_data3").place(x=720,y=210)

    w1 = tk.Label(root,text="Data_1_X").place(x=1140,y=150)
    w2 = tk.Label(root,text="Data_2_Y").place(x=1140,y=180)
    w3 = tk.Label(root,text="Data_3_Z").place(x=1140,y=210)

    display1 = tk.Label(root,text="Reading_the_data1").place(x=1220,y=150)
    display2 = tk.Label(root,text="Reading_the_data2").place(x=1220,y=180)
    display3 = tk.Label(root,text="Reading_the_data3").place(x=1220,y=210)




    #-------create Plot object on GUI_1-------
    #this is for adding figure in canvas
    fig = Figure();
    global canvas
    canvas  = FigureCanvasTkAgg(fig, master= root)  #A  tk.DrawingArea.
    canvas.draw()
    ax = fig.add_subplot(111,projection='3d')
    ax.patch.set_facecolor('black')

    #ax = plt.axes(xlim=(0,100), ylim(0,120));  #displaying only 100 sam
    ax.set_title('accelerometer ');
    ax.set_xlabel('X_label')
    ax.xaxis.label.set_color("yellow")
    ax.set_ylabel('Y_label')
    ax.yaxis.label.set_color("yellow")
    #ax.set_zlabel('Z_label')

    ax.set_xlim(0,100)
    ax.set_ylim(-50,10)
    global lines
    lines = ax.plot3D([],[],[],color='red')[0]

    toolbar = NavigationToolbar2Tk(canvas, root)
    toolbar.update()

    #canvas  = FigureCanvasTkAgg(fig, master= root)  #A  tk.DrawingArea.
    canvas.get_tk_widget().place(x=10, y= 300, width = 600, height = 400)
    #canvas.draw()






    #-------create Plot object on GUI_2-------
    #add figure canvas
    global canvas_2
    global lines_2
    
    fig_2 = Figure();
    ax_2 = fig_2.add_subplot(111,projection='3d')

    #ax = plt.axes(xlim=(0,100), ylim(0,120));  #displaying only 100 sam
    ax_2.set_title('gyrometer ');
    ax_2.set_xlabel('X_label')
    ax_2.set_ylabel('Y_label')
    ax_2.set_zlabel('Z_label')

    ax_2.set_xlim(0,100)
    ax_2.set_ylim(-50,10)
    #ax_2.set_zlim(1, 10)
    lines_2 = ax_2.plot3D([],[],[])[0]

    canvas_2  = FigureCanvasTkAgg(fig_2, master= root)  #A  tk.DrawingArea.
    
    canvas_2.get_tk_widget().place(x=550, y= 300, width = 600, height = 400)
    canvas_2.draw()




    #-------create Plot object on GUI_3-------
    #add figure canvas
    global canvas_3
    global lines_3
    
    fig_3 = Figure();
    ax_3 = fig_3.add_subplot(111,projection='3d')

    #ax = plt.axes(xlim=(0,100), ylim(0,120));  #displaying only 100 sam
    ax_3.set_title('magnetometer ');
    ax_3.set_xlabel('X_label')
    ax_3.set_ylabel('Y_label')
    ax_3.set_zlabel('Z_label')

    ax_3.set_xlim(0,100)
    ax_3.set_ylim(-50,10)
    ax_3.set_zlim(0, 1)
    lines_3 = ax_3.plot3D([],[],[])[0]

    canvas_3  = FigureCanvasTkAgg(fig_3, master= root)  #A  tk.DrawingArea.
    
    canvas_3.get_tk_widget().place(x=1050, y= 300, width = 600, height = 400)
    canvas_3.draw()


    #------Right side image------------
    
    
    #----------Exit Button---------------
    

    #t1.start()
    #t1.join()

    root.after(1,plot_data_1)
    root.after(1,plot_data_2)
    root.after(1,plot_data_3)
    exitButton = tk.Button(root, text='close',fg= "white", bg = "red",font="time 15 bold",width = 16,command = root.destroy).place(x=800,y=710)

    root.mainloop()

#basic window is ready 
def main2():
    root_main = Tk()
    root_main.title("DRDO")
    root_main.configure(background = "black")
    root_main.iconbitmap(r'F:\Maskottchen\drdo\favicon.ico')
    root_main.geometry("700x600")
    tk.Button(root_main,text = "Launch",fg= "white", bg = "red",font="time 15 bold",width = 16,command = main).place(x=245,y=300)
    root_main.mainloop()

main2()