# import these modules 
from nltk.stem import WordNetLemmatizer 
  
lemmatizer = WordNetLemmatizer() 
  
print("rocks :", lemmatizer.lemmatize("rocks")) 
print("corpora :", lemmatizer.lemmatize("corpora")) 
  
# a denotes adjective in "pos" 
print("better :", lemmatizer.lemmatize("better", pos ="v")) 

print(lemmatizer.lemmatize("stripes", 'v'))  
#> strip

print(lemmatizer.lemmatize("stripes", 'n'))  
#> stripe