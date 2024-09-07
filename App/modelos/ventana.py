class Ventana:
    """
    Clase que representa una ventana para la cotización.

    Atributos:
    ----------
    estilo : str
        El estilo de la ventana (O, X, XO, OXO).
    ancho : float
        El ancho total de la ventana en cm.
    alto : float
        El alto total de la ventana en cm.
    acabado : str
        El tipo de acabado del aluminio.
    tipo_vidrio : str
        El tipo de vidrio (Transparente, Bronce, Azul).
    esmerilado : bool
        Indica si el vidrio es esmerilado.
    cantidad : int
        La cantidad de ventanas de este tipo a cotizar.
    """

    def __init__(self, estilo, ancho, alto, acabado, tipo_vidrio, esmerilado, cantidad):
        """
        Inicializa una instancia de la clase Ventana.

        Parámetros:
        ----------
        estilo : str
            Estilo de la ventana.
        ancho : float
            Ancho de la ventana en cm.
        alto : float
            Alto de la ventana en cm.
        acabado : str
            Tipo de acabado del aluminio.
        tipo_vidrio : str
            Tipo de vidrio.
        esmerilado : bool
            Indica si el vidrio es esmerilado.
        cantidad : int
            Cantidad de ventanas a cotizar.
        """
        self.estilo = estilo
        self.ancho = ancho
        self.alto = alto
        self.acabado = acabado
        self.tipo_vidrio = tipo_vidrio
        self.esmerilado = esmerilado
        self.cantidad = cantidad

    def calcular_dimension_nave(self):
        """
        Calcula las dimensiones de cada nave según el estilo de la ventana.

        Retorna:
        -------
        tuple:
            Ancho y alto de cada nave.
        """
        naves = {"O": 1, "X": 1, "XO": 2, "OXO": 3}[self.estilo]
        ancho_nave = self.ancho / naves
        alto_nave = self.alto
        return ancho_nave, alto_nave

    def __str__(self):
        """
        Representación en cadena de la ventana.

        Retorna:
        -------
        str:
            Descripción de la ventana.
        """
        esmerilado_text = "Sí" if self.esmerilado else "No"
        return (f"Ventana {self.estilo} - Ancho: {self.ancho} cm, Alto: {self.alto} cm, "
                f"Acabado: {self.acabado}, Vidrio: {self.tipo_vidrio}, Esmerilado: {esmerilado_text}, "
                f"Cantidad: {self.cantidad}")
