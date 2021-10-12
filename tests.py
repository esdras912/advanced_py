import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
# plt method with str

type_plot = 'plot'


plt.title(f"func")
to_execute = f'plt.{type_plot}(x,y)'
plt.text(3,4,"Texto")
x = [1,2,3]
y = [12,4,4]




def test(*args, **kwargs):

    print(f"{args[0]}")

    print(kwargs['x'])


# df_creation 
def iris_values(*args,**kwargs):
    df = sns.load_dataset('iris')

    df_to_return = pd.DataFrame([df['sepal_length'] , df['petal_length']]).T
    
    plt.scatter(df_to_return['sepal_length'], df['petal_length'])
    plt.savefig("plot.png")
    return df_to_return



iris_values()