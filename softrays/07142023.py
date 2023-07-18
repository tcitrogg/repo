# dicts
# keys: int, float, complex, str, bytes
# values: any type

bio = {
    "radiance": {
        "fullname": "Radiance B",
        "age": 293
    },
    "luffy": {
        "fullname": "Monkey D Luffy",
        "age": 20
    }
}
# print(bio)
# bio.update({"sanji": {"fullname": "Vinsmoke Sanji", "age": 22}})
# print(bio.get("radiance"))

# for each_bio in bio:
#     print(f"{each_bio}:: {bio[each_bio]}")

# for each_key, each_val in bio.items():
#     print(f"key is {each_key} | val is {each_val}")

# while loop

index = 0

# while index < 5:
#     print(index)
#     index = index + 1


# break keyword

# while index < 10:
#     if index == 5:
#         break
#     print(index)
#     index += 1
    

# while index < 10:
#     if index % 2 == 0:
#         print(index)
#     index += 1


# while index < 10:
#     if index == 5:
#         pass
#     else:
#         print(index)
#     index += 1

# while index < 10:
#     if index != 5:
#         print(index)
#     index += 1

running = True

while running:
    cmd = input("C:/users/kgyk> ")
    if cmd == "exit":
        break
    else:
        print(f"you entered {cmd}")

print("the end")