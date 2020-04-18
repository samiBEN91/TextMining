import os
import nltk
import nltk.corpus
nltk.download('gutenberg') 
print("\n")
print (nltk.corpus.gutenberg.fileids())
hamlet=nltk.corpus.gutenberg.words('shakespeare-hamlet.txt')
print (hamlet)

for word in hamlet [:5]:
	print (word, sep=' ', end=' ')

print("\n")
print (os.getcwd())
print ("coucou")