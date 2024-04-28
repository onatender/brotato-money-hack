import time
from tkinter import *
import tkinter
from pymem import Pymem
from pymem.ptypes import RemotePointer

import keyboard

pm = Pymem("GodotSeaven_GDK_desktop.exe")

offsets = [0x148,0x140,0x108,0x28,0x58,0x20,0x200]

def getPointerAddress(base, offsets):
    remote_pointer = RemotePointer(pm.process_handle, base)
    for offset in offsets:
        if offset != offsets[-1]:
            remote_pointer = RemotePointer(pm.process_handle, remote_pointer.value + offset)
        else:
            return remote_pointer.value + offset
# while not keyboard.is_pressed('q'):
#         pm.write_int(getPointerAddress(pm.base_address + 0x03674F10,offsets=offsets),1000)

gui = Tk()
gui.title("Brotato Hile")
Label(text="Para").grid(row=0,column=0)
strvar = StringVar()
textbox = Entry(gui, width=15,textvariable=strvar,state="readonly")
textbox.grid(row=0,column=1)
Label(text="Yeni Para").grid(row=1,column=0)
strvar2 = StringVar()
textbox2 = Entry(gui, width=15,textvariable=strvar2)
textbox2.grid(row=1,column=1)
def yap():
    pm.write_int(getPointerAddress(pm.base_address + 0x03674F10,offsets=offsets),int(strvar2.get()))
btn = Button(gui,text="Yap",command=yap) 
btn.grid(row=2,column=0,columnspan=2)

while True:
    strvar.set(pm.read_int(getPointerAddress(pm.base_address + 0x03674F10,offsets=offsets)))
    gui.update()
    
