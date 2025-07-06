import pygame

class SpriteSheet:
    def __init__(self, file, sprites):
        self.sprite_sheet_image = pygame.image.load(file).convert_alpha()
        self.sprites = sprites

    def get_sprites(self):
        sprites = {}
        for sprite in self.sprites:
            sprites[sprite.name] = self._get_sprite_surface(sprite)
        return sprites

    def _get_sprite_surface(self, sprite):
        """Extracts a single sprite from the sheet image."""
        sprite_surface = pygame.Surface(sprite.size, pygame.SRCALPHA)  # transparent background
        sprite_surface.blit(self.sprite_sheet_image, (0, 0), pygame.Rect(sprite.pos, sprite.size))
        return sprite_surface