import pygame
from scene import Scene
from ui_elements.button import Button

class StartMenu(Scene):
    def __init__(self, scene_manager):
        self.title = pygame.font.Font('fonts/Unbounded-Medium.ttf', 25).render('This Is Duck!', True, (200, 200, 200))
        self.play_button = Button((300, 275), (200, 50), 'Играть')

    def draw(self, screen):
        screen.fill((25, 35, 40))
        screen.blit(self.title, (screen.get_width() / 2 - self.title.get_width() / 2, 200))

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