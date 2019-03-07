import mcpi.minecraft as minecraft
import mcpi.block as block
from random import randint
import time

#Variables
levelSize=12    #Width and Length
levelHeight=1   #Height and Delay
structAlt=40    #Altitude to Build
MakeTNT=True    #Players can make TNT
entityToPlace=1
mc = minecraft.Minecraft.create()
#Clear Blocks Below
mc.setBlocks(levelSize*-2,0,levelSize*-2,levelSize*2,structAlt-30,levelSize*2,block.AIR)

#Wipe area and Build arena
def BuildArena():
	mc.setBlocks(levelSize*-2,structAlt-30,levelSize*-2,levelSize*2,structAlt+80,levelSize*2,block.AIR)
	time.sleep(0.2)
	mc.setBlocks(levelSize*-1,structAlt-6,levelSize*-1,levelSize,structAlt-6,levelSize,block.TNT,1);
	time.sleep(0.2)
	mc.setBlocks(levelSize*-1,structAlt-5,levelSize*-1,levelSize,structAlt+levelHeight-5,levelSize,block.SAND);
	time.sleep(0.2)
	BuildStructures()
#Build Lobby and Put Creepers in
def BuildLobby():
  global players
  mc.setBlocks(15+levelSize,structAlt-5,-15,15+levelSize,structAlt+10,15,block.AIR);
  #Main Box
  mc.setBlocks(20+levelSize,structAlt-1,-10,10+levelSize,structAlt+5,10,block.WOOD);
  mc.setBlocks(19+levelSize,structAlt,-9,11+levelSize,structAlt+4,9,block.AIR);
  time.sleep(0.1)
  #Creeper Area
  mc.setBlocks(19+levelSize,structAlt,-8,14+levelSize,structAlt+5,-3,block.GLASS);
  mc.setBlocks(19+levelSize,structAlt,-7,15+levelSize,structAlt+4,-4,block.AIR);
  time.sleep(0.1)
  for ent in range(1,11):
    try:
      if ent!=players:
        mc.entity.setPos(ent,18+levelSize,structAlt,-6)
      
    except:
      print("No Entity!")
  for ENT in players:
    mc.entity.setPos(ENT,18+levelSize,structAlt,3)
  #Floor and Window
  mc.setBlocks(10+levelSize,structAlt,-10,10+levelSize,structAlt+4,10,block.AIR);
  time.sleep(0.1)
  mc.setBlocks(20+levelSize,structAlt-1,-10,10+levelSize,structAlt-1,10,block.STONE_BRICK,3);
  #Controls and Decor
  mc.setBlock(17+levelSize,structAlt,3,block.TNT)#GO
  mc.setBlock(17+levelSize,structAlt,5,block.GRAVEL)#GO
  mc.setBlock(17+levelSize,structAlt,7,block.SANDSTONE)#GO
  mc.setBlock(17+levelSize,structAlt,1,26,9)#Respawn
  mc.setBlock(18+levelSize,structAlt,1,26,5)#Respawn
  mc.setBlock(15+levelSize,structAlt+4,3,block.GLOWSTONE_BLOCK)
  mc.setBlock(15+levelSize,structAlt+4,6,block.GLOWSTONE_BLOCK)
  mc.setBlock(15+levelSize,structAlt+4,0,block.GLOWSTONE_BLOCK)
#Get Block removes
def Up_Lobby():
  global entityToPlace
  global levelHeight
  # Check for Go Signal
  if mc.getBlock(17+levelSize,structAlt,3)==0:
    mc.setBlock(17+levelSize,structAlt,3,block.TNT)
    BuildArena()
    mc.postToChat("Ready")
    mc.entity.setPos(entityToPlace,randint(-10,10),levelHeight+structAlt-2,randint(-10,10))
    entityToPlace=entityToPlace+1
    #Make Platform an Put Players on it
    mc.setBlocks(-5,+structAlt+10,-5,5,structAlt+10,5,block.GLASS)
    #Destroy Platform
    time.sleep(10)
    mc.postToChat("Go")
    mc.setBlocks(-5,+structAlt+10,-5,5,structAlt+10,5,block.AIR)
#Destroy Ground under entities
def RmvGnd():
	try:
		for ENT in players:
			ENTpos=mc.entity.getPos(ENT)
			if ENTpos.y>structAlt-7 and mc.getBlock(ENTpos.x,ENTpos.y-1,ENTpos.z)!=block.AIR.id:
				mc.setBlock(ENTpos.x,structAlt-6,ENTpos.z,block.AIR)
	except:
		print("No Entity"+str(ENT))
#Add Random Blocks to game
def addRandBlocks():
	if randint(0,10)<1 and mc.getBlock(17+levelSize,structAlt,5)==13:#Gravel
		mc.setBlock(randint(levelSize*-1,levelSize),structAlt+5,randint(levelSize*-1,levelSize),block.GRAVEL)
#Hit Block To Make TNT
def MkTNT():
	if MakeTNT:
		hits = mc.events.pollBlockHits()
		for hit in hits:
			mc.setBlock(hit.pos.x, hit.pos.y, hit.pos.z, 46, 1)

def BuildStructures():
	if mc.getBlock(17+levelSize,structAlt,7)==24:
		mc.setBlocks(-4,structAlt+levelHeight-4,-4,4,structAlt+levelHeight-3,4,block.SAND);

#Program Start
mc.postToChat("Initializing TNT Run...")
players=mc.getPlayerEntityIds()
BuildArena()
BuildLobby()

#Main Loop

while True:
	try:
		RmvGnd()
		addRandBlocks()
		#MkTNT()
		Up_Lobby()
	except:
		print("Something Didn't Work")
		time.sleep("0.5")
