class Clients:
    def __init__(self, phone, name, rating) -> None:
        self.phone = phone
        self.name = name
        self.clients_rating = rating


class Cars:
    def __init__(self, model, number, color, condition) -> None:
        self.model = model
        self.number = number
        self.color = color
        self.condition = condition


class Drivers:
    def __init__(self, name, car, rating) -> None:
        self.name = name
        self.car = car
        self.rating = rating


class Track:
    def __init__(self, where, where_t) -> None:
        self.where = where
        self.where_t = where_t


class Order:
    def __init__(self, data, track, client, driver, cost) -> None:
        self.data = data
        self.track = track
        self.client = client
        self.driver = driver
        self.cost = cost


class Stock:
    def __init__(self, promocode, time_of_action, condition_of_action):
        self.promocode = promocode
        self.time_of_action = time_of_action
        self.condition_of_action = condition_of_action


class Rate:
    def __init__(self, cost_economy, cost_comfort, cost_biznes):
        self.cost_economy = cost_economy
        self.cost_comfort = cost_comfort
        self.cost_biznes = cost_biznes


class Application:
    def __init__(self, price, route, driver_rating):
        self.price = price
        self.route = route
        self.driver_rating = friver_rating
