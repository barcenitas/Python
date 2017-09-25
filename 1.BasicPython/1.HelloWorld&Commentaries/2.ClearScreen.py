"""
Created by Edgar Daniel Barcenas Martinez
Proteco Gen 34. FI UNAM
September 24, 2017
"How to Clear Screen in console from python"
"""

#First
import os 
#clear =lambda: os.system('clear') #if you are in Linux or MacOs
#clear =lambda: os.system('cls') #if you are in Windows

#in my case i'm in MacOS
clear =lambda: os.system('clear')
 
#Later i execute this command in my console -> clear()
clear()
