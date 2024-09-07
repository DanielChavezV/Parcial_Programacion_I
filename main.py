from App.modelos.ventana import Ventana
from App.modelos.cotizador import Cotizador
from datetime import datetime

def mostrar_menu():
    """
    Muestra el menú de opciones al usuario.
    """
    print("\n--- Menú Principal ---")
    print("1. Cotizar una nueva ventana")
    print("2. Ver resumen de cotización actual")
    print("3. Finalizar y mostrar total")
    print("4. Salir")
    print("------------------------")

def solicitar_datos_cliente():
    """
    Solicita al usuario los datos del cliente para la cotización.

    Retorna:
    -------
    dict:
        Diccionario con los datos del cliente.
    """
    print("\n--- Datos del Cliente ---")
    nombre = input("Ingrese el nombre del cliente: ")
    direccion = input("Ingrese la dirección del cliente: ")
    telefono = input("Ingrese el número de contacto del cliente: ")
    correo = input("Ingrese el correo electrónico del cliente: ")

    cliente = {
        "nombre": nombre,
        "direccion": direccion,
        "telefono": telefono,
        "correo": correo,
        "fecha": datetime.now().strftime("%d-%m-%Y")
    }

    return cliente

def solicitar_datos_ventana():
    """
    Solicita al usuario los datos para crear una ventana.

    Retorna:
    -------
    Ventana:
        Objeto de la clase Ventana con los datos ingresados por el usuario.
    """
    while True:
        estilo = input("Ingrese el estilo de la ventana (O, X, XO, OXO): ").upper()
        if estilo not in ["O", "X", "XO", "OXO"]:
            print("Estilo no válido. Por favor, elija entre O, X, XO, OXO.")
            continue
        
        try:
            ancho = float(input("Ingrese el ancho de la ventana en cm: "))
            alto = float(input("Ingrese el alto de la ventana en cm: "))
        except ValueError:
            print("Entrada no válida. El ancho y alto deben ser números.")
            continue
        
        acabado = input("Ingrese el tipo de acabado (Pulido, Lacado Brillante, Lacado Mate, Anodizado): ")
        if acabado not in ["Pulido", "Lacado Brillante", "Lacado Mate", "Anodizado"]:
            print("Acabado no válido. Elija entre: Pulido, Lacado Brillante, Lacado Mate, Anodizado.")
            continue
        
        tipo_vidrio = input("Ingrese el tipo de vidrio (Transparente, Bronce, Azul): ")
        if tipo_vidrio not in ["Transparente", "Bronce", "Azul"]:
            print("Tipo de vidrio no válido. Elija entre: Transparente, Bronce, Azul.")
            continue
        
        esmerilado = input("¿El vidrio es esmerilado? (Si/No): ").lower() == 'si'
        
        try:
            cantidad = int(input("Ingrese la cantidad de ventanas de este tipo: "))
        except ValueError:
            print("Cantidad no válida. Debe ser un número entero.")
            continue

        # Confirmación de los datos ingresados
        print("\nResumen de la ventana ingresada:")
        print(f"  Estilo: {estilo}, Ancho: {ancho} cm, Alto: {alto} cm")
        print(f"  Acabado: {acabado}, Tipo de Vidrio: {tipo_vidrio}, Esmerilado: {'Sí' if esmerilado else 'No'}")
        print(f"  Cantidad: {cantidad}")
        
        confirmar = input("¿Los datos ingresados son correctos? (Si/No): ").lower()
        if confirmar == 'si':
            break
        else:
            print("Por favor, ingrese los datos nuevamente.\n")
    
    return Ventana(estilo, ancho, alto, acabado, tipo_vidrio, esmerilado, cantidad)

def ver_resumen(cliente, lista_ventanas):
    """
    Muestra el resumen de las ventanas cotizadas hasta el momento.
    """
    print("\n--- Resumen de Cotización ---")
    print(f"Cliente: {cliente['nombre']}")
    print(f"Dirección: {cliente['direccion']}")
    print(f"Teléfono: {cliente['telefono']}")
    print(f"Correo: {cliente['correo']}")
    print(f"Fecha: {cliente['fecha']}")
    print("\n--- Detalle de Ventanas ---")
    
    if not lista_ventanas:
        print("No hay ventanas cotizadas aún.")
    else:
        for i, ventana in enumerate(lista_ventanas, 1):
            print(f"{i}. Estilo: {ventana.estilo}, Ancho: {ventana.ancho} cm, Alto: {ventana.alto} cm")
            print(f"   Acabado: {ventana.acabado}, Tipo de Vidrio: {ventana.tipo_vidrio}, Esmerilado: {'Sí' if ventana.esmerilado else 'No'}")
            print(f"   Cantidad: {ventana.cantidad}")
    print("-------------------------")

def main():
    print("Bienvenido al sistema de cotización de ventanas PQR")
    cliente = solicitar_datos_cliente()
    cotizador = Cotizador()
    lista_ventanas = []

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            ventana = solicitar_datos_ventana()
            lista_ventanas.append(ventana)
            print("¡Ventana agregada exitosamente!")
        
        elif opcion == '2':
            ver_resumen(cliente, lista_ventanas)
        
        elif opcion == '3':
            if not lista_ventanas:
                print("No hay ventanas cotizadas para calcular el total.")
                continue
            ver_resumen(cliente, lista_ventanas)
            costo_total = cotizador.calcular_costo_total(lista_ventanas)
            print(f"\nEl costo total de la cotización es: ${costo_total}")
            print("Gracias por utilizar el sistema de cotización. ¡Hasta luego!")
            break
        
        elif opcion == '4':
            print("Gracias por utilizar el sistema de cotización. ¡Hasta luego!")
            break
        
        else:
            print("Opción no válida. Por favor, seleccione una opción del menú.")

if __name__ == "__main__":
    main()
