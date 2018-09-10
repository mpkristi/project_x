def check_multiple(number, multiple):
	if (number%multiple)==0:
		return True
	else:
		return False

def print_fizz():
	print("fizz")

def print_buzz():
	print("buzz")

def print_number(number):
	print(number)

def counting(start,end,multiple1,multiple2):
	for i in range(start,end+1):
		if(check_multiple(i,multiple1)):
			print_fizz()
		elif(check_multiple(i,multiple2)):
			print_buzz()
		else:
			print_number(i)

def fizzbuzz():
	start = input("Startpoint: ")
	end = input("Endpoint: ")
	multiple1 = input("Fizz-multiple: ")
	multiple2 = input("Buzz-multiple: ")
	counting(start,end,multiple1,multiple2)


def main():
	fizzbuzz()

main()
