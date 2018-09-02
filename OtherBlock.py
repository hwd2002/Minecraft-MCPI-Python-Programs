#OtherBlock program
#by hwd2002
import time
# Tkinter Stuff
from tkinter import *
try:
    # Minecraft Stuff
    from mcpi.minecraft import Minecraft
    mc = Minecraft.create() # create Minecraft Object
    mc.postToChat("OtherBlockGUI Starting...")
except ConnectionRefusedError:
    print("Connection Refused")

def TNT():
    command=mc.setBlock(x, y, z, 46, 1)
    print("Placed TNT (Primed)")
    
def Cobweb():
    command=mc.setBlock(x, y, z, 30)
    print("Placed Cobweb")

def Water():
    command=mc.setBlock(x, y, z, 8)
    print("Placed Water")

def Lava():
    command=mc.setBlock(x, y, z, 10)
    print("Placed Lava")

def Furnace():
    command=mc.setBlock(x, y, z, 62)
    print("Placed Furnace (Active)")

def Pos(): # Get Position
    global x
    global y
    global z
    x, y, z = mc.player.getPos()
    print(x, y, z)
    
tk = Tk()
# Buttons
C=Button(tk, text="Cobwebs",         command=Cobweb , height = 1, width = 10)
T=Button(tk, text="TNT (Primed)",    command=TNT    , height = 1, width = 10)
W=Button(tk, text="Water",           command=Water  , height = 1, width = 10)
L=Button(tk, text="Lava",            command=Lava   , height = 1, width = 10)
F=Button(tk, text="Furnace(Active)", command=Furnace, height = 1, width = 10)
P=Button(tk, text="Get Position",    command=Pos    , height = 1, width = 10)
P.pack()
T.pack()
W.pack()
L.pack()
F.pack()
C.pack()
Pos()
tk.mainloop()
