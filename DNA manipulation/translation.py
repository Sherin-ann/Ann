#usage python3 translation.py

#Fuction for translation: DNA to protein 
def translate(s):
	s = s.upper()
	codon = { 'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M', 'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L', 'TTA':'L', 'TTG':'L', 'GTA':'V', 'GTC':'V','GTG':'V', 'GTT':'V', 'TTC':'F', 'TTT':'F', 'TGC':'C', 'TGT':'C', 'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A', 'GGA':'G', 'GGC':'G', 
	'GGG':'G', 'GGT':'G', 'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P', 'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T', 'AGC':'S', 'AGT':'S',
	'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S', 'TAC':'Y', 'TAT':'Y', 'TGG':'W', 'CAA':'Q', 'CAG':'Q', 'AAC':'N', 'AAT':'N', 'CAC':'H', 
	'CAT':'H', 'GAA':'E', 'GAG':'E', 'GAC':'D', 'GAT':'D', 'AAA':'K', 'AAG':'K', 'AGA':'R', 'AGG':'R', 'CGA':'R', 'CGC':'R', 'CGG':'R', 		'CGT':'R', 'TAA':'-', 'TAG':'-', 'TGA':'-'}
	seq1=""
	if len(s)%3 == 0:
		for i in range(0, len(s), 3): 
		    c = s[i:i + 3] 
		    seq1 += codon[c]
		print("\nTranslated sequence:") 
		print(seq1,"\n")
	else:
		print("Error! Enter valid sequence whose length is a multiple of 3!")

#Input DNA sequence
s = input("Enter your sequence: ")

#Call function
translate(s)
