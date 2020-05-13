#usage python3 classification.py

#function to identify which category the amino acid fall in
def classify(a):
a = a.capitalize()
if(a == 'Alanine' or a == 'Isoleucine' or a == 'Leucine' or a == 'Methionine' or a == 'Phenylalanine' or a == 'Valine' or a == 'Proline' or a == 'Glycine' or a == 'Tryptophan'):
		print("Non-polar and neutral")
	
	elif(a == 'Glutamine' or a == 'Asparagine' or a == 'Cysteine' or a == 'Tyrosine' or a == 'Threonine' or a == 'Serine'):
		print("Polar and neutral")

	elif(a == 'Arginine' or a == 'Lysine' or a == 'Histidine'):
		print("Basic and polar")
    
	elif(a == 'Aspartic acid' or a == 'Glutamic acid'):
		print("Acidic and polar")
    
	else:
		print("Please select from the drop-down list.")
    
#input protein sequence
a = input('Enter amino acid name: ")
#function call
classify(a)
