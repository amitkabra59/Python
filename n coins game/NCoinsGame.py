
def winner(n, A, B):
	if((n-1)%6 == 0):
		print B, " is the winner"
	else:
		print A, " is the winner"
		
def main():
	n = input("enter the number of coins :")
	first = input("enter the name of the player who starts the game :")
	second = input("enter the name of the 2nd player :")
	winner(n, first, second)
		
main()
