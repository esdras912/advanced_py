import mypy


def intern_validate():
    word : str = input("Inserta una palabra: ")
    if word == word[::-1]:
        positive_answer : str = f'Tu palabra "{word}" es un palindromo'
        print(positive_answer)
    
    else :
        negative_answer : str = f'TU palabra "{word}" no es un palindromo :('
        print(negative_answer)


def evaluation(word : str) -> bool:
    word = word.replace(" ", "").lower()
    return word == word[::-1]


def run():
    print(evaluation("ana"))
if __name__ == '__main__':
    run()