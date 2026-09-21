# PYTHON 100 PROJECTS IN 100 DAYS

## Day 21: Snake Game - Part 2

### 📌 About The Project

In this project, I completed the **Snake Game** developed in Python using the **Turtle** module. This is the second part of the project, where I added the main gameplay mechanics, including food, snake growth, score tracking, and collision detection.
The player controls the snake using the arrow keys. When the snake eats the food, it grows by one segment and the score increases. The game ends when the snake collides with the screen boundaries or with its own body.
This second part focuses on implementing **game logic, collision detection, object interaction, and score management**, completing the basic Snake Game.

### 🧠 What I Learned
- Understanding inheritance in Object-Oriented Programming (OOP) by creating classes that inherit functionality from the Turtle class. [Documentation](https://docs.python.org/3.14/library/turtle.html)
- Creating a Food class that inherits from Turtle using `class Food(Turtle):`.
- Using `super().__init__()` to initialize the inherited Turtle functionality inside the Food class.
- Understanding how inheritance allows a class to reuse and extend the attributes and methods of another class.
- Using `random.randint()` to position the food on the screen.
- Creating a Scoreboard class to manage the game score.
- Updating and clearing text displayed with Turtle.
- Extending the snake dynamically by adding new segments.
- Using `self.segments[-1].position()` to get the position of the last segment.
- Detecting collisions using `distance()`.
- Detecting collisions between the snake and the food.
- Detecting collisions between the snake and the screen boundaries using `xcor()` and `ycor()`.
- Detecting collisions between the snake's head and its own body.
- Organizing the project into multiple Python modules.
- Managing the game state with a `game_is_on` variable.
- Building the complete gameplay loop by combining movement, interaction, score, and collision mechanics.


### 🛠 Technologies Used
- Python
- Turtle
- VS Code
- Git
- GitHub

### 📚 Libraries Used

```python
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
```

### ▶️ How to Run the Project

1. Run the project in the terminal:

```bash
python Day_021/main.py
```

### Thanks for your attention!!

---
