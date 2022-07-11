# Uses python3
import sys

def get_change(n):
    numCoins = 0
    numOnes = 0
    numFives = 0
    numTens = 0
    
    
    while (n >= 0):
    	
    	#useage of tens
    	numTens = n/10
    	n = n % 10
    	
    	#useage of fives
    	numFives = n/5
    	n = n % 5
    	
    	#useage of ones
    	numOnes = n/1
    	n = n % 1
    
    numCoins = numOnes + numFives + numTens
    
    return numCoins

if __name__ == '__main__':
	n = int(input())
	print(get_change(n))

