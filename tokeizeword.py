# Natural Language Tool Kit 
import nltk  
  
#nltk.download('all')  

# import the existing word and sentence tokenizing  
# libraries 
from nltk.tokenize import sent_tokenize, word_tokenize

  
text = "Natural language processing (NLP) is a field " + \
       "of computer science, artificial intelligence " + \
        "thereof."

print(sent_tokenize(text))
wortokenize=word_tokenize(text)
print(wortokenize)
print(wortokenize[1])
print (len(wortokenize))

for i in (wortokenize):
       print(i)
       

for j in range (len(wortokenize)):
       print (wortokenize[j])
       

for i in (wortokenize):
       print(i)
       break