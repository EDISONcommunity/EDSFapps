
# coding: utf-8

# In[5]:


import pandas as pd
import operator


# In[6]:


def getCompetenceToImprove(dif_w):
    diff_weigheted_sorted = sorted(dif_w, key=lambda x: x[1], reverse=True)
    competence_to_improve = [x for x in diff_weigheted_sorted if x[1] > 0.5]
    return competence_to_improve


# In[7]:


def getTuple_knowScore(dict_w, ontology):
    filtering_comp = [x for x in list(ontology.individuals()) if x.get_name() in dict_w.keys()]
    knowList = []
    for item in filtering_comp:
        for knowl in item.knowledge:
            knowList.append((knowl.get_name(), dict_w.get(item.get_name())))
    return knowList


# In[8]:


def getAVG_knowledge(l_w):
    df = pd.DataFrame(l_w)
    df.columns = ['knowledge', 'weight']
    df['weight'] = df['weight'].apply(pd.to_numeric)
    know_groups = df.groupby("knowledge")
    means = know_groups['weight'].mean()
    return means.to_dict()


# In[9]:


def getAVG_units(dict_, ontology):
    k_fromOntology = [x for x in list(ontology.individuals()) if x.get_name() in dict_.keys()]
    units_avg = dict()
    for item in k_fromOntology:
        k_units = list(item.boK_mapping)
        l = []
        for k in k_units:
            tot = 1
            toAdd = dict_[item.get_name()]
            if(k.get_name() in units_avg):
                toAdd = (toAdd+units_avg[k.get_name()])
                tot += 1
            units_avg[k.get_name()] = toAdd/tot # Nested Dictionary
    return units_avg


# In[11]:


def getDS_Course_Score(ds, name, units_avg):
    index = 1
    voc = dict()
    for ds_sub in ds:
        inner = dict()
        for knw in ds_sub:
            units = knw.boK_mapping
            for u in units:
                for course in u.course:
                    inner[course.get_name()] = units_avg[u.get_name()]
        inner_sorted = sorted(inner.items(), key=operator.itemgetter(1), reverse=True)
        voc[name+'0'+str(index)] = inner_sorted
        index = index+1
    return voc

