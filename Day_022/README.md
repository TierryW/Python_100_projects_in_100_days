# PYTHON 100 PROJECTS IN 100 DAYS

## Day 22: Pong Game

### 📌 About The Project

In this project, I developed a **Pong Game** in Python using the **Turtle** module. The game is a two-player version of the classic Pong, where each player controls a paddle and tries to prevent the ball from passing through their side of the screen. The right paddle is controlled using the **Up and Down arrow keys**, while the left paddle is controlled using the **W and S keys**. The ball continuously moves across the screen, bouncing off the top and bottom boundaries and the paddles. The game also includes a **scoreboard** that keeps track of each player's score. Whenever the ball passes one of the paddles, the opposing player receives a point and the ball is reset to the center.


### 🧠 What I Learned
- Understanding inheritance by creating classes that inherit functionality from the Turtle class. [Documentation](https://docs.python.org/3.14/library/turtle.html)
- Using `class Paddle(Turtle):` to create a custom paddle object.
- Using `class Ball(Turtle):` to create a custom ball object.
- Using `class Scoreboard(Turtle):` to create a custom scoreboard object.
- Using `super().__init__()` to initialize inherited Turtle functionality.
- Creating reusable methods to control the movement of game objects.
- Using `screen.onkeypress()` to connect keyboard keys to specific functions.
- Using `screen.listen()` to enable keyboard input.
- Moving the paddles vertically using `ycor()` and `goto()`.
- Preventing the paddles from moving outside the screen boundaries.
- Using `xcor()` and `ycor()` to detect the ball's position.
- Detecting collisions between the ball and the screen boundaries.
- Using `distance()` to detect collisions between the ball and the paddles.
- Creating a `bounce_y()` method to reverse the ball's vertical movement.
- Creating a `bounce_x()` method to reverse the ball's horizontal movement.
- Increasing the ball's speed after successful paddle collisions.
- Using `time.sleep()` to control the speed of the game loop.
- Using `screen.tracer(0)` and `screen.update()` to manually control screen updates.
- Resetting the ball position after a player scores.
- Creating a scoreboard that dynamically updates during the game.
- Using `self.clear()` to remove the previous score before displaying the updated score.
- Organizing the game into separate modules for the paddle, ball, scoreboard, and main game logic.

### 🛠 Technologies Used
- Python
- Turtle
- VS Code
- Git
- GitHub

### 📚 Libraries Used

```python
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
```

### ▶️ How to Run the Project

1. Run the project in the terminal:

```bash
python Day_022/main.py
```

### Thanks for your attention!!

---
