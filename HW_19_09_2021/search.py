import json

with open('./data.json', 'r') as file:
    data = json.load(file)

client_name = input('client ')
order_data = input('time of order ')
result = []

for order in data['db']['orders']:
    if order['client']['name'] == client_name and order['data'] == order_data:
        result.append(order)
print(result)