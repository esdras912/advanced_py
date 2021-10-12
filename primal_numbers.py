from typing import List

def evaluate(number : int) -> bool:
    possible_divisors : List = [n for n in range(2,number) if number % n == 0]
    return len(possible_divisors) == 0





def run():
    number = 3.5
    print(evaluate(number))

if __name__ == '__main__':

    run()