# -*- coding: utf-8 -*-
"""
Created on Sat Oct 30 21:48:44 2021

@author: PS
"""
#pip install tabulate
#import libraries
import pandas as pd 
import numpy as np
import math
from tabulate import tabulate

#import disease with dataset
data=pd.read_csv(r"Disease.csv",encoding= 'unicode_escape',error_bad_lines=False,header=None)

#get indexes of all diseases
list_indexes_diseases=[]
for i in range (0,len(data)):
    disease_temp2=data.iloc[[i],0].values
    disease_temp2=str(disease_temp2) 
    if((disease_temp2)=="[nan]"):
        pass
    else:
        list_indexes_diseases.append(i)
        
#append a list of all diseases   
diseases_list=[]
for j in range(0,len(list_indexes_diseases)):
        diseases_index=list_indexes_diseases[j]
        diseases=data.iloc[[diseases_index],0].values
        diseases=str(diseases)
        #remove the numbers
        diseases=diseases[16:-2]
        diseases_list.append(diseases)
    
#clean values like / and ^ etc
disease_list_cleaned=[]
for k in range(0,len(diseases_list)):

   disease_list_df = pd.DataFrame(diseases_list)
   diseases=disease_list_df.iloc[[k],0].values
   diseases=str(diseases)
   ind3=diseases.find('\\')
   if(k==90):
       diseases="['candidiasis oral']"
       disease_list_cleaned.append(diseases)
       continue
   if(ind3!=-1):
       ind4=diseases.find('0')
       start = ind3
       stop = ind4
       # Remove charactes from ind 1 to ind2
      
       diseases = diseases[0: start:] + " " + diseases[stop + 1::]
   ind1=diseases.find('^')
   if(ind1!=-1):
       ind2=diseases.find('_')
       start = ind1
       stop = ind2
       # Remove charactes from index ind 1 to ind 2
      
       diseases = diseases[0: start:] + " " + diseases[stop + 1::]
   ind1=diseases.find('^')
   if(ind1!=-1):
       ind2=diseases.find('_')
       start = ind1
       stop = ind2
       # Remove charactes from ind 1 to ind 2
       diseases = diseases[0: start:] + " " + diseases[stop + 1::]
   ind3=diseases.find('\\')
   if(ind3!=-1):
       ind4=diseases.find('0')
       start = ind3
       stop = ind4
       # Remove charactes from ind1 to ind 2
      
       diseases = diseases[0: start:] + " " + diseases[stop + 1::]
   
   ind3=diseases.find('\\')
   if(ind3!=-1):
       ind4=diseases.find('0')
       start = ind3
       stop = ind4
       # Remove charactes from ind 1 to ind2
      
       diseases = diseases[0: start:] + " " + diseases[stop + 1::]
   ind3=diseases.find('[')
   if(ind3!=-1):
       ind4=diseases.find(']')
       start = ind3
       stop = ind4
       # Remove charactes from ind 1 to ind2
      
       diseases = diseases[start+1: stop:]
       diseases=diseases[1:-1]
   disease_list_cleaned.append(diseases)
diseases=disease_list_cleaned

#append all the symptoms
symptoms_list=[]
for j in range(0,len(data)):
        symptoms=data.iloc[[j],2].values
        symptoms=str(symptoms)
        #remove the numbers
        symptoms=symptoms[16:-2]
        symptoms_list.append(symptoms)
#clean the symptoms list  remove ^ _ etc
symptoms_list_cleaned=[]
symptoms_list=symptoms_list[0:-1]
for m in range(0,len(symptoms_list)):
   symptoms_list_df = pd.DataFrame(symptoms_list)
   symptoms=symptoms_list_df.iloc[[m],0].values
   symptoms=str(symptoms)
   ind1=symptoms.find('^')
   if(ind1!=-1):
       ind2=symptoms.find('_')
       start = ind1
       stop = ind2
       # Remove charactes from ind 1 to ind 2
       symptoms = symptoms[0: start:] + " " + symptoms[stop + 1::]
   ind1=symptoms.find('^')
   if(ind1!=-1):
       ind2=symptoms.find('_')
       start = ind1
       stop = ind2
       # Remove charactes from ind 1 to ind 2
       symptoms = symptoms[0: start:] + " " + symptoms[stop + 1::]
   ind1=symptoms.find('\\')
   if(ind1!=-1):
       ind2=symptoms.find('0')
       start = ind1
       stop = ind2
       # Remove charactes from ind 1 to ind 2
       symptoms = symptoms[0: start:] + " " + symptoms[stop + 1::]
   ind1=symptoms.find('\\')
   if(ind1!=-1):
       ind2=symptoms.find('0')
       start = ind1
       stop = ind2
       # Remove charactes from ind 1 to ind 2
       symptoms = symptoms[0: start:] + " " + symptoms[stop + 1::]
   ind3=symptoms.find('[')
   if(ind3!=-1):
       ind4=symptoms.find(']')
       start = ind3
       stop = ind4
       # Remove charactes from ind 1 to ind2
      
       symptoms = symptoms[start+1: stop:]
       symptoms=symptoms[1:-1]
   symptoms_list_cleaned.append(symptoms)
symptoms=symptoms_list_cleaned

#save data in text file and csv  
'''
with open("symptoms2.txt", "w") as output:
    output.write(str(symptoms))
with open("diseases2.txt", "w") as output:
    output.write(str(diseases))

k=0;
dff=pd.DataFrame(diseases)
dff.to_csv('GFG4.csv')
 dff=pd.DataFrame(symptoms)
dff.to_csv('GFG3.csv')
'''
#input sparse matrix
data2=pd.read_csv(r"Disease_list_new.csv",encoding= 'unicode_escape',error_bad_lines=False,header=None)    
#fill in sparse matrix with corresponding 1s and 0s
k=0;
for i in range(1,len(data2)-1):
    indexes=list_indexes_diseases[k]
    indexes2=list_indexes_diseases[k+1]
    for j in range(indexes,indexes2):
        data2.at[i,j] = 1
    if(k<132):
        k+=1
#fill in last row
data2.at[134,1863] = 1
data2.at[134,1864] = 1
data2.at[134,1865] = 1 
        