
# coding: utf-8

# In[4]:


import numpy as np


# In[1]:


def removeKey(K, model, coordinates):
    if(K in model.wv.vocab):
        list_dict = list(model.wv.vocab.keys())
        # Fondamentale mantenere l'allineamento
        index = list_dict.index(K)
        upd_vector = np.delete(coordinates, index, axis=0)
        coordinates = upd_vector
        del model.wv.vocab[K]
    return coordinates


# In[2]:


def coordinatesAlignment(bigram, coordinates, model):
    for item in bigram:
        entry = item.split()
        coordinates = removeKey(entry[0], model, coordinates)
        coordinates = removeKey(entry[1], model, coordinates)
        coordinates = removeKey(entry[0]+entry[1], model, coordinates)


# In[3]:


def tensorBoardOutput(model, coordinates):
    np.savetxt('wordCoordinatesTensor.tsv', coordinates, delimiter="\t") #Save1
    f = open('wordMetadataTensor.tsv','w') #Save2
    for item in model.wv.vocab:
        f.write(str(item)+'\n')
    f.close()

