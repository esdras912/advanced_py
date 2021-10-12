import matplotlib.pyplot as plt
# plt method with str

type_plot = 'plot'


plt.title(f"func")
to_execute = f'plt.{type_plot}(x,y)'
plt.text(3,4,"Texto")
x = [1,2,3]
y = [12,4,4]

exec(to_execute)
plt.savefig("done.png")



def test(*args, **kwargs):

    print(f"{args[0]}")

    print(kwargs['x'])


test("hola", x = 'hola2')