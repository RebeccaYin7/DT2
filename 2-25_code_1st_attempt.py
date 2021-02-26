# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 21:53:25 2021

@author: siptest
"""

import random
import numpy as np
import matplotlib.pyplot as plt


SpO2_target = 92 

#percentage above normal 
Act_level = 0.05 

FlowRate_baseline = input("What is the baseline flow rate?")
hypoxic_state = 89

current_O2 = input("What is the current oxygen level")

def flow_algorithm(): 
    #print current flow rate & spO2 to csv 
    #add timescale 
    #plots - one SpO2 and one flow rate 
    #random number generator affects flow rate 
    num_hypoxic = 0
    if(current_O2 < hypoxic_state): 
        num_hypoxic = num_hypoxic + 1
        print("Alert: Hypoxic State!")
    diff_SpO2 = SpO2_target - (current_O2 * (1-Act_level))
    newFlow = FlowRate_baseline + diff_SpO2
    #send newFlow to machine

def sim_data(): 
    random_start = random.randint(85, 100)
    data_values = []
    for i in range(100): 
        rand_change = random.randint(-1, 1)
        temp_data = random_start + rand_change
        data_values.append(temp_data)
    np.savetxt('C:/Users/siptest/Desktop/DT2/dataVals.csv',
               data_values, delimiter=',')

def generate_plot(): 
    data = np.genfromtxt('C:/Users/siptest/Desktop/DT2/dataVals.csv', delimiter = ',')
    plt.plot(data)
    plt.savefig('C:/Users/siptest/Desktop/DT2/dataValsPlt.csv', transparent=True)

sim_data()
generate_plot()
