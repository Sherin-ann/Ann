#usage python3 gc_count.py

#function definition
def GCCount(s):
    s = s.upper()
    count_G = s.count('G') 
    count_C = s.count('C')
    #count_GC = s.count('CG')   CG dinucleotide count
    GC = ((count_G + count_C) / float(len(s))) * 100
    print("\nGC Content is: %.4f" %GC,"%")

#Input sequence
s = input("Enter your sequence: ")

#call function
GCCount(s)
