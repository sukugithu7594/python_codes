
def sieveofprime(n1,n2):
	parr = [True for i in range(n2+1)]
	for i in range(2,int(n2 ** 0.5)):
		if(parr[i]==True):
			for j in range(i*i,n2+1,i):
				parr[j]=False
	for i in range(n1,n2):
		if(parr[i]):
			print(i)

if __name__=='__main__':
	beg=int(input("Enter the range beginning:"))
	end=int(input("Enter the range ending:"))
	sieveofprime(beg,end)