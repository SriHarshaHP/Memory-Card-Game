import random as rn
l=["########","########","########","########","########"]
l1=["###00###","###01###","###02###","###03###","###04###",
    "###05###","###06###","###07###","###08###","###09###",
    "###10###","###11###","###12###","###13###","###14###",
    "###15###","###16###","###17###","###18###","###19###",
    "###20###","###21###","###22###","###23###","###24###"]
def cards():
    n=0
    for k in range(5):
        for j in range(5):
            for i in range(5):
                if(j==2):
                    print(l1[n],end=" ")
                    n+=1
                else:
                    print(l[i],end=" ")
            print()
        print()
cards()
d={}
n=0
for i in range(199):
    for j in range(5):
        d[n]=[i,j]
        n+=1
lpick=["***!!***","***!!***","***@@***","***@@***","***##***","***##***","***%%***","***%%***","***^^***","***^^***",
       "***&&***","***&&***","***((***","***((***","***))***","***))***","***__***","***__***","***++***","***++***",
       "***==***","***==***","***--***","***--***","***~~***"]
'''for i in range(20):
    r1=rn.randint(0,24)
    r2=rn.randint(0,24)
    lpick[r1],lpick[r2]=lpick[r2],lpick[r1]'''
mach=[]

for x in range(10):
    pick=int(input("Enter the 1st PICK:"))
    n=0
    for k in range(5):
        for j in range(5):
            for i in range(5):
                xyz=''
                for z in mach:
                    if([k,i] in z):
                        xyz="t"
                if(xyz=="t"):
                    print("||||||||",end=" ")
                elif([k,i]==d[pick] and j==2):
                    print(lpick[pick],end=" ")
                elif([k,i]==d[pick]):
                    print("********",end=" ")
                elif(j==2):
                    print(l1[n],end=" ")
                    n+=1
                else:
                    print(l[i],end=" ")
                if(pick==n):
                    n+=1
            print()
        print()
    pick2=int(input("Enter the 2nd PICK:"))
    n1=0
    for k in range(5):
        for j in range(5):
            for i in range(5):
                xyz=""
                for z in mach:
                    if([k,i] in z):
                        xyz="t"
                if(xyz=="t"):
                    print("||||||||",end=" ")
                elif([k,i]==d[pick] and j==2):
                    print(lpick[pick],end=" ")
                elif([k,i]==d[pick2] and j==2):
                    print(lpick[pick2],end=" ")
                elif([k,i]==d[pick] or [k,i]==d[pick2]):
                    print("********",end=" ")
                elif(j==2):
                    print(l1[n1],end=" ")
                    n1+=1
                else:
                    print(l[i],end=" ")
                if(pick==n and pick2==n1):
                    n1+=1
            print()
        print()
    if(lpick[pick]==lpick[pick2]):
        dlist=[d[pick],d[pick2]]
        mach.append(dlist)
    else:
        print("NO MATCH")
        ch=input("DO u want to continue")
        if(ch!="y"):
            break
