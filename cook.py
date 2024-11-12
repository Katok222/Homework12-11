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
                if ingredient_data[0]:  # Пропускаем пустые строки
                    if len(ingredient_data) == 3:  # Проверяем правильный формат
                        ingredient = {
                            'ingredient_name': ingredient_data[0],
                            'quantity': int(ingredient_data[1]),
                            'measure': ingredient_data[2]
                        }
                        ingredients.append(ingredient)

            cook_book[dish_name] = ingredients
            
            # Добавляем отладочные выводы в цикл
            print(f"Читаем блюдо: {dish_name}")  # После считывания имени блюда
            print(f"Количество ингредиентов: {ingredient_count}")  # После считывания количества ингредиентов
            print(f"Ингредиенты: {ingredient_data}")  # После считывания каждого ингредиента

    return cook_book

if __name__ == "__main__":
    file_path = 'C:\\Users\\DNS\\Desktop\\hwork\\files\\recipes.txt'  # Укажите путь к вашему файлу с рецептами
    cook_book = read_recipes_from_file(file_path)
    print(cook_book)