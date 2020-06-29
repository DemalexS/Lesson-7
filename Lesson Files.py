with open("recipes.txt", encoding = "utf8") as f:
    cook_book = {}
    while True:
        dish_name = f.readline().strip()
        if not dish_name:
            break

        ingr_num = f.readline().strip()

        i = 0
        ingridients = []
        while i < int(ingr_num):
            ingr = f.readline().strip().split(" | ")
            ingr = {'ingredient_name': ingr[0], 'quantity': ingr[1], 'measure': ingr[2]}
            ingridients.append(ingr)
            #print(ingr)
            i += 1

        cook_book[dish_name] = ingridients
        f.readline()



def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for ingridient in cook_book[dish]:
            if ingridient['ingredient_name'] in shop_list.keys():
                shop_list[ingridient['ingredient_name']]['quantity'] = int(shop_list[ingridient['ingredient_name']]['quantity']) + int(ingridient['quantity']) * person_count

            else:
                shop_list[ingridient['ingredient_name']] = {'measure': ingridient['measure'], 'quantity': int(ingridient['quantity']) * person_count}



    print(shop_list)

get_shop_list_by_dishes(["Омлет", "Фахитос"], 2)