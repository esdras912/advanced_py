
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from typing import List, Dict



def graph_this(func):
    def wrapper(*args,**kwargs):
        # returned data from func !Must be a Pandas dataframe!
        plot_info = func(*args, **kwargs)


        module: str =  kwargs['module']
        plot_type:str = kwargs['type'] 
        title: str = kwargs['title']
        other_params:  Dict[str,str] =  kwargs['other_params']

        plt.figure(figsize=(9,6))
        plt.grid()

        PLOT_LINE_CODE : str = ''
        if module == 'sns':  # you must name this value how it is imported at your code "import seaborn as -------" 
            PLOT_LINE_CODE = f"{module}.{plot_type}(x = plot_info['{kwargs['x_df_name']}'],y = plot_info['{kwargs['y_df_name']}'])"

            if other_params != {}:
                PLOT_LINE_CODE = PLOT_LINE_CODE[:-1]
                for k,v in other_params.items():
                    PLOT_LINE_CODE = PLOT_LINE_CODE + f", {k} = {v}"
                PLOT_LINE_CODE = PLOT_LINE_CODE + ')'


            

        elif module == 'plt': # you must name this value how it is imported at your code import matplotlibpyplot as -------
            PLOT_LINE_CODE = f"{module}.{plot_type}(plot_info['{kwargs['x_df_name']}'],plot_info['{kwargs['y_df_name']}'])"
            if other_params != {}:
                PLOT_LINE_CODE = PLOT_LINE_CODE[:-1]
                for k,v in other_params.items():
                    PLOT_LINE_CODE =  PLOT_LINE_CODE + f", {k} = {v}"
                PLOT_LINE_CODE = PLOT_LINE_CODE + ')'


        exec(PLOT_LINE_CODE)
        plt.title(title)
        plt.savefig(f"{title}.png")
        plt.clf()


    return wrapper



@graph_this
def iris_values(*args,**kwargs):
    df = sns.load_dataset('iris')
    return df


iris_values(module = 'sns', x_df_name = 'petal_length', y_df_name = 'sepal_length',
 title = 'Iris_plot', type = 'scatterplot' , other_params = {'hue' : "plot_info['species']"})



@graph_this
def tips_values(*args,**kwargs):
    df = sns.load_dataset('tips')
    return df

tips_values(module = 'sns',x_df_name = 'total_bill', y_df_name = 'tip',
 title = 'Tips_Plot',type ='scatterplot', other_params = {'hue': "plot_info['sex']"})









