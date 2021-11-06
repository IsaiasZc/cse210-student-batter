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
                self._brick_collision(ball)
        if ball.get_position().equals(constants.MAX_X) and :
            bricks.pop(idx)
            self._wall_collision(ball)


    def _brick_collision(self, ball):
        y = ball.get_velocity().get_y() * -1
        x = ball.get_velocity().get_x()
        ball.set_velocity(Point(x,y))    
        
    def _wall_collision(self, ball):
        y = ball.get_velocity.get_y() 
        x = ball.get_velocity.get_x() * -1
        ball.set_velocity(Point(x,y))    