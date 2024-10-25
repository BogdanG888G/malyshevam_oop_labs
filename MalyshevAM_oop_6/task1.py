class Bus:
    def __init__(self, speed, distance):
        self.__speed = speed
        self.__distance = distance
        self.__max_speed = 120
        self.__passengers = []
        self.__capacity = 75
        self.__empty_seats = None
        self.__seats_occupied = None
        self.__fuel_tank = 100
        self.__toplivo = None
        self.__kartet_tank = 6
        self.__maslo = None
        self.__luggage_spaces = 150
        self.__luggage = None

    def set_speed(self):
        return self.__speed

    def get_speed(self, value):
        if value > self.__max_speed:
            raise ValueError(f"Скорость не может превышать {self.__max_speed} км/ч.")
        self.__speed = value

    def get_distance(self):
        return self.__distance

    def set_distance(self, value):
        self.__distance = value

    def get_passengers(self):
        return self.__passengers

    def set_passengers(self, value):
        if len(value) > self.__capacity:
            raise ValueError(f"Количество пассажиров не может превышать {self.__capacity}.")
        self.__passengers = value
        self.__seats_occupied = len(value)
        self.__empty_seats = self.__capacity - len(value)

    
    def get_max_speed(self):
        return self.__max_speed
    
    def get_empty_seats(self):
        return self.__empty_seats


    def set_empty_seats(self, value):
        if value > self.__capacity:
            raise ValueError(f"Свободные места не могут превышать {self.__capacity}.")
        self.__empty_seats = value

    
    def get_seats_occupied(self):
        return self.__seats_occupied

    def set_seats_occupied(self, value):
        if value > self.__capacity:
            raise ValueError(f"Занятые места не могут превышать {self.__capacity}.")
        self.__seats_occupied = value
    
    def get_toplivo(self):
        return self.__toplivo

    def set_toplivo(self, value):
        if value > self.__fuel_tank:
            raise ValueError(f"Количество топлива не может превышать {self.__fuel_tank} литров.")
        self.__toplivo = value

    
    def get_maslo(self):
        return self.__maslo

    def set_maslo(self, value):
        if value > self.__kartet_tank:
            raise ValueError(f"Количество масла не может превышать {self.__kartet_tank} литров.")
        self.__maslo = value
    
    def get_luggage(self):
        return self.__luggage

    def set_luggage(self, value):
        if value > self.__luggage_spaces:
            raise ValueError(f"Количество багажа не может превышать {self.__luggage_spaces} мест.")
        self.__luggage = value
    
    def get_fuel_tank(self):
        return self.__fuel_tank

    
    def get_kartet_tank(self):
        return self.__kartet_tank

    
    def get_luggage_spaces(self):
        return self.__luggage_spaces

    def display_info(self):
        print(f"Скорость: {self.__speed} км/ч")
        print(f"Пройденное расстояние: {self.__distance} км")
        print(f"Максимальная скорость: {self.__max_speed} км/ч")
        print(f"Пассажиры: {self.__passengers} (занято мест: {self.__seats_occupied}, свободно: {self.__empty_seats})")
        print(f"Количество топлива: {self.__toplivo} литров")
        print(f"Количество масла: {self.__maslo} литров")
        print(f"Количество багажа: {self.__luggage} (макс. мест: {self.__luggage_spaces})")

    speed = property(get_speed, set_speed)
    distance = property(get_distance, set_distance)
    passengers = property(get_passengers, set_passengers)
    max_speed = property(get_max_speed)
    empty_seats = property(get_empty_seats, set_empty_seats)
    seats_occupied = property(get_seats_occupied, set_seats_occupied)
    toplivo = property(get_toplivo, set_toplivo)
    maslo = property(get_maslo, set_maslo)
    luggage = property(get_luggage, set_luggage)
    fuel_tank = property(get_fuel_tank)
    kartet_tank = property(get_kartet_tank)
    luggage_spaces = property(get_luggage_spaces)


bus1 = Bus(80, 500)
bus2 = Bus(60, 300)
bus3 = Bus(100, 1200)

# Установка значений для автобусов через сеттеры
bus1.passengers = ["Пассажир1", "Пассажир2", "Пассажир3"]
bus1.toplivo = 80
bus1.maslo = 5
bus1.luggage = 100

bus2.passengers = ["Пассажир4", "Пассажир5"]
bus2.toplivo = 60
bus2.maslo = 4
bus2.luggage = 50

bus3.passengers = ["Пассажир6", "Пассажир7", "Пассажир8", "Пассажир9"]
bus3.toplivo = 90
bus3.maslo = 5.5
bus3.luggage = 130

# Вывод информации об автобусах
bus1.display_info()
print("\n")
bus2.display_info()
print("\n")
bus3.display_info()