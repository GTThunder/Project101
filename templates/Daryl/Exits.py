from templates.Daryl.Train import Train

class Exits(Train):

    def __init__(self, station, exits, type_of_line, location, nearby):
        Train.__init__(self, station, exits, type_of_line)
        self.__location = location
        self.__nearby = nearby

    def get_location(self):
        return self.__location

    def get_nearby(self):
        return self.__nearby

    def set_location(self, location):
        self.__location = location

    def set_nearby(self, nearby):
        self.__nearby = nearby

    def __str__(self):
        return 'MRT station is {}, type of line is {}. Exit {} leads to {}, the nearby facilities are {}' \
            .format(self.get_station(), self.get_type_of_line(), self.get_exits(), self.__location, self.__nearby)

class Exit:
    exits = []
    choice = []

    def __init__(self):
        self.create_exits()

    def create_exits(self):
        e1 = Exits('Bishan', 'A', 'North South Line', 'Junction 8', 'Junction 8 Shopping Centre')
        self.add_exit(e1)
        e2 = Exits('Bishan', 'B', 'North South Line', 'Bishan Road (Northbound)', 'Bishan Stadium')
        self.add_exit(e2)
        e3 = Exits('Bishan', 'C', 'North South Line', 'Bishan Road (Southbound)', 'Raffles Institution')
        self.add_exit(e3)
        e4 = Exits('Bishan', 'D', 'North South Line', 'Bishan Bus Interchange', 'Bishan Bus Interchange')
        self.add_exit(e4)
        e5 = Exits('Bishan', 'E', 'North South Line', 'Junction 8', 'Junction 8 Basement')
        self.add_exit(e5)


    def add_exit(self, exit):
        self.__class__.exits.append(exit)

    def show_exits(self):
        while True:
            number = 1
            for exit in self.__class__.exits:
                print(number, exit)
                number += 1
            choice = int(input('Enter your choice (1,2,3,4,5): '))
            if choice == 1 or 2 or 3 or 4 or 5:
                exit = self.__class__.exits[choice - 1]
                self.__class__.choice.append(exit)
                break

    def display_choices(self):
        print('You have chosen:')
        for order in self.__class__.choice:
            print(order)


exit = Exit()
exit.show_exits()
exit.display_choices()


