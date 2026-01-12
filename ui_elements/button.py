import pygame

class Button:
    def __init__(self, position: tuple[int, int], size: tuple[int, int], text: str, color: tuple[int, int, int] | tuple[int, int, int, int]=(32, 32, 32), hover_color: tuple[int, int, int] | tuple[int, int, int, int]=(44, 45, 46)):
        self.rect = pygame.Rect(position[0], position[1], size[0], size[1])
        self.color = color
        self.hover_color = hover_color
        self.text = text
        self.is_hovered = False
        self.hover_status = 0
        self.font = pygame.font.Font('fonts/Unbounded-Medium.ttf', 16)

    def draw(self, screen):
        color = self.hover_color if self.is_hovered else self.color

        pygame.draw.rect(screen, color, self.rect, border_radius=10)
        text_surf = self.font.render(self.text, True, (200, 200, 200))
        text_rect = text_surf.get_rect(center=self.rect.center)
        screen.blit(text_surf, text_rect)

    def check_hover(self, pos):
        self.is_hovered = self.rect.collidepoint(pos)
        return self.is_hovered

    def is_clicked(self, pos, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            return self.rect.collidepoint(pos)
        return False