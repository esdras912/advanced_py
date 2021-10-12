from http.client import RESET_CONTENT
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns




def graph_this(func):
    def wrapper(*args,**kwargs):
        plot_info = func(*args, **kwargs)
        
        plot_type = kwargs['type'] 
        title = kwargs['title']


        x_values = plot_info[0]
        y_values = plot_info[1]
        

        PLOT_LINE_CODE = f'plt.{plot_type}(x_values, y_values)'

        exec(PLOT_LINE_CODE)
        plt.title(title)

        plt.savefig(f"{title}.png")


    return wrapper



@graph_this
def iris_values(*args,**kwargs):
    df = sns.load_dataset('iris')

    df_to_return = pd.DataFrame([df['sepal_length'] , df['petal_length']])
    return [list(df['sepal_length']), list(df['petal_length'])]



iris_values(type = 'scatter', title = 'Iris_Data_Set')












def run():
    pass

if __name__ == '__main__':
    run()