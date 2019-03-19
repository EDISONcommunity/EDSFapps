import gensim.parsing.preprocessing as preprocessing
import gensim.corpora.textcorpus as textcorpus
import json
import re
import smart_open
from gensim.models.doc2vec import TaggedDocument
from nltk.corpus import stopwords

def readFile(path):
    competencies_json = []
    with smart_open.smart_open(path, encoding="utf8") as f:
        for line in f:
            competencies_json.append(json.loads(line))
    return competencies_json

def transformText(text):        
    
    # Convert text to lower
    text = text.lower()
    # Removing non ASCII chars
    text = re.sub(r'[^\x00-\x7f]',r' ',text)
    # Remove the punctuation
    text = preprocessing.strip_punctuation2(text)
    # Strip all the numeric
    text = preprocessing.strip_numeric(text)
    # Strip multiple whitespaces
    text = textcorpus.strip_multiple_whitespaces(text) 
    # Stemming
    stem = preprocessing.stem_text(text)    
    # Remove stop words
    stops = set(stopwords.words("english"))  
    stops.add('also')
    filtered_words = [word for word in stem.split() if word not in stops]
    return textcorpus.remove_short(filtered_words, minsize=3)
    
    
def splitAndTag(file):
    list_comp = []
    for comp in file:
        list_comp.append(TaggedDocument((transformText(comp['skillText'])), [comp['skillName']]))
    return list_comp