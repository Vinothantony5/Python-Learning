string = input()
uppcase=""
lowcase=""
evennum=[]
oddnum=[]
for i in string:
    if i.isupper():
        uppcase+=i
    elif i.islower():
        lowcase+=i
    elif i.isdigit():
        if int(i)%2==0:
            evennum.append(i)
        else:
            oddnum.append(i)
print("".join(sorted(lowcase))+"".join(sorted(uppcase))+"".join(sorted(oddnum))+"".join(sorted(evennum)))