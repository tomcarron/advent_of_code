import numpy as np
#Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?
file1 = open('input', 'r')
lines = file1.readlines()
cals=0
elfs=[]
for line in lines:
    if line == '\n':
        elfs.append(int(cals))
        cals=0
    else:
        cals+=int(line)
print("The elf carrying the most calories is carrying ", max(elfs)," calories")

#Now find the calories carried by the top three elves
#sort the list
sorted=np.sort(elfs)
print("The top 3 elves are carrying ",np.sum(sorted[-3:])," calories in total")



    


