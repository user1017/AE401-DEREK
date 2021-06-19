# -*- coding: utf-8 -*-
"""
Created on Sat Jun 19 10:03:15 2021

@author: Derek
"""

from mcpi.minecraft import Minecraft
mc= Minecraft.create()

x,y,z=mc.player.getTilePos()

import random

for j in range(10):
    x,y,z=mc.player.getTilePos()
    x=x+j

    for i in range(10):
        r=random.randrange(1,16)
        z=z+1
        mc.setBlock(x,y,z,35,r) 