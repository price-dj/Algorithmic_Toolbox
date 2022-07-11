import unittest
import random


seq = [2,3,9,2,9]

def merge_sort(seq):
	"""Accepts a mutable sequence. Utilizes merge_sort to sort in place, return
	a sorted sequence"""
	if len(seq) == 1:
		return seq
	else:
        #recursion: break sequence down into chunks of 1
		mid = len(seq)//2
		left = merge_sort(seq[:mid])
		right = merge_sort(seq[mid:])

		i, j, k = 0, 0, 0 #i= left counter, j= right counter, k= master counter
		
		inversions = 0
		
        #run until left or right is out
		while i < len(left) and j < len(right):
            #if current left val is < current right val; assign to master list
			if left[i] < right[j]:
				seq[k] = left[i]
				i += 1; k += 1
            #else assign right to master
			else:
				seq[k] = right[j]
				j += 1; k += 1
				

        #handle remaining items in remaining list
		remaining = left if i < j else right
		r = i if remaining == left else j

		while r < len(remaining):
			seq[k] = remaining[r]
			r += 1; k += 1

		return (seq)

#class test_mergesort(unittest.TestCase):
    #def test_mergesort(self):
        #test = [random.randrange(0, 10000) for _ in range(2000)]
        #self.assertEqual(merge_sort(test), sorted(test))

#if __name__ == '__main__':
    #unittest.main()
    
    
merge_sort(seq)
print(seq)
