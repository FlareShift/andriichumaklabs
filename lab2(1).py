class Computer:
    instance_count = 0

    def __init__(self, frequency=0, cores=0, memory=0, hdd=0):
        self.__frequency = frequency  
        self._cores = cores         
        self._memory = memory       
        self.__hdd = hdd             
        Computer.instance_count += 1 

    def __str__(self):
        return (f'Computer(frequency={self.__frequency} MHz, '
                f'cores={self._cores}, memory={self._memory} MB, '
                f'hdd={self.__hdd} GB)')

    @property
    def cost(self):
        return (self.__frequency * self._cores / 100 +
                self._memory / 80 + self.__hdd / 20)

    @property
    def is_suitable(self):
        return (self.__frequency >= 2000 and
                self._cores >= 2 and
                self._memory >= 2048 and
                self.__hdd >= 320)

    @staticmethod
    def get_instance_count():
        return Computer.instance_count

    @classmethod
    def from_string(cls, data):
        frequency, cores, memory, hdd = map(int, data.split(','))
        return cls(frequency, cores, memory, hdd)


class Laptop(Computer):
    def __init__(self, frequency=0, cores=0, memory=0, hdd=0, battery_life=0):
        super().__init__(frequency, cores, memory, hdd)
        self._battery_life = battery_life  

    def __str__(self):
        return (f'Laptop(frequency={self._Computer__frequency} MHz, '
                f'cores={self._cores}, memory={self._memory} MB, '
                f'hdd={self._Computer__hdd} GB, battery_life={self._battery_life} min)')

    @property
    def cost(self):
        return super().cost + self._battery_life / 10

    @property
    def is_suitable(self):
        return super().is_suitable and self._battery_life >= 60


if __name__ == "__main__":
    computer = Computer(2400, 4, 4096, 500)
    print(computer)
    print(f'Cost: {computer.cost}')
    print(f'Is suitable: {computer.is_suitable}')

    laptop = Laptop(2200, 4, 4096, 500, 120)
    print(laptop)
    print(f'Cost: {laptop.cost}')
    print(f'Is suitable: {laptop.is_suitable}')

    print(f'Total instances created: {Computer.get_instance_count()}')

    new_computer = Computer.from_string("3000,4,8192,1000")
    print(new_computer)
