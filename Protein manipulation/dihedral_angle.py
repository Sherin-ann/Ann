#usage python3 dihedral_angle.py
import numpy as np
import math
import os

os.system("clear")
a=[]; b=[]; c=[]; d=[]

print("\n------Torsion Angle Calculation------\n")

#function for taking x,y,z cordinates of 4 points a,b,c,d
def list_def(n):
	for i in range(0, 3): 
		elements = float(input()) 
		n.append(elements)
	return n
print("Enter cordinates of a:")
list_def(a)
print("Enter cordinates of b:")
list_def(b)
print("Enter cordinates of c:")
list_def(c)
print("Enter cordinates of d:")
list_def(d)

#print the cordinates of a,b,c,d on screen
print("\nX,Y,Z cordinates of a are:\n",a)
print("X,Y,Z cordinates of b are:\n",b)
print("X,Y,Z cordinates of c are:\n",c)
print("X,Y,Z cordinates of d are:\n",d)

#vector calculation and finding normal to the planes
ba = np.subtract(a,b)
bc = np.subtract(c,b)
bd = np.subtract(d,b)

q1=np.around(np.cross(bc,ba),3)
q2=np.around(np.cross(bc,bd),3)
dp=np.dot(q1,q2)

q4=round(np.sqrt(q1[0]**2 + q1[1]**2 + q1[2]**2),3)
q5=round(np.sqrt(q2[0]**2 + q2[1]**2 + q2[2]**2),3)
ta1 = (dp/(q4*q5))

ta = math.degrees(math.acos(ta1))
q3 = np.cross(q1,q2)
dot = np.dot(q3,bc)

#degree symbol
deg=u"\u00b0"

if(dot < 0):
    print("\nThe value of torsion angle is: ", round(-ta,3), deg, sep='')
else:
    print("\nThe value of torsion angle is: ",round(ta,3), deg, sep='')
print("\n")

#default values
#a = [11.453, 17.324, 11.284], b = [13.744, 18.237, 10.881], c = [12.724, 17.274, 10.444], d = [13.204, 16.528, 9.234]
