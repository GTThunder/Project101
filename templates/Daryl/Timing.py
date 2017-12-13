from templates.Daryl.Train import Train

class Timing(Train):

    def __init__(self, station, exits, type_of_line, timing, direction):
        Train.__init__(self, station, exits, type_of_line)
        self.__timing = timing
        self.__direction = direction

    def get_timing(self):
        return self.__timing

    def get_direction(self):
        return self.__direction

    def set_timing(self, timing):
        self.__timing = timing

    def set_direction(self, direction):
        self.__direction = direction

    def __str__(self):
        return 'Name of station is {}, type of line is {}, estimated arrival of train is {}, ' \
               'direction heading towards is {}'.format(self.get_station(), self.get_type_of_line(),
                self.__timing, self.__direction)

class Time:
    timing = []
    choice = []

    def __init__(self):
        self.create_timing()

    def create_timing(self):
        t1 = Timing('Bishan', 'A', 'Circle Line', '3 mins', 'Towards HabourFront')
        self.add_timing(t1)
        t2 = Timing('Bishan', 'B', 'Circle Line', '4 mins', 'Towards Marina Bay')
        self.add_timing(t2)
        t3 = Timing('Bishan', 'B', 'Circle Line', '5 mins', 'Towards Dhoby Ghaut')
        self.add_timing(t3)
        t4 = Timing('Bishan', 'C', 'North South Line', '3 mins', 'Marina Bay')
        self.add_timing(t4)
        t5 = Timing('Bishan', 'D', 'North South Line', '5 mins', 'Jurong East')
        self.add_timing(t5)

    def add_timing(self, time):
        self.__class__.timing.append(time)

    def show_timing(self):
        while True:
            number = 1
            for time in self.__class__.timing:
                print(number, time)
                number += 1
            choice = int(input('Enter your choice (1,2,3,4,5): '))
            if choice == 1 or 2 or 3 or 4 or 5:
                time = self.__class__.timing[choice - 1]
                self.__class__.choice.append(time)
                break

    def display_choices(self):
        print('You have chosen:')
        for order in self.__class__.choice:
            print(order)


x = Time()
x.show_timing()
x.display_choices()


