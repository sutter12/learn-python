computer = {
    "brand": "Apple",
    "model": "Macbook Pro",
    "screensize": 13,
    "color": "Silver",
    "price": 1299,
    "thunderbolt ports": 2,
    "year": 2020
}
money = 1500
print(computer)
print(computer["brand"])

if money == computer["price"]:
    print("You can buy")
else:
    print("no funds :(")

computer["price"] = 1600
computer["weight"] = "2lb"
print(computer)

for x in computer:
    print(x)

for x in computer:
    print(computer[x])