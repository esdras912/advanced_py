
# def main():
#     number = 4

#     def nested():
#         print(number)

#     return nested


# my_func = main()
# my_func()




def repeater(name : str):
    def n_repeater(n : int):
        print(n * name)
    

    return n_repeater




def make_division_by(n):
    assert n != 0 , "no division by zero"
    def get_number(x):
        return x /n
    return get_number



division_by_5 = make_division_by(0)
print(division_by_5(25))

