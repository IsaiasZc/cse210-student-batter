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
        ball_next_position = self._next_position(ball)
        for idx,brick in enumerate(bricks):
            if ball_next_position.equals(brick.get_position()):
                bricks.pop(idx)
                self._paddle_or_brick_collision(ball)
                
        if (ball_next_position.get_x() == constants.MAX_X) or (ball_next_position.get_x() == 1):
            self._wall_collision(ball)
            
        if paddle.get_position().equals(ball.get_position()):
            self._paddle_or_brick_collision(ball)# 
        
        for i in range(11):
            x = paddle.get_position().get_x() + i
            y = paddle.get_position().get_y()
            if ball_next_position.get_x() == x and ball_next_position.get_y() == y:
                self._paddle_or_brick_collision(ball)
    # un faavor, si puedes escribelo porque mi esposa está hablando y no te escucho bien
    # ella tiene los audifonos :'v
    # decia que el next position parece que hiciera lo mismo que probe, solo copie
    # esta lineael primer if y cambie  MAX_Y , y el metodo le puse paddle_or_bric.----
    # nada mas me faltaria eso de -1 para que no los coma sino los choque normal...
    # creo que si llamamos el next position al princi´pio, lo podemos usar para todos
    # eso pense tambien. pero estoy viendo que hace realmente ese metodo 
    # intentemos a ver-OK, no se no veo nada... esta en blanco?
    # creo que la comparacion está mal - creo que falta el punto?
    # sin el punto es, lo que pasa es que estabamos consultando un metodo de mas
    # ahh ok.. .intentemos de nuevo- hay un bug o me parece? en el primer caracter de
    # paddle al chocar, ah si? no lo noté, a ver otra vez- a creo que ee el SHARE
    # no no, sucede lo siguiente: cuando va debajo del paddle, vuelve a aparecer arriba, choca con un *
    # se regresa y vuelve  a chocar con el paddle. Supongo que estabien, solo son bugs
    # del Compartir.
    # creo qque si, hay otro tema, como el paddle se mueve a la misma velocidad de que el bat.
    # es dificil darle el alcance a veces, creo que deberia ser mas rapido.Es verdad
    # Dale push!, ok

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
        x = 1 + (x1 + x2 - 1) % (constants.MAX_X - 1)
        y = 1 + (y1 + y2 - 1) % (constants.MAX_Y - 1)
        position = Point(x, y)
        return position
        # es lo mismo que el move actors action
        # su objetivo es predecir el siguiente movimiento, haré una prueba.
        # jejeje let's try

# hey ya hay un metdo para una nueva posicion en point creo
# pero es para saber cual será la siguiente posicion? porque la idea es predecir el siguiente movimiento
# y así evitar que reemplace las cosas, creo que eso podemos hacerlo en el point.