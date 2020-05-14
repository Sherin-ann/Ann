#usage python3 weight_charge.py

#function definition
def weight(s):
    s = s.upper()
    weights = {'A': 71.04, 'C': 103.01, 'D': 115.03, 'E': 129.04, 'F': 147.07,
       'G': 57.02, 'H': 137.06, 'I': 113.08, 'K': 128.09, 'L': 113.08,
       'M': 131.04, 'N': 114.04, 'P': 97.05, 'Q': 128.06, 'R': 156.10,
       'S': 87.03, 'T': 101.05, 'V': 99.07, 'W': 186.08, 'Y': 163.06 }

    wt = sum(weights[i] for i in s)
    print("\nWeight of the protein: ")
    print(round(wt,4))

def charge(s):
    s = s.upper()
    charge = 0
    polar = {"C":-.045,"D":-.999,"E":-.998,"H":.091,"K":1,"R":1,"Y":-.001}
   
    for x in s:
        charge += polar.get(x,0)
    print("\nCharge of the protein:")
    print(round(charge,4))
 
#Input protein sequence
s = input("Enter protein sequence: ")
#function call
weight(s)
charge(s)

