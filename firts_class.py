# def run()
#     pass


class Coordenada:

    def __init__(self, x, y):
        self.x = x
        self.y = y
    

    def distancia(self, otra_coordenada):
        x_diff = (self.x - otra_coordenada.x)**2
        y_diff = (self.y - otra_coordenada.y)**2
        return (x_diff + y_diff)**0.5

if __name__ == "__main__":
    # run()
    coordena_1 = Coordenada(5,10)
    coordena_2 = Coordenada(-9,-5)

    print(coordena_1.distancia(coordena_2))
    print(isinstance( coordena_2, Coordenada))