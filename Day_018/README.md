# PYTHON 100 PROJECTS IN 100 DAYS

## Day 18: Hirst Spot Painting (GUI)

### 📌 About The Project

In this project, I developed a **Hirst Spot Painting** in Python using the Turtle graphics library. The application creates a digital artwork composed of colored dots, randomly selecting colors extracted from an inspiration image.
The project was inspired by the artwork of [Damien Hirst](https://www.artsy.net/artwork/damien-hirst-histidyl-8), known for his colorful spot paintings. I first extracted the main colors from the reference image using the `colorgram` library and then used those colors to recreate a similar composition with Python.

### 🧠 What I Learned
- Using the `Turtle` library to create drawings with Python - [Documentation](https://docs.python.org/pt-br/3.14/library/turtle.html)
- Changing the Turtle drawing speed using `speed()`
- Using `penup()` and `hideturtle()` to control the Turtle cursor
- Changing the Turtle's direction using `setheading()`
- Creating random RGB colors using `random.randint()`
- Using RGB color values with `colormode(255)`
- Extracting colors from an image using the `colorgram` library
- Accessing RGB values from extracted colors
- Creating a list of RGB color tuples
- Drawing colored dots using `dot()`
- Using loops to generate a grid of dots
- Using the modulo operator to control when the Turtle moves to the next line
- Creating different geometric shapes with Turtle

### 🛠 Technologies Used
- Python
- Turtle
- Colorgram
- VS Code
- Git
- GitHub

### 📚 Libraries Used
```python
from turtle import Turtle, Screen, colormode
import random
import colorgram
```

### ▶️ How to Run the Project
1. Install the required library:

```bash
pip install colorgram.py
```

2. Run the project in the terminal:

```bash
python Day_018/main.py
```

### Thanks for your attention!!

---
