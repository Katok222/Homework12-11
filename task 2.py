def read_recipes_from_file(file_path):
    cook_book = {}

    with open(file_path, 'r', encoding='utf-8') as file:
        while True:
            dish_name = file.readline().strip()
            if not dish_name:  # Если достигнут конец файла
                break

            ingredient_count = int(file.readline().strip())
            ingredients = []

            for _ in range(ingredient_count):
                ingredient_data = file.readline().strip().split(' | ')
                if len(ingredient_data) == 3:  # Проверяем правильный формат
                    ingredient = {
                        'ingredient_name': ingredient_data[0],
                        'quantity': int(ingredient_data[1]),
                        'measure': ingredient_data[2]
                    }
                    ingredients.append(ingredient)

            cook_book[dish_name] = ingredients

    return cook_book

def get_shop_list_by_dishes(dishes, person_count, cook_book):
    shop_list = {}

    for dish in dishes:
        if dish in cook_book:  # Проверяем, что блюдо есть в кулинарной книге
            ingredients = cook_book[dish]
            for ingredient in ingredients:
                ingredient_name = ingredient['ingredient_name']
                quantity = ingredient['quantity'] * person_count
                measure = ingredient['measure']

                if ingredient_name in shop_list:
                    shop_list[ingredient_name]['quantity'] += quantity  # Увеличиваем количество
                else:
                    shop_list[ingredient_name] = {'measure': measure, 'quantity': quantity}  # Добавляем новый ингредиент

    return shop_list

if __name__ == "__main__":
    file_path = 'C:\\Users\\DNS\\Desktop\\hwork\\files\\recipes.txt'  # Укажите путь к вашему файлу с рецептами
    cook_book = read_recipes_from_file(file_path)

    # Пример вызова функции
    dishes = ['Запеченный картофель', 'Омлет']
    person_count = 2
    result = get_shop_list_by_dishes(dishes, person_count, cook_book)
    print(result)