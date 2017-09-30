"""
*args and * kwargs demo
"""

class Car(object):
    """ father class """
    def __init__(self, color, brand):
        self.color = color
        self.brand = brand


class BlueCar(Car):
    """ child class """
    def __init__(self, *args, **kwargs):
        super(BlueCar, self).__init__(*args, **kwargs)
        self.color = 'blue'





def main():
    """ test """
    my_car = BlueCar('red', 'Super!')
    print my_car.color
    print my_car.brand

if __name__ == '__main__':
    main()
