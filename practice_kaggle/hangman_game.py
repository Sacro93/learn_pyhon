import random as rd
words=["Ferrari","Caballo","Payaso","Celular","Cafe","Moto","Viaje","Television"]
word=rd.choice(words).upper()
index=rd.randint(0,len(words)-1)
letter=word[index]
first_letter=len(word[:index])
last_letter=len(word[index+1:])
a_clue=(first_letter*" _ ") +letter+ (last_letter*" _ ")
print(a_clue)
word_user= input("Adivine la palabra: ").upper()
condition=word_user == word
print("Gano?", condition)