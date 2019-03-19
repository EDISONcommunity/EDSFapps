
# coding: utf-8

# In[8]:


import Document_Preprocessing_and_Tagging
from collections import Counter
from itertools import tee, islice


# In[1]:


def ngrams(lst, n):
    tlst = lst
    while True:
        a, b = tee(tlst)
        l = tuple(islice(a, n))
        if len(l) == n:
            yield l
            next(b)
            tlst = b
        else:
            break


# In[9]:


def getNGramFromDocuments(cj, num):
    l = []
    for i in range(0, len(cj)):
        l.append(Document_Preprocessing_and_Tagging.transformText(cj[i]['skillText']))
    flat_list = [item for sublist in l for item in sublist]
    pairs = Counter(ngrams(flat_list, num))
    return list(pairs.items())


# In[11]:


def computeCommonNgrams(all_ng, limit):
    bigram = []
    for item in all_ng:
        if(item[1] >= limit):
            bigram.append(item[0][0]+" "+item[0][1])

    mainList = list()
    for elem in bigram:
        h_list = []
        h_list.append(elem)
        mainList.append(h_list)
    return bigram, mainList

