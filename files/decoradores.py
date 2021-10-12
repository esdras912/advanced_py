# un decorador es una función que recibe en sus parámetros otra función crea una función
# en esa función le añade cosas despues la ejecuta y retorna esa función creada



def decorador(funcc):
    def envoltura(word):
        word = word.lower()
        funcc(word)

    return envoltura
        

@decorador
def iniciar(word):
    print(f"palabra {word}")
    print(word == word[::-1])


iniciar("anA")


