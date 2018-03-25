#list to store data set
one=[]
two=[]
three=[]
four=[]
five=[]
count=0
count1=0
window=0
window2=0
inc1=0
inc2=0
#flag with two person window
flag=[0,0]
flag2=[0,0]
size=int(input("Enter the window size\n"))
threshold=int(input("Enter the threshold\n"))


def entry(x):
    global flag, count, window, window2, inc1, inc2
    #First person
    #print("1st Person")
    if three[x]<=threshold and flag[0]==0 and flag[1]==0 and window<=size: #and flag2[0]==0 and flag2[1]==0:
        flag[0]=1
        print("flag set 1")
        if window==0:
            inc1=1
    elif four[x]<=threshold and flag[0]==1 and window<=size:
        flag[0]=2
        #print("flag 0=2")
    elif five[x]<=threshold and flag[0]==2 and window<=size:
        flag[0]=3
        #print("flag 0=2")
    if window==size:
        window=0
        flag[0]=0
        inc1=0
    if flag[0]==3:
        print("Entry")
        count=count+1
        flag[0]=0
        window=0
        inc1=0
        fob.write("Entry")
        fob.write("\n")
    #Second Person
    #print("2nd Person")
    if three[x]<=threshold and flag[1]==0 and flag[0]==3 and window2<=size: #and flag2[0]==0 and flag2[1]==0:
        flag[1]=1
        print("flag set 1")
        if window2==0:
            inc2=1
    elif four[x]<=threshold and flag[1]==1 and window2<=size:
        flag[1]=2
        #print("flag 1=2")
    elif five[x]<=threshold and flag[1]==2 and window2<=size:
        flag[1]=3
        #print("flag 1=2")
    if window2==size:
        window=0
        flag[1]=0
        inc2=0
    
    if flag[1]==3:
        count=count+1
        print("Entry")
        flag[1]=0
        window2=0
        inc2=0
        fob.write("Entry")
        fob.write("\n")
    if inc1==1:
        window+=1
        #print("one incremented")
    if inc2==1:
        window2+=1
        #print("two incremented")

def exit1(x):
    global flag, count1, window, window2, inc1, inc2
    #First person
    #print("1st Person")
    if five[x]<=threshold and flag2[0]==0 and flag2[1]==0 and window<=size: #and flag[0]==0 and flag[1]==0:
        flag2[0]=1
        print("flag2 set 1")
        if window==0:
            inc1=1            
            
    if four[x]<=threshold and flag2[0]==1 and window<=size:
        flag2[0]=2
        #print("flag2 0=2")
    if three[x]<=threshold and flag2[0]==2 and window<=size:
        flag2[0]=3
        #print("flag2 0=3")
    if window==size:
        window=0
        flag2[0]=0
        inc1=0
        
    
    if flag2[0]==3:
        print("Exit")
        count1=count1+1
        flag2[0]=0
        window=0
        inc1=0
        fob.write("Exit")
        fob.write("\n")
    #Second Person
    #print("2nd Person")
    if five[x]<=threshold and flag[1]==0 and flag2[0]==32 and window2<=size: #and flag[0]==0 and flag[1]==0:
        flag2[1]=1
        print("flag2 set 1")
        if window2==0:
            inc2=1
    if four[x]<=threshold and flag2[1]==1 and window2<=size:
        flag2[1]=2
        #print("flag2 1=2")
    if three[x]<=threshold and flag2[1]==2 and window2<=size:
        flag2[1]=3
        #print("flag2 1=2")
    if window2==size:
        window2=0
        flag2[1]=0
        inc2=0
    
    if flag2[1]==3:
        count1=count1+1
        print("Exit")
        flag2[1]=0
        window2=0
        inc2=0
        fob.write("Exit")
        fob.write("\n")
    if inc1==1:
        window+=1
        #print("one incremented")
    if inc2==1:
        window2+=1
        #print("two incremented")


# Reading from file and saving int the list
fob=open("Entry Exit 28th june2.csv",'r')
for line in fob:
    buffer=line.rstrip("\n").split(",")
    #print(buffer)
    one.append(str(buffer[0]))
    two.append(str(buffer[1]))
    three.append(int(buffer[2]))
    four.append(int(buffer[3]))
    five.append(int(buffer[4]))
fob.close()

#Main function
fob=open("28th june result.csv",'w+')
s=""
for i in range(0,len(one)):
    s=str(i)+"\t"+str(three[i])+","+str(four[i])+","+str(five[i])
    print(s)
    entry(i)
    exit1(i)
fob.close()
print("Entries=",count)
print("Exits=",count1)

