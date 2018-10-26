a=['1','2','3','4','5','6','7','8','9']

def b():
	print(a[0]+'|'+a[1]+'|'+a[2])
	print("--------------------")
	print(a[3]+'|'+a[4]+'|'+a[5])
	print("--------------------")
	print(a[6]+'|'+a[7]+'|'+a[8])
p1Turn=True
while True:
	b()
	s=input("choose place:")
	if(s in a):
#missing condition		
		else:
			if p1Turn:
				print("p1>>")
				a[int(s)-1]='x'
				p1Turn=not  p1Turn
			else:
				print("p2>>")
				a[int(s)-1]='o'
				p1Turn=not  p1Turn
			for d in(0,3,6):
				if(a[d]==a[d+1] and a[d]==a[d+2]):
					print("bye.....bye")
					exit()
			for d in range(3):
				if(a[d]==a[d+3] and a[d]==a[d+6]):
					print("bye.....bye")
					exit()
					print("bye.....bye")
					exit()
			if(a[2]==a[4] and a[2]==a[6]):
					print("bye.....bye")
					exit()
	else:
		print("invalid position")
		continue
		
		


