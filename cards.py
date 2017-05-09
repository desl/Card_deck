from random import randint
from functools import wraps

def log(f,*args,**kwargs):
	@wraps(f)
	def wrap_func(*args,**kwargs):
		print("{}{}{}".format(f,args, kwargs))
		return f(*args,**kwargs)
	return wrap_func

class Deck():

	def __init__(self):
		self.cards = [Card(val, suit) for suit in ["Hearts","Diamonds","Clubs","Spades"] for val in ["A",2,3,4,5,6,7,8,9,10,"J","Q","K"]]
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

	@log
	def deal_one(self):
		card = self.shoe.pop()
		self.dealt.append(card)
		return card

	@log
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


d = Deck()
d.shuffle()

# print(d)
# print("{} cards".format(len(d.shoe)))

for i in d:
	print(i)

print(d.deal_one())
# print(d.deal(5))
# d.deal_one()
