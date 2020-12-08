class Automovil:

    def __init__(self, marca, tipo):
        self.marca = marca
        self.tipo = tipo


    def start_engine(self):
        print(f'Starting {self.marca} {self.tipo} engine')
        


    def stop_engine(self):
        print(f'Stopping {self.marca} {self.tipo} engine')


if __name__ == "__main__":

    auto_1 = Automovil('MERCEDEZ','C98')
    auto_2 = Automovil('NISAN','AA8')
    print(auto_1.start_engine())
    print(auto_2.start_engine())