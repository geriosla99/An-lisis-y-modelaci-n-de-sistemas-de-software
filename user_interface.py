# user_interface.py

"""
Patón de Capas

Es uno de los patrones de arquitectura de software, donde el patrón de capas organiza el software en capas separadas, donde cada capa tiene una responsabilidad
específica.
Ejemplo: Aplicaciones web con capas de presentación, lógica y datos.
Ventajas: Simplifica el mantenimiento y la separación de preocupaciones.
Entonces, generalmente se tiene la capa de PRESENTACIÓN donde se hace la visualización, la capa de NEGOCIO se hacen las funciones y la capa de DATOS se hace 
la computación.

Capa de Presentación:
    Se encarga de manejar la interación entre un cliente y la aplicación. (toma las solicitudes del usuario y las pone en acciones para las capas de negocio
    y persistencia)
    Al ser una capa de presentación que está mas cerca del usuario, por ende sabe como manejar un clic, un topuch a un botón, esta capa toma dichas solicitudes
    y lo transforma para que las demás capas lo puedan entender después.
        - El cliente puede ser:
            - Un ser humano
            - Un programa externo
        - Responsabilidades
            - Entrega y solicita información al usuario.
            - Interpreta solicitudes del usuario en acciones para las capas de negocio y persistencia.
        Ejemplos de componentes en la capa de presentación.
            - Una aplicación web.
            - Una interfaz por consola.
            - Una aplicación de escritorio.
            - Una aplicación móvil.
            - Un servicio web.
            - Una API

Capa de Dominio:
    Es la que contiene la lógica de negocio del sistema. Es una funcionalidad que centra para que el negocio opere, debe esconder el acceso a datos.
    Contiene el trabajo o las tareas para las cuales el sistema está heho.
        Ejemplos
            - Cálculos basados en datos de entrada y datos almacenados.
            - Validaciones de datos que viene de la capa de presentación.
            - Definir qué algoritmo o lógica de negocio utilizar.
        Otros nombres para esta capa.
            - Capa de negocio
            - Capa de lógica de negocio.
            - Capa de lógica de dominio.
                    * Todas representan la msma idea, concentrar las reglas del negocio en el sistema.

Capa de Acceso a Datos:
    Se comunica con bases de datos u otros sistemas de persistencia para obtener y guardar información. (La que tiene el código para conectarse a una fuente
    de información)
    De forma más general, se comunica con sistemas que realizan tareas en nombre de la aplicación.
            - Monitores de transacciones.
            - Sistemas de mensajería.
            - Capa de persistencia.
            - Capa de datos.
            - Entre otros.
"""
from business_logic import BusinessLogic
from data_access import DataAccess

class UserInterface:
    def __init__(self, business_logic):
        self.business_logic = business_logic

    def display(self):
        item = input("Introduce un elemento para guardar: ")
        self.business_logic.process_data(item)
        print("Datos actuales:", self.business_logic.data_access.get_data())

# Clase principal
if __name__ == "__main__":
    data_access = DataAccess()
    business_logic = BusinessLogic(data_access)
    ui = UserInterface(business_logic)
    ui.display()
