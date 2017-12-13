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
        e1 = Exits('Bishan', 'A', 'NSL / CCL', 'Junction 8', 'Junction 8 Shopping Centre')
        self.add_exit(e1)
        e2 = Exits('Bishan', 'B', 'NSL / CCL', 'Bishan Road (Northbound)', 'Bishan Stadium')
        self.add_exit(e2)
        e3 = Exits('Bishan', 'C', 'NSL / CCL', 'Bishan Road (Southbound)', 'Raffles Institution')
        self.add_exit(e3)
        e4 = Exits('Bishan', 'D', 'NSL / CCL', 'Bishan Bus Interchange', 'Bishan Bus Interchange')
        self.add_exit(e4)
        e5 = Exits('Bishan', 'E', 'NSL / CCL', 'Junction 8', 'Junction 8 Basement')
        self.add_exit(e5)
        e6 = Exits('Serangoon', 'A', 'NEL / CCL', 'Upper Serangoon Road (Southbound)', 'Serangoon Central')
        self.add_exit(e6)
        e7 = Exits('Serangoon', 'B', 'NEL / CCL', 'Upper Serangoon Road (Northbound)', 'Sunglade')
        self.add_exit(e7)
        e8 = Exits('Serangoon', 'C', 'NEL / CCL', 'Serangoon Central (Southbound)', 'Serangoon Central')
        self.add_exit(e8)
        e9 = Exits('Serangoon', 'D', 'NEL / CCL', 'Lew Lian Gardens', 'Lew Lian Gardens Apartment')
        self.add_exit(e9)
        e10 = Exits('Serangoon', 'E', 'NEL / CCL', 'NEX', 'NEX')
        self.add_exit(e10)



    def add_exit(self, exit):
        self.__class__.exits.append(exit)

    def show_exits(self):
        while True:
            number = 1
            for exit in self.__class__.exits:
                print(number, exit)
                number += 1
            choice = int(input('Enter your choice (1,2,3,4,5,6,7,8,9,10): '))
            if choice == 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9 or 10:
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


