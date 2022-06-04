

class UserOS:
    def __init__(self, id, user_id, username, phone_number, language, barber_id, step):
        self.id = id
        self.user_id = user_id
        self.username = username
        self.phone_number = phone_number
        self.language = language
        self.barber_id = barber_id
        self.step = step

class Barber:
    def __init__(self, id, user_id, photo, fullname, shop_id, start_time, end_time):
        self.id = id
        self.user_id = user_id
        self.photo = photo
        self.fullname = fullname
        self.shop_id = shop_id
        self.start_time = start_time
        self.end_time = end_time

class BarberShop:
    def __init__(self, id,  name, photo, location):
        self.id = id
        self. name = name
        self.photo = photo
        self.location = "longitude:latitude".split(":") if location is not None else location.split(":")

class Order:
    def __init__(self, id,barber_id, customer_id, time, day, service_id):
        self.id = id
        self.barber_id = barber_id
        self.customer_id = customer_id
        self.time = time
        self.day = day
        self.service_id = service_id

class Service:
    def __init__(self, id, name):
        self.id = id
        self.name = name
