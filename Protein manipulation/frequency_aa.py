#usage python3 frequency_aa.py
def freq():
	s = s.lower(s)
	l = len(s)
  c_m = s.count('m')
  c_v = s.count('v')
  c_i = s.count('i')
  c_l = s.count('l')
  c_k = s.count('k')
  c_r = s.count('r')
  c_h = s.count('h')
  c_d = s.count('d')
  c_e = s.count('e')
  c_n = s.count('n')
  c_p = s.count('p')
  c_f = s.count('f')
  c_g = s.count('g')
  c_a = s.count('a')
  c_y = s.count('y')
  c_w = s.count('w')
  c_c = s.count('c')
  c_s = s.count('s')
  c_t = s.count('t')
  c_q = s.count('q')
  
	print("\nAmino Acid\t Frequency\n")
	print("Methione\t",round(c_m/l,4))
	print("Valine\t\t",round(c_v/l,4))
	print("Isoleucine\t",round(c_i/l,4))
	print("Leucine\t\t",round(c_l/l,4))
	print("Lysine\t\t",round(c_k/l,4))
	print("Arginine\t",round(c_r/l,4))
	print("Histidine\t",round(c_h/l,4))
	print("Aspartic acid\t",round(c_d/l,4))
	print("Glutamic acid\t",round(c_e/l,4))
	print("Asparagine\t",round(c_n/l,4))
	print("Glutamine\t",round(c_q/l,4))
	print("Threonine\t",round(c_t/l,4))
	print("Serine\t\t",round(c_s/l,4))
	print("Cysteine\t",round(c_c/l,4))
	print("Tryptophan\t",round(c_w/l,4))
	print("Tyrosine\t",round(c_y/l,4))
	print("Alanine\t\t",round(c_a/l,4))
	print("Glycine\t\t",round(c_g/l,4))
	print("Phenylalanine\t",round(c_f/l,4))
	print("Proline\t\t",round(c_p/l,4))
  
#Input protein sequence
s = input("Enter protein sequence: ")
#call function
freq(s) 
