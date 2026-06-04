# PYTHON 100 PROJECTS IN 100 DAYS

## Day 6: Escaping The Maze (Reeborg's World)

### 📌 About The Project
In this project, I created a custom world and a Python solution for Reeborg's World.
The goal is to guide the robot through a maze and reach the target location. To make the challenge more interesting, the robot starts with a random orientation, meaning it can face different directions each time the world is loaded.

### 🧠 What I Learned
- Creating helper functions (`def`)
- Using loops (`while`)
- Using conditionals (`if`, `elif`, `else`)
- Problem-solving with algorithms
- Maze navigation logic
- Adapting code to randomized starting conditions

### ⚙️ How The Solution Works
The solution is divided into two stages:

#### 1. Initial Positioning
The robot first moves forward until it reaches a wall. Once it finds the wall, it turns left to begin navigating the maze from a consistent position.

#### 2. Right-Hand Rule Navigation
After positioning itself, the robot follows the right-hand rule:
- If the path on the right is open, turn right and move.
- Otherwise, if the path ahead is clear, move forward.
- If neither path is available, turn left.
The robot repeats this process until it reaches the goal.

### 🛠️ Technologies Used
- Python
- Reeborg's World
- VS Code
- Git
- GitHub

### ▶️ How To Run
1. Download the project files.
2. Open Reeborg's World ([Reeborg's World](https://reeborg.ca/reeborg.html)).
3. Import the provided world (`EscapingMaze.json`).
4. Copy the contents of `solution.py`.
5. Paste the code into the Reeborg's World editor.
6. Click ▶️.
7. Watch the robot solve the maze automatically.

### Thanks for your attention!!
---
