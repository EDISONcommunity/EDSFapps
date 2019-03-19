
# coding: utf-8

# In[2]:


import Document_Preprocessing_and_Tagging
import matplotlib.pyplot as plt
from math import pi


# In[1]:


def computeSimilarity(text, model):
    outcome = Document_Preprocessing_and_Tagging.transformText(text)
    model.random.seed(0)
    inferred_vector = model.infer_vector(outcome)
    sims = model.docvecs.most_similar([inferred_vector], topn=len(model.docvecs))
    sims.sort(key=lambda x: x[0])
    return sims


# In[ ]:


def plotSpiderChart(similarity):
    categories = [x[0] for x in similarity]
    values = [x[1] for x in similarity]
    N = len(categories)
    
    # We are going to plot the first line of the data frame.
    # But we need to repeat the first value to close the circular graph:
    values += values[:1]
    values

    # What will be the angle of each axis in the plot? (we divide the plot / number of variable)
    angles = [n / float(N) * 2 * pi for n in range(N)]
    angles += angles[:1]

    # Initialise the spider plot
    ax = plt.subplot(111, polar=True)

    # Draw one axe per variable + add labels labels yet
    plt.xticks(angles[:-1], categories, color='black', size=7)

    # Draw ylabels
    ax.set_rlabel_position(0)
    plt.ylim(0,1)

    # Plot data
    ax.plot(angles, values, linewidth=1, linestyle='solid')

    # Fill area
    #ax.fill(angles, values, 'b', alpha=0.1)
    plt.show()


# In[ ]:


def plotSpiderChart2Graphs(sim1_in, sim2_in):
    sim1 = sim1_in.copy()
    sim1.sort(key=lambda x: x[0])
    sim2 = sim2_in.copy()
    sim2.sort(key=lambda x: x[0])
    #print('sim1')
    #print(sim1)
    #print('sim2')
    #print(sim1)
    categories = [x[0] for x in sim1]
    values1 = [x[1] for x in sim1]
    values2 = [x[1] for x in sim2]
    N = len(categories)
    
    values1 += values1[:1]
    values1
    
    values2 += values2[:1]
    values2

    angles = [n / float(N) * 2 * pi for n in range(N)]
    angles += angles[:1]

    ax = plt.subplot(111, polar=True)
    plt.xticks(angles[:-1], categories, color='black', size=7)

    ax.set_rlabel_position(0)
    plt.ylim(0,1)
    ax.plot(angles, values1, linewidth=1, linestyle='solid')
    ax.plot(angles, values2, linewidth=2, linestyle='solid')
    plt.show()

