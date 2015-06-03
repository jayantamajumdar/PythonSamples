# Bear Matching for Zoo breeding program with numerous constraints
# Goal: Given a file with an array of [name,gender,mother,father,age],
# find all possible pairs of bears suitable for mating

# Constraints:
# Bears must be different genders
# Ages of both bears must be between 2.0 and 6.0
# Difference in bear age can be at most 1 year
# Both bears must currently be childless
# Bears matched must have no common grandparents


def matching_bears(filename):

    import re

# F := List of female bears, M := List of male bears
# D := Dictionary containing all bears
    F= []
    M = []
    D = {}

# Reading in and formatting our input file

    file = open(filename)
    for line in file:
        line = line.lower()
        line = line.split(":")
        line2 = []
        for i in line:
            i = i.strip()
            i = re.sub(' +',' ' , i)
            line2.append(i)
        line2[4] = int(10.0 * float(line2[4]))
       
        if line2[0] in D:
            continue
        else:
            D[line2[0]] = line2[1:]
        
        if (line2[1] ==  "f" and line2[0] not in F):
           F.append(line2[0])
        elif(line2[1] == "m" and line2[0] not in M):
            M.append(line2[0])
        else:
            continue
        print line2
  
    print 'm=', M
    print 'f=', F
    print D
    print
    print
    D2 = {}
 

 # Numerous small functions to determine age, parents, grandparents, 
 # children, etc. for any given bear in our dictionary   
    def age(x):
        return D[x][3]
    
    
    def parents(x):
        if x in D:
            return [D[x][1],D[x][2]]
        else:
           return []
    
    def gp(x):
        return parents(D[x][1]) + parents(D[x][2])
             
                
    def family(x):
        D2[x] = [x] + parents(x) + gp(x)
        return D2[x]
    
    for i in M:
        family(i)
    for i in F:
        family(i)
            
    
    def children(x):
        for d in D:
            if (x == D[d][1] or x == D[d][2]):
                return 1
            else:
                continue
        return 0
        
    def familycheck(x,y):
       # print D2[x],D2[y]
        for i in D2[x]:
            if i in D2[y] and i != 'nil':   
                if (x,y) in pairing:
                    pairing.remove((x,y))
                    return
                else:
                    return
            elif((x,y) in pairing):
                continue
            elif(i not in D2[y]):
                pairing.append((x,y)) 
    
    pairing = []


#Final loop for comparing all attributes of all pairs to produce our pairings

    for f in F:
       for i in range(len(M)):
            if (age(f)<20 or age(f)>60 or age(M[i])<20 or age(M[i])>60):
                continue
            else:
                if(abs(age(f) - age(M[i])) > 10):
                    continue
                else:
                    if (children(f) != 0 or children(M[i]) != 0):   
                        continue
                    else:
                        familycheck(f,M[i])
    return pairing
           
  
    file.close()


 # Returns a list of pairs.
  