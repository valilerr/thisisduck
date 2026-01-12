import pygame

from scene import Scene
from ui_elements.button import Button


class ResultScene(Scene):
    def __init__(self, scene_manager):
        self.result_item = scene_manager.prev_scene.items[0]
        self.image = pygame.image.load(f'images/{self.result_item['изображение']}')
        self.result_label = pygame.font.Font('fonts/Unbounded-Regular.ttf', 25).render(f'Вы загадали картинку "{self.result_item['название']}"!', True, (200, 200, 200))
        self.play_button = Button((275, 500), (250, 50), 'Играть еще раз')

    def draw(self, screen):
        screen.fill((25, 35, 40))
        screen.blit(self.image, (screen.get_width() / 2 - self.image.get_width() / 2, screen.get_height() / 2 - self.image.get_height() / 2))
        screen.blit(self.result_label, (screen.get_width() / 2 - self.result_label.get_width() / 2, 100))
        self.play_button.draw(screen)
        self.play_button.check_hover(pygame.mouse.get_pos())

        if self.play_button.is_hovered:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

    def handle_events(self, event, scene_manager):
        if self.play_button.is_clicked(pygame.mouse.get_pos(), event):
            scene_manager.start_scene('StartScene')
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)