import mcpi.minecraft as minecraft
import mcpi.block as block
mc = minecraft.Minecraft.create()
height=5
for x in range(-128,128):
	for z in range(-128,128):
		mc.setBlocks(x,-64,z,x,64,z,block.AIR);
		mc.setBlocks(x,-60,z,x,-60+height,z,block.GRASS);
		mc.setBlocks(x,-61,z,x,-63,z,block.STONE);
		mc.setBlocks(x,-64,z,x,-64,z,block.BEDROCK);
mc.postToChat("Done")
print("Done")
