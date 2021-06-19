# -*- coding: utf-8 -*-
"""
Created on Sat Jun 19 10:31:26 2021

@author: Derek
"""

from mcpi.minecraft import Minecraft
mc= Minecraft.create()

x,y,z=mc.player.getTilePos()

from random import randrange
import time

r=randrange(0,16)
t=0

while True:
    hits=mc.events.pollBlockHits()
    if len(hits)>0:
        hit=hits[0]
        
        block=mc.getBlockWithData(hit.pos)
        data=block.data
        if data==r:
            mc.postToChat("恭喜找到我")
            mc.setBlock(hit.pos,57)
            break
        elif data<r:
            mc.postToChat("找更大的子ID吧")
        elif data>r:
            mc.postToChat("找更小的子ID吧") 
            
        t=t+1
        if t>5:
            mc.postToChat("失敗")
            time.sleep(3)
            x,y,z=mc.player.getTilePos()
            mc.createExplosion(x,y,z)
                  