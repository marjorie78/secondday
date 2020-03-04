
while True:

try:
	gross=input("How much are you making?")
	gross=int(gross)
	tax=0
	if gross<1000:
		tax=0.1
	elif gross<2000:
		tax=0.11
	elif gross<4000:
		tax=0.12
	else:
		tax=0.14
	kids=input("How many kids do you know to have?")
	kids=int(kids)
	ifgross<2000:
		tax=tax-kids*0.01
	else:
		tax=tax-kids*0.005
	net=gross*(1-tax)
	print("you take home",net,"euros")
except:
	print("give me a number")
