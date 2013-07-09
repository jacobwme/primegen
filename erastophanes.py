#!/usr/bin/env python3
import math
import time

class erastophanes:
	# Initialize the sieve
	def __init__(self,ceiling):
		# List for discovered primes
		self.plist                 = []
		# Map of integer range to sieve
		self.pmap                  = [True] * ceiling
		# Mark 0 and 1 not prime
		self.pmap[0], self.pmap[1] = False, False
		# Start with a floor of 0
		self.floor                 = 0
		# Sieve for primes and append them to the prime list
		for i in self.sieve(ceiling):
			self.plist.append(i)
		# Update the floor
		self.floor = ceiling
	# Sieve the pmap, using an enumeration starting from self.floor
	# 1,1 if the floor is 1, 100,100 if the floor is 100, etc 
	def sieve(self,ceiling):
		for i, j in enumerate(self.pmap,start=self.floor):
			if j:
				yield i
				for k in range(i*i,ceiling,i):
						self.pmap[k-self.floor] = False
	# Expand the sieve, generate a new pmap and remove composites of primes in plist
	def expand(self,ceiling):
		self.pmap = [True] * (ceiling-self.floor)
		for i in self.plist:
			if i * i < ceiling:
				# Find the lowest multiple of i above self.floor
				j = int(math.ceil(self.floor/i))
				# Iterate through mutliples of i from self.floor to ceiling
				for k in range(i*j,ceiling,i):
					if k < self.floor:
						# Pass this iteration if k is less than self.floor
						pass
					else:
						# Mark the pmap index not prime
						self.pmap[(i*j)-self.floor] = False
					j = j + 1
		# Sieve for primes and append them to the prime list
		for i in self.sieve(ceiling):
			self.plist.append(i)
		# Update the floor
		self.floor = ceiling
	
if __name__ == '__main__':
	# Start the timer
	startTime = time.time()
	# Initialize the sieve with a ceiling of 1000000
	test = erastophanes(1000000)
	i = sum(test.plist)
	thisTime = time.time() - startTime
	print("The primes under 1000000 sum to {sum}, time elapsed is {time}".format(sum=i,time=thisTime))
	for i in range(2000000,2001000000,1000000):
		test.expand(i)
		j = sum(test.plist)
		thisTime = time.time() - startTime
		print("The primes under {ceiling} sum to {sum}, time elapsed is {time}".format(ceiling=i,sum=j,time=thisTime))
