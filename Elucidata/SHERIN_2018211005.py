#import libraries
import numpy as np
import csv
import pandas as pd
import os
os.system("clear")

with open("gene_data_anomaly.csv", 'r') as f:		#read file
	genes = list(csv.reader(f, delimiter=","))
genes = np.array(genes)
#print(genes.shape)
data5=[]
data6=[]
#save headers of rows and columns
for i in range(1,22384):
	data5.append(genes[i][0])
col_head=data5
for j in range(31):
	data6.append(genes[0][j])
row_head=data6

data1 = []
for i in range(1,22384):
	data=[]
	new1 = []
	for j in range(1,31,3):
		
		data2=[]
		data3=[]
		for k in range(3):			#read the data in three sets
			if genes[i][j+k] == "":
				data2.append(0.0)
			else:
				data3.append(float(genes[i][j+k]))
			
		#conditions for filling the missing data	
		if (len(data2) == 3):
			continue
		elif (len(data2) == 2):
			data2[0]=data3[0]
			data2[1]=data3[0]
			data.append(float(data2[0]))
			data.append(float(data2[1]))
			data.append(float(data3[0]))
		elif (len(data2) ==1):
			data2=(sum(data3)/len(data3))
			for k in range(3):
				# print(i,j+k)
				if genes[i][j+k] == "":
					data.append(float(data2))
				else:
					data.append(float(genes[i][j+k]))
				
		else:
			data.append(float(data3[0]))
			data.append(float(data3[1]))
			data.append(float(data3[2]))
			
	
	data1.append(list(data))
# print(data1)
with open("result.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerow(row_head)    
    writer.writerows(col_head[i:i+1] + list(row) for i, row in enumerate(data1))

#final file with first row first column as empty
new1 = pd.read_csv("result.csv")
new1_data = new1.dropna(axis = 0, how ='any') 
#new1_data.columns = ['' if x=='symbol' else x for x in new1_data.columns]
new1_data.to_csv('SHERIN_2018211005.csv', index=False) 
os.remove("result.csv")

#PART 2
new2 = pd.read_csv("SHERIN_2018211005.csv") #read the cleaned data
new2_data = pd.DataFrame(new2)
cols = [0,10,11,12,25,26,27]
new2_data = new2_data[new2_data.columns[cols]]
# print(new2_data)
new2_data.to_csv('new2.csv', index=False) 

with open("new2.csv", 'r') as f:		#read file with 0hrs and 12 hrs data
	genes = list(csv.reader(f, delimiter=","))
genes = np.array(genes)

data_mean=[]
for i in range(1,22165):
	data0=[]
	for j in range(1,7,3):
		data3=[]
		
		for k in range(3):			#read the data in three sets
			data3.append(float(genes[i][j+k]))
		#print(data3)
		data3_mean = float(sum(data3)/len(data3))
		data0.append(float(data3_mean))
		#print(data0)
	data_mean.append(data0)		#calculate the means and append to a new file
#print(data_mean)
data5=[]
data6=[]
#save headers of rows and columns
for i in range(1,22165):
	data5.append(genes[i][0])
col_head=data5
row_head=['symbol','mean1','mean2']
with open("result.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerow(row_head)    
    writer.writerows(col_head[i:i+1] + list(row) for i, row in enumerate(data_mean))

with open("result.csv", 'r') as f:		#read file
	genes = list(csv.reader(f, delimiter=","))
genes = np.array(genes)
data1=[]
for i in range(1,22165):
	data=[]
	for j in range(1,3,2):
		diff = abs(float(genes[i][j])-float(genes[i][j+1]))
		data.append(diff)
	data1.append(data)
#print(data1)
data5=[]
data6=[]
for i in range(1,22165):
	data5.append(genes[i][0])
col_head=data5
row_head=['symbol','diff']
with open("result_new.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerow(row_head)    
    writer.writerows(col_head[i:i+1] + list(row) for i, row in enumerate(data1))

#get the rows with maximum difference
df = pd.read_csv('result_new.csv')
df = df.sort_values(by ='diff',ascending=False )
df.to_csv('final_result.csv', index=False) 

df1 = pd.read_csv('final_result.csv')
df0=df1['symbol']
df2=df0.head(100)
#send the output to txt file
df2.to_string('SHERIN_2018211005.txt', index=False)
#remove meta files generated
os.remove("final_result.csv")
os.remove("new2.csv")
os.remove("result.csv")
os.remove("result_new.csv")
#remove first row first column of csv file
new1_rem = pd.read_csv("SHERIN_2018211005.csv")
new1_rem.columns = ['' if x=='symbol' else x for x in new1_rem.columns]
new1_rem.to_csv('SHERIN_2018211005.csv', index=False) 
print("The required SHERIN_2018211005.csv and SHERIN_2018211005.txt files have been generated!")




