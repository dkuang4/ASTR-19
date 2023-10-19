#this program is for Code Journal 1, prompt 3

#define a function f(x)
def f(x):
	return x**3 + 8 #returns a value when f(x) is called

#define main function of program
def main():
	#print result
	print(f(9))

	#an if statement that executes if f(9)>27
	if f(9) > 27:
		print('YAY!')

#execute main function
if __name__ == "__main__":
	main()