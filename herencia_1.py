class TipoComprobante:
    def __init__(self, precioUnitario, cantidad):
        self.precioUnitario = precioUnitario
        self.cantidad = cantidad

    def calcularTotal(self):
        return self.precioUnitario * self.cantidad

class Factura(TipoComprobante):

    def __init__(self, precioUnitario):
        super().__init__(precioUnitario, cantidad=5)

class Nota_credito(TipoComprobante):

    def __init__(self, precioUnitario):
        super().__init__(precioUnitario,cantidad=1)

if __name__ == '__main__':
    tipo_comprobante = TipoComprobante(precioUnitario=20, cantidad=10)
    print (tipo_comprobante.calcularTotal())

    factura = Factura(precioUnitario=50)
    print(factura.calcularTotal())