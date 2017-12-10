import datetime

class Train:

    def __init__(self, station, exits, type_of_line):
        self.__station = station
        self.__exits = exits
        self.__type_of_line = type_of_line
        currentdatetime = datetime.datetime.now()
        create_date = str(currentdatetime.day) + "-" + str(currentdatetime.month) + "-" + str(currentdatetime.year)  # DD-MM-YYYY format
        self.__create_date = create_date


    def get_station(self):
        return self.__station

    def get_exits(self):
        return self.__exits

    def get_type_of_line(self):
        return self.__type_of_line

    def get_created_date(self):
        return self.__created_date

    def set_station(self, station):
        self.__station = station

    def set_exits(self, exits):
        self.__exits = exits

    def set_type_of_line(self, type_of_line):
        self.__type_of_line = type_of_line

    def set_created_date(self, create_date):
        self.__created_date = create_date

