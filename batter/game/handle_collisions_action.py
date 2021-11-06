import random
from game import constants
from game.action import Action
from game.point import Point

class HandleCollisionsAction(Action):
    """A code template for handling collisions. The responsibility of this class of objects is to update the game state when actors collide.
    
    Stereotype:
        Controller
    """

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        paddle = cast["paddle"][0] # there's only one
        ball = cast["ball"][0] # there's only one
        bricks = cast["brick"]
        for idx,brick in enumerate(bricks):
            if ball.get_position().equals(brick.get_position()):
                bricks.pop(idx)
                velocity = ball.get_velocity().reverse_y()
                ball.set_velocity(velocity)
            if ball.get_position().equals(brick.get_position()):
                bricks.pop(idx)
                velocity = ball.get_velocity().reverse_x()
                ball.set_velocity(velocity)
