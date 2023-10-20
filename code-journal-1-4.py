#this program is for Code Journal 1, prompt 4
#if run with no command line arguments, the default is penguins
#otherwise, any animal's info can be passed :D

#import system library
import sys

#declare a class
class animal:
	#define physical parameters of animal

	#initialize function
	def __init__(self, anname="penguin", wingspan=203., legs=22.3, eyes=2, tail=True, fur=False):
		#data members to pass arguments thru involving parameters
		self.name = anname
		self.wing_len = wingspan
		self.leg_len = legs
		self.eye_num = eyes
		self.tail_bool = tail
		self.fur_bool = fur

	#define a function to print
	def printInfo(self):
		print(f"My favorite animals are {self.name}(s).")
		print("Here are their physical characteristics:")
		print(f"Their arm/wingspan can be about {self.wing_len} cm wide,")
		print(f"their legs can be about {self.leg_len} cm long,")
		print(f"they have {self.eye_num} eyes,")

		if self.tail_bool == True:
			print("a tail,")
		else:
			print("do not have a tail,")

		if self.fur_bool == True:
			print("and fur!")
		else:
			print("and no fur!")

#main function of the program
def main():
	#set default values
	anname = "penguin"
	wingspan = 203.
	legs = 22.3
	eyes = 2
	tail = True
	fur = False

	#if command line arguments exist (besides program name),
	#set prev. defined variables to argument values
	if len(sys.argv)>=2:
		anname = str(sys.argv[1])

	if len(sys.argv)>=3:
		wingspan = float(sys.argv[2])

	if len(sys.argv)>=4:
		legs = float(sys.argv[3])

	if len(sys.argv)>=5:
		eyes = int(sys.argv[4])

	if len(sys.argv)>=6:
		tail = sys.argv[5]

	if len(sys.argv)>=7:
		fur = sys.argv[6]

	#initialize the class
	fav_animal = animal(anname=anname, wingspan=wingspan, legs=legs, eyes=eyes, tail=tail, fur=fur)

	#print the info
	fav_animal.printInfo()

#run the main function
if __name__ == "__main__":
	main()