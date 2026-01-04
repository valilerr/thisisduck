import pygame

from scene import Scene
from questions_scene import QuestionsScene

class ResultScene(Scene):
    def __init__(self):
        self.title = pygame.font.Font('fonts/Unbounded-Medium.ttf', 25).render('This Is Duck!', True, (200, 200, 200))
        self.result_item = QuestionsScene().items[0]
        self.image = pygame.image.load(f'images/{self.result_item['изображение']}')
        self.result_label = pygame.font.Font('fonts/Unbounded-Regular.ttf', 25).render(f'Вы загадали картинку "{self.result_item['название']}"!', True, (200, 200, 200))

    def draw(self, screen):
        screen.fill((25, 35, 40))
        screen.blit(self.title, (screen.get_width() / 2 - self.title.get_width() / 2, 25))
        screen.blit(self.image, (screen.get_width() / 2 - self.image.get_width() / 2, screen.get_height() / 2 - self.image.get_height() / 2))
        screen.blit(self.result_label, (screen.get_width() / 2 - self.result_label.get_width() / 2, 100))

    def handle_events(self, event, scene_manager):
        pass