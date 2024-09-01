import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer

paragraph = "At eight o'clock on Thursday morning Arthur didn't feel very good. He got up from bed and went to brush his teeth. At 10 o'clock Arthur headed to his astronomy class."

#tokenizes by word
word_tokens = nltk.word_tokenize(paragraph, language='english',preserve_line=True)
print("tokens: ",word_tokens)

#part of speech tags the sentence
tagged = nltk.pos_tag(nltk.word_tokenize(paragraph, language='english',preserve_line=True))
print("part of speech tagging: ",tagged)

gibberish = "'Twas brillig, and the slithy toves did gyre and gimble in the wabe: all mimsy were the borogoves, and the mome raths outgrabe."
gibberish_tagged = nltk.pos_tag(nltk.word_tokenize(gibberish, language='english',preserve_line=True))
print("gibberish pos tag: ", gibberish_tagged)


#filtering stopwords
stop_words = set(stopwords.words("english"))
split_sentence = paragraph.split(" ")
filtered_data = []
for word in split_sentence:
    if word not in stop_words:
        filtered_data.append(word)
print(filtered_data)

#stemming
stem_string = "The crew of the USS Discovery discovered many discoveries. Discovering is what explorers do."
stemmer = PorterStemmer()
words = nltk.word_tokenize(stem_string, language='english',preserve_line=True)
stemmed_words = [stemmer.stem(word) for word in words]
print("original: ",words)
print("stemmed: " ,stemmed_words)

#lemmatization
lemmatizer = WordNetLemmatizer()
lem_string = "The children in the class learned about all the stars in the galaxies"
words = nltk.word_tokenize(lem_string, language='english',preserve_line=True)
lem_words = [lemmatizer.lemmatize(word) for word in words]
print("original: ", words)
print("lemmatized", lem_words)

