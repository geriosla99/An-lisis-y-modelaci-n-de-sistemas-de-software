#El patrón intérprete es un patrón de diseño de software que define una gramática
# para un lenguaje y proporciona un intérprete que usa esa gramática para interpretar
# sentencias en el lenguaje. Es útil para desarrollar lenguajes específicos
# de dominio (DSL) y para la interpretación de expresiones complejas
# en aplicaciones de software.
from abc import ABC, abstractmethod

class Expression(ABC):
    @abstractmethod
    def interpret(self):
        pass

class Number(Expression):
    def __init__(self, value):
        self.value = value

    def interpret(self):
        return self.value

class Add(Expression):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def interpret(self):
        return self.left.interpret() + self.right.interpret()


def main():
    # Interpretar la expresión "3 + 5"
    expression = Add(Number(3), Number(5))
    result = expression.interpret()
    print(f"Resultado de 3 + 5: {result}")

if __name__ == "__main__":
    main()


#El patrón intérprete se utiliza en aplicaciones que requieren
# la interpretación de lenguajes específicos de dominio (DSL), como calculadoras,
# analizadores de expresiones matemáticas y motores de reglas.
# Se implementa definiendo una gramática y creando clases que
# representan las reglas de esa gramática, permitiendo la
# evaluación de expresiones complejas.