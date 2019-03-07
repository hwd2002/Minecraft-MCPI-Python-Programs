import mcpi.minecraft as minecraft
import mcpi.block as block
from random import randint
import time, math
mc = minecraft.Minecraft.create()
PlayerX=0
OldX=False
Hit=False
CamX=0
Alt=mc.getHeight(0,0)
PlayerY=20+Alt
PlayerZ=0
Reload=0
Sensitivity=0.3
#Clear Area
mc.saveCheckpoint()
mc.setBlocks(-4,-2+Alt,-4,4,2+Alt,4,0)
mc.setBlocks(PlayerX-20,PlayerY,PlayerZ-20,PlayerX+20,PlayerY,PlayerZ+20,0)
mc.setBlocks(PlayerX-10,PlayerY-2,PlayerZ-10,PlayerX+10,PlayerY-2,PlayerZ+10,80)
#Player Control Towers
mc.setBlocks(-3,-1+Alt,-3,3,-1+Alt,3,2)
mc.player.setPos(0.5,Alt,0)
mc.setBlocks(-2,Alt,0,-2,Alt,0,1)#Right
mc.setBlocks(2,Alt,0,2,Alt,0,1)#Left
mc.setBlocks(0,Alt,2,0,Alt,2,1)#Up
mc.setBlock(0,Alt+1,2,block.DIAMOND_BLOCK)#UpPointer
mc.setBlocks(0,Alt,-2,0,2+Alt,-2,1)#Down
#Get Player to face north
mc.postToChat("Face the Diamond block, press Tab and then Sneak.")
Calibrating=True
while Calibrating:
    Pos=mc.player.getPos()
    mc.player.setPos(0.5,Alt,0.5)
    if Pos.y<Alt:
        Calibrating=False
mc.camera.setFixed()
mc.camera.setPos(CamX,PlayerY+6,PlayerZ+3)
Shots=[]
Asteroids=[]
Game=True
try:
    while Game:
        Pos=mc.player.getPos()
        mc.player.setPos(0.5,Alt,0.5)
        
        if Hit==False:#Alive
            #Move and Fire
            OldX=False
            if Reload>0:#Reload Time
                Reload=Reload-1
            if Pos.y<Alt and Reload<1 and len(Shots)<=4:#Fire
                Shots.append([PlayerX,PlayerY,PlayerZ+1])
                Reload=5
            if Pos.x>0.5+Sensitivity and PlayerX<5:#Right
                PlayerX=PlayerX+1
                OldX=True
            if Pos.x<0.5-Sensitivity and PlayerX>-5:#Left
                PlayerX=PlayerX-1
                OldX=True
            
            #Draw Ship
            mc.setBlock(PlayerX-1,PlayerY,PlayerZ,44)
            mc.setBlock(PlayerX+1,PlayerY,PlayerZ,44)
            if Reload<1:
                mc.setBlock(PlayerX,PlayerY,PlayerZ,247,0)
            else:
                mc.setBlock(PlayerX,PlayerY,PlayerZ,247,2)
            mc.setBlock(PlayerX,PlayerY,PlayerZ+1,89)

            
            #Del Old Blocks
            if OldX:
                mc.setBlock(PlayerX-2,PlayerY,PlayerZ,0)
                mc.setBlock(PlayerX+2,PlayerY,PlayerZ,0)
                mc.setBlock(PlayerX-1,PlayerY,PlayerZ+1,0)
                mc.setBlock(PlayerX+1,PlayerY,PlayerZ+1,0)

            #Update Bullets
            try:
                for B in range(len(Shots)):
                    Shots[B][2]=Shots[B][2]+1
                    if Shots[B][2]>10:
                        mc.setBlock(Shots[B][0],Shots[B][1],Shots[B][2]-1,0)
                        del Shots[B]
                    else:
                        mc.setBlock(Shots[B][0],Shots[B][1],Shots[B][2],246)
                        mc.setBlock(Shots[B][0],Shots[B][1],Shots[B][2]-1,0)
            except:
                pass

            
            #Update Asteroids
            try:
                #New Asteroid
                if randint(0,12)==1 and len(Asteroids)<5:
                    Asteroids.append([randint(-4,4),PlayerY,PlayerZ+10])
                #Update Asteroids
                for A in range(len(Asteroids)):
                    BlockA=mc.getBlock(Asteroids[A][0],Asteroids[A][1],Asteroids[A][2])
                    BlockB=mc.getBlock(Asteroids[A][0],Asteroids[A][1],Asteroids[A][2]-1)
                    if BlockA==246 or BlockB==246:
                        del Asteroids[A]
                    if Asteroids[A][2]<-10:
                        mc.setBlock(Asteroids[A][0],Asteroids[A][1],Asteroids[A][2],0)
                        del Asteroids[A]
                    else:
                        Asteroids[A][2]=Asteroids[A][2]-1
                        mc.setBlock(Asteroids[A][0],Asteroids[A][1],Asteroids[A][2],49)
                        mc.setBlock(Asteroids[A][0],Asteroids[A][1],Asteroids[A][2]+1,0)

            except:
                pass


            #Check for collisions
            Hit=False
            Check=mc.getBlock(PlayerX-1,PlayerY,PlayerZ)
            if Check!=44:
                Hit=True
            Check=mc.getBlock(PlayerX+1,PlayerY,PlayerZ)
            if Check!=44:
                Hit=True
            Check=mc.getBlock(PlayerX,PlayerY,PlayerZ)
            if Check!=247:
                Hit=True

            #Die
            if Hit:
                mc.player.setPos(0,-200,0)
                time.sleep(1)
                mc.player.setPos(0,Alt,0)
                time.sleep(2)

            #Sleep
            time.sleep(0.1)
        
        elif Pos.y<0:#Respawn
            Hit=False
            Asteroids=[]
            Shots=[]
            PlayerX=0
            mc.restoreCheckpoint()
            mc.setBlocks(PlayerX-20,PlayerY,PlayerZ-20,PlayerX+20,PlayerY,PlayerZ+20,0)
            mc.setBlocks(PlayerX-10,PlayerY-2,PlayerZ-10,PlayerX+10,PlayerY-2,PlayerZ+10,80)
            time.sleep(0.5)
except:
    print("Bye")
    mc.camera.setNormal()
    mc.restoreCheckpoint()
