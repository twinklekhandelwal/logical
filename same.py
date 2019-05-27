a=[1,2,3]
b=[1,2,3]
i=0
#this is my same program 
while(i<len(a)):
	if b[i] not in a:
		print("a,b is false")
		break
#here is increament
	i=i+1

if(i==len(a)):
	print("a,b is true")		