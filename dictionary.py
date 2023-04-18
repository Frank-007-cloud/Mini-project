import json
from spellchecker import SpellChecker
word=input("Enter word ")
word=word.lower() #change words to lower case (step 4)

spell=SpellChecker()

mispelled=spell.unknown([word])
#print(spell.unknown([word]))
#print(mispelled)


#step 2
with open("data.json") as file:
    data=json.load(file)
    
#step 3

def definition():
    global word
    if word in data:
        print(word)
        for value in data[word]:
            print(value)
#step 4
    else:
       for mispelledword in mispelled:
           correct=spell.correction(mispelledword)
           print(correct)
           
           relatedwords=spell.candidates(mispelledword)
           print(" Or did you mean: ")
           print(','.join(relatedwords))
           word=input("please enter word again: ")
           
           for value in data[word]:
               print(word+':\n',value)
               break
        
definition()

#step 6 (spell checker)
