import io
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 
  
example_sent = "This is a sample sentence, showing off the stop words filtration."
  
stop_words = set(stopwords.words('english')) 
print("stopwords\n",stop_words) 
word_tokens = word_tokenize(example_sent)
print ("\n")
print("wordtoken\n",word_tokens)  
  
filtered_sentence = [w for w in word_tokens if not w in stop_words] 
print ("\n")
print("filtered_sentence\n",filtered_sentence) 

filtered_sentence = [] 
  
for w in word_tokens: 
    if w not in stop_words: 
        filtered_sentence.append(w) 
  
print(word_tokens) 
print(filtered_sentence)


stop_words=set(stopwords.words('english'))
file1 = open("text.txt") 
line = file1.read()# Use this to read file content as a stream:
print("line\n",line) 
words = line.split()
print("words\n",words) 
for r in words: 
    if not r in stop_words: 
        appendFile = open('filteredtext.txt','a') 
        appendFile.write(" "+r) 
        appendFile.close() 