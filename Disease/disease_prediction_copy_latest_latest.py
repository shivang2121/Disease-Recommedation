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
from tkinter import *
from tkinter import messagebox
from tkinter import messagebox

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
data2.columns = data2.iloc[0]
data2 = data2[1:]
list_diseases=[]
for i in range(0,len(data2)):
    list_diseases.append(i)
d2 = pd.DataFrame(list_diseases)    
Y1= d2.iloc[:,0].values
X1=data2.iloc[:,0:1866].values
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X1,Y1,test_size=0.2)


symptoms=symptoms
l2=[]
for x in range(0,len(symptoms)):
    l2.append(0)

def message():
    if (Symptom1.get() == "None" and  Symptom2.get() == "None" and Symptom3.get() == "None" and Symptom4.get() == "None" and Symptom5.get() == "None"):
        messagebox.showinfo("ENTER SYMPTOMS")
    else :
        NaiveBayes()

def NaiveBayes():
    from sklearn.ensemble import RandomForestClassifier
    gnb= RandomForestClassifier(n_estimators = 10, criterion = 'entropy', random_state = 0)
    gnb.fit(X_train,np.ravel(y_train))
    from sklearn.metrics import accuracy_score
    y_pred = gnb.predict(X_test)
    print(y_pred)
    print(accuracy_score(y_test, y_pred))
    print(accuracy_score(y_test, y_pred, normalize=False))

    psymptoms = [Symptom1.get(),Symptom2.get(),Symptom3.get(),Symptom4.get(),Symptom5.get()]

    for k in range(0,len(symptoms)):
        for z in psymptoms:
            if(z==symptoms[k]):
                l2[k]=1

    inputtest = [l2]
    predict = gnb.predict(inputtest)
    predicted=predict[0]

    h='no'
    for a in range(0,len(diseases)):
        if(diseases[predicted] == diseases[a]):
            h='yes'
            break

    if (h=='yes'):
        t3.delete("1.0", END)
        t3.insert(END, diseases[a])
    else:
        t3.delete("1.0", END)
        t3.insert(END, "No Disease")
       
# Tinker
root = Tk()
root.title(" Disease Prediction From Symptoms")
root.configure()

Symptom1 = StringVar()
Symptom1.set(None)
Symptom2 = StringVar()
Symptom2.set(None)
Symptom3 = StringVar()
Symptom3.set(None)
Symptom4 = StringVar()
Symptom4.set(None)
Symptom5 = StringVar()
Symptom5.set(None)

w2 = Label(root, justify=LEFT, text=" Disease Prediction using Symptoms ")
w2.config(font=("Elephant", 30))
w2.grid(row=1, column=0, columnspan=2, padx=100)

NameLb1 = Label(root, text="")
NameLb1.config(font=("Elephant", 20))
NameLb1.grid(row=5, column=1, pady=10,  sticky=W)

S1Lb = Label(root,  text="Symptom 1")
S1Lb.config(font=("Elephant", 15))
S1Lb.grid(row=7, column=1, pady=10 , sticky=W)

S2Lb = Label(root,  text="Symptom 2")
S2Lb.config(font=("Elephant", 15))
S2Lb.grid(row=8, column=1, pady=10, sticky=W)

S3Lb = Label(root,  text="Symptom 3")
S3Lb.config(font=("Elephant", 15))
S3Lb.grid(row=9, column=1, pady=10, sticky=W)

S4Lb = Label(root,  text="Symptom 4")
S4Lb.config(font=("Elephant", 15))
S4Lb.grid(row=10, column=1, pady=10, sticky=W)

S5Lb = Label(root,  text="Symptom 5")
S5Lb.config(font=("Elephant", 15))
S5Lb.grid(row=11, column=1, pady=10, sticky=W)

lr = Button(root, text="Predict",height=2, width=20, command=message)
lr.config(font=("Elephant", 15))
lr.grid(row=15, column=1,pady=20)

OPTIONS = (symptoms)

S1En = OptionMenu(root, Symptom1,*OPTIONS)
S1En.grid(row=7, column=2)

S2En = OptionMenu(root, Symptom2,*OPTIONS)
S2En.grid(row=8, column=2)

S3En = OptionMenu(root, Symptom3,*OPTIONS)
S3En.grid(row=9, column=2)

S4En = OptionMenu(root, Symptom4,*OPTIONS)
S4En.grid(row=10, column=2)

S5En = OptionMenu(root, Symptom5,*OPTIONS)
S5En.grid(row=11, column=2)

NameLb = Label(root, text="")
NameLb.config(font=("Elephant", 20))
NameLb.grid(row=13, column=1, pady=10,  sticky=W)

NameLb = Label(root, text="")
NameLb.config(font=("Elephant", 15))
NameLb.grid(row=18, column=1, pady=10,  sticky=W)

t3 = Text(root, height=2, width=30)
t3.config(font=("Elephant", 20))
t3.grid(row=20, column=1 , padx=10)

root.mainloop()
