import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def inital_exploration(data):
    print("Data info:")
    print(data.info())
    print("Rows and Columns:")
    print(data.shape)
    return 

def missing_values(data):
    print("Missing Values:")
    return data.isnull().sum()

def standarize_columns(data):
    data.columns = data.columns.str.lower().str.replace(" ", "_")
    data.columns = data.columns.str.replace("[", "")
    data.columns = data.columns.str.replace("]", "")
    data.columns = data.columns.str.replace("&", "n")
    return data.columns

def drop_columns(data, columns):
    return data.drop(columns=columns)


def create_copy(data):
    df = data.copy()
    return df


