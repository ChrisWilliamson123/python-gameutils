import pygame

from .game_settings import GameSettings
from .state.state_manager import StateManager

class GameManager:
    """Manages game states and shared resources"""
    def __init__(self, screen_size, caption, states_builder, initial_state_type, state_transition_logic_fn, context, settings):
        # Pygame initialisation
        pygame.init()
        self.screen = pygame.display.set_mode((screen_size[0], screen_size[1]))
        pygame.display.set_caption(caption)
        self.clock = pygame.time.Clock()
        self.settings = settings

        # TODO: Winner

        self.context = context

        # State initialisation
        states = states_builder(self)

        self.state_manager = StateManager(states, initial_state_type, state_transition_logic_fn)

        # Ensure the game is running
        self.running = True

    def run(self):
        """Main game loop"""
        while self.running:
            dt = self.clock.tick(self.settings.framerate or 60) / 1000

            # Event handling
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self.running = False
                else:
                    self.current_state.handle_event(event)

            self.current_state.update(dt)
            self.current_state.render()

            pygame.display.flip()

        pygame.quit()

    # State helpers
    @property
    def current_state(self):
        return self.state_manager.current_state

    def change_state(self, new_state_type):
        self.state_manager.change_state(new_state_type)

    def change_to_previous_state(self):
        self.state_manager.change_state(self.state_manager.previous_state_type)

    def render_previous_state(self):
        self.state_manager.previous_state.render()
