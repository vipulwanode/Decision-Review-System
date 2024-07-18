import tkinter
import cv2 #pip install opencv-python
import PIL.Image,PIL.ImageTk #pip install pillow
from functools import partial
import threading
import time
import imutils #pip install imutils

stream=cv2.VideoCapture('clip.mp4')
flag=True
def play(speed):
    global flag
    print(f'you clicked on play.speed is {speed}')
    
    #play the video in reverse mode
    frame1=stream.get(cv2.CAP_PROP_POS_FRAMES)
    stream.set(cv2.CAP_PROP_POS_FRAMES,frame1 + speed)
    grabbed,frame = stream.read()
    if not grabbed:
        exit()
    frame=imutils.resize(frame,width=SET_WIDTH,height=SET_HEIGHT)
    frame=PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0,image=frame,anchor=tkinter.NW)
    if flag:
        canvas.create_text(132,29,fill='red',font='times 26 bold',text='Decision Pending')
    flag=not flag

def pending(decision):

    #display decision pending image
    frame = cv2.cvtColor(cv2.imread('pending.jpg'),cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame,width=SET_WIDTH,height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image=frame
    canvas.create_image(0,0,image=frame,anchor=tkinter.NW)


    #wait for 1sec
    time.sleep(1.5)


    #display sponser image
    frame = cv2.cvtColor(cv2.imread('sponser2.jpg'),cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame,width=SET_WIDTH,height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image=frame
    canvas.create_image(0,0,image=frame,anchor=tkinter.NW)

    #wait 1.5 sec
    time.sleep(1.5)


    #display out/notout image
    if decision=='out':
        decisionimg='out.png'
    else:
        decisionimg='not_out.jpg'

    frame = cv2.cvtColor(cv2.imread(decisionimg),cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame,width=SET_WIDTH,height=SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image=frame
    canvas.create_image(0,0,image=frame,anchor=tkinter.NW)


def out():
    thread = threading.Thread(target=pending,args=('out',))
    thread.daemon=1
    thread.start()

    print('player is out')
def not_out():
    thread = threading.Thread(target=pending,args=('not_out',))
    thread.daemon=1
    thread.start()
    print('player is not out ')




#width & height of our main screen 
SET_WIDTH=650
SET_HEIGHT=368

#tkinter gui start here 
window = tkinter.Tk()
window.title('Decision Review System ')
cv_img=cv2.cvtColor(cv2.imread("welcome3.jpg"),cv2.COLOR_BGR2RGB)
canvas = tkinter.Canvas(window, width=SET_WIDTH,height=SET_HEIGHT)
photo=PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(cv_img))
image_on_canvas=canvas.create_image(0,0,ancho=tkinter.NW,image=photo)
canvas.pack()
print()
print()

#buttons to control to playback
btn=tkinter.Button(window,text="<<   Previous (Fast)", bg='pink',font='times 13 bold',width=70,height=2,command=partial(play,-25))
btn.pack()

btn=tkinter.Button(window,text="<<   Previous (Slow)",bg='pink',font='times 13 bold',width=70,height=2,command=partial(play,-2))
btn.pack()

btn=tkinter.Button(window,text="    Next (Slow)  >>",bg='white',font='times 13 bold',width=70,height=2,command=partial(play,2))
btn.pack()

btn=tkinter.Button(window,text="   Next (Fast)  >>",bg='white',font='times 13 bold',width=70,height=2,command=partial(play,25))
btn.pack()

btn=tkinter.Button(window,text="  Give out   >>",bg='pink',font='times 14 bold',width=64,height=1,command = out)
btn.pack()

btn=tkinter.Button(window,text="Give Not_out   >>",bg='pink',font='times 14 bold',width=64,height=1,command = not_out)
btn.pack()

window.mainloop()