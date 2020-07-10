#Steps of data anlysis
#Mining
#Explore
#Cleaning
#Inference
#Modeling
#Communication

import os
import pandas as ps
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt


class Explore():
    
    def __init__(self):
        
    def bs = pd.read_csv("file.csv"):
    
    def bs.summarize():
    
class Clean_data():
    def __init__(self):
        
    def removena(self,...):
    #Depending on the situation, na's can be removed   
    def imputena(self,...)
    # but there are cases when they can be imputed by the rest of the data
    def normalize(self,...):
    # Normalize or log-transform
    def scale(self,...):
    #scale 0-1

class Inference():
    def __init__(self):
        
    def visualize(self,...):
        
    def correlation(self,...):
    #check for multicolinearity, it will affect regression
    
    def stat_tests(self,...):
    #Other statistical tests may be necessary

class Modeling():
    def __init__(self):
        
    def data_split(self,...):
    #Split the data into training and test (generally 70/30%)
    
    def ml_tool(self,...):
    #depending on data, it will change
    
    def accuracy():
    #measure the predictive power of the model
    
class Communication():
    def __init__(self):
        
    def boxplot(self,):
    
    def scatterplot(self,)

    def heatmap(self,)
