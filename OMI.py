# -*- coding: utf-8 -*-
"""
#***********************************************************************#
# Copyright (C) 2014 Prabod Rathnayaka									#
# This file is part of OMI-The Game.									#
#																		#
# OMI-The Game is free software: you can redistribute it and/or modify  #
# it under the terms of the GNU General Public License as published by  #
# the Free Software Foundation, either version 3 of the License, or     #
# any later version.													#
#																		#
# OMI-The Game is distributed in the hope that it will be useful,		#
# but WITHOUT ANY WARRANTY; without even the implied warranty of		#
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the			#
# GNU General Public License for more details.							#
#																		#
# You should have received a copy of the GNU General Public License		#
#***********************************************************************#

"""


#Imports
import math
import random

from Tkinter import *
from Canvas import Rectangle, CanvasText, Group, Window


#########################################################################
class Cards:
	"""

	Class that used to Shuffle cards,Divide cards among four players,and 
	card Drawing instuctions to cpu players.

	"""
	def __init__(self):
		self.CardDeck = range(0,32) #Saves the card deck into a list
		self.Dummy=[0,0,0,0] # dummy for choose fovourite
		self.temp = [] # Temp for check 
		self.difsuit=True
		
	def DivideRound1(self,player1,player2,player3,player4):
	
		""" Shuffling until gets 2 or more from same suit """ 
		while self.difsuit:
				random.shuffle(self.CardDeck) #shuffle the cards
				for i in CardDeck[0:4]:  
					if i//8==0:
						self.temp.append(0) 
				
					if i//8==1:
						self.temp.append(1)
				
					if i//8==2:
						self.temp.append(2)
				
					if i//8==3:
						self.temp.append(3)
						
				if temp.count(0) == temp.count(1) == temp.count(2) == temp.count(3):
					random.shuffle(self.CardDeck) #shuffle the cards
				else:
					self.difsuit=False
					
		for i in range(4):
			player1.append([])
			player1[i].append(self.CardDeck[i]//8) #suit of the card
			player1[i].append(self.CardDeck[i])  #Four Cards to Player1
		for i in range(4,8):
			player2.append([])
			player2[i].append(self.CardDeck[i]//8) #suit of the card
			player2[i].append(self.CardDeck[i])  #Four Cards to Player1
		
		for i in range(8,12):
			player3.append([])
			player3[i].append(self.CardDeck[i]//8) #suit of the card
			player3[i].append(self.CardDeck[i])  #Four Cards to Player1
		
		for i in range(12,16):
			player4.append([])
			player4[i].append(self.CardDeck[i]//8) #suit of the card
			player4[i].append(self.CardDeck[i])  #Four Cards to Player1
	
	def DivideRound2(self,player1,player2,player3,player4):		
		for i in range(16,20):
			player1.append(self.CardDeck[i])  #Four Cards to Player1
		
		for i in range(20,24):
			player2.append(self.CardDeck[i])  #Four Cards to Player2
		
		for i in range(24,28):
			player3.append(self.CardDeck[i])  #Four Cards to Player3
		
		for i in range(28,32):
			player4.append(self.CardDeck[i])  #Four Cards to Player4	
				
	def Favourite(self,playerX): #Choosing Favourite
		for i in range(4):
			if playerX[i][1]//8==0:
				self.Dummy[0]+=playerX[i][1]%8 
			
			if playerX[i][1]//8==1:
				self.Dummy[1]+=playerX[i][1]%8
				
			if playerX[i][1]//8==2:
				self.Dummy[2]+=playerX[i][1]%8
				
			if playerX[i][1]//8==3:
				self.Dummy[3]+=playerX[i][1]%8
			
		return self.Dummy.index(max(self.Dummy))
			
##########################################################################

class RotatePlayer:
	def __init__(self,South,East,North,West,max,choosefav,Fav,master):
		self.Player1 = [] 
		self.Player2 = [] 
		self.Player3 = [] 
		self.Player4 = [] 
	
	def DivideCards(self,Player1,Player2,Player3,Player4):
		
		Card=Cards() #call Cards class
		
		Card.DivideRound1(self.Player1,self.Player2,self.Player3,self.Player4)
		
		if ChooseFav % 4 == 0: #Prompting for Fav from the user
			self.w=popupFav(master)
			self.master.wait_window(self.w.top)
			Fav=self.w.value
		else:
			Fav=card.Favourite(choosefav)
			Card.DivideRound2(self.Player1,self.Player2,self.Player3,self.Player4)
			
	def Chooseplayer(self,South,East,North,West):
		if max == 0:
			South = self.Player1
			East = self.Player2
			North = self.Player3
			West = self.Player4
		elif max == 1:
			East = self.Player1
			North = self.Player2
			West = self.Player3
			South = self.Player4
		elif max == 2:
			North = self.Player1
			West = self.Player2
			South = self.Player3
			East = self.Player4
		else:
			West = self.Player1
			South = self.Player2
			East = self.Player3
			North = self.Player4
			
#######################################################################################			
class popupFav(object): #popup window for Fav prompt for user
    def __init__(self,master):
        top=self.top=Toplevel(master)
        self.l=Label(top,text= u'තුරුම්පු තෝරන්න')
        self.l.pack()
        self.b0=Button(top,image=PhotoImage(file = "image/spade.gif"),command=self.spade,relief="ridge",height="50px",width="50px")
        self.b0.pack(side=LEFT)
        
        self.b1=Button(top,image=PhotoImage(file = "image/club.gif"),command=self.club,relief="ridge",height="50px",width="50px")
        self.b1.pack(side=LEFT)
        
        self.b2=Button(top,image=PhotoImage(file = "image/diamond.gif"),command=self.diamond,relief="ridge",height="50px",width="50px")
        self.b2.pack(side=LEFT)
        
        self.b3=Button(top,image=PhotoImage(file = "image/heart.gif"),command=self.heart,relief="ridge",height="50px",width="50px")
        self.b3.pack(side=LEFT)
        
    def spade(self):
        self.value=0
        self.top.destroy()
	def club(self):
		self.value=1
        self.top.destroy()
    def diamond(self):
        self.value=2
        self.top.destroy()
    def heart(self):
        self.value=3
        self.top.destroy()
#########################################################################################

class mainscreen(object):
	def __init__(self,master):
		self.imageList=[] #save card images
		
		for i in range(32):
			self.imageList.append(PhotoImage(file = "image/"+ str(i) + ".gif"))
		
		self.South = [] #User
		self.East = [] #Cpu player1
		self.North = [] #Cpu Team mate with user
		self.West = [] #Cpu player2
		
		self.max = 0 #Record the player who played the highest card, South=0 East =1 North =2 West =3
		self.Fav = 0 #Saves The Favourite suit for the Round
		self.choosefav = 0 #Record the player who have to choose favourite suit South=0 East =1 North =2 West =3 
		self.round = 0 #ongoing round
		
		# divide cards into 4 lists
		if self.round % 4 == 0:
			DivideCards(self.South,self.East,self.North,self.West)
			self.round += 1
			self.choosefav += 1
		elif self.round % 4 == 1:
			DivideCards(self.East,self.North,self.West,self.South)
			self.round += 1
			self.choosefav += 1
			Fav=Favourite(self.East)
		elif self.round % 4 == 2:
			DivideCards(self.North,self.West,self.South,self.East)
			self.round += 1
			self.choosefav += 1
			Fav=Favourite(self.North)
		elif self.round % 4 == 3:
			DivideCards(self.West,self.South,self.East,self.North)
			self.round += 1
			self.choosefav += 1
			Fav=Favourite(self.West)
		
		South.sort() #sort the card set 
		
	def DealFirst(self,Player):
		for i in range(8):
			if Player[i][1] == 7 or Player[i][1] == 15 or Player[i][1] == 23 or Player[i][1] == 31 and Player[i][0] != self.Fav:
				return Player[i][1] #If you got an Ace fire Away !!
			else:
				min=9
				if Player[i][1] <min and Player[i][0] != self.Fav:
					min = Player[i][1]
		return min
