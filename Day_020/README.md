# PYTHON 100 PROJECTS IN 100 DAYS

## Day 20: Snake Game - Part 1

### 📌 About The Project

In this project, I started developing a **Snake Game** in Python using the **Turtle** module. This is a two-day project, and in the first part, the focus was on creating the snake, implementing its movement, working with screen coordinates, and creating a simple animation system.
The snake is composed of multiple square segments, which move together while following the position of the segment in front of them. The game also uses keyboard controls to change the snake's direction.
This first part focuses mainly on understanding **animation and coordinates with Turtle**, preparing the project structure for the next stage of the game.

### 🧠 What I Learned
- Creating a snake using multiple `Turtle` objects. [Documentation](https://docs.python.org/3.14/library/turtle.html)
- Organizing the snake using a Python `class`.
- Working with X and Y coordinates using `xcor()` and `ycor()`.
- Moving objects to specific coordinates with `goto()`.
- Changing the direction of a Turtle with `setheading()`.
- Getting the current direction using `heading()`.
- Using `forward()` to move the snake's head.
- Creating a simple animation loop with `screen.update()`.
- Using `screen.tracer(0)` to control screen updates manually.
- Using `time.sleep()` to control the animation speed.
- Using keyboard events with `screen.onkey()`.
- Preventing the snake from immediately reversing its direction.
- Using constants to organize positions, movement distance, and directions.
- Applying Object-Oriented Programming (OOP) to structure the game.

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
import time
```

### ▶️ How to Run the Project

1. Run the project in the terminal:

```bash
python Day_020/main.py
```

### Thanks for your attention!!

---
