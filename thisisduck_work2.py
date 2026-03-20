from time import sleep

class ThisIsDuck:
    def __init__(self):
        while True:
            self.start_game()
    
    items = [
        {'название': 'Утка', 'изображение': 'duck.jpg', 'свойства': {'живое': 'живое', 'цвет': 'желтый', 'тип': 'животное'}},
        {'название': 'Яблоко', 'изображение': 'apple.jpg', 'свойства': {'живое': 'живое', 'цвет': 'красный', 'тип': 'фрукт'}},
        {'название': 'Лягушка', 'изображение': 'frog.jpg','свойства': {'живое': 'живое', 'цвет': 'зеленый', 'тип': 'животное'}},
        {'название': 'Игрушечная утка', 'изображение': 'duck_toy.jpg','свойства': {'живое': 'не живое', 'цвет': 'желтый', 'тип': 'животное'}},
        {'название': 'Арбуз', 'изображение': 'watermelon.jpg','свойства': {'живое': 'живое', 'цвет': 'зеленый', 'тип': 'фрукт'}},
        {'название': 'Банан', 'изображение': 'banana.jpg','свойства': {'живое': 'живое', 'цвет': 'желтый', 'тип': 'трава'}},
        {'название': 'Клубника', 'изображение': 'strawberry.jpg','свойства': {'живое': 'живое', 'цвет': 'красный', 'тип': 'ягода'}},
        {'название': 'Лебедь', 'изображение': 'swan.jpg','свойства': {'живое': 'живое', 'цвет': 'белый', 'тип': 'птица'}},
        {'название': 'Кактус', 'изображение': 'cactus.jpg','свойства': {'живое': 'живое', 'цвет': 'зеленый', 'тип': 'растение'}},
        {'название': 'Игрушечный заяц', 'изображение': 'rabbit_toy.jpg','свойства': {'живое': 'не живое', 'цвет': 'белый', 'тип': 'животное'}},
        {'название': 'Кот', 'изображение': 'cat.jpg','свойства': {'живое': 'живое', 'цвет': 'серый', 'тип': 'животное'}},
        {'название': 'Собака', 'изображение': 'dog.jpg','свойства': {'живое': 'живое', 'цвет': 'коричневый', 'тип': 'животное'}},
        {'название': 'Орёл', 'изображение': 'eagle.jpg','свойства': {'живое': 'живое', 'цвет': 'коричневый', 'тип': 'птица'}},
        {'название': 'Лимон', 'изображение': 'limon.jpg','свойства': {'живое': 'живое', 'цвет': 'желтый', 'тип': 'фрукт'}},
        {'название': 'Апельсин', 'изображение': 'orange.jpg','свойства': {'живое': 'живое', 'цвет': 'оранжевый', 'тип': 'фрукт'}},
        {'название': 'Игрушечный медведь', 'изображение': 'bear_toy.jpg','свойства': {'живое': 'не живое', 'цвет': 'коричневый', 'тип': 'животное'}}
    ]

    def check_answer(self, answer: str) -> bool:
        if answer.lower() == 'да':
            return True
        else:
            return False
        
    def max(self, numbers: list) -> int:
        max_number = -10000000

        for number in numbers:
            if number > max_number:
                max_number = number

        return max_number
        
    def ask_questions(self, items: list) -> dict:
        answers = {}
        last_questions = []
        keys = []
        color = 'цвет'
        alive = 'живое'

        for item in items:
            keys.append(len(item['свойства']))

        key_count = self.max(keys)

        for item in items:
            if len(answers) < key_count:
                for key, value in item['свойства'].items():
                    need_continue = False
                    for question in last_questions:
                        if key == question or value == question:
                            need_continue = True
                            break

                    if need_continue:
                        continue

                    if key != color:
                        question = f'Это {value}?'
                    elif key == color:
                        question = f'Оно {value[0:-2]}ого цвета?'
                    else:
                        question = f'Оно {value} формы?'

                    bool_answer = self.check_answer(input(question+'\n'))

                    if bool_answer:
                        answers[key] = value
                        last_questions.append(key)
                    elif key == alive:
                        answers[key] = 'не живое'
                        last_questions.append(key)
                    elif key == color:
                        last_questions.append(value)
                    elif key == 'тип':
                        last_questions.append(value)
            else:
                return answers
    
    def check(self, items: list, answers: dict):
        for item in items:
            need_delete = False
            for key, value in answers.items():
                if item['свойства'].get(key) != value:
                    need_delete = True

            if need_delete:
                items.remove(item)
                self.check(items, answers)

    def open_all_images(self):
        img = plt.imread('images/all.png')
        plt.imshow(img)
        plt.axis('off')
        plt.show()



    def start_game(self):
        game_items = list(self.items)

        print('Загадайте картинку из списка (животное, фрукт, ягода, растение или птица)')
        for i in range(len(game_items)):
            print(f'{i + 1}. {game_items[i]['название']}')

        #self.open_all_images()

        sleep(3)

        print('\nЗагадали?')
        ready = self.check_answer(input())

        if ready:
            answers = self.ask_questions(game_items)
            self.check(game_items, answers)
            print(f'\nВы загадали картинку "{game_items[0]['название']}"\n')
            sleep(5)

ThisIsDuck()