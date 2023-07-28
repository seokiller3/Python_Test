things = {
    'Тент': 1500,
    'Спальник': 1000,
    'Горелка': 300,
    'Палатка': 2000,
    'Кружка': 200,
    'Еда': 1000
}

max_weight_capacity = 4000

sorted_items = sorted(things.items(), key=lambda x: x[1])
backpack = {}
current_weight = 0

for item, weight in sorted_items:
    if current_weight + weight <= max_weight_capacity:
        backpack[item] = weight
        current_weight += weight

print(backpack)
