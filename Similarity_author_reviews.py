import math 
newdict = {}
newdict= eval(open("D:\word1.txt").read())

def get_similarity(x,y):
    l=[]
    m=[]
    for name in newdict.keys():
        if(name == x):
            l=newdict[name]
    
    for name in newdict.keys():
        if(name == y):
            m=(newdict[name])
    #To identify the common reviews among authors
    d1_keys =set(l.keys())
    d2_keys =set(m.keys())
    intersection_keys= d1_keys.intersection(d2_keys)
    new_list=[]
    for element in intersection_keys:
        val1 = m[element]
        val2 = l[element]
        diff = abs(val1-val2) ** 2
        new_list.append(diff)
    total =sum(new_list)
    euclid=math.sqrt(total)
    return euclid

def similarities(x):
    for name in newdict.keys():
        if(name not in x):
            print((x,name),":",get_similarity(name,x))
        
euclidean=get_similarity('Jill Brown','Mary Doyle')
print("Similarity Score is :",euclidean)
all_similarities =similarities('Nancy Pollock')





