from bert_serving.client import BertClient
import tensorflow as tf
import numpy as np
import os
import pandas as pd
import time
import progressbar

bc = BertClient()  # ip address of the GPU machine

dir_name = "/Users/jaswanttummala/downloads/questions.csv"
question1 = np.array(pd.read_csv(dir_name, usecols=["question1"]))
question2 = np.array(pd.read_csv(dir_name, usecols=["question2"]))
question1 = question1.tolist()
question2 = question2.tolist()
temp1= []
temp2= []
for i in range(len(question1)):
    temp1.append(str(question1[i][0]))
    temp2.append(str(question2[i][0]))

temp1.append("")
temp2.append("")

def divide_chunks(l, n): 
      
    # looping till length l 
    for i in range(0, len(l), n):  
        yield l[i:i + n] 
  
# How many elements each 
# list should have 
n = 6318
question1 = list(divide_chunks(temp1, n))
question2 = list(divide_chunks(temp2, n))

for i in len(question1):
    x = bc.encode(question1[i])
    pd.DataFrame(x).to_csv("/home/josh_tummala/question1" + str(i) + ".csv")
    print()
    print(i)
    print(1)
    print()
for i in len(question2):
    x = bc.encode(question2[i])
    pd.DataFrame(x).to_csv("/home/josh_tummala/question2" + str(i) + ".csv")
    print()
    print(i)
    print(2)
    print()
