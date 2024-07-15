from turtle import Turtle

ALIGNMENT="center"
FONT = ("Courier",20,"bold")



class ScoreBoard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score=0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,270)
        with open("data.txt") as data:
            self.highscore =  int(data.read())
        self.update_scoreboard()
        

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore} ",move=False, align=ALIGNMENT,font= FONT)


    def increase_score(self):
           self.score+=1
           self.clear()
           self.update_scoreboard()

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.highscore}")
        self.score = 0
        self.update_scoreboard()

   

    def get_score(self):
         return self.score
         
