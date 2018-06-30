from sklearn.feature_extraction.text import TfidfVectorizer
import nltk, string 
import json # json module for API responses

# Static data
dsLabels = ["DSDA01", "DSDA02", "DSDA03", "DSDA04",
            "DSDA05", "DSDA06", "DSDK01", "DSDK02",
            "DSDK03", "DSDK04", "DSDK05", "DSDK06",
            "DSDM01", "DSDM02", "DSDM03", "DSDM04",
            "DSDM05", "DSDM06", "DSENG01", "DSENG02",
            "DSENG03", "DSENG04", "DSENG05", "DSENG06",
            "DSRM01", "DSRM02", "DSRM03", "DSRM04",
            "DSRM05"]

# Create word stemmer
stemmer = nltk.stem.porter.PorterStemmer()
# dictionary used to remove punctuation
remove_punctuation_map = dict((ord(char), None) for char in string.punctuation)

# Load in all competence documents
data = []
with open('./data/competences.jsonl', encoding="utf8") as f:
    for line in f:
        data.append(json.loads(line))

'''
SKLearn document similarity
'''
def calculateSim(text):
    obj = {}
    for comp in data:
        score = cosine_sim(comp['skillText'], text)
        if score > 1:
            score = 1
        obj.update({comp['skillName']: score})
    return obj

'''
Iterator that stems all words in a list
'''
def stem_tokens(tokens):
    return [stemmer.stem(item) for item in tokens]

'''
Remove punctuation, lowercase and stem all words in a cv
'''
def normalize(text):
    return stem_tokens(nltk.word_tokenize(text.lower().translate(remove_punctuation_map)))

# Vectorizor from SKLearn that is used to get the features used to calculate the cosine similarity
vectorizer = TfidfVectorizer(tokenizer=normalize, stop_words='english')

'''
Calculates the actual cosine similarity
'''
def cosine_sim(text1, text2):
    tfidf = vectorizer.fit_transform([text1, text2])
    return ((tfidf * tfidf.T).A)[0,1]
