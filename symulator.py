#!/usr/bin/env python
from random import randint
import time

class RepairFly :
#Class to simulating problem during the fly

   def __init__(self,d,a) :
	
	if d== 0 : 
           dstr="left"
	else :
           dstr="right"

	self.dict={"dir":dstr, "alpha":a}

   def repair(self) :
   #Function to repair angle
   
	if self.dict["dir"]=="left":
	   print "Correction to rigt ",self.dict["alpha"]
        else:
           print "Correction to left ",self.dict["alpha"]

   			



