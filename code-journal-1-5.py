#This program is for Code Journal 1, prompt 5

#import libraries
import numpy as np
from astropy.table import Table

#main function of the program
def main():
	#define two arrays to make a table
	x = np.linspace(0, 2*np.pi, 1000)
	y = np.sin(x)

	#create a table
	sine_table = Table([x,y], names = ['x', 'sin(x)'])

	#print table
	print(sine_table)

if __name__ == "__main__":
	main()