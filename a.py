from PIL import Image,ImageEnhance,ImageTk
import cv2
from tkinter import Tk
from tkinter.ttk import Label,Button

class Window(Tk):
    def __init__(self):
        super().__init__()
        self.wm_title("form")
        self.geometry("550x420")

        # button_1=Button(self,text="show tabel",command=self.show_frame)
        # button_1.place(x=50,y=350,width=100,height=50)
        self.label=Label(self,text='This is a label')
        self.label.place(x=80,y=20)
        self.cap = cv2.VideoCapture("rtsp://admin:admin1234@192.168.1.15:554/cam/realmonitor?channel=1&subtype=0")
    def show_frame(self):
        # print("ok")
        print('ok:',self.cap.read()[1].shape)
        scale_percent=40
        width=int(self.cap.read()[1].shape[1]*scale_percent/100)
        height=int(self.cap.read()[1].shape[0]*scale_percent/100)
        dim=(width,height)
        resized=cv2.resize(self.cap.read()[1],dim,interpolation=cv2.INTER_AREA)
        print('dc:',resized.shape)
        cv2image=cv2.cvtColor(resized,cv2.COLOR_BGR2RGB)
        img=Image.fromarray(cv2image)
        tkimage=ImageTk.PhotoImage(image=img)
        self.label.imgtk=tkimage
        self.label.configure(image=tkimage)
        self.label.after(20,self.show_frame)
if __name__=="__main__":
    app=Window()
    app.mainloop()


# cap = cv2.VideoCapture("rtsp://admin:admin1234@192.168.1.15:554/cam/realmonitor?channel=1&subtype=0")
