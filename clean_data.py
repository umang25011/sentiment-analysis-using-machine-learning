#GET FILE AND READ DATA INTO train_data[] and target[]
root_path="" #address of folder.so we don't have to write whole file address
filename=""#enter file name here , clean_filename.txt will be generated
train_data=[] #to hold text
target=[] #to hold actual answer of text


file=open(root_path+filename) 
for line in file:
  splitted_line=[]
  splitted_line=line.split()
  if splitted_line[0] =="":   #specify how to split the data
    target.append(0) # 0->NEGATIVE 
  else:
    target.append(1) # 1->POSITIVE
  train_data.append(' '.join(splitted_line[1:]))
file.close()
del file
  
#CLEAN DATA
def clean_data(data): #for for cleaning data
    
    import re #for removing non word character
    import nltk 
    from nltk.corpus import stopwords #list of available stopwords by nltk
    from nltk.stem import PorterStemmer,WordNetLemmatizer #for stemming and lemmatization

    stemmer= PorterStemmer()
    lemmatizer=WordNetLemmatizer()
    english_stop_words=stopwords.words('english')
    
    train_data_cleaned=[]
    
    for line in data:
        temp_data=[]
        line= re.sub("\W+|\d+"," " ,line.lower()) #remove non word characters
        
        for word in line.split():
            word=word.strip()
            if word not in english_stop_words:
                word=stemmer.stem(word) #stemming
                word=lemmatizer.lemmatize(word) #lemmatization
                temp_data.append(word)
        
        train_data_cleaned.append(' '.join(temp_data))   
    return train_data_cleaned

train_data= clean_data(train_data)

file=open(root_path+"clean_"+filename,'w',encoding="utf8") #save clean_data so we don't have to clean data again

#save data in this manner -> clean_text:target(actucal answer of that text)
for i in range(len(train_data)):
    file.write(train_data[i])
    file.write(":") 
    file.write(str(target[i]))
    file.write("\n")
del file
