from random import randint
from functools import wraps
import csv
import collections

def log(f,*args,**kwargs):
	@wraps(f)
	def wrap_func(*args,**kwargs):
		print("{}{}{}".format(f,args, kwargs))
		return f(*args,**kwargs)
	return wrap_func

class Deck():

	def __init__(self):
		self.cards = [Card(val, suit) for suit in ["Hearts"] for val in ["A",2,3,4,"Q","K"]]
		# self.cards = [Card(val, suit) for suit in ["Hearts","Diamonds","Clubs","Spades"] for val in ["A",2,3,4,5,6,7,8,9,10,"J","Q","K"]]
		self.shoe = self.cards[:]
		self.discarded = []
		self.dealt = []
		self.iter_idx = 0

	def __str__(self):
		deck_string = ""
		for card in d.cards:
			deck_string += "{}\n".format(card)
		return deck_string

	def shuffle(self):
		new_deck = []
		while len(self.shoe) > 0:
			random_card_idx = randint(0,len(self.shoe)-1)
			new_deck.append(self.shoe.pop(random_card_idx))
		self.shoe = new_deck

	def save_deck(self):
		self.pack('shoe.csv',self.shoe)
		self.pack('dealt.csv',self.dealt)
		self.pack('discarded.csv',self.discarded)

	def load_deck(self):
		self.shoe = self.unpack('shoe.csv',self.shoe)
		self.dealt = self.unpack('dealt.csv',self.dealt)
		# self.unpack('discarded.csv',self.discarded)

	def pack(self,file_name,arr):
		with open(file_name, 'w') as csvfile:
			data_writer = csv.writer(csvfile, delimiter="|")
			for c in arr:
				data_writer.writerow([c.val, c.suit])
			csvfile.close()

	def unpack(self,file_name,arr):
		local_arr = []
		with open(file_name) as csvfile:
			reader = csv.reader(csvfile, delimiter='|')
			rows = list(reader)
			for row in rows:
				local_arr.append(row)
		arr = []
		# print("arr")
		# print(arr)
		# print("self.shoe before")
		# print(self.shoe)
		for c in local_arr:
			for cr in self.cards:
				if self.same(c[0],cr.val,c[1],cr.suit):
					arr.append(cr)
		# print("self.shoe after")
		# print(self.shoe)
		return arr

	def same(self,v1,v2,s1,s2):  # (value1,value2,suit1,suit2)
		return str(v1) == str(v2) and str(s1) == str(s2)

	# @log
	def deal_one(self):
		card = self.shoe.pop()
		self.dealt.append(card)
		return card

	# @log
	def deal(self, how_many):
		counter = 0
		card_arr = []
		for i in range(0,how_many):
			card_arr.append(self.shoe.pop())
			self.dealt.append(card_arr[i])
		return card_arr

	def __iter__(self):
		return self

	def __next__(self):
		pass
		if self.iter_idx > len(self.cards)-1:
			raise StopIteration
			self.iter_idx = 0
		else:
			self.iter_idx += 1
			return self.cards[self.iter_idx-1]

	def __repr__(self):
		return "Cards: {}\nShoe: {}\nDealt: {}\nDiscarded: {}".format(self.cards, self.shoe, self.dealt, self.discarded)



class Card:

	def __init__(self, value, suit):
		self.val = value
		self.suit = suit
		self.location = None;

	def __str__(self):
		return "{c} of {s}".format(c=self.val,s=self.suit)

	def __repr__(self):
		return "{c} of {s}".format(c=self.val,s=self.suit)


class Player:
	def __init__(self,name):
		self.name = name
		self.hand = []



# print(d.dealt)
# print(d.deal(5))
# d.deal_one()
