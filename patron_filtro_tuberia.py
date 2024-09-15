#El patrón Filtro-Tubería organiza el procesamiento de datos en etapas sucesivas.
# Cada etapa, o filtro, realiza una transformación específica y luego pasa los
# datos al siguiente filtro a través de una tubería. Esto facilita la modularidad
# y la flexibilidad en el manejo de datos.
#ejemplo:
#filtro para verificar si un numero es positivo
def filter_negatives(numbers):
    return [num for num in numbers if num >= 0]

#filtro para elevar el numero
def square_numbers(numbers):

    return [num**2 for num in numbers]

#proceso de tuberia
def process_pipeline(data, filters):

    for filter_func in filters:
        data = filter_func(data)
    return data

def get_user_input():

    while True:
        input_str = input("Introduce una lista de números separados por comas: ")
        try:
            numbers = [int(num.strip()) for num in input_str.split(",") if num.strip()]
            return numbers
        except ValueError:
            print("Error: Por favor, introduce solo números separados por comas.")

# Solicitar números al usuario
user_numbers = get_user_input()

# definir el pipeline de filtros
pipeline = [filter_negatives, square_numbers]

# procesar el flujo de datos a través de los filtros
result = process_pipeline(user_numbers, pipeline)

print("Resultados después de filtrar y elevar al cuadrado:", result)


#El patrón Filtro-Tubería se usa en procesamiento de datos,
# sistemas de compilación y flujos de trabajo en aplicaciones.
# Se implementa creando filtros independientes para cada tarea y
# conectándolos en serie mediante tuberías, permitiendo la transformación y
# el paso de datos entre cada etapa.