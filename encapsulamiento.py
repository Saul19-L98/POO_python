class Coordinate(object):
    
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y
        
    @property 
    def x(self):
        return self.__x
    
    @x.setter
    def set_x(self, coor_x):
        if coor_x >= 0:
            self.__x = coor_x
        else:
            raise ValueError('This is not a valid coordinate')
        
    @property
    def y(self):
        return self.__y
        
    @y.setter
    def set_y(self, coor_y):
        if coor_y >= 0:
            self.__y = coor_y
        else:
            raise ValueError('This is not a valid coordinate')
    
    def distance(self, coor):
        if isinstance(coor, Coordinate):
            res_x = (self.__x + coor.__x) ** 2
            res_y = (self.__y + coor.__y) ** 2
            resul = (res_x + res_y) ** (1/2)
            return resul
        raise ValueError('This is not a valid coordinate')
    
    def __str__(self):
        return f'x: {self.__x} - y: {self.__y}'


if __name__ == "__main__":
    coor_one = Coordinate()
    
    print(f'{str(coor_one)}')
    coor_one.set_x = 5
    print(f'{str(coor_one)}')