from time import sleep

def check_answer(answer):
    if answer == 'да':
        return True
    else:
        return False

def check_item(items_list, index, answer, yes_or_no):
    for item in items_list:
        if yes_or_no and item[index] != answer:
            items_list.remove(item)
            check_item(items_list, index, answer, yes_or_no)
        elif not yes_or_no and item[index] == answer:
            items_list.remove(item)
            check_item(items_list, index, answer, yes_or_no)

items = [
    ['Утка', 'живое', 'желтый', 'животное'],
    ['Яблоко', 'живое', 'красный', 'фрукт'],
    ['Лягушка', 'живое', 'зеленый', 'животное'],
    ['Игрушечная утка', 'не живое', 'желтый', 'животное'],
    ['Арбуз', 'живое', 'зеленый', 'фрукт'],
    ['Банан', 'живое', 'желтый', 'фрукт'],
    ['Клубника', 'живое', 'красный', 'ягода'],
    ['Лебедь', 'живое', 'белый', 'птица'],
    ['Кактус', 'живое', 'зеленый', 'растение'],
    ['Игрушечный заяц', 'не живое', 'белый', 'животное'],
    ['Кот', 'живое', 'серый', 'животное'],
    ['Собака', 'живое', 'черный', 'животное'],
    ['Орёл', 'живое', 'черный', 'птица'],
    ['Лимон', 'живое', 'желтый', 'фрукт'],
    ['Апельсин', 'живое', 'оранжевый', 'фрукт'],
    ['Игрушечный медведь', 'не живое', 'коричневый', 'животное']
]

questions = [['Это живое?', 1, 'живое'],
             ['Это фрукт?', 3, 'фрукт'],
             ['Это животное', 3, 'животное'],
             ['Это птица?', 3, 'птица'],
             ['Это ягода?', 3, 'ягода'],
             ['Оно желтого цвета?', 2, 'желтый'],
             ['Оно серого цвета?', 2, 'серый'],
             ['Оно коричневого цвета?', 2, 'коричневый'],
             ['Оно оранжевого цвета?', 2, 'оранжевый'],
             ['Оно черного цвета?', 2, 'черный'],
             ['Оно красного цвета?', 2, 'красный'],
             ['Оно зеленого цвета?', 2, 'зеленый'],
             ['Оно белого цвета?', 2, 'белый']
]

def start_game():
    game_items = list(items)

    print('Загадайте картинку из списка (животное, фрукт, ягода, растение или птица)')
    for i in range(len(game_items)):
        print(f'{i + 1}. {game_items[i][0]}')

    sleep(3)

    print('\nЗагадали?')
    ready = check_answer(str.lower(input()))

    if ready:
        for question in questions:
            if len(game_items) != 1:
                print(question[0])
                bool_answer = check_answer(str.lower(input()))

                check_item(game_items, question[1], question[2], bool_answer)


        print('')
        print(f'\nВы загадали картинку "{game_items[0][0]}"\n')
        sleep(5)

while True:
    start_game()