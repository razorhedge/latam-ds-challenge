from matplotlib import pyplot as plt
import pandas as pd

def simple_histogram(data:pd.DataFrame, column:str, enlarge:bool=False):
    if enlarge:
        plt.figure(figsize=(20,5))
    data[column].value_counts().plot.bar()