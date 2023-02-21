print("Lista zakupów")
shopping_dict = {"piekarnia": ["chleb", "pączek", "bułki"],
                 "warzywniak": ["marchew", "seler", "rukola"],
                 }
print(shopping_dict)

print("")

num_items = []

for store, items in shopping_dict.items():
    item_list = [item.title() for item in items]
    for i in items:
        num_items.append(i)
    print(f"Idę do {store.title()} i kupuję {item_list}.")
print(f"W sumie kupuję {len(num_items)} produktów.")

#Pozdrawiam Patryk! :D