from App.modelos.ventana import Ventana

class Cotizador:
    """
    Clase para calcular el costo de cotización de ventanas.
    """

    def __init__(self):
        """
        Inicializa una instancia de la clase Cotizador con los precios base.
        """
        # Inicialización de precios
        self.precios_acabado = {
            "Pulido": 50700,
            "Lacado Brillante": 54200,
            "Lacado Mate": 53600,
            "Anodizado": 57300
        }
        self.precios_vidrio = {
            "Transparente": 8.25,
            "Bronce": 9.15,
            "Azul": 12.75
        }
        self.costo_chapa = 16200
        self.costo_esquina = 4310
        self.costo_esmerilado = 5.20

    def calcular_costo_ventana(self, ventana):
        """
        Calcula el costo de una ventana específica.

        Parámetros:
        ----------
        ventana : Ventana
            Objeto de la clase Ventana.

        Retorna:
        -------
        float:
            Costo total de las ventanas de este tipo.
        """
        # Determinar el número de naves basado en el estilo de la ventana
        ancho_nave, alto_nave = ventana.calcular_dimension_nave()
        naves = {"O": 1, "X": 1, "XO": 2, "OXO": 3}[ventana.estilo]

        # Calcular el costo del aluminio
        perimetro_nave = (2 * (ancho_nave - 2) + 2 * (alto_nave - 2)) * 2.5
        costo_aluminio = perimetro_nave * self.precios_acabado[ventana.acabado] / 100

        # Calcular el costo del vidrio
        area_vidrio = (ancho_nave - 1.5) * (alto_nave - 1.5)
        costo_vidrio = area_vidrio * self.precios_vidrio[ventana.tipo_vidrio]
        if ventana.esmerilado:
            costo_vidrio += area_vidrio * self.costo_esmerilado

        # Calcular costos adicionales (esquinas y chapas)
        num_esquinas = 4 * naves
        costo_total_esquinas = num_esquinas * self.costo_esquina
        costo_total_chapas = (1 if "X" in ventana.estilo else 0) * self.costo_chapa * naves

        # Calcular el costo total de la ventana
        costo_ventana = costo_aluminio + costo_vidrio + costo_total_esquinas + costo_total_chapas

        return costo_ventana * ventana.cantidad

    def calcular_costo_total(self, lista_ventanas):
        """
        Calcula el costo total de todas las ventanas en la lista.

        Parámetros:
        ----------
        lista_ventanas : list
            Lista de objetos de la clase Ventana.

        Retorna:
        -------
        float:
            Costo total de todas las ventanas, incluyendo el descuento si aplica.
        """
        costo_total = 0
        cantidad_total = 0

        # Calcular el costo total de todas las ventanas
        for ventana in lista_ventanas:
            costo_total += self.calcular_costo_ventana(ventana)
            cantidad_total += ventana.cantidad

        # Aplicar descuento si hay más de 100 ventanas
        descuento = 0.1 if cantidad_total > 100 else 0
        return round(costo_total * (1 - descuento), 2)
