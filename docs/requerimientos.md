# Requerimientos del Sistema de Cotización de Ventanas para PQR

## Requerimientos Funcionales

1. **Selección de estilo de ventana**: El sistema debe permitir al usuario seleccionar entre los estilos de ventana disponibles:
   - O: Fijo
   - X: Móvil
   - XO: Un panel fijo y otro móvil
   - OXXO: Dos móviles entre dos fijos
   - OXO: Dos fijos y uno móvil en el centro

2. **Dimensiones de la ventana**: El usuario debe ingresar las dimensiones (ancho y alto) de la ventana, y el sistema calculará las dimensiones de cada nave de acuerdo con el estilo seleccionado.

3. **Selección de materiales**:
   - **Acabado del aluminio**: El sistema debe permitir seleccionar entre pulido, lacado brillante, lacado mate y anodizado.
   - **Tipo de vidrio**: El sistema debe permitir seleccionar entre vidrio transparente, bronce, azul, con la opción de esmerilado.

4. **Cálculo de costos**:
   - El sistema debe calcular el costo del aluminio por metro lineal.
   - El costo del vidrio debe calcularse por cm².
   - El sistema debe sumar los costos de las esquinas y las chapas para naves móviles (X).

5. **Descuento por volumen**: Si la cantidad de ventanas supera las 100 unidades, el sistema debe aplicar un descuento del 10% al costo total.

6. **Generación de cotización**: El sistema debe generar una cotización final detallada con los materiales y costos totales