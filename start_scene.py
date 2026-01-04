import pygame
from scene import Scene
from ui_elements.button import Button

class StartScene(Scene):
    def __init__(self):
        self.title = pygame.font.Font('fonts/Unbounded-Medium.ttf', 25).render('This Is Duck!', True, (200, 200, 200))
        self.text_label = pygame.font.Font('fonts/Unbounded-Regular.ttf', 18).render('Выберите и запомните одну из картинок', True, (175, 175, 175))
        self.image = pygame.image.load('images/all.png')
        self.next_button = Button((300, 525), (200, 50), 'Загадал(а)')

    def draw(self, screen):
        screen.fill((25, 35, 40))
        screen.blit(self.title, (screen.get_width() / 2 - self.title.get_width() / 2, 25))
        screen.blit(self.text_label, (screen.get_width() / 2 - self.text_label.get_width() / 2, 75))
        screen.blit(self.image, (screen.get_width() / 2 - self.image.get_width() / 2, screen.get_height() / 2 - self.image.get_height() / 2 + 10))

        self.next_button.draw(screen)
        self.next_button.check_hover(pygame.mouse.get_pos())

        if self.next_button.is_hovered:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

    def handle_events(self, event, scene_manager):
        if self.next_button.is_clicked(pygame.mouse.get_pos(), event):
            scene_manager.start_scene('QuestionsScene')
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)