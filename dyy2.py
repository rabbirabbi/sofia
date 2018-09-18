
#write a programme to roll a die
#command random
import random
#use while loop
while True:
	r=input("press  y or n :")
#use if else statement give the conditions	
	if(r=='y'):
		print(random.randint(1,6))
		exit()
	else:
    	 print("quit")
    	 
