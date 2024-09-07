class Cliente:
    """
    Clase que representa a un cliente.

    Atributos:
    ----------
    nombre : str
        Nombre del cliente.
    direccion : str
        Dirección del cliente.
    telefono : str
        Número de contacto del cliente.
    correo : str
        Correo electrónico del cliente.
    fecha : str
        Fecha de la cotización.
    """

    def __init__(self, nombre, direccion, telefono, correo, fecha):
        """
        Inicializa una instancia de la clase Cliente.

        Parámetros:
        ----------
        nombre : str
            Nombre del cliente.
        direccion : str
            Dirección del cliente.
        telefono : str
            Número de contacto del cliente.
        correo : str
            Correo electrónico del cliente.
        fecha : str
            Fecha de la cotización.
        """
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.correo = correo
        self.fecha = fecha

    def __str__(self):
        """
        Representación en cadena del cliente.

        Retorna:
        -------
        str:
            Descripción del cliente.
        """
        return (f"Cliente: {self.nombre}\nDirección: {self.direccion}\n"
                f"Teléfono: {self.telefono}\nCorreo: {self.correo}\nFecha: {self.fecha}")
