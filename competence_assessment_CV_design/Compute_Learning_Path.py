
# coding: utf-8

# In[7]:


import pandas as pd


# In[8]:


# Prendere le materie, fare il merging eliminando i doppioni
def getCourseFromGaps(c_t_i, course_dictionary):
    returnDict = dict()
    for comp in c_t_i:
        subjects = course_dictionary[comp[0]]
        for sub in subjects:
            returnDict[sub[0].replace("_"," ")] = sub[1]
    return returnDict


# In[9]:


def getCoursesAndCredits(path):
    cmp_cfu = pd.read_csv(path, sep='\t', header=0)
    return dict([(i,a) for i, a in zip(cmp_cfu.Course, cmp_cfu.Credits)])


# In[10]:


def applyTaxionomy(sub, course_credits):
    complete = dict()
    half = dict()
    for course in sub.items():
        if(course[1] <= 3):
            complete[course[0]] = min(round(course[1]), course_credits[course[0]], 3)

        elif(course[1] > 3 and course[1] < 7):
            complete[course[0]] = min(round(course[1]), course_credits[course[0]], 6)

        elif(course[1] >= 7): 
            current_credits = round(course_credits[course[0]]/2)
            complete[course[0]] = current_credits
            half[course[0]] = course_credits[course[0]]-current_credits
    return complete, half


# In[11]:


def generatePeriods(year):
    periods = []
    for ind in range(1, (year+1)):
        for sem in range(1,3):
            periods.append(str(ind)+"° Year - "+str(sem)+"° Semester")
    return periods


# In[12]:


# Auxiliary functions
def intersection(lst1, lst2): 
    lst3 = [value for value in lst1 if value in lst2] 
    return lst3 

def extractCourse(lis):
    outcome = []
    for elem in lis:
        outcome.append(elem[0])
    return outcome


# In[13]:


def getLearingPath(complete, half):
    sem_name = generatePeriods(2)
    semesters = dict()
    num_subj = 0
    tot_credits = 0
    index = 0
    counter_sem = 0
    boolean_continue = True
    list_courses_in_semester = list()

    for course in complete.items():
        if((tot_credits + course[1]) < 25 and num_subj<4):
            num_subj += 1
            tot_credits += course[1]
            list_courses_in_semester.append(course)

        else:
            semesters[sem_name[index]] = list_courses_in_semester
            index += 1 
            susp = intersection(extractCourse(list_courses_in_semester), list(half.keys()))

            list_courses_in_semester = list()
            num_subj = 0
            tot_credits = 0
            counter_sem += 1
            if(counter_sem==4):
                boolean_continue = False
                break

            for s in susp:
                list_courses_in_semester.append((s, half[s]))
                num_subj += 1
                tot_credits += half[s]
                #
                del half[s]

            if((tot_credits + course[1]) > 25 or num_subj==4):
                semesters[sem_name[index]] = list_courses_in_semester
                index += 1
                list_courses_in_semester = list()
                num_subj = 0
                tot_credits = 0

            list_courses_in_semester.append(course)
            num_subj += 1
            tot_credits += course[1]           

    if(boolean_continue):    
        semesters[sem_name[index]] = list_courses_in_semester
        index += 1
        list_courses_in_semester = list()
        num_subj = 0
        tot_credits = 0

        # Penso che se sono avanzati degli insegnamenti non potranno certo andare nel semestre corrente ma nel successivo
        if(len(half)!=0):
            for item in half.items():
                list_courses_in_semester.append(item)
            semesters[sem_name[index]] = list_courses_in_semester
            
    return semesters        


# In[14]:


def prettyPrintLP(semeste):
    for itm in semeste.items():
        print(itm[0]+'\n')
        for curs in itm[1]:
            print('\t'+str(curs))
        print('\n')

