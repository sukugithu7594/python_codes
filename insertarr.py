#function to insert an element into nth postion of an array
def insertlist(a,pos,val):
	l=[val]
	if len(a)==0:
		return l
	if pos>len(a):
		pos=len(a)
	a=a[0:pos]+l+a[pos:len(a)]
	print(a)
	return a

if __name__=='__main__':
	a=[4,8,9]
	a=insertlist(a,2,10)
	a=insertlist(a,5,2)
	a=insertlist(a,6,11)
	print(a)