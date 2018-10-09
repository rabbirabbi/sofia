import random
ss1=0
ss2=0
if(u=='r','p','s'):
	while(True):
		d={1:'r',2:'p',3:'s'}
		c=d[random.randint(1,3)]
		u=(input("r,p,s:"))
		print(c)
		if(c==u):
			print("tie!!!!!")
		elif((c=='r'and u=='s') or (c=='p' and u=='r') or (c=='s' and u=='p')):
			ss1=ss1+1
			print("c won the game")
		else:
			ss2=ss2+1
			print("u won the game")
			if(u=='q'):
				print("byee!!!")
		exit()
	if(ss1==3 or ss2==3):
		exit()