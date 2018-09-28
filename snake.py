#write a programm to play snake and ladder
import random 
p=0
#use while loop and add the conditions
while(p<=100):
#roll a die 	
	a=input("enter r or q:")
	if(a=='r'):
		r=(random.randint(1,6))
		p=p+r
#print position and number in dice		
		print("my position:",p)
		print("num in dice:",r)
#position of snakes and ladders 
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
#limit of the game is 100
		elif(p>=100):
			p=p-r
			print("congrats u won the game")
#to quit			
		if(a=='q'):
			print("bye")
			exit()





