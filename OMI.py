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
		
	def DivideCards(self,Player1,Player2,Player3,Player4):
		
		Card=Cards() #call Cards class
		
		Card.DivideRound1(Player1,Player2,Player3,Player4)
		
		if self.chooseFav % 4 == 0: #Prompting for Fav from the user
			self.w=popupFav(self.master)
			self.master.wait_window(self.w.top)
			Fav=self.w.value
		else:
			Fav=card.Favourite(self.chooseFav)
			Card.DivideRound2(Player1,Player2,Player3,Player4)
			
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
		self.top=Toplevel(master)
		l=Label(self.top,text=u"තුරුම්පු තෝරන්න")
		l.pack()
		value=self.value=0
		Photospade=PhotoImage(file = "image/spade.gif")
		Photoclub=PhotoImage(file = "image/club.gif")
		Photodiamond=PhotoImage(file = "image/diamond.gif")
		Photoheart=PhotoImage(file = "image/heart.gif")
		b0=Button(self.top,image=Photospade,command=self.spade, relief="ridge",height="50px",width="50px")
		b0.pack(side=LEFT)
		b1=Button(self.top,image=Photoclub,command=self.club, relief="ridge",height="50px",width="50px")
		b1.pack(side=LEFT)
		b2=Button(self.top,image=Photodiamond,command=self.diamond,relief="ridge",height="50px",width="50px")
		b2.pack(side=LEFT)
		b3=Button(self.top,image=Photoheart,command=self.heart, relief="ridge",height="50px",width="50px")
		b3.pack(side=LEFT)
		master.mainloop()
        
		
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
		self.master=master
		for i in range(32):
			self.imageList.append(PhotoImage(file = "image/"+ str(i) + ".gif"))
		
		self.South = [] #User
		self.East = [] #Cpu player1
		self.North = [] #Cpu Team mate with user
		self.West = [] #Cpu player2
		
		self.player1=0
		self.player2=0
		self.player3=0
		self.player4=0
		
		self.max = 0 #Record the player who played the highest card, South=0 East =1 North =2 West =3
		self.Fav = 0 #Saves The Favourite suit for the Round
		self.choosefav = 0 #Record the player who have to choose favourite suit South=0 East =1 North =2 West =3 
		self.round = 0 #ongoing round
		
		self.OMI()
		##GUI
		self.canvas = Canvas(self.master,
                             background='#070')
		self.canvas.pack(fill=BOTH, expand=TRUE)
		usercard1 = Label(self.canvas, image=self.imageList[self.South[0]], cursor="left_ptr")
		usercard1.place(x=-40, y=-30)
		usercard1.bind("<1>", self.ClickHandler1)
		
		usercard2 = Label(self.canvas, image=self.imageList[self.South[1]], cursor="left_ptr")
		usercard2.place(x=-40, y=-10)
		usercard2.bind("<1>", self.ClickHandler2)
		
		usercard3 = Label(self.canvas, image=self.imageList[self.South[2]], cursor="left_ptr")
		usercard3.place(x=-40, y=-10)
		usercard3.bind("<1>", self.ClickHandler3)
		
		usercard4 = Label(self.canvas, image=self.imageList[self.South[3]], cursor="left_ptr")
		usercard4.place(x=-40, y=30)
		usercard4.bind("<1>", self.ClickHandler4)
		
		usercard5 = Label(self.canvas, image=self.imageList[self.South[4]], cursor="left_ptr")
		usercard5.place(x=-40, y=50)
		usercard5.bind("<1>", self.ClickHandler5)
		
		usercard6 = Label(self.canvas, image=self.imageList[self.South[5]], cursor="left_ptr")
		usercard6.place(x=-40, y=70)
		usercard6.bind("<1>", self.ClickHandler6)
		
		usercard7 = Label(self.canvas, image=self.imageList[self.South[6]], cursor="left_ptr")
		usercard7.place(x=-40, y=90)
		usercard7.bind("<1>", self.ClickHandler7)
		
		usercard8 = Label(self.canvas, image=self.imageList[self.South[7]], cursor="left_ptr")
		usercard9.place(x=-40, y=110)
		usercard8.bind("<1>", self.ClickHandler8)
		self.master.mainloop()
	def OMI(self):
		Board = []
		
		# divide cards into 4 lists
		if self.round % 4 == 0:
			Rotate=RotatePlayer(self.South,self.East,self.North,self.West,max,self.round,self.Fav,self.master)
			Rotate.DivideCards(self.South,self.East,self.North,self.West)
			self.round += 1
			self.choosefav += 1
		elif self.round % 4 == 1:
			Rotate=RotatePlayer(self.East,self.North,self.West,self.South,max,self.round,self.Fav,self.master)
			Rotate.DivideCards(self.East,self.North,self.West,self.South)
			self.round += 1
			self.choosefav += 1
			Fav=Favourite(self.East)
		elif self.round % 4 == 2:
			Rotate=RotatePlayer(self.North,self.West,self.South,self.East,max,self.round,self.Fav,self.master)
			Rotate.DivideCards(self.North,self.West,self.South,self.East)
			self.round += 1
			self.choosefav += 1
			Fav=Favourite(self.North)
		elif self.round % 4 == 3:
			Rotate=RotatePlayer(self.West,self.South,self.East,self.North,max,self.round,self.Fav,self.master)
			Rotate.DivideCards(self.West,self.South,self.East,self.North)
			self.round += 1
			self.choosefav += 1
			Fav=Favourite(self.West)
		print self.South,self.East,self.North,self.West
		print Board
		
		self.South.sort() #sort the card set 
		win = False
		while(win):
			if max == 0:
				DealUser(self)
				DealOther(self.East,Board)
				DealOther(self.North,Board)
				DealOther(self.West,Board)
			elif max == 1:
				DealFirst(self.East,Board)
				DealOther(self.North,Board)
				DealOther(self.West,Board)
				DealUser(self)
			elif max == 2:
				DealFirst(self.North,Board)
				DealOther(self.West,Board)
				DealUser(self)
				DealOther(self.East,Board)
			elif max == 3:
				DealFirst(self.West,Board)
				DealUser(self)
				DealOther(self.East,Board)
				DealOther(self.North,Board)
			
	
		
	
	def DealUser(self):
		pass
	
	def DealFirst(self,Player,Board):#cpu player dealing first
		for i in range(8):
			if (Player[i] == 7 or Player[i] == 15 or Player[i] == 23 or Player[i] == 31 ) and Player[i]//8 != self.Fav:
				Board.append(Player[i]) #If you got an Ace, fire Away !!
				Player.pop(Player.index(Player[i]))
				played=True
				break
			else:
				min=32
				if Player[i] <min and Player[i]//8 != self.Fav:
					min = Player[i]
		if not played:
			Board.append(min) #If you got nothing pass the hand.
			Player.pop(Player.index(min))
			
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
		minother = 8 #lowest card of other cards
		maxboard = 0 #highest card of board
		
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
				if other_cards[i] % 8 < minother:
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
					Player.pop(Player.index(min(fav_card)))
					
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
				if Board.index(maxboard) == len(Board)-2 and len(other_cards) >0:
					Board.append(minother)
					Player.pop(Player.index(minother))
					
				else:
					Board.append(min(fav_cards))
					Player.pop(Player.index(min(fav_cards)))

# Main function, run when invoked as a stand-alone Python program.

def main():
    root = Tk()
    game = mainscreen(root)
    root.protocol('WM_DELETE_WINDOW', root.quit)
    root.mainloop()

if __name__ == '__main__':
    main()
