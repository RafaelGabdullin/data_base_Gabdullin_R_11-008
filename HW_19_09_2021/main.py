import json
from typing import cast
from classess import Cars, Clients, Drivers, Order, Track, Application, Rate, Stock

clients = [Clients('79274288749', 'Raphael', '4,8'),
           Clients('89274056108', 'Danil', '4,9')]
cars = [Cars('BMV', 'a 135 rd', 'white', 'Good'), Cars('Mersedes', '0 345 00', 'black', 'Normal')]
drivers = [Drivers('Vasiliy', cars[0], 4.6), Drivers('Kostya', cars[1], 4.1)]
tracks = [Track('xxx', 'yyy'), Track('zzz', 'ccc')]
orders = [Order('13.09.2021 16:45', tracks[0], clients[0], drivers[0], cost=250),
          Order('13.08.2021 13:32', tracks[1], clients[1], drivers[1], cost=300)]
applications = []
db = {
    'clients': list(cl.__dict__ for cl in clients),

    'drivers': list({'name': dr.name,
                     'car': {'model': dr.car.model, 'number': dr.car.number},
                     'rating': dr.rating} for dr in drivers),

    'cars': list(car.__dict__ for car in cars),

    'orders': list({'data': der.data,
                    'track': {'where': der.track.where, 'where_t': der.track.where_t},
                    'client': {'phone': der.client.phone, 'name': der.client.name},
                    'driver': {'name': der.driver.name,
                               'car': {'model': der.driver.car.model, 'number': der.driver.car.number},
                               'rating': der.driver.rating},
                    'cost': der.cost} for der in orders),

    'tracks': list(tr.__dict__ for tr in tracks)
}

data = {'db': db}
print(data)
with open('./data.json', 'w', encoding='utf8') as f:
    json.dump(data, f)
