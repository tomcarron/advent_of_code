file1 = open('input_day2', 'r')
lines = file1.readlines()
opps=["A","B","C"]
mes=["X","Y","Z"]
total_score=0
for line in lines:
    score=0
    opp,me=line.split()
    #score for choice
    score+=mes.index(me)+1
    #draw
    if opps.index(opp) == mes.index(me):
        score+=3
    #opp rock
    elif opp == "A":
        if me == "Y":
            score+=6
        elif me == "Z":
            score+=0
    elif opp == "B":
        if me == "Z":
            score+=6
        elif me == "X":
            score+=0
    else:
        if me == "X":
            score+=6
        elif me == "Y":
            score+=0
    total_score+=score
    
print(total_score)

"""part 2"""
#,y,z lose draw win
total_score=0
for line in lines:
    score=0
    opp,me=line.split()
    if me == "X":
        score+=0
        if opp == "A":
            score+=3
        elif opp == "B":
            score+=1
        else:
            score+=2
    elif me =="Y":
        score+=3
        if opp == "A":
            score+=1
        elif opp == "B":
            score+=2
        else:
            score+=3
    else:
        score+=6
        if opp == "A":
            score+=2
        elif opp == "B":
            score+=3
        else:
            score+=1
    total_score+=score   
print(total_score)