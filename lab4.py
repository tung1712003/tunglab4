from itertools import combinations
# Словарь предметов: обозначение, размер, очки выживания
stuff_dict = {
    'r': ('rifle', 3, 25),
    'p': ('pistol', 2, 15),
    'a': ('ammo', 2, 15),
    'm': ('medkit', 2, 20),
    'i': ('inhaler', 1, 5),
    'k': ('knife', 1, 15),
    'x': ('axe', 3, 20),
    't': ('talisman', 1, 25),
    'f': ('flask', 1, 15),
    'd': ('antidot', 1, 10),
    's': ('supplies', 2, 20),
    'c': ('crossbow', 2, 20)
}



maximum_space = 2 * 4  # Предполагая, что у Тома есть 2 строки и 4 столбца в рюкзаке

# Начальные очки выживания и наличие болезни
current_survival_points = 10  # Предполагая, что у Тома начально 10 очка выживания
infection_present = True
asthma_present = False

#Инициализация матрицы для хранения очков выживания с использованием понимания списка
survival_matrix = [[0 for each_space in range(maximum_space + 1)] for each_space in range(len(stuff_dict) + 1)]


# Заполнение матрицы
for i, item in enumerate(stuff_dict.values()):
    symbol, size, points = item
    for space in range(maximum_space + 1):
        if size > space:
            survival_matrix[i + 1][space] = survival_matrix[i][space]
        else:
            survival_matrix[i + 1][space] = max(
                survival_matrix[i][space],
                survival_matrix[i + 1][space - size] + points
            )

# Получение выбранных предметов
selected_items = []
space = maximum_space
for i in range(len(stuff_dict), 0, -1):
    if survival_matrix[i][space] != survival_matrix[i - 1][space]:
        selected_items.append(list(stuff_dict.keys())[i - 1])
        space -= stuff_dict[selected_items[-1]][1]

# Отображение выбранных предметов в виде двумерного массива
inventory = [selected_items[i:i+4] for i in range(0, len(selected_items), 4)]

# Проверка на наличие ингалятора или антидота
if 'i' not in selected_items and asthma_present:
    selected_items.append('i')
if 'd' not in selected_items and infection_present:
    selected_items.append('d')

# результат
print("Ивентарь:")
for row in inventory:
    print(row)
print(f"Итоговые очки выживания: {survival_matrix[len(stuff_dict)][maximum_space]}")




#Допзадание

# Максимальное количество ячеек в рюкзаке
max_cells = 7

valid_combinations = []
for r in range(1, len(stuff_dict) + 1):
    for combination in combinations(stuff_dict.keys(), r):
        total_space = sum(stuff_dict[item][1] for item in combination)
        total_survival_points = sum(stuff_dict[item][2] for item in combination)
        if total_space <= max_cells and total_survival_points > 0:
            valid_combinations.append(combination)

# Выводим найденные комбинации
for i, combination in enumerate(valid_combinations, 1):
    print(f"Комбинация {i}: {combination}")