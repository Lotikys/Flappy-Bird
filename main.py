import spritePro as s


class GameScene(s.Scene):
    def __init__(self):
        super().__init__()
        self.bg = s.Sprite("background.jfif",pos=s.WH_C,size=s.WH,scene =self)
        self.player = s.Sprite("bird.png",pos =(100,300),size = (50,50), scene = self)
        self.player_body = s.add_physics(self.player,s.PhysicsConfig(bounce=1.0))
        s.physics.set_gravity(980)
if __name__ == '__main__':
    s.run(scene=GameScene,size=(400,600),title ="Flappy Bird")
