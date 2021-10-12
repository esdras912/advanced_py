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


                

        PLOT_LINE_CODE = f"{kwargs['module']}.{plot_type}(plot_info['{kwargs['x_df_name']}'],plot_info['{kwargs['y_df_name']}'])"

        exec(PLOT_LINE_CODE)
        plt.title(title)

        plt.savefig(f"{title}.png")


    return wrapper



@graph_this
def iris_values(*args,**kwargs):
    df = sns.load_dataset('iris')

    df_to_return = pd.DataFrame([df['sepal_length'] , df['petal_length']])
    return df_to_return.T



iris_values(module = 'sns',type = 'scatterplot', title = 'Iris_Data_Set', x_df_name = 'sepal_length', 
            y_df_name = 'petal_length')












def run():
    pass

if __name__ == '__main__':
    run()