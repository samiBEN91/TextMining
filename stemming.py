# import these modules 
from nltk.stem import PorterStemmer 
from nltk.tokenize import word_tokenize 
   
ps = PorterStemmer() 
  
# choose some words to be stemmed 
words = ["program", "programs", "programer", "programing", "programers"] 
  
for w in words: 
    print(w, " : ", ps.stem(w)) 

sentence = "Programers program with programing languages"
words1= word_tokenize(sentence)
print("words1\n",words1) 
   
for w in words1: 
    print(w, " : ", ps.stem(w)) 