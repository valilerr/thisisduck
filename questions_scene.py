import pygame

from scene import Scene
from ui_elements.button import Button

game_items = [
    {'название': 'Утка', 'изображение': 'duck.png', 'свойства': {'живое': 'живое', 'цвет': 'желтый', 'тип': 'животное'}},
    {'название': 'Яблоко', 'изображение': 'apple.png', 'свойства': {'живое': 'живое', 'цвет': 'красный', 'тип': 'фрукт'}},
    {'название': 'Лягушка', 'изображение': 'frog.png', 'свойства': {'живое': 'живое', 'цвет': 'зеленый', 'тип': 'животное'}},
    {'название': 'Игрушечная утка', 'изображение': 'duck_toy.png', 'свойства': {'живое': 'не живое', 'цвет': 'желтый', 'тип': 'животное'}},
    {'название': 'Арбуз', 'изображение': 'watermelon.png', 'свойства': {'живое': 'живое', 'цвет': 'зеленый', 'тип': 'фрукт'}},
    {'название': 'Банан', 'изображение': 'banana.png', 'свойства': {'живое': 'живое', 'цвет': 'желтый', 'тип': 'трава'}},
    {'название': 'Клубника', 'изображение': 'strawberry.png', 'свойства': {'живое': 'живое', 'цвет': 'красный', 'тип': 'ягода'}},
    {'название': 'Лебедь', 'изображение': 'swan.png', 'свойства': {'живое': 'живое', 'цвет': 'белый', 'тип': 'птица'}},
    {'название': 'Кактус', 'изображение': 'cactus.png', 'свойства': {'живое': 'живое', 'цвет': 'зеленый', 'тип': 'растение', 'колючесть': 'колючее'}},
    {'название': 'Игрушечный заяц', 'изображение': 'rabbit_toy.png', 'свойства': {'живое': 'не живое', 'цвет': 'белый', 'тип': 'животное'}},
    {'название': 'Кот', 'изображение': 'cat.png', 'свойства': {'живое': 'живое', 'цвет': 'серый', 'тип': 'животное'}},
    {'название': 'Игрушечная собака', 'изображение': 'dog_toy.png', 'свойства': {'живое': 'не живое', 'цвет': 'коричневый', 'тип': 'животное'}},
    {'название': 'Орёл', 'изображение': 'eagle.png', 'свойства': {'живое': 'живое', 'цвет': 'коричневый', 'тип': 'птица'}},
    {'название': 'Лимон', 'изображение': 'limon.png', 'свойства': {'живое': 'живое', 'цвет': 'желтый', 'тип': 'фрукт'}},
    {'название': 'Апельсин', 'изображение': 'orange.png', 'свойства': {'живое': 'живое', 'цвет': 'оранжевый', 'тип': 'фрукт'}},
    {'название': 'Игрушечный медведь', 'изображение': 'bear_toy.png', 'свойства': {'живое': 'не живое', 'цвет': 'коричневый', 'тип': 'животное'}},
    {'название': 'Игрушечный осьминог', 'изображение': 'octopus_toy.png', 'свойства': {'живое': 'не живое', 'цвет': 'бело-голубой', 'тип': 'животное', 'плавает': 'плавает'}},
    {'название': 'Чебурашка', 'изображение': 'cheburashka_toy.png', 'свойства': {'живое': 'не живое', 'цвет': 'коричневый', 'тип': 'животное', 'умеет говорить': 'умеет говорить'}},
    {'название': 'Игрушечный жираф', 'изображение': 'giraffe_toy.png', 'свойства': {'живое': 'не живое', 'цвет': 'желтый', 'тип': 'животное', 'высота': 'высокое'}},
    {'название': 'Игрушечная панда', 'изображение': 'panda_toy.png', 'свойства': {'живое': 'не живое', 'цвет': 'бело-черный', 'тип': 'животное', 'что ест': 'ест бамбук'}},
    {'название': 'Игрушечная белка', 'изображение': 'squirrel_toy.png', 'свойства': {'живое': 'не живое', 'цвет': 'коричневый', 'тип': 'животное', 'что ест': 'ест орехи'}},
    {'название': 'Игрушечная лиса', 'изображение': 'fox_toy.png', 'свойства': {'живое': 'не живое', 'цвет': 'оранжевый', 'тип': 'животное'}},
    {'название': 'Игрушечный енот', 'изображение': 'raccoon_toy.png', 'свойства': {'живое': 'не живое', 'цвет': 'бело-черный', 'тип': 'животное'}},
    {'название': 'Капибара', 'изображение': 'capibara.png', 'свойства': {'живое': 'живое', 'цвет': 'коричневый', 'тип': 'животное'}},
    {'название': 'Игрушечная шиншилла', 'изображение': 'chinchilla_toy.png', 'свойства': {'живое': 'не живое', 'цвет': 'бело-серый', 'тип': 'животное'}}
]

class QuestionsScene(Scene):
    def __init__(self, scene_manager):
        self.yes_button = Button((195, 325), (200, 50), 'Да')
        self.no_button = Button((405, 325), (200, 50), 'Нет')
        self.question_label = pygame.font.Font('fonts/Unbounded-Regular.ttf', 20).render('', True, (200, 200, 200))
        self.questions = {}
        self.is_asked = False
        self.current_key = ''
        self.current_value = ''
        self.items = list(game_items)
        print(f'Items count: {len(self.items)}')
        self.ask_questions()

    def ask_questions(self):
        for item in self.items:
            need_break = False
            for key, value in item['свойства'].items():
                if self.questions.get(key) == value or key == 'живое' and self.questions.get(key):
                    continue

                if key != 'цвет' and key != 'плавает' and key != 'умеет говорить' and key != 'высота' and key != 'что ест':
                    current_question = f'Это {value}?'
                elif key == 'цвет':
                    current_question = f'Оно {value[0:-2]}ого цвета?'
                else:
                    current_question = f'Оно {value}?'

                self.question_label = pygame.font.Font('fonts/Unbounded-Regular.ttf', 20).render(current_question, True, (200, 200, 200))

                self.current_key = key
                self.current_value = value
                self.questions[key] = value

                self.is_asked = True
                need_break = True
                print(current_question)
                print(self.current_key)
                break

            if need_break:
                break

    def check(self, key, value, answer):
        for item in self.items:
            if answer and item['свойства'].get(key) != value:
                self.items.remove(item)
                print(*self.items)
                self.check(key, value, answer)
            elif not answer and item['свойства'].get(key) == value:
                self.items.remove(item)
                print(*self.items)
                self.check(key, value, answer)



    def draw(self, screen):
        screen.fill((25, 35, 40))
        screen.blit(self.question_label, (screen.get_width() / 2 - self.question_label.get_width() / 2, 200))
        self.yes_button.draw(screen)
        self.no_button.draw(screen)

        self.yes_button.check_hover(pygame.mouse.get_pos())
        self.no_button.check_hover(pygame.mouse.get_pos())

        if self.yes_button.is_hovered or self.no_button.is_hovered:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

    def handle_events(self, event, scene_manager):
        if self.yes_button.is_clicked(pygame.mouse.get_pos(), event):
            self.check(self.current_key, self.current_value, True)
            print('Да')
            self.ask_questions()
        elif self.no_button.is_clicked(pygame.mouse.get_pos(), event):
            self.check(self.current_key, self.current_value, False)
            print('Нет')
            self.ask_questions()

        if len(self.items) == 1:
            scene_manager.start_scene('ResultScene')
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)