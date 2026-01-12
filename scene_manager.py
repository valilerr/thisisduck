import pygame

class SceneManager:
    def __init__(self):
        self.scenes = {}
        self.prev_scene = None
        self.current_scene = None

    def add_scene(self, name, scene):
        self.scenes[name] = scene
        print(f'Added Scene [{name}]')

    def remove_scene(self, name):
        self.scenes[name] = None
        print(f'Scene [{name}] removed')

    def start_scene(self, name):
        if self.scenes.get(name):
            self.prev_scene = self.current_scene
            self.current_scene = self.scenes[name](self)
            print(f'Scene [{name}] started.')
        else:
            print(f'Scene [{name}] not found.')

    def draw(self, screen):
        self.current_scene.draw(screen)

    def handle_events(self, event, scene_manager):
        self.current_scene.handle_events(event, scene_manager)