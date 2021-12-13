from math import floor


def compareSeq(s1:str,s2:str):
    total=0
    for i in range(min(len(s1),len(s2))):
        total+= (1 if s1[i]==s2[i] else 0)
    return floor(100*(total/(max(len(s1),len(s2)))))

file=open('output.fas','r')
l=[l.strip().split('\n') for l in ''.join(file.readlines()).split('>')][1:]
file.close()
fin=[]
for i in l:
    fin.append((i[0],''.join(i[1:])))
for i in range(len(fin)):
    for j in range(i+1,len(fin)):
        print(fin[i][0],"vs",fin[j][0],"  ",compareSeq(fin[i][1],fin[j][1]),"%")
