records = {}

records["00/00AZ000"] = {
    "fullname": "Radiance Be",
    "age": 2
}

user = records["00/00AZ000"]
user["email"] = "bnierimi/tcitrogg"
user["age"] = 10
# print(user)

basket = [
    "apple", "banana", "mango"
]

last_item = basket.pop()
print(last_item)

print(basket[-1])