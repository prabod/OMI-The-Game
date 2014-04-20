# -*- coding: utf-8 -*-
# -*- coding:sid_ET UTF-8-*- 
#-*- coding:si_LK UTF-8-*-
# -*- coding:sk_SK ISO-8859-2 -*-
"""
#***********************************************************************#
# Copyright (C) 2014 Prabod Rathnayaka                                  #
# This file is part of OMI-The Game.                                    #
#                                                                       #
# OMI-The Game is free software: you can redistribute it and/or modify  #
# it under the terms of the GNU General Public License as published by  #
# the Free Software Foundation, either version 3 of the License, or     #
# any later version.                                                    #
#                                                                       #
# OMI-The Game is distributed in the hope that it will be useful,       #
# but WITHOUT ANY WARRANTY; without even the implied warranty of        #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the	        #
# GNU General Public License for more details.                          #
#                                                                       #
# You should have received a copy of the GNU General Public License     #
#***********************************************************************#

"""


#Imports
import math
import random
import time
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
				for i in self.CardDeck[0:4]:  
					if i//8==0:
						self.temp.append(0) 
				
					if i//8==1:
						self.temp.append(1)
				
					if i//8==2:
						self.temp.append(2)
				
					if i//8==3:
						self.temp.append(3)
						
				if self.temp.count(0) == self.temp.count(1) == self.temp.count(2) == self.temp.count(3):
					random.shuffle(self.CardDeck) #shuffle the cards
				else:
					self.difsuit=False
					
		for i in range(4):
			player1.append(self.CardDeck[i])  #Four Cards to Player1
		for i in range(4,8):
			player2.append(self.CardDeck[i])  #Four Cards to Player1
		
		for i in range(8,12):
			player3.append(self.CardDeck[i])  #Four Cards to Player1
		
		for i in range(12,16):
			player4.append(self.CardDeck[i])  #Four Cards to Player1
	
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
			if playerX[i]//8==0:
				self.Dummy[0]+=playerX[i]%8 
			
			if playerX[i]//8==1:
				self.Dummy[1]+=playerX[i]%8
				
			if playerX[i]//8==2:
				self.Dummy[2]+=playerX[i]%8
				
			if playerX[i]//8==3:
				self.Dummy[3]+=playerX[i]%8
			
		return self.Dummy.index(max(self.Dummy))
			
##########################################################################

class RotatePlayer:
	def __init__(self,Player1,Player2,Player3,Player4,max,choosefav,Fav,master):
		self.Player1 = [] 
		self.Player2 = [] 
		self.Player3 = [] 
		self.Player4 = [] 
		self.chooseFav=choosefav
		self.master=master
		
	
	def Chooseplayer(self,South,East,North,West):
		if max == 0:
			South = self.Player1
		elif max == 1:
			East = self.Player1
		elif max == 2:
			North = self.Player1
		else:
			West = self.Player1
			
#######################################################################################	

class mainscreen(object):
	def __init__(self,master):
		self.imageList=[] #save card images
		self.master=master
		
		for i in range(32):
			self.imageList.append(PhotoImage(file = "image/"+ str(i) + ".gif"))
		self.Board = []
		self.South = [] #User
		self.East = [] #Cpu player1
		self.North = [] #Cpu Team mate with user
		self.West = [] #Cpu player2
		self.Boardcard=[]
		self.win = False
		self.userhandwin = 0
		self.cpuhandwin = 0
		self.Player1 = [] 
		self.Player2 = [] 
		self.Player3 = [] 
		self.Player4 = [] 
		
		self.player1=0
		self.player2=0
		self.player3=0
		self.player4=0
		
		self.ver=150
		self.hor=260
		
		self.prompt=False
		self.pro=False
		
		self.max = 0 #Record the player who played the highest card, South=0 East =1 North =2 West =3
		self.Fav = 0 #Saves The Favourite suit for the Round
		self.choosefav = 0 #Record the player who have to choose favourite suit South=0 East =1 North =2 West =3 
		self.round = 0 #ongoing round
		self.user=False
		
		self.Eastcard=[]
		self.Northcard=[]
		self.Westcard=[]
		
		self.OMI()
		self.play()
		self.GUI()
		##GUI
	def GUI(self):
		self.canvas = Canvas(self.master,
                             background='#070')
		self.canvas.pack(fill=BOTH, expand=TRUE)
		self.usercard1 = Label(self.canvas, image=self.imageList[self.South[0]], cursor="left_ptr")
		self.usercard1.place(x=260, y=450)
		self.usercard1.bind("<1>",self.ClickHandler1)
		
		self.usercard2 = Label(self.canvas, image=self.imageList[self.South[1]], cursor="left_ptr")
		self.usercard2.place(x=280, y=450)
		self.usercard2.bind("<1>",self.ClickHandler2)
		
		self.usercard3 = Label(self.canvas, image=self.imageList[self.South[2]], cursor="left_ptr")
		self.usercard3.place(x=300, y=450)
		self.usercard3.bind("<1>",self.ClickHandler3)
		
		self.usercard4 = Label(self.canvas, image=self.imageList[self.South[3]], cursor="left_ptr")
		self.usercard4.place(x=320, y=450)
		self.usercard4.bind("<1>",self.ClickHandler4)
		
		self.l = Label(self.canvas, text=u"තුරුම්පු තෝරන්න")
		self.Photospade=PhotoImage(file = "image/spade.gif")
		self.Photoclub=PhotoImage(file = "image/club.gif")
		self.Photodiamond=PhotoImage(file = "image/diamond.gif")
		self.Photoheart=PhotoImage(file = "image/heart.gif")
		self.b0=Label(self.canvas,image=self.Photospade, relief="ridge",height="50px",width="50px")
		self.b0.bind("<1>",self.spade)
		
		self.b1=Label(self.canvas,image=self.Photoclub, relief="ridge",height="50px",width="50px")
		self.b1.bind("<1>",self.club)
		
		self.b2=Label(self.canvas,image=self.Photodiamond,relief="ridge",height="50px",width="50px")
		self.b2.bind("<1>",self.diamond)
		
		self.b3=Label(self.canvas,image=self.Photoheart, relief="ridge",height="50px",width="50px")
		self.b3.bind("<1>",self.heart)
		
		self.backh=PhotoImage(file = "image/backh.gif")
		self.backv=PhotoImage(file = "image/backv.gif")
		
		
		
		for h in range(4):
			self.Eastcard.append(Label(self.canvas, image = self.backv))
			self.Eastcard[h].place(x=650,y=self.ver)
			self.Northcard.append(Label(self.canvas, image = self.backh))
			self.Northcard[h].place(x=self.hor,y=50)
			self.Westcard.append(Label(self.canvas, image = self.backv))
			self.Westcard[h].place(x=50,y=self.ver)
			self.ver+=20
			self.hor+=20
			
		for i in range(len(self.Board)):
			sec=0
			self.Boardcard.append(Label(self.canvas, image=self.imageList[self.Board[i]]))
			if i == 0:
				dx=300
				dy=200
			elif i == 1:
				dx=400
				dy=200
			elif i == 2:
				dx=300
				dy=320
			elif i == 3:
				dx=400
				dy=320			
			self.Boardcard[i].place(x=dx, y=dy)
			self.master.update_idletasks()
						
		if self.prompt:
			self.l.place(x=300,y=300)
			self.b0.place(x=250,y=350)
			self.b1.place(x=320,y=350)
			self.b2.place(x=390,y=350)
			self.b3.place(x=460,y=350)
			self.master.update_idletasks()
		
		if self.pro:
			self.usercard5 = Label(self.canvas, image=self.imageList[self.South[4]], cursor="left_ptr")
			self.usercard5.place(x=340, y=450)
			self.usercard5.bind("<1>",self.ClickHandler5)
		
			self.usercard6 = Label(self.canvas, image=self.imageList[self.South[5]], cursor="left_ptr")
			self.usercard6.place(x=360, y=450)
			self.usercard6.bind("<1>",self.ClickHandler6)
		
			self.usercard7 = Label(self.canvas, image=self.imageList[self.South[6]], cursor="left_ptr")
			self.usercard7.place(x=380, y=450)
			self.usercard7.bind("<1>",self.ClickHandler7)
		
			self.usercard8 = Label(self.canvas, image=self.imageList[self.South[7]], cursor="left_ptr")
			self.usercard8.place(x=400, y=450)
			self.usercard8.bind("<1>",self.ClickHandler8)
			
			for h in range(4,8):
				self.Eastcard.append(Label(self.canvas, image = self.backv))
				self.Eastcard[h].place(x=650,y=self.ver)
				self.Northcard.append(Label(self.canvas, image = self.backh))
				self.Northcard[h].place(x=self.hor,y=50)
				self.Westcard.append(Label(self.canvas, image = self.backv))
				self.Westcard[h].place(x=50,y=self.ver)
				self.ver+=20
				self.hor+=20
			self.master.update_idletasks()
			self.pro= False
				
	def DivideCards(self,Player1,Player2,Player3,Player4):
		
		Card=Cards() #call Cards class
		
		Card.DivideRound1(Player1,Player2,Player3,Player4)
		
		if self.round % 4 == 0: #Prompting for Fav from the user
			self.prompt=True
		else:
			self.pro=True
			if self.round == 1:
				plyr = self.East
			elif self.round == 2:
				plyr = self.North
			else:
				plyr = self.West
			self.Fav=Card.Favourite(plyr)
		Card.DivideRound2(Player1,Player2,Player3,Player4)
		self.master.update_idletasks()
				
	def DrawCards(self):
		self.usercard1 = Label(self.canvas, image=self.imageList[self.South[0]], cursor="left_ptr")
		self.usercard1.place(x=260, y=450)
		self.usercard1.bind("<1>",self.ClickHandler1)
		
		self.usercard2 = Label(self.canvas, image=self.imageList[self.South[1]], cursor="left_ptr")
		self.usercard2.place(x=280, y=450)
		self.usercard2.bind("<1>",self.ClickHandler2)
		
		self.usercard3 = Label(self.canvas, image=self.imageList[self.South[2]], cursor="left_ptr")
		self.usercard3.place(x=300, y=450)
		self.usercard3.bind("<1>",self.ClickHandler3)
		
		self.usercard4 = Label(self.canvas, image=self.imageList[self.South[3]], cursor="left_ptr")
		self.usercard4.place(x=320, y=450)
		self.usercard4.bind("<1>",self.ClickHandler4)
		
		self.usercard5 = Label(self.canvas, image=self.imageList[self.South[4]], cursor="left_ptr")
		self.usercard5.place(x=340, y=450)
		self.usercard5.bind("<1>",self.ClickHandler5)
		
		self.usercard6 = Label(self.canvas, image=self.imageList[self.South[5]], cursor="left_ptr")
		self.usercard6.place(x=360, y=450)
		self.usercard6.bind("<1>",self.ClickHandler6)
		
		self.usercard7 = Label(self.canvas, image=self.imageList[self.South[6]], cursor="left_ptr")
		self.usercard7.place(x=380, y=450)
		self.usercard7.bind("<1>",self.ClickHandler7)
		
		self.usercard8 = Label(self.canvas, image=self.imageList[self.South[7]], cursor="left_ptr")
		self.usercard8.place(x=400, y=450)
		self.usercard8.bind("<1>",self.ClickHandler8)
		for h in range(4,8):
				self.Eastcard.append(Label(self.canvas, image = self.backv))
				self.Eastcard[h].place(x=650,y=self.ver)
				self.Northcard.append(Label(self.canvas, image = self.backh))
				self.Northcard[h].place(x=self.hor,y=50)
				self.Westcard.append(Label(self.canvas, image = self.backv))
				self.Westcard[h].place(x=50,y=self.ver)
				self.ver+=20
				self.hor+=20
		self.master.update()
		
	def spade(self,event):
		self.Fav=0
		self.l.destroy()
		self.b0.destroy()
		self.b1.destroy()
		self.b2.destroy()
		self.b3.destroy()
		self.prompt=False
		
		self.usercard1.destroy()
		self.usercard2.destroy()
		self.usercard3.destroy()
		self.usercard4.destroy()
		self.South.sort()
		self.DrawCards()
		self.Favlabel=Label(self.canvas,height="50",width="50")
		self.Favlabel.place(x=300, y=550)
		self.Favlabel["image"]=self.Photospade
               
	def club(self,event):
		self.Fav=1
		self.l.destroy()
		self.b0.destroy()
		self.b1.destroy()
		self.b2.destroy()
		self.b3.destroy()
		self.prompt=False
		
		self.usercard1.destroy()
		self.usercard2.destroy()
		self.usercard3.destroy()
		self.usercard4.destroy()
		self.South.sort()
		
		self.DrawCards()
		self.Favlabel=Label(self.canvas,height="50",width="50")
		self.Favlabel.place(x=300, y=550)
		self.Favlabel["image"]=self.Photoclub
		
	def diamond(self,event):
		self.Fav=2
		self.l.destroy()
		self.b0.destroy()
		self.b1.destroy()
		self.b2.destroy()
		self.b3.destroy()
		self.prompt=False
		
		self.usercard1.destroy()
		self.usercard2.destroy()
		self.usercard3.destroy()
		self.usercard4.destroy()
		self.South.sort()
		
		self.DrawCards()
		self.Favlabel=Label(self.canvas,height="50",width="50")
		self.Favlabel.place(x=300, y=550)
		self.Favlabel["image"]=self.Photodiamond
		
	def heart(self,event):
		self.Fav=3
		self.l.destroy()
		self.b0.destroy()
		self.b1.destroy()
		self.b2.destroy()
		self.b3.destroy()
		self.prompt=False
		
		self.usercard1.destroy()
		self.usercard2.destroy()
		self.usercard3.destroy()
		self.usercard4.destroy()
		self.South.sort()
		
		self.DrawCards()
		self.Favlabel=Label(self.canvas,height="50",width="50")
		self.Favlabel.place(x=300, y=550)
		self.Favlabel["image"]=self.Photoheart
	
	def DEAL(self):
		if self.max == 0:
			self.DealUsermax0()
			self.handwincheck()
			self.roundwincheck()
		elif self.max == 1:
			self.handwincheck()
			self.roundwincheck()
		elif self.max == 2:
			self.DealUsermax2()
			self.handwincheck()
			self.roundwincheck()
		elif self.max == 3:
			self.DealUsermax3()
			self.handwincheck()
			self.roundwincheck()
		self.master.update_idletasks()	
		self.updateBoard()
		
	def ClickHandler1(self,event):
		self.Board.append(self.South[0])
		self.usercard1.destroy()
		self.master.update()
		self.updateBoard()
		self.DEAL()
		
	def ClickHandler2(self,event):
		self.Board.append(self.South[1])
		self.usercard2.destroy()
		self.master.update()
		self.updateBoard()
		self.DEAL()
		
	
	def ClickHandler3(self,event):
		self.Board.append(self.South[2])
		self.usercard3.destroy()
		self.master.update()
		self.updateBoard()
		self.DEAL()
	
	def ClickHandler4(self,event):
		self.Board.append(self.South[3])
		self.usercard4.destroy()
		self.master.update()
		self.updateBoard()
		self.DEAL()
	
	def ClickHandler5(self,event):
		self.Board.append(self.South[4])
		self.usercard5.destroy()
		self.master.update()
		self.updateBoard()
		self.DEAL()
	
	def ClickHandler6(self,event):
		self.Board.append(self.South[5])
		self.usercard6.destroy()
		self.master.update()
		self.updateBoard()
		self.DEAL()
		
	def ClickHandler7(self,event):
		self.Board.append(self.South[6])
		self.usercard7.destroy()
		self.master.update()
		self.updateBoard()
		self.DEAL()
		
	def ClickHandler8(self,event):
		self.Board.append(self.South[7])
		self.usercard8.destroy()
		self.master.update()
		self.updateBoard()
		self.DEAL()
	
	def updateBoard(self):
		if len(self.Board)>0:
			self.Boardcard.append(Label(self.canvas, image=self.imageList[self.Board[len(self.Board)-1]]))
			if len(self.Board)-1 == 0:
				dx=300
				dy=200
			elif len(self.Board)-1 == 1:
				dx=400
				dy=200
			elif len(self.Board)-1 == 2:
				dx=300
				dy=320
			elif len(self.Board)-1 == 3:
				dx=400
				dy=320			
			self.Boardcard[len(self.Boardcard)-1].place(x=dx, y=dy)
		time.sleep(0.1)
		self.master.update_idletasks()
	
	def handwincheck(self):
		self.max=self.Board.index(max(self.Board))
		time.sleep(0.1)
		
		for i in range(len(self.Boardcard)):
			j=self.Boardcard[i]
			k=j.place_info()
			if self.max == 0:
				destx=330
				desty=450
			elif self.max == 1:
				destx=650
				desty=250
			elif self.max == 2:
				destx=330
				desty=50
			elif self.max == 3:
				destx=50
				desty=250
			kv=eval(k["y"])+10
			kh=eval(k["x"])+10
			first=0
			dest=0
			if self.max == 0 or self.max == 2:
				first=eval(k["y"])
				dest=desty
			elif self.max == 1 or self.max == 3:
				first=eval(k["x"])
				dest=destx
			for h in range(first,dest,10):
				j.place_forget()
				self.master.update()
				if self.max == 0 or self.max == 2:
					kx=kh
					j.place(x=kx,y=h)
					j.tkraise()
					self.master.update()
				elif self.max == 1 or self.max == 3:
					ky=kv	 
					j.place(x=h,y=ky)
					j.tkraise()
					self.master.update()
				
			self.Boardcard[i].destroy()
			time.sleep(0.1)
		self.Boardcard=[]
		if self.max == 0 or self.max == 2:
			self.userhandwin+=1
			time.sleep(0.1)
		elif self.max == 1 or self.max == 3:
			self.cpuhandwin+=1
			time.sleep(0.1)
		time.sleep(0.1)
		self.Board=[]
		self.play()
	def roundwincheck(self):
		if self.userhandwin == 5 or self.cpuhandwin == 5:
			time.sleep(0.1)
			self.canvas.destroy()
			self.Board = []
			self.South = [] #User
			self.East = [] #Cpu player1
			self.North = [] #Cpu Team mate with user
			self.West = [] #Cpu player2
			self.Boardcard=[]
			self.win = False
			self.userhandwin = 0
			self.cpuhandwin = 0
			self.Player1 = [] 
			self.Player2 = [] 
			self.Player3 = [] 
			self.Player4 = [] 
			self.prompt=False
			self.pro=False
			self.user=False
			self.ver=150
			self.hor=260
			self.Eastcard=[]
			self.Northcard=[]
			self.Westcard=[]
			self.OMI()
			self.GUI()
			self.play()
			
			
	def OMI(self):
		
		self.played=False
		# divide cards into 4 lists
		if self.round % 4 == 0:
			
			self.DivideCards(self.South,self.East,self.North,self.West)
			self.round += 1
			self.choosefav += 1
		elif self.round % 4 == 1:
			
			self.DivideCards(self.East,self.North,self.West,self.South)
			self.round += 1
			self.choosefav += 1
			
		elif self.round % 4 == 2:
			
			self.DivideCards(self.North,self.West,self.South,self.East)
			self.round += 1
			self.choosefav += 1
			
		elif self.round % 4 == 3:
			
			self.DivideCards(self.West,self.South,self.East,self.North)
			self.round += 1
			self.choosefav += 1
			
		print self.South,self.East,self.North,self.West
		print self.Board
	
	def play(self):
		if(not self.win):
			if self.max == 1:
				self.DealFirst(self.East,self.Board)
				time.sleep(0.5)
				self.Eastcard[random.randint(0, len(self.Eastcard)-1)].destroy()
				self.master.update()
				time.sleep(0.5)
				self.updateBoard()
				time.sleep(0.1)
				print self.Board
				self.DealOther(self.North,self.Board)
				time.sleep(0.5)
				self.Northcard[random.randint(0, len(self.Northcard)-1)].destroy()
				self.master.update()
				time.sleep(0.5)
				self.updateBoard()
				time.sleep(0.1)
				
				
				self.DealOther(self.West,self.Board)
				time.sleep(0.5)
				self.Westcard[random.randint(0, len(self.Westcard)-1)].destroy()
				self.master.update()
				time.sleep(0.5)
				self.updateBoard()
				time.sleep(0.1)
				
				
			elif self.max == 2:
				self.DealFirst(self.North,self.Board)
				time.sleep(0.5)
				self.Northcard[random.randint(0, len(self.Northcard)-1)].destroy()
				self.master.update()
				time.sleep(0.5)
				self.updateBoard()
				time.sleep(0.1)
				
				self.DealOther(self.West,self.Board)
				time.sleep(0.5)
				self.updateBoard()
				self.Westcard[random.randint(0, len(self.Westcard)-1)].destroy()
				self.master.update()
				time.sleep(0.5)
				self.updateBoard()
				time.sleep(0.1)
				
			elif self.max == 3:
				self.DealFirst(self.West,self.Board)
				time.sleep(0.5)				
				self.Westcard[random.randint(0, len(self.Westcard)-1)].destroy()
				self.master.update()
				time.sleep(0.5)
				self.updateBoard()
				time.sleep(0.1)
			else:
				return
	
		
	
	def DealUsermax0(self):
		self.DealOther(self.East,self.Board)
		time.sleep(0.5)
		self.Eastcard[random.randint(0, len(self.Eastcard)-1)].destroy()
		self.master.update()
		time.sleep(0.5)
		self.updateBoard()
		time.sleep(0.1)
		
		self.DealOther(self.North,self.Board)
		time.sleep(0.5)
		self.Northcard[random.randint(0, len(self.Northcard)-1)].destroy()
		self.master.update()
		time.sleep(0.5)
		self.updateBoard()
		time.sleep(0.1)
		
		self.DealOther(self.West,self.Board)
		time.sleep(0.5)
		self.Westcard[random.randint(0, len(self.Westcard)-1)].destroy()
		self.master.update()
		time.sleep(0.5)
		self.updateBoard()
		time.sleep(0.1)
	
	def DealUsermax2(self):
		self.DealOther(self.East,self.Board)
		time.sleep(0.5)
		self.Eastcard[random.randint(0, len(self.Eastcard)-1)].destroy()
		self.master.update()
		time.sleep(0.5)
		self.updateBoard()
		time.sleep(0.1)
		
	def DealUsermax3(self):
		self.DealOther(self.East,self.Board)
		time.sleep(0.5)
		self.Eastcard[random.randint(0, len(self.Eastcard)-1)].destroy()
		self.master.update()
		time.sleep(0.5)
		self.updateBoard()
		time.sleep(0.1)
		
		self.DealOther(self.North,self.Board)
		time.sleep(0.5)
		self.Northcard[random.randint(0, len(self.Northcard)-1)].destroy()
		self.master.update()
		time.sleep(0.5)
		self.updateBoard()
		time.sleep(0.1)
	
	def DealFirst(self,Player,Board):#cpu player dealing first
		self.favmin=0
		for i in range(len(Player)):
			if (Player[i] == 7 or Player[i] == 15 or Player[i] == 23 or Player[i] == 31 ) and Player[i]//8 != self.Fav:
				Board.append(Player[i]) #If you got an Ace, fire Away !!
				Player.pop(Player.index(Player[i]))
				self.played=True
				return
			else:
				self.min=32
				if Player[i] <self.min and Player[i]//8 != self.Fav:
					self.min = Player[i]
				elif Player[i]//8 == self.Fav:
					if Player[i]%8 < 8:
						self.favmin=Player[i]
		if not self.played:
			if self.min==32:
				Board.append(self.favmin)
				Player.pop(Player.index(self.favmin))
			else:
				Board.append(self.min) #If you got nothing pass the hand.
				Player.pop(Player.index(self.min))
		self.updateBoard()	
	def DealOther(self,Player,Board):
		
		suitofcard = Board[0]//8 #store the suit of first dealt card
		card_suit_high = [] #local list to store the cards Player got according to suitofcard
		card_suit_low = [] #local list to store the cards Player got according to suitofcard
		fav_cards = [] #local list to store the Favourite cards 
		other_cards = [] #local list to store the cards Player got not according to suitofcard
		gotfav = False
		gotsuit = False #Boolean variable to record if player got cards in suitofcard
		cut = False #Boolean variable to record if board have been cut with a favourite
		cutmax = 0 #If Cut is true this stores the highest value of cut card
		minother = 15 #lowest card of other cards
		maxboard = 0 #highest card of board
		maxboardindex=0
		""" Instruction for cpu player when dealing 2nd.
		Note:- No cutting needed probably your teammate will come up with something """
		
		for i in range(len(Player)):				
			if Player[i] // 8 == suitofcard:
				if Player[i] > Board[0]:
					card_suit_high.append(Player[i])
					gotsuit = True
				else:
					card_suit_low.append(Player[i])
					gotsuit = True
			elif Player[i] // 8 != self.Fav:
				other_cards.append(Player[i])
			
			elif Player[i] // 8 == self.Fav:
				fav_cards.append(Player[i])
				gotfav = True
				fav_cards.sort()
				
		for i in range(len(Board)):
			if Board[i]//8 == self.Fav:
				cut = True
				cutmax = Board[i]
		
		for i in range(len(other_cards)):
			if other_cards[i] % 8 <= minother%8:
				minother = other_cards[i]
					
		if len(Board)<2:
			if (Player[i] == 7 or Player[i] == 15 or Player[i] == 23 or Player[i] == 31 ) and Player[i]//8 == suitofcard:
				Board.append(Player[i]) #If you got an Ace, fire Away !!
				Player.pop(Player.index(Player[i]))
			if gotsuit:	
				if len(card_suit_high) > 0:
					Board.append(min(card_suit_high))
					Player.pop(Player.index(min(card_suit_high)))
				else:
					Board.append(min(card_suit_low))
					Player.pop(Player.index(min(card_suit_low)))
			else:
				Board.append(minother)
				Player.pop(Player.index(minother))
				
		else:
			for i in range(len(Board)):
				if Board[0]//8 == Board[i]//8 and maxboard < Board[i]%8:
						maxboard = Board[i]%8
						maxboardindex = i
			if gotsuit:	
				if (Player[i] == 7 or Player[i] == 15 or Player[i] == 23 or Player[i] == 31 ) and Player[i]//8 == suitofcard:
					Board.append(Player[i]) #If you got an Ace, fire Away !!
					Player.pop(Player.index(Player[i]))
				
				elif len(card_suit_high) > 0:
					Board.append(min(card_suit_high))
					Player.pop(Player.index(min(card_suit_high)))
				else:
					Board.append(min(card_suit_low))
					Player.pop(Player.index(min(card_suit_low)))
			
			elif cut and gotfav:
				if Board.index(cutmax) == len(Board)-2:
					Board.append(minother)
					Player.pop(Player.index(minother))
					
				elif min(fav_cards) > cutmax:
					Board.append(min(fav_cards))
					Player.pop(Player.index(min(fav_cards)))
					
				elif cutmax > min(fav_cards) and cutmax < max(fav_cards):
					for i in range(len(fav_cards)):
						if fav_cards[i] > cutmax:
							Board.append(fav_cards[i])
							Player.pop(Player.index(fav_cards[i]))
							break
			elif not gotfav:
				Board.append(minother)
				Player.pop(Player.index(minother))
			
			elif not cut and gotfav:
				if Board[maxboardindex] == len(Board)-2 and len(other_cards) >0:
					Board.append(minother)
					Player.pop(Player.index(minother))
					
				else:
					Board.append(min(fav_cards))
					Player.pop(Player.index(min(fav_cards)))

# Main function, run when invoked as a stand-alone Python program.

def main():
    root = Tk()
    root.geometry("800x700+200+100")
    game = mainscreen(root)
    root.protocol('WM_DELETE_WINDOW', root.quit)
    root.mainloop()
if __name__ == '__main__':
    main()
