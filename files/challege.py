import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns




def graph_this(func):
    def wrapper(*args,**kwargs):
        plot_info = func()
        
        plot_type = plot_info[0] 
        x_values = plot_info[1]
        y_values = plot_info[2]
        title = kwargs['title']



    return wrapper




def iris_values():
    df = sns.load_dataset('iris')
    return [list(df['sepal_length']), list(df['petal_length'])]


print(iris_values())














def run():
    pass

if __name__ == '__main__':
    run()