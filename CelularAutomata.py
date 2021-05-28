#this code is just for use on the processing.py plataform, such as a python sketch

from random import randint


#size of the sketch image
size(1000,1000)

rule=[]
rule=[0,0,0,1,1,1,1,0]




def SeedTransformation(last_me, me, next_me):

    #return the next state of a seed given a rule: "111, 110, 101, 100, 011, 010, 001, 000"

    state=[]
    state.extend([last_me, me, next_me])

    if state==[1,1,1]:
        return rule[0]
    if state==[1,1,0]:
        return rule[1]
    if state==[1,0,1]:
        return rule[2]
    if state==[1,0,0]:
        return rule[3]
    if state==[0,1,1]:
        return rule[4]
    if state==[0,1,0]:
        return rule[5]
    if state==[0,0,1]:
        return rule[6]
    if state==[0,0,0]:
        return rule[7]



initial_state=[]                                                               
#initial_state=[0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0]                                                                                
#65 vertices
#initial_state=[0,0,0,0,0,0,0,1,0,0,0,0,0,0,0]
initial_state=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
generationOne=initial_state


time=100

NumbersLife=[]
for t in range(time):
    
    cel=[]
    for j in range(len(initial_state)):
        cel.append(0)
    
    countCel=0
    for i in range(len(initial_state)):
        if(i==0):
            last_me1=generationOne[len(initial_state)-1]
            me1=generationOne[i]
            next_me1=generationOne[i+1]
        elif(i==(len(initial_state)-1)):
            last_me1=generationOne[i-1]
            me1=generationOne[i]
            next_me1=generationOne[0]
        else:
            last_me1=generationOne[i-1]
            me1=generationOne[i]
            next_me1=generationOne[i+1]
            
        cel[i]=conta(last_me1, me1 ,next_me1)
        if(cel[i]==0):
            fill(50)
            rect(6*i,6*t+6,6,6)
            
        if (cel[i]==1):
          countCel+=1      

    NumbersLife.append(countCel)
    generationOne=cel
    #print(cel)
        
            
print(NumbersLife)            
    
    
