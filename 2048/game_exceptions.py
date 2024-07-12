"game_exceptions.py gère les exceptions liées au jeu"

class GameException(Exception):
    "Exception liée au jeu"
    def __init__(self, msg):
        super().__init__() # Hériter des attributs de la classe Exception
        self.msg = msg # Message de l'exception

    def __str__(self):
        return self.msg

    def __repr__(self):
        return self.msg


class InvalidDirectionException(GameException):
    "Direction de déplacement invalide pour les nombres"
    def __init__(self):
        super().__init__(msg="Direction de déplacement invalide. Les directions valides sont 'haut', 'gauche', 'bas' et 'droite'.") # Hériter des attributs de la classe GameException
    def __repr__(self):
        return self.msg
    
    def __str__(self):
        return self.msg