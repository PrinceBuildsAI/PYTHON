#Append(), Extend(), Add(), Update() #use

x = [ 1, 2, 3]
print(x)            

x.append(100)               #Append()-> Append only add one element in list like= x.append(100) and x.append(100,200) not possible  
print(x)
                        
x.extend([200,300])         #Extend()-> Extend can add multiple element list
print(x)                    # []-> use for list


set1 = {10,20,30}           #Add()-> Add is used to add only one element in {Set}
print(set)

set1.add(40)
print(set1)                 #set is unordered but list is ordered

set1.update({50,60,70})     #update() is used to add multiple value is set  
print(set1)

