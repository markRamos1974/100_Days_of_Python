from snake_segment import SnakeSegment

class Snake:
    
    def __init__(self):
        self.snake_segments = []
        self.create_snake()

        self.head = self.snake_segments[0]
        self.tail = self.snake_segments[len(self.snake_segments) - 1]  
        self.head.color("cyan")

        for segments in self.snake_segments:
            segments.showturtle()

    def create_snake(self):
        initial_positions = [(0, 0), (-20, 0), (-40, 0)]
        for position in initial_positions:
            new_segment = SnakeSegment()
            new_segment.setposition(position)
            self.snake_segments.append(new_segment)

    def move(self):
        for segment_index, segment in reversed(list(enumerate(self.snake_segments))):
            x_position = self.snake_segments[segment_index - 1].xcor()
            y_position = self.snake_segments[segment_index - 1].ycor()
            
         
            if segment_index != 0:
                segment.setposition(x_position, y_position)

        
        self.head.forward(20)
        self.tail.showturtle()

    def add_snake_segment(self):
        new_segment = SnakeSegment()
        self.snake_segments.append(new_segment) 
        self.tail = new_segment
    
    def reset_snake(self):
        for segments in self.snake_segments:
            segments.hideturtle()
        self.snake_segments = []
        self.create_snake()
        self.head = self.snake_segments[0]
        self.tail = self.snake_segments[len(self.snake_segments) - 1]  
        self.head.color("cyan")

        for segments in self.snake_segments:
            segments.showturtle()





