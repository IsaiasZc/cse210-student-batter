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
        score = cast["score"][0]
        self._is_playing = True
        ball_next_position = self._next_position(ball)
        for idx,brick in enumerate(bricks):
            # recognize when the ball has collision with
            # the brick.
            if ball_next_position.equals(brick.get_position()):
                bricks.pop(idx)
                self._paddle_or_brick_collision(ball)
                score.add_points(1)
        # self._ball_velocity(ball, paddle)        
        
        # collision with the sides
        if (ball_next_position.get_x() in range(constants.MAX_X-1,constants.MAX_X)) or (ball_next_position.get_x() == 1):
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
                self._ball_velocity(ball, i)
                self._paddle_or_brick_collision(ball)
        
        # self._paddle_boundaries(paddle)


    def _paddle_or_brick_collision(self, ball):
        """ Recognize when the ball has collision with a
        a paddle or brinck and set the velocity and oposit y axis direction.

        Args:
            ball (Actor): The game ball.
        """
        y = ball.get_velocity().get_y() * -1
        x = ball.get_velocity().get_x()
        ball.set_velocity(Point(x,y))    
        
    def _wall_collision(self, ball):
        """ Recognize when the ball has collision with the walls
        and set the velocity and oposit x axis direction.

        Args:
            ball (Actor): The game ball.
        """
        y = ball.get_velocity().get_y() 
        x = ball.get_velocity().get_x() * -1
        ball.set_velocity(Point(x,y))

    def _next_position(self,ball):
        """predict the next position of the ball to bounce 
        against the different elements of the screen
        
        Args:
            ball (Actor): The game ball.
        """
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
        """return the _is_paying boolean."""
        return self._is_playing
    
    def _ball_velocity(self,ball, idx):
        """Establish a condition for changing the velocity of the ball
        in order to make the game harder. The ball turns fastar when hits 
        the first and last symbol of the paddle.
        Args:
            ball (Actor): The game ball.
            idx (element): the paddle position.
        """


        y = ball.get_velocity().get_y()
        x = ball.get_velocity().get_x()

        if idx == 0 or idx == 11:
            if abs(x) == 1:
                x *= 2
            ball.set_velocity(Point(x, y))
        


                