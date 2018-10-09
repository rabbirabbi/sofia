a=['1','2','3','4','5','6','7','8','9']

def b():
	print(a[0]+'|'+a[1]+'|'+a[2])
	print("--------------------")
	print(a[3]+'|'+a[4]+'|'+a[5])
	print("--------------------")
	print(a[6]+'|'+a[7]+'|'+a[8])
p1Turn=True
for i in range(9):
	b()
#p1 plays	
	if p1Turn:
		s=input("p1,choose place:")
		if s in a:
			a[int(s)-1]='x'
			p1Turn=not p1Turn
#p2 plays				
	else:
		t=input("p2,choose place:")
		if t in a:
			a[int(t)-1]='o'
			p1Turn=not p1Turn
for i in range(0,1,2):		
a1=[1,2,3]
a2=[4,5,6]
a3=[7,8,9]
a4=[1,5,9]
a5=[3,5,7]
a6=[1,4,7]
a7=[2,5,8]
a8=[3,6,9]
if((a1==s) or (a2==s) or (a3==s) or  (a4==s) or (a5==s) or (a6==s) or (a7==s) or (a8==s)):
	
	print("p1 won")				


