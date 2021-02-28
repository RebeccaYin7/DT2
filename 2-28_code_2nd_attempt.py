# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 21:53:25 2021

@author: siptest
"""

import random
import decimal
import numpy as np
import matplotlib.pyplot as plt


#percentage above normal 
Act_level = 0.05 

flow_rate = input("What is the baseline flow rate?")
hypoxic_state = 90


def flow_algorithm(): 
    outputs = []
    
    flow_rate = input("What is the baseline flow rate?")
    flow_rate = int(flow_rate)
    data = np.genfromtxt('C:/Users/siptest/Desktop/DT2/dataVals.csv', delimiter = ',')
    plt.plot(data)
    plt.xlabel("Time ")
    plt.ylabel("SpO2 Input")
    plt.title("SpO2 Input vs. Time")
    plt.savefig('C:/Users/siptest/Desktop/DT2/dataVals.jpg', transparent=True)
    for current_O2 in data: 
        flow_rate = 0 
        if(current_O2 < hypoxic_state - 3): 
            print("Alert: Hypoxic State!")
            flow_rate += 1
        elif (current_O2 < hypoxic_state): 
            print("Alert: Hypoxic State!")
            flow_rate += 0.5 
        elif (current_O2 > hypoxic_state + 3): 
            flow_rate -= 1
        elif (current_O2 > hypoxic_state): 
            flow_rate -= 0.5 
        outputs.append(flow_rate)
    np.savetxt("C:/Users/siptest/Desktop/DT2/Response.csv", outputs, delimiter = ',')
    #send newFlow to machine

def sim_data(): 
    random_start = random.randint(85,94)
    data_values = []
    for i in range(100): 
        rand_change = random.randint(-5, 5)
        temp_data = random_start + rand_change
        data_values.append(temp_data)
    np.savetxt('C:/Users/siptest/Desktop/DT2/dataVals.csv',
               data_values, delimiter=',')

sim_data()
flow_algorithm()
plt.figure()
response = np.genfromtxt("C:/Users/siptest/Desktop/DT2/Response.csv", delimiter = ',')
plt.plot(response) 
plt.xlabel("Time")
plt.ylabel("Change in Flow Rate") 
plt.title("Change in Flow Rate vs. Time")
plt.savefig('C:/Users/siptest/Desktop/DT2/Response.jpg', transparent=True)
