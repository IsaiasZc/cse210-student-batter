import random
from game import constants
from game.action import Action
from game.point import Point
from game.input_service import InputService

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
        self._is_playing = True
        ball_next_position = self._next_position(ball)
        for idx,brick in enumerate(bricks):
            # recognize when the ball has collision with
            # the brick.
            if ball_next_position.equals(brick.get_position()):
                bricks.pop(idx)
                self._paddle_or_brick_collision(ball)
                
        # collision with the sides
        if (ball_next_position.get_x() == constants.MAX_X) or (ball_next_position.get_x() == 1):
            self._wall_collision(ball)

        elif (ball.get_position().get_y() == 1):
            # top collision.
            self._paddle_or_brick_collision(ball)
        
        elif ball.get_position().get_y() == (constants.MAX_Y - 1):
            self._is_playing = False
            print("THANKS!!!")
            # collision with the bottom
       
        for i in range(12):
            # recognize a paddle collision.
            x = paddle.get_position().get_x() + i
            y = paddle.get_position().get_y()
            if ball_next_position.get_x() == x and ball_next_position.get_y() == y:
                self._paddle_or_brick_collision(ball)
        
        # self._paddle_boundaries(paddle)


    def _paddle_or_brick_collision(self, ball):
        y = ball.get_velocity().get_y() * -1
        x = ball.get_velocity().get_x()
        ball.set_velocity(Point(x,y))    
        
    def _wall_collision(self, ball):
        y = ball.get_velocity().get_y() 
        x = ball.get_velocity().get_x() * -1
        ball.set_velocity(Point(x,y))

    def _next_position(self,ball):
        position = ball.get_position()
        velocity = ball.get_velocity()
        x1 = position.get_x()
        y1 = position.get_y()
        x2 = velocity.get_x()
        y2 = velocity.get_y()
        x = x1 + x2 #% (constants.MAX_X - 1)
        y = y1 + y2 #% (constants.MAX_Y - 1)
        position = Point(x, y)
        return position
    
    def get_is_playing(self):
        return self._is_playing

    
    # def _paddle_boundaries(self,paddle):
    #     position = paddle.get_position()
    #     x = position.get_x()
    #     while x == 1: 
    #         paddle.set_position(paddle.get_position())
        
