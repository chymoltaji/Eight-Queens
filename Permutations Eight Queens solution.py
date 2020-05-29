from itertools import permutations

n=8
cols=range(n)
count=0
for vec in permutations(cols):
    if(n==len(set(vec[i]+i for i in cols))==len(set(vec[i]-i for i in cols))):
        print (vec)
        count+=1
print(count)