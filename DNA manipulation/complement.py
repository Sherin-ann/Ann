#usage python3 complement.py

#Function definition
def complement(s):
	s = s.upper()
	a=''
	print("\nComplementary DNA sequence:")
	complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'} 
	for i in s:
		a += complement[i] 
	print(a)

#input sequence
s = input("Enter your sequence: ")

#call function
complement(s)
