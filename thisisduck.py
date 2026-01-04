import pygame

from result_scene import ResultScene
from start_scene import StartScene
from scene_manager import SceneManager
from start_menu import StartMenu
from questions_scene import QuestionsScene

scene_manager = SceneManager()
scene_manager.add_scene('StartMenu', StartMenu)
scene_manager.add_scene('StartScene', StartScene)
scene_manager.add_scene('QuestionsScene', QuestionsScene)
scene_manager.add_scene('ResultScene', ResultScene)

class ThisIsDuck:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption('ThisIsDuck!')
        self.running = True
        scene_manager.start_scene('StartMenu')

        while self.running:
            pygame.display.update()

            scene_manager.draw(self.screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                scene_manager.handle_events(event, scene_manager)

ThisIsDuck()