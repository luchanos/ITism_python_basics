# имя, цену, категорию
# product = ["Orange", 100, "Fruits"]
# product_dict = {
#     "name": "Orange",
#     "price": 100,
#     "category": "Fruits"
# }


# product_dict = dict()

# name = input("Enter 'name' of the product: ")
# price = int(input("Enter 'price' of the product: "))
# category = input("Enter 'category' of the product: ")
# product_dict["name"] = name
# product_dict["price"] = price
# product_dict["category"] = category
# print(product_dict)

# credit = int(input("Credit card balance: "))
# if product_dict["price"] > credit:
#     print("Not enough money!")
# elif product_dict["price"] == credit:
#     print("Purchase successful! Warning: 0 balance of card!")
# else:
#     print("Purchase successful!")


orange_dict = {
    "name": "Orange",
    "price": 100,
    "category": "Fruits"
}

potato_dict = {
    "name": "potato",
    "price": 20,
    "category": "Vegetables"
}

carrot_dict = {
    "name": "carrot",
    "price": 45,
    "category": "Vegetables"
}

shop_product_list = [orange_dict, potato_dict, carrot_dict]

for product in shop_product_list:
    if product["name"] == "potato":
        continue
    print(product)

print("*" * 100)

num = 0
while True:
    if shop_product_list[num]["name"] == "potato":
        num += 1
        continue
    print(shop_product_list[num])
    num += 1
    if num >= len(shop_product_list):
        break

















