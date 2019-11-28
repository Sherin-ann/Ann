#!/usr/bin/python3
#########################################################################
##    Author: Sherin Ann Eapen                                         ##
##    Program to convert spoken english to written english             ##
#########################################################################

def rules():
    fullform = {
	    "num":{"zero": 0, "one" : 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10, "twenty": 20, "thirty":30, "forty": 40, "fifty":50,"sixty":60,"seventy":70,"eighty":80,"ninety":90,"hundred":100
                  },
            "tup": { "single":1, "double":2, "triple":3, "quadruple":4 
		   },
                         
            "abbre": { "C M": "CM", "P M": "PM", "A M": "AM" 
		     },
            "currency": {
                          "dollar": "$","dollars": "$", "percent": "%" ,"rupees" : "₹","rupee" : "₹", "euros":"€"
                        }
            
                }
    return fullform

def para_convert():
        fullform=rules()

        para=input("\n\tEnter the paragraph you wish to convert: \n")	#enter the paragraph 
        words = para.split(" ")						#store each word in a list
        num=fullform['num']
        tup=fullform['tup']
        abbre=fullform['abbre']
        curr=fullform['currency']
        length_para=len(words)						#length of paragraph

        print("\n\tHere is your spoken to written english paragraph: \n")
        i=0                                                             #counter for the loop

        while i<length_para:						#convert the paragraph usings the rules defined in the function rules()
                if i+1 != length_para:
                        if (words[i].lower()) in tup.keys() and (len(words[i+1])==1):
                                print((words[i+1])*tup[words[i].lower()], end=" ")
                                i=i+2
                        elif words[i].lower() in num.keys() and (words[i+1] in curr.keys()):
                                print(curr[words[i+1]]+str(num[words[i].lower()]), end=" ")
                                i=i+2
                        elif ((words[i]+" "+words[i+1]) in abbre.keys()):
                                print((words[i]+words[i+1]), end =" ")
                                i+=2
                        else:
                                print(words[i], end=" ")
                                i=i+1
                else:
                        print(words[i], end=" ")
                        i=i+1
        print("\n")



