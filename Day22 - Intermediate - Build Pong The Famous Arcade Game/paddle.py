from turtle import Turtle

class Paddle:

    def __init__(self, position):
        self.paddle_segments = []
        self.initialize_paddle_segments()

        self.head = self.paddle_segments[0]
        self.head.setheading(90)

        self.tail = self.paddle_segments[-1]
        self.tail.setheading(270)
        self.direction = "Up"
        self.move_value = 150

        

        self.head.setposition(position, 50)
   
        for segment_index in range(len(self.paddle_segments)):
            
            if segment_index != 0:
                prev_segment_xcor = self.paddle_segments[segment_index - 1].xcor()
                prev_segment_ycor = self.paddle_segments[segment_index - 1].ycor()
                self.paddle_segments[segment_index].setposition(prev_segment_xcor, prev_segment_ycor - 21)

        
    def initialize_paddle_segments(self):
        for _ in range(6):
            new_segment = Turtle()
            new_segment.color("White")
            new_segment.shape("square")
            new_segment.penup()
           
            self.paddle_segments.append(new_segment)


    def paddle_move_up(self):
        if self.head.ycor() < 360.00:
            for segment_index, segment in reversed(list(enumerate(self.paddle_segments))):
                if segment_index != 0:
                    prev_segment_xcor = self.paddle_segments[segment_index - 1].xcor()
                    prev_segment_ycor = self.paddle_segments[segment_index - 1].ycor() + (self.move_value - 20)
                    segment.setposition(prev_segment_xcor, prev_segment_ycor)

            self.head.forward(self.move_value)

    def paddle_move_down(self):
        if self.tail.ycor() > -342.00:
            for segment_index, segment in list(enumerate(self.paddle_segments)):
                if segment_index != len(self.paddle_segments) - 1:
                    next_segment_xcor = self.paddle_segments[segment_index + 1].xcor()
                    next_segment_ycor = self.paddle_segments[segment_index + 1].ycor() - (self.move_value - 20)
                    segment.setposition(next_segment_xcor, next_segment_ycor)

            self.tail.forward(self.move_value)
  

    def is_going_up(self):
        return self.direction == "Up"
        


