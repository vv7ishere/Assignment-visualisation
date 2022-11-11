#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 10:15:11 2022

@author: vishnuv
"""

import pandas as pd
import matplotlib.pyplot as plt

#comparing offensive stats of different clubs using Line graph
def lineplotofEPL():
    """
    This function compares the offensive stats of different clubs
    """
    plt.rcParams['font.size'] = 20
    plt.figure(figsize=(20 , 20))
    plt.plot(data_epl['name'],data_epl['off'],label = 'offense')
    plt.plot(data_epl['name'],data_epl['def'],label = 'defence')
    plt.xticks(fontsize = 20, rotation=90)
    plt.legend()
    plt.xlabel("CLUBS",fontsize = 20 )
    plt.ylabel("OFFENSIVE AND DEFENSIVE STATS",fontsize=20)
    plt.title("OFFENSIVE AND DEFENSIVE COMPARISON",fontsize=22)
    plt.savefig("PLOT 1")
    plt.show()
    
 #comparing soccer power index points of different clubs using bar diagram   
def plotofEPL():
    """
    This function compares the soccer power index points of different clubs
    """
    plt.figure(figsize=(22,22))
    plt.bar(data_epl['name'],data_epl['spi'])
    plt.xticks(fontsize = 16, rotation=90)
    plt.xlabel("Clubs",fontsize = 20)
    plt.ylabel("Soccer power index points",size = 20)
    plt.title("SPI OF CLUBS",fontsize = 20)
    plt.savefig("PLOT 2")
    plt.show()
    
#comparing defensive stats of different clubs using pie diagram    
def plotPie():
    """
    This function compares the defensive stats of different clubs
    """
    plt.figure(figsize=(11,11))
    plt.pie(pie_data["def"],autopct='%1.0f%%')
    plt.legend(labels = pie_data['name'], bbox_to_anchor = (1.0 , 1.0), fontsize = 16)
    plt.title("DEFENSIVE COMPARISON", fontsize = 16)
    plt.savefig("PLOT 3")
    plt.show()
   
EPL=pd.read_csv("//Users//vishnuv//Desktop//spi_global_rankings....7kk.csv")
data_epl = EPL[0:10]
pie_data = EPL[0:5]

#calling function to plot offensive comparison of different clubs
lineplotofEPL()
#calling function to plot spi comparison of different clubs
plotofEPL()
#calling function to plot defensive comparison of different clubs
plotPie()