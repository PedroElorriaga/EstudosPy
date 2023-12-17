# O @classmethod permite que você chame o metodo de 
# uma classe sem precisar instânciar a classe, como no exemplo abaixo:

class Escritor():
    def __init__(self):
        pass

    def escreve(self, text):
        print(text)


    # Vale ressaltar que por convenção usamos o cls
    # para referênciar a classe no classmethod, no lugar onde ficaria o self.]
    @classmethod
    def escreve_novo(cls, text):
        print(text)

# Escritor.escreve("Olá!") # Não vai executar
Escritor.escreve_novo("Olá!") # Vai executar

instancia_escritor = Escritor() # Cria a Instância
instancia_escritor.escreve("Olá! Instanciado") # Vai executar