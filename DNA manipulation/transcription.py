#usage python3 transcription.py

#Function for transcription - DNA to mRNA
def transcript(s):
    s = s.upper()   
    print("\nSequence after Transcription:")
    print(s.replace('T','U'))

#Input DNA sequence
s = input("Enter your sequence: ")
   
#call the function
transcript(s) 
