def missingnum(a,n):
	total =a[0];
	arrxor = 0;

	for i in range(1,n):
		total = total ^ a[i]
		arrxor = arrxor ^ i
	arrxor = arrxor ^ i+1
	arrxor = arrxor ^ i+2
	return total ^ arrxor;

if __name__=='__main__':
	n= int(input("Enter the number of elements:"))
	a=[]
	print("Enter the elements:")
	for i in range(0,n):
		temp=int(input())
		a.append(temp)
	reqnum = missingnum(a,len(a))
	print("Missing Number is: ",reqnum)