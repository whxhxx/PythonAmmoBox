"""
*args and * kwargs demo
"""

class Car(object):
    """ father class """
    def __init__(self,  color, brand, num):
        self.color = color
        self.brand = brand
        self.num = num


class BlueCar(Car):
    """ child class """

    # *args : parameters need to be given in order
    # **kwargs: parameters need to be given according to keys
    def __init__(self, *args, **kwargs):
        super(BlueCar, self).__init__(*args, **kwargs)

        self.color = 'blue'





def main():
    """ test """

    # parameters are using *args
    car1 = BlueCar('red', 'Porsche', 999)

    # parameters are using **kwargs so they don't need to be in order
    car2 = BlueCar(num = 9, color = 'green', brand = 'Jeep')

    # mixed way: **kwargs alfter *args
    car3 = BlueCar('yellow', 'Benz', num = 101 )

    print car1.color, car1.brand, car1.num
    print car2.color, car2.brand, car2.num
    print car3.color, car3.brand, car3.num

if __name__ == '__main__':
    main()
