inpu=str(input("Enter the sentance :"))

inpu=inpu.split(' ')
count=0
for i in inpu:
    if  i == "S":
        count+=1
print("frequency of word : ",count)
