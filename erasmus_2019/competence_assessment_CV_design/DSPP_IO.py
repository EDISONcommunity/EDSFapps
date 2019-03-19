
# coding: utf-8

# In[3]:


import pandas as pd


# In[4]:


def getWeightsForDSPP(fileName, dspp):
    with open(fileName, 'r') as f:
        list_weights = f.readlines()
    list_weights = [x.strip() for x in list_weights] # It removes whitespace characters like `\n` at the end of each line
    
    weighted_list = []
    for item in list_weights:
        tuple_w = item.split("\t")
        if(tuple_w[1] == dspp):
            weighted_list.append((tuple_w[0], tuple_w[2]))
    dic = dict(weighted_list)
    for e in ['DSDA', 'DSENG', 'DSDM', 'DSRMP', 'DSDK']:
        dic.pop(e)
    return dic


# In[5]:


def getNormalizedDictionary(dict_w):
    normalized_dict = {k: int(v)/10 for k, v in dict_w.items()}
    lstdic = list()
    for key, value in normalized_dict.items():
        lstdic.append([key, value])
    return lstdic


# In[6]:


def getDifferences(sim, norm_dic):
    diff_list = []
    for i in range(0,len(sim)):
        divider = sim[i][1]
        if(divider < 0):
            divider = 0 # Sim però possono essere anche negativi essendo calcolati tramite la cosine_similarity, occhio!
        diff_value = norm_dic[i][1] - sim[i][1]
        if(diff_value < 0):
            diff_value = 0
        diff_list.append((norm_dic[i][0], diff_value))
    return diff_list


# In[7]:


def getWeightedDifferences(sim, diff_list, norm_dic):
    diff_weigheted = []
    value = 0
    for i in range(0,len(sim)):
        weighted_value = diff_list[i][1]*norm_dic[i][1]
        diff_weigheted.append((norm_dic[i][0], weighted_value))
    return diff_weigheted


# In[8]:


def getExcelTable(diff_list, dspp):
    df = pd.DataFrame(diff_list, columns=['DSComp', 'Score_diff'])
    df.to_excel('difference '+dspp+'.xlsx')


# In[9]:


def getExcelWeightedTable(diff_weigheted, dspp):
    df = pd.DataFrame(diff_weigheted, columns=['DSComp', 'Score_diff_weighted'])
    df.to_excel('difference_weighted '+dspp+'.xlsx')

