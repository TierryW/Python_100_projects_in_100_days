# PYTHON 100 PROJECTS IN 100 DAYS

## Day 23: Turtle Crossing

### 📌 About The Project

In this project, I developed a **Turtle Crossing Game** in Python using the **Turtle** module. The objective is to help the player-controlled turtle cross the road and reach the finish line without colliding with the cars. The player moves the turtle forward using the **Up arrow key**, while cars are randomly created and continuously move across the screen. Whenever the player reaches the finish line, the turtle returns to the starting position, the level increases, and the cars become faster. If the turtle collides with a car, the game ends and the **GAME OVER** message is displayed.

### 🧠 What I Learned
- Creating classes that inherit functionality from the Turtle class. [Documentation](https://docs.python.org/3.14/library/turtle.html)
- Using `class Player(Turtle):` to create a custom player object.
- Using `class CarManager:` to manage multiple car objects.
- Using `class Scoreboard(Turtle):` to create a custom scoreboard.
- Using `super().__init__()` to initialize inherited Turtle functionality.
- Using `screen.onkeypress()` to connect the Up arrow key to the player's movement.
- Using `screen.listen()` to enable keyboard input.
- Using `goto()` to position objects on the screen.
- Using `setheading()` to define the turtle's initial direction.
- Using `ycor()` to check the player's vertical position.
- Using `is_at_finish_line()` to determine when the player reaches the end of the road.
- Creating multiple car objects and storing them in a list.
- Using `random.randint()` to randomly determine when new cars are created.
- Using `random.choice()` to assign random colors to the cars.
- Using random Y coordinates to create cars at different positions on the road.
- Using a `for` loop to move all cars stored in the `all_cars` list.
- Using `backward()` to move the cars from right to left.
- Using `distance()` to detect collisions between the player and cars.
- Using `time.sleep()` to control the speed of the game loop.
- Using `screen.tracer(0)` and `screen.update()` to manually control screen updates.
- Creating a level system that increases the difficulty of the game.
- Increasing the car movement speed whenever the player completes a level.
- Using `self.car_speed` to control the movement speed of all cars.
- Using `self.level` to keep track of the current game level.
- Using `self.clear()` to remove the previous scoreboard before displaying the updated level.
- Organizing the project into separate modules for the player, car manager, scoreboard, and main game logic.

### 🛠 Technologies Used
- Python
- Turtle
- VS Code
- Git
- GitHub

### 📚 Libraries Used

```python
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import time
```

### ▶️ How to Run the Project

1. Run the project in the terminal:

```bash
python Day_023/main.py
```

### Thanks for your attention!!

---
