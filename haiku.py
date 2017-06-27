#Haiku
import random
wordList1 = ["Enchanting", "Amazing", "Colourful", "Delightful", "Delicate"]
wordList2 = ["visions", "distance", "conscience", "process", "chaos"]
wordList3 = ["superstitious", "contrasting", "graceful", "inviting", "contradicting", "overwhelming"]
wordList4 = ["true", "dark", "cold", "warm", "great"]
wordList5 = ["scenery","season", "colours","lights","Spring","Winter","Summer","Autumn"]
wordList6 = ["undeniable", "beautiful", "irreplaceable", "unbelievable", "irrevocable"]
wordList7 = ["inspiration", "imagination", "wisdom", "thoughts"]

#x = random.randrange(0, len(wordList1))
#x2 = random.randrange(0, len(wordList2))
#x3 = random.randrange(0, len(wordList3))
#x4 = random.randrange(0, len(wordList4))
#x5 = random.randrange(0, len(wordList5))
#x6 = random.randrange(0, len(wordList6))
#x7 = random.randrange(0, len(wordList7))

#wordList1[x]
#wordList2[x2]
#wordList3[x3]
#wordList4[x4]
#wordList5[x5]
#wordList6[x6]
#wordList7[x7]


#poem = wordList1[x] + " " + wordList2[x2] + ","

#poem1 = wordList3[x3] + " " + wordList4[x4] + " " + wordList5[x5]  + ","
#poem2 = wordList6[x6] + " " + wordList7[x7] + "."

x = wordList1[random.randrange(0,4,1)]
x1 = wordList2[random.randrange(0,4,1)]
x2 = wordList3[random.randrange(0,5,1)]
x3 = wordList4[random.randrange(0,4,1)]
x4 = wordList5[random.randrange(0,7,1)]
x5 = wordList6[random.randrange(0,4,1)]
x6 = wordList7[random.randrange(0,3,1)]



poem = x + " " + x1 + ","

poem1 = x2 + " " + x3 + " " + x4  + ","
poem2 = x5 + " " + x6 + "."




print(poem)
print(poem1)
print(poem2)
