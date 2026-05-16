import spritePro as s

bg =s.Sprite("background.jfif",pos = (200,300),size=(400,600))
player = s.Sprite("bird.png",pos =(100,300),size = (50,50))
s.run(size=(400,600),title="Flappy Bird")

