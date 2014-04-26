#!/usr/bin/env python
# -*- coding: utf-8 -*-
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
import tkMessageBox


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
		self.master.title("OMI-The Game")
		menubar = Menu(self.master) #Create a Menu
		self.master.config( menu = menubar)
			
		filemenu = Menu( menubar, tearoff = 0) #File dropdown
		menubar.add_cascade( label = u"ගොනුව", menu = filemenu)
		filemenu.add_command( label = u"ඉවත් වන්න", command = self.master.quit) #child item Quit
			
		helpmenu = Menu( menubar, tearoff = 0) #Help dropdown
		menubar.add_cascade( label = u"උදව්", menu = helpmenu)
		helpmenu.add_command( label = u"About") #child item About
		
		self.userkata=0
		self.cpukata=0
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
		self.sepo=False
		self.player1=0
		self.player2=0
		self.player3=0
		self.player4=0
		self.baldu=False
		self.ver=150
		self.hor=260
		
		self.prompt=False
		self.pro=False
		
		
		self.Fav = 0 #Saves The Favourite suit for the Round
		self.choosefav = 0 #Record the player who have to choose favourite suit South=0 East =1 North =2 West =3 
		self.round = 0 #ongoing round
		self.max = self.round%4 #Record the player who played the highest card, South=0 East =1 North =2 West =3
		self.user=False
		
		self.Eastcard=[]
		self.Northcard=[]
		self.Westcard=[]
		
		self.tempy=[]
		
		self.OMI()
		self.GUI()
		self.play()
		
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
		
		self.Photochoosefav=PhotoImage(file = "image/choosefav.gif")
		
		self.Photoscore=PhotoImage(file = "image/score.gif")
		self.scorelabel=Label(self.canvas, image=self.Photoscore, borderwidth=0)
		self.scorelabel.place(x=75,y=550)
		
		self.scorehandwin=Label(self.canvas, text=str(self.userhandwin), borderwidth=0,bg="#070")
		self.scorehandwin["font"]="Ubuntu 15 bold"
		self.scorehandlose=Label(self.canvas, text=str(self.cpuhandwin), borderwidth=0,bg="#070")
		self.scorehandlose["font"]="Ubuntu 15 bold"
		self.scorehandwin.place(x=300,y=650)
		self.scorehandwin.tkraise()
		self.scorehandlose.place(x=450,y=650)
		self.scorehandlose.tkraise()
		
		self.scoreuserkata=Label(self.canvas, text=str(self.userkata), borderwidth=0,bg="#070")
		self.scoreuserkata["font"]="Ubuntu 15 bold"
		self.scorecpukata=Label(self.canvas, text=str(self.cpukata), borderwidth=0,bg="#070")
		self.scorecpukata["font"]="Ubuntu 15 bold"
		self.scoreuserkata.place(x=540,y=650)
		self.scoreuserkata.tkraise()
		self.scorecpukata.place(x=650,y=650)
		self.scorecpukata.tkraise()
		
		self.l = Label(self.canvas, image=self.Photochoosefav,borderwidth=0)
		self.Photospade=PhotoImage(file = "image/spade.gif")
		self.Photoclub=PhotoImage(file = "image/club.gif")
		self.Photodiamond=PhotoImage(file = "image/diamond.gif")
		self.Photoheart=PhotoImage(file = "image/heart.gif")
		self.b0=Label(self.canvas,image=self.Photospade, relief="ridge")
		self.b0.bind("<1>",self.spade)
		
		self.b1=Label(self.canvas,image=self.Photoclub, relief="ridge")
		self.b1.bind("<1>",self.club)
		
		self.b2=Label(self.canvas,image=self.Photodiamond,relief="ridge")
		self.b2.bind("<1>",self.diamond)
		
		self.b3=Label(self.canvas,image=self.Photoheart, relief="ridge")
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
			self.l.place(x=270,y=300)
			self.b0.place(x=250,y=350)
			self.b1.place(x=320,y=350)
			self.b2.place(x=390,y=350)
			self.b3.place(x=460,y=350)
			self.master.update_idletasks()
		
		if self.pro:
			self.usercard1.destroy()
			self.usercard2.destroy()
			self.usercard3.destroy()
			self.usercard4.destroy()
			self.South.sort()
			for i in range(len(self.South)):
				self.tempy.append(self.South[i]*8)
			
			self.DrawCards()
			self.Favlabel=Label(self.canvas,height="50",width="50")
			self.Favlabel.place(x=195, y=620)
			self.Favlabel.tkraise()
			if self.Fav == 0:
				self.Favlabel["image"]=self.Photospade
			elif self.Fav == 1:
				self.Favlabel["image"]=self.Photoclub
			elif self.Fav == 2:
				self.Favlabel["image"]=self.Photodiamond
			elif self.Fav == 3:
				self.Favlabel["image"]=self.Photoheart
			self.pro= False
				
	def DivideCards(self,Player1,Player2,Player3,Player4):
		
		Card=Cards() #call Cards class
		
		Card.DivideRound1(Player1,Player2,Player3,Player4)
		
		if self.round % 4 == 0: #Prompting for Fav from the user
			self.prompt=True
		else:
			self.pro=True
			if self.round %4 == 1:
				plyr = self.East
			elif self.round %4==2:
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
		for i in range(len(self.South)):
			self.tempy.append(self.South[i]*8)
			
		self.DrawCards()
		self.Favlabel=Label(self.canvas)
		self.Favlabel.place(x=195, y=620)
		self.Favlabel.tkraise()
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
		for i in range(len(self.South)):
			self.tempy.append(self.South[i]*8)
		
		self.DrawCards()
		self.Favlabel=Label(self.canvas,height="50",width="50")
		self.Favlabel.place(x=195, y=620)
		self.Favlabel.tkraise()
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
		for i in range(len(self.South)):
			self.tempy.append(self.South[i]*8)
		
		self.DrawCards()
		self.Favlabel=Label(self.canvas,height="50",width="50")
		self.Favlabel.place(x=195, y=620)
		self.Favlabel.tkraise()
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
		for i in range(len(self.South)):
			self.tempy.append(self.South[i]*8)
		
		self.DrawCards()
		self.Favlabel=Label(self.canvas,height="50",width="50")
		self.Favlabel.place(x=195, y=620)
		self.Favlabel.tkraise()
		self.Favlabel["image"]=self.Photoheart
	
	def DEAL(self):
		if self.max == 0:
			self.DealUsermax0()
			self.handwincheck()
		elif self.max == 1:
			self.handwincheck()
		elif self.max == 2:
			self.DealUsermax2()
			self.handwincheck()
		elif self.max == 3:
			self.DealUsermax3()
			self.handwincheck()
		self.master.update_idletasks()	
		self.updateBoard()
		
	def ClickHandler1(self,event):
		self.Board.append(self.South[0])
		self.tempy.pop(self.tempy.index(self.South[0]*8))
		self.usercard1.destroy()
		self.master.update()
		self.updateBoard()
		self.Baldu()
		if not self.baldu:
			self.DEAL()
		else:
			tkMessageBox.showinfo(" ", u"අත බාල්දුයි!!,කැට 2ක් පරාදයි!!")
			self.cpukata+=2
			self.Boardcard=[]
			self.Board=[]
			self.Newround()
		
	def ClickHandler2(self,event):
		self.Board.append(self.South[1])
		self.tempy.pop(self.tempy.index(self.South[1]*8))
		self.usercard2.destroy()
		self.master.update()
		self.updateBoard()
		self.Baldu()
		if not self.baldu:
			self.DEAL()
		else:
			tkMessageBox.showinfo(" ", u"අත බාල්දුයි!!,කැට 2ක් පරාදයි!!")
			self.cpukata+=2
			self.Boardcard=[]
			self.Board=[]
			self.Newround()
		
	
	def ClickHandler3(self,event):
		self.Board.append(self.South[2])
		self.tempy.pop(self.tempy.index(self.South[2]*8))
		self.usercard3.destroy()
		self.master.update()
		self.updateBoard()
		self.Baldu()
		if not self.baldu:
			self.DEAL()
		else:
			tkMessageBox.showinfo(" ", u"අත බාල්දුයි!!,කැට 2ක් පරාදයි!!")
			self.cpukata+=2
			self.Boardcard=[]
			self.Board=[]
			self.Newround()
	
	def ClickHandler4(self,event):
		self.Board.append(self.South[3])
		self.tempy.pop(self.tempy.index(self.South[3]*8))
		self.usercard4.destroy()
		self.master.update()
		self.updateBoard()
		self.Baldu()
		if not self.baldu:
			self.DEAL()
		else:
			tkMessageBox.showinfo(" ", u"අත බාල්දුයි!!,කැට 2ක් පරාදයි!!")
			self.cpukata+=2
			self.Boardcard=[]
			self.Board=[]
			self.Newround()
	
	def ClickHandler5(self,event):
		self.Board.append(self.South[4])
		self.tempy.pop(self.tempy.index(self.South[4]*8))
		self.usercard5.destroy()
		self.master.update()
		self.updateBoard()
		self.Baldu()
		if not self.baldu:
			self.DEAL()
		else:
			tkMessageBox.showinfo(" ", u"අත බාල්දුයි!!,කැට 2ක් පරාදයි!!")
			self.cpukata+=2
			self.Boardcard=[]
			self.Board=[]
			self.Newround()
	
	def ClickHandler6(self,event):
		self.Board.append(self.South[5])
		self.tempy.pop(self.tempy.index(self.South[5]*8))
		self.usercard6.destroy()
		self.master.update()
		self.updateBoard()
		self.Baldu()
		if not self.baldu:
			self.DEAL()
		else:
			tkMessageBox.showinfo(" ", u"අත බාල්දුයි!!,කැට 2ක් පරාදයි!!")
			self.cpukata+=2
			self.Boardcard=[]
			self.Board=[]
			self.Newround()
		
	def ClickHandler7(self,event):
		self.Board.append(self.South[6])
		self.tempy.pop(self.tempy.index(self.South[6]*8))
		self.usercard7.destroy()
		self.master.update()
		self.updateBoard()
		self.Baldu()
		if not self.baldu:
			self.DEAL()
		else:
			tkMessageBox.showinfo(" ", u"අත බාල්දුයි!!,කැට 2ක් පරාදයි!!")
			self.cpukata+=2
			self.Boardcard=[]
			self.Board=[]
			self.Newround()
		
	def ClickHandler8(self,event):
		self.Board.append(self.South[7])
		self.tempy.pop(self.tempy.index(self.South[7]*8))
		self.usercard8.destroy()
		self.master.update()
		self.updateBoard()
		self.Baldu()
		if not self.baldu:
			self.DEAL()
		else:
			tkMessageBox.showinfo(" ", u"අත බාල්දුයි!!,කැට 2ක් පරාදයි!!")
			self.cpukata+=2
			self.Boardcard=[]
			self.Board=[]
			self.Newround()
	
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
		temp=[]
		for i in range(0,len(self.Board)):
			if self.Board[i]//8 == self.Fav:
				temp.append((self.Board[i]+2)**7)
			elif self.Board[i]//8 == self.Board[0]//8 and not self.Board[i]//8 == self.Fav:
				temp.append(self.Board[i]%8)
			else:
				temp.append(0)
		self.prevmax=self.max
		if temp.index(max(temp)) == 0:
			self.max=self.prevmax
		elif temp.index(max(temp)) == 1:
			self.max=(self.prevmax+1)%4
		elif temp.index(max(temp)) == 2:
			self.max=(self.prevmax+2)%4
		elif temp.index(max(temp)) == 3:
			self.max=(self.prevmax+3)%4
		temp=[]
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
				desty=0
			elif self.max == 3:
				destx=0
				desty=250
			kv=eval(k["y"])+10
			kh=eval(k["x"])+10
			first=0
			dest=0
			if self.max == 0 :
				first=eval(k["y"])
				dest=desty
			elif self.max == 2:
				first=desty
				dest=eval(k["y"])
			elif self.max == 1:
				first=eval(k["x"])
				dest=destx
			elif self.max == 3:
				first=destx
				dest=eval(k["x"])
				
			for h in range(first,dest,10):
				time.sleep(0.0001)
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
			j.place_forget()	
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
		self.scorehandwin["text"]=str(self.userhandwin)
		self.scorehandlose["text"]=str(self.cpuhandwin)
		self.master.update()
		self.Board=[]
		
		if (self.userhandwin <= 4 and self.cpuhandwin <4) or (self.userhandwin > 4 and self.cpuhandwin ==0) or (self.userhandwin ==0 and self.cpuhandwin >4)or (self.userhandwin < 4 and self.cpuhandwin <=4) :
			self.play()
		else:
			self.roundwincheck()
	
	def roundwincheck(self):
		if self.userhandwin == 5 and self.cpuhandwin >0:
		
			time.sleep(0.5)
			time.sleep(0.5)
			if self.round %4 ==0 or self.round %4 ==2:
				if self.sepo:
					self.userkata+=2
					tkMessageBox.showinfo(" ", u"කලින් අත සෙපෝරුයි!!,\n කැට 2යි")
				else:
					self.userkata+=1
					tkMessageBox.showinfo(" ", u"තුරුම්පු කියලා දිනුම්!!,\n කැට 1යි")
				self.sepo=False
			elif self.round %4 ==1 or self.round %4 ==3:
				if self.sepo:
					self.usrekata+=2
					tkMessageBox.showinfo(" ", u"කලින් අත සෙපෝරුයි!!,\n කැට 2යි")
				else:
					self.userkata+=2
					tkMessageBox.showinfo(" ", u"තුරුම්පු කියලා පරාදයි!!,\n කැට 2යි")
				self.sepo=False
			self.Newround()
			
		elif self.userhandwin > 0 and self.cpuhandwin ==5:
			time.sleep(0.5)
			time.sleep(0.5)
			if self.round %4 ==1 or self.round %4 ==3:
				if self.sepo:
					self.cpukata+=2
					tkMessageBox.showinfo(" ", u"කලින් අත සෙපෝරුයි!!,\n කැට 2ක් පරාදයි")
					self.sepo=False
				else:
					self.cpukata+=1
					tkMessageBox.showinfo(" ", u"පරාදයි!!,\n කැටයක් පරාදයි")
			elif self.round %4 ==0 or self.round %4 ==2:
				if self.sepo:
					self.cpukata+=2
					tkMessageBox.showinfo(" ", u"කලින් අත සෙපෝරුයි!!,\n කැට 2ක් පරාදයි")
					self.sepo=False
				else:
					self.cpukata+=2
					tkMessageBox.showinfo(" ", u"පරාදයි!!,\n කැට 2ක් පරාදයි")
			self.Newround()
			
		elif self.userhandwin == 8:
			time.sleep(0.5)
			time.sleep(0.5)
			if self.round %4 ==0 or self.round %4 ==2:
				self.userkata+=2
				tkMessageBox.showinfo(" ", u"කපෝතියි!!,\n කැට 2යි")
			elif self.round %4 ==1 or self.round %4 ==3:
				self.userkata+=2
				tkMessageBox.showinfo(" ", u"කපෝතියි!!,\n කැට 3යි")
			self.Newround()
			
		elif self.cpuhandwin == 8:
			time.sleep(0.5)
			time.sleep(0.5)
			if self.round %4 ==1 or self.round %4 ==3:
				self.cpukata+=2
				tkMessageBox.showinfo(" ", u"කපෝතියි!!,\n කැට 2ක් පරාදයි")
			elif self.round %4 ==0 or self.round %4 ==2:
				self.cpukata+=2
				tkMessageBox.showinfo(" ",u"කපෝතියි!!,\n කැට 3ක් පරාදයි")
			self.Newround()
			
		elif self.userhandwin == 4 and self.cpuhandwin ==4:
			time.sleep(0.5)
			time.sleep(0.5)
			self.sepo=True
			tkMessageBox.showinfo(" ", u"අත සෙපෝරුයි!!")
			self.Newround()
	def Baldu(self):
		soc=self.Board[0]//8
		pcs=self.Board[len(self.Board)-1]//8
		if soc != pcs:
			for i in range(len(self.tempy)):
				if self.tempy[i]//64 == soc:
					self.baldu=True
					return
					
	def Newround(self):
		if self.userkata >=10:
			tkMessageBox.showinfo(" ", u"සුභ පැතුම්!!\n ඔබ තරගය ජය ගත්තා!!!")
			self.userkata=0
			self.cpukata=0
		elif self.cpukata >=10:
			tkMessageBox.showinfo(" ", u"ඔබ තරගය පරාජය වුනා!!")
			self.userkata=0
			self.cpukata=0
			 
		self.round+=1
		self.max=self.round % 4
		self.canvas.destroy()
		self.Board = []
		self.South = [] #User
		self.East = [] #Cpu player1
		self.North = [] #Cpu Team mate with user
		self.West = [] #Cpu player2
		self.Boardcard=[]
		self.userhandwin = 0
		self.cpuhandwin = 0
		self.Player1 = [] 
		self.Player2 = [] 
		self.Player3 = [] 
		self.Player4 = [] 
		self.baldu=False
		
		self.prompt=False
		self.pro=False
		self.user=False
		self.ver=150
		self.hor=260
		self.Eastcard=[]
		self.Northcard=[]
		self.Westcard=[]
		self.tempy=[]
		self.OMI()
		self.GUI()
		self.play()
			
			
	def OMI(self):
		
		self.played=False
		# divide cards into 4 lists
		if self.round % 4 == 0:
			
			self.DivideCards(self.South,self.East,self.North,self.West)
			
		elif self.round % 4 == 1:
			
			self.DivideCards(self.East,self.North,self.West,self.South)
			
		elif self.round % 4 == 2:
			
			self.DivideCards(self.North,self.West,self.South,self.East)
			
		elif self.round % 4 == 3:
			
			self.DivideCards(self.West,self.South,self.East,self.North)
		
	def play(self):
		if(not self.win):
			if self.max == 1 :
				self.DealFirst(self.East,self.Board)
				time.sleep(0.5)
				lst=random.randint(0, len(self.Eastcard)-1)
				self.Eastcard[lst].destroy()
				self.Eastcard.pop(lst)
				self.master.update()
				time.sleep(0.5)
				self.updateBoard()
				time.sleep(0.1)
				
				self.DealOther(self.North,self.Board)
				time.sleep(0.5)
				lst=random.randint(0, len(self.Northcard)-1)
				self.Northcard[lst].destroy()
				self.Northcard.pop(lst)
				self.master.update()
				time.sleep(0.5)
				self.updateBoard()
				time.sleep(0.1)
				
				self.DealOther(self.West,self.Board)
				time.sleep(0.5)
				lst=random.randint(0, len(self.Westcard)-1)
				self.Westcard[lst].destroy()
				self.Westcard.pop(lst)
				self.master.update()
				time.sleep(0.5)
				self.updateBoard()
				time.sleep(0.1)
				return
				
			elif self.max == 2:
				self.DealFirst(self.North,self.Board)
				time.sleep(0.5)
				lst=random.randint(0, len(self.Northcard)-1)
				self.Northcard[lst].destroy()
				self.Northcard.pop(lst)
				self.master.update()
				time.sleep(0.5)
				self.updateBoard()
				time.sleep(0.1)
				
				self.DealOther(self.West,self.Board)
				time.sleep(0.5)
				lst=random.randint(0, len(self.Westcard)-1)
				self.Westcard[lst].destroy()
				self.Westcard.pop(lst)				
				self.master.update()
				time.sleep(0.5)
				self.updateBoard()
				time.sleep(0.1)
				return
			elif self.max == 3:
				self.DealFirst(self.West,self.Board)
				time.sleep(0.5)				
				lst=random.randint(0,len(self.Westcard)-1)
				self.Westcard[lst].destroy()
				self.Westcard.pop(lst)
				self.master.update()
				time.sleep(0.5)
				self.updateBoard()
				time.sleep(0.1)
				return
			else:
				return
	
		
	
	def DealUsermax0(self):
		self.DealOther(self.East,self.Board)
		time.sleep(0.5)
		lst=random.randint(0,len(self.Eastcard)-1)
		self.Eastcard[lst].destroy()
		self.Eastcard.pop(lst)
		self.master.update()
		time.sleep(0.5)
		self.updateBoard()
		time.sleep(0.1)
		
		self.DealOther(self.North,self.Board)
		time.sleep(0.5)
		lst=random.randint(0,len(self.Northcard)-1)
		self.Northcard[lst].destroy()
		self.Northcard.pop(lst)
		self.master.update()
		time.sleep(0.5)
		self.updateBoard()
		time.sleep(0.1)
		
		self.DealOther(self.West,self.Board)
		time.sleep(0.5)
		lst=random.randint(0,len(self.Westcard)-1)
		self.Westcard[lst].destroy()
		self.Westcard.pop(lst)
		self.master.update()
		time.sleep(0.5)
		self.updateBoard()
		time.sleep(0.1)
		return
		
	def DealUsermax2(self):
		self.DealOther(self.East,self.Board)
		time.sleep(0.5)
		lst=random.randint(0,len(self.Eastcard)-1)
		self.Eastcard[lst].destroy()
		self.Eastcard.pop(lst)
		self.master.update()
		time.sleep(0.5)
		self.updateBoard()
		time.sleep(0.1)
		return
		
	def DealUsermax3(self):
		self.DealOther(self.East,self.Board)
		time.sleep(0.5)
		lst=random.randint(0,len(self.Eastcard)-1)
		self.Eastcard[lst].destroy()
		self.Eastcard.pop(lst)
		self.master.update()
		time.sleep(0.5)
		self.updateBoard()
		time.sleep(0.1)
		
		self.DealOther(self.North,self.Board)
		time.sleep(0.5)
		lst=random.randint(0,len(self.Northcard)-1)
		self.Northcard[lst].destroy()
		self.Northcard.pop(lst)
		self.master.update()
		time.sleep(0.5)
		self.updateBoard()
		time.sleep(0.1)
		return
		
	def DealFirst(self,Player,Board):#cpu player dealing first
		favmin=55
		mini=55
		self.played=False
		if len(Player)==1:
			Board.append(Player[0]) #If you got an Ace, fire Away !!
			Player.pop(Player.index(Player[0]))
			return
		for i in range(len(Player)):
			if (Player[i] == 7 or Player[i] == 15 or Player[i] == 23 or Player[i] == 31 ) and Player[i]//8 != self.Fav:
				Board.append(Player[i]) #If you got an Ace, fire Away !!
				Player.pop(Player.index(Player[i]))
				self.played=True
				return
		
		if not self.played:
			for i in range(len(Player)):
				if Player[i]//8 != self.Fav:
					if Player[i]%8 <= mini%8:
						mini = Player[i]
				elif Player[i]//8 == self.Fav:
					if Player[i]%8 <= favmin%8:
						favmin=Player[i]
		if not self.played:
			if mini == 55:
				Board.append(favmin)
				Player.pop(Player.index(favmin))
			else:
				Board.append(mini) #If you got nothing pass the hand.
				Player.pop(Player.index(mini))
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
		pp=False
		""" Instruction for cpu player when dealing 2nd.
		Note:- No cutting needed probably your teammate will come up with something """
		if len(Player)==1:
			Board.append(Player[0]) #If you got an Ace, fire Away !!
			Player.pop(Player.index(Player[0]))
			return
			
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
			for i in range(len(Player)):
				if (Player[i] == 7 or Player[i] == 15 or Player[i] == 23 or Player[i] == 31 ) and Player[i]//8 == suitofcard:
					Board.append(Player[i]) #If you got an Ace, fire Away !!
					Player.pop(Player.index(Player[i]))
					return
			if gotsuit:	
				if len(card_suit_high) > 0:
					Board.append(min(card_suit_high))
					Player.pop(Player.index(min(card_suit_high)))
					return
				else:
					Board.append(min(card_suit_low))
					Player.pop(Player.index(min(card_suit_low)))
					return
			elif minother!=15:
				Board.append(minother)
				Player.pop(Player.index(minother))
				return
			else:
				Board.append(min(fav_cards))
				Player.pop(Player.index(min(fav_cards)))
				return
		else:
			if gotsuit:
				for i in range(len(Player)):
					if (Player[i] == 7 or Player[i] == 15 or Player[i] == 23 or Player[i] == 31 ) and Player[i]//8 == suitofcard:
						Board.append(Player[i]) #If you got an Ace, fire Away !!
						Player.pop(Player.index(Player[i]))
						pp=True
						return
				if not pp:
					if len(card_suit_high) > 0:
						Board.append(min(card_suit_high))
						Player.pop(Player.index(min(card_suit_high)))
						return
					else:
						Board.append(min(card_suit_low))
						Player.pop(Player.index(min(card_suit_low)))
						return
			
			elif cut and gotfav:
				if Board.index(cutmax) == len(Board)-2 and minother!=15:
					Board.append(minother)
					Player.pop(Player.index(minother))
					return
					
				elif min(fav_cards) > cutmax:
					Board.append(min(fav_cards))
					Player.pop(Player.index(min(fav_cards)))
					return
					
				elif cutmax > min(fav_cards) and cutmax < max(fav_cards):
					for i in range(len(fav_cards)):
						if fav_cards[i] > cutmax:
							Board.append(fav_cards[i])
							Player.pop(Player.index(fav_cards[i]))
							return
			elif not gotfav:
				Board.append(minother)
				Player.pop(Player.index(minother))
				return
				
			elif not cut and gotfav:
				for i in range(len(Board)):
					if Board[0]//8 == Board[i]//8 and maxboard < Board[i]%8 and not cut:
						maxboard = Board[i]%8
						maxboardindex = i
				if Board[maxboardindex] == len(Board)-2 and len(other_cards) >0:
					Board.append(minother)
					Player.pop(Player.index(minother))
					return
					
				else:
					Board.append(min(fav_cards))
					Player.pop(Player.index(min(fav_cards)))
					return

# Main function, run when invoked as a stand-alone Python program.

def main():
    root = Tk()
    root.geometry("800x700+200+100")
    game = mainscreen(root)
    root.protocol('WM_DELETE_WINDOW', root.quit)
    root.mainloop()
if __name__ == '__main__':
    main()
