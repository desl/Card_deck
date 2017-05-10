import cards



d = cards.Deck()
d.shuffle()

# for i in d:
# 	print(i)

d.deal_one()
d.save_deck()

# d.load_deck()

print("Shoe:")
print(d.shoe)

print("Dealt:")
print(d.dealt)