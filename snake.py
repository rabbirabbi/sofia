
import random 
p=0
while(p<=100):
	a=input("enter r or q:")
	if(a=='r'):
		r=(random.randint(1,6))
		p=p+r
		print("my position:",p)
		print("num in dice:",r)
		if(p==8):
			print("congrats u can climb the ladder")
			p=37
		elif(p==11):
			print("oops sry u r bite by snake")
			p=2
		elif(p==13):
			print("congrats u can climb the ladder")
			p=34
		elif(p==25):
			print("oops sry u r bite by snake")
			p=4
		elif(p==38):
			print("oops sry u r bite by snake")
			p=9
		elif(p==40):
			print("congrats u can climb the ladder")
		elif(p==52):
			print("congrats u can climb the ladder")
			p=81
		elif(p==65):
			print("oops sry u r bite by snake")
			p=46
		elif(p==76):
			print("congrats u can climb the ladder")
			p=97
		elif(p==89):
			print("oops sry u r bite by snake")
			p=70
		elif(p==93):
			print("oops sry u r bite by snake")
			p=64
		elif(p>=100):
			p=p-a
			print("congrats u won the game")
		if(a=='q'):
			print("bye")
			exit()





