class CasillaDeVotacion:
    def __init__(self, identificador,pais):
        self.identificador = identificador
        self._pais = pais
        self._region = None


    @property
    def region(self):
        return self._region

    @region.setter
    def region(self, region):
        if region in self._pais:
            self._region = region
        #El error se encontraba en no haber puesto else XD
        else:
            raise ValueError(f'La región {region} no es valido.')


if __name__ == "__main__":
    casilla = CasillaDeVotacion(123,['Mexico','Morelos','Morazan'])
    print(casilla.region)
    casilla.region = 'Morazan'
    print(casilla.region)
