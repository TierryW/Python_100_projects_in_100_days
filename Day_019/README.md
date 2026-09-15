# PYTHON 100 PROJECTS IN 100 DAYS

## Day 19: Turtle Race

### 📌 About The Project

In this project, I developed a **Turtle Race** in Python using the Turtle graphics library. The application creates a race between six colored turtles and allows the user to place a bet by choosing which turtle they think will win.
The program validates the user's input to make sure a valid turtle color is selected before starting the race. Each turtle moves a random distance on every iteration, creating a different race outcome each time. At the end, the program identifies the winning turtle and informs the user whether their prediction was correct.

### 🧠 What I Learned
- Using the `Turtle` and `Screen` classes to create a graphical application - [Documentation](https://docs.python.org/3.14/library/turtle.html)
- Creating multiple Turtle objects using a `for` loop
- Storing multiple Turtle objects in a list
- Using `screen.textinput()` to receive user input through a graphical interface
- Cleaning and standardizing user input with `strip()` and `lower()`
- Using a `while` loop to repeatedly request input until a valid color is provided
- Using `random.randint()` to generate random movement distances
- Using `xcor()` to check the Turtle's horizontal position
- Using `pencolor()` to retrieve the Turtle's current color
- Using lists to store colors and Y-axis positions
- Positioning multiple Turtle objects using `goto()`
- Using `penup()` to move the Turtle without drawing
- Creating a race loop that continues until one Turtle reaches the finish line
- Comparing the winning Turtle's color with the user's prediction

### 🛠 Technologies Used
- Python
- Turtle
- VS Code
- Git
- GitHub

### 📚 Libraries Used

```python
from turtle import Turtle, Screen
import random
```

### ▶️ How to Run the Project

1. Run the project in the terminal:

```bash
python Day_019/main.py
```

### Thanks for your attention!!

---
