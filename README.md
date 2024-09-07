# PARCIAL 1 PROGRAMACION I 
## Proyecto: Sistema de Cotización de Ventanas para PQR

![Fondo](https://img2.rtve.es/v/16039379/?w=1600)

## Descripción

La empresa PQR, dedicada a la fabricación de ventanas de aluminio, requiere un sistema automatizado que optimice su proceso de cotización, actualmente gestionado de forma manual. El objetivo principal de este proyecto es desarrollar un programa que permita calcular el costo de las ventanas según las especificaciones del cliente, teniendo en cuenta el tipo de ventana, los acabados del aluminio, los tipos de vidrio, y las dimensiones.

El sistema debe ser capaz de manejar los estilos de ventana disponibles (O, XO, OXXO, OXO), calcular el costo de materiales (aluminio, vidrio, esmerilado) y aplicar descuentos cuando se realicen pedidos en grandes volúmenes.

#Funcionalidades:

#####Selección de estilos de ventanas: 
El sistema permite elegir entre los siguientes estilos de ventana:

- O: Fija, de un solo panel.

- X: Móvil, de un solo panel.

- XO: Combinación de un panel fijo (O) y uno móvil (X).

- OXXO: Dos paneles móviles entre dos paneles fijos.

- OXO: Dos paneles fijos con uno móvil en el centro.

- Cálculo de dimensiones: El costo de la ventana se calcula según el ancho y alto total de la ventana, dividiendo correctamente cada nave según el estilo seleccionado.

#####Cálculo de materiales:

Acabados de aluminio: Los usuarios pueden seleccionar entre cuatro acabados distintos:

- Pulido: $50,700 por metro lineal.

- Lacado Brillante: $54,200 por metro lineal.

- Lacado Mate: $53,600 por metro lineal.

- Anodizado: $57,300 por metro lineal.

#####Tipos de vidrio:
- Transparente: $8.25 por cm².

- Bronce: $9.15 por cm².

- Azul: $12.75 por cm².

- Esmerilado (opcional): $5.20 adicional por cm².

#####Cálculo de componentes adicionales:

- Esquinas: $4,310 por esquina.

- Chapas: $16,200 por cada nave móvil (X).

#####Descuentos por volumen: 

Aplicación automática de un descuento del 10% si el número de ventanas solicitadas supera las 100 unidades.

#####Generación de cotización final: 
El sistema genera un resumen con el costo total de cada ventana y el costo global para el cliente.

## Requerimientos del Proyecto

#####Requerimientos Funcionales
- Los usuarios deben ser capaces de seleccionar entre los diferentes estilos de ventanas.
- El sistema debe calcular el precio en función de las dimensiones, materiales y componentes adicionales.
- Debe permitir seleccionar acabados de aluminio y tipos de vidrio.
- El sistema debe manejar pedidos en masa y aplicar descuentos por volumen.
- Debe ser capaz de generar una cotización final para el cliente.

Para ejecutar este proyecto, necesitas tener instaladas las siguientes herramientas:

- **Python**: 3.x (Se recomienda la última versión estable)

- **Entorno virtual (venv)**

- **Librerías**: Librerías especificadas en requirements.txt

# Instalación

1. Clona el Repositorio:

	Si estás utilizando Git, clona el repositorio a tu máquina local:

```bash
git clone  https://github.com/DanielChavezV/Parcial_Programacion_I.git
```

2. Crear y activar el entorno virtual:

	```bash
python -m venv venv
source venv/bin/activate  # Linux/MacOS
venv\Scripts\activate  # Windows
```
3. Instalar las dependencias:

	```bash
pip install -r requirements.txt
```

# Ejecución

Para ejecutar el proyecto, usa el siguiente comando:

```bash
python main.py
```

# Autor
**Daniel Steven Chavez Valdes**
**Ingeniería de Sistemas 4 Semestre**
**Universidad Libre Seccional Cali**
