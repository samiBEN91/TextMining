import numpy as np   
import pandas as pd  
# Creating the Bag of Words model 
from sklearn.feature_extraction.text import CountVectorizer
# library to clean data 
import re  
  
# Natural Language Tool Kit 
import nltk  
  
nltk.download('stopwords') 
  
# to remove stopword 
from nltk.corpus import stopwords 
  
# for Stemming propose  
from nltk.stem.porter import PorterStemmer 

# Import dataset 
dataset = pd.read_csv('Restaurant_Reviews.tsv', delimiter = '\t')  
#print(dataset.head())
#print(dataset.info())

# Initialize empty array 
# to append clean text  
corpus = []
# 1000 (reviews) rows to clean 
for i in range(0, 3):  
      
    # column : "Review", row ith 
    review = re.sub('[^a-zA-Z]', ' ', dataset['Review'][i])  
    # convert all cases to lower cases 
    review = review.lower()
     # append each string to create 
    # array of clean text 
    # split to array(default delimiter is " ") 
    review = review.split()
    corpus.append(review)

    # creating PorterStemmer object to 
    # take main stem of each word 
    ps = PorterStemmer()
     # loop for stemming each word 
    # in string array at ith row     
    review = [ps.stem(word) for word in review 
                if not word in set(stopwords.words('english'))]  
    # rejoin all string array elements 
    # to create back into a string 
    review = ' '.join(review)

    # append each string to create 
    # array of clean text  
    corpus.append(review)  

  
# To extract max 1500 feature. 
# "max_features" is attribute to 
# experiment with to get better results 
cv = CountVectorizer(max_features = 1500)
print (cv)  

# X contains corpus (dependent variable) 
X = cv.fit_transform(corpus).toarray()

# y contains answers if review 
# is positive or negative 
y = dataset.iloc[:, 1].values

print(y)  
  




