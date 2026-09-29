# 🐍 Snake Game

A classic Snake Game built with **Python and Pygame**, featuring a modern dark-themed interface, keyboard controls, score tracking, persistent high scores, increasing difficulty, and restart functionality.

## 🎮 Features

- Classic Snake gameplay with grid-based movement.
- Keyboard controls using the **Arrow Keys**.
- Food generation at random grid positions.
- Snake grows when food is collected.
- Score and snake length displayed in the HUD.
- Persistent **high-score system** using `highscore.txt`.
- Increasing game speed as the snake grows.
- Wall collision detection.
- Self-collision detection.
- Start menu with game instructions.
- Game-over screen with final score.
- **C** key to play again.
- **Q** key to quit.
- Prevents the snake from immediately reversing direction.
- Clean, responsive game loop with separate game states.

## 🛠️ Technologies Used

- **Python 3**
- **Pygame**
- **Random** module
- File handling for high-score persistence

## 📁 Project Structure

```text
Snake-Game/
│
├── snake_game.py
├── highscore.txt
└── README.md
```

> `highscore.txt` is created/updated by the game to store the player's best score.

## ⚙️ Requirements

Make sure Python is installed on your system.

Install Pygame using:

```bash
pip install pygame
```

## ▶️ How to Run

1. Clone or download the project.
2. Open the project folder in VS Code or a terminal.
3. Install the required dependency:

```bash
pip install pygame
```

4. Run the game:

```bash
python snake_game.py
```

## 🎯 Controls

| Key | Action |
|---|---|
| `SPACE` / `ENTER` | Start the game |
| `↑` | Move Up |
| `↓` | Move Down |
| `←` | Move Left |
| `→` | Move Right |
| `C` | Play Again after Game Over |
| `Q` | Quit |

## 🧠 Game Logic

The game uses a grid-based movement system where the snake moves in fixed blocks. The current direction controls the snake's movement, while the game continuously checks for wall and self-collision.

When the snake eats food:

- The snake length increases.
- A new food position is generated.
- The score increases.
- The game speed can increase as the snake becomes longer.
- A new high score is saved when the current score exceeds the previous record.

## 🏆 High Score System

The game stores the best score in a local `highscore.txt` file. When the game starts, the saved score is loaded. During gameplay, a higher score is automatically saved for future sessions.

## 🖥️ Interface

The game includes:

- Start screen
- Game HUD
- Score display
- Best-score display
- Snake length display
- Grid-based play area
- Food indicator
- Game-over screen
- New high-score notification

## 📌 Learning Outcomes

This project demonstrates practical use of:

- Python functions
- Loops and conditional statements
- Lists and dictionaries
- Random number generation
- File handling
- Event handling
- Collision detection
- Game-state management
- Object rendering with Pygame
- Keyboard input handling

## 🚀 Future Improvements

Possible future enhancements include:

- Sound effects and background music
- Pause/resume functionality
- Multiple difficulty levels
- Power-ups and special food
- Different themes and skins
- Leaderboard system
- Mobile/touch controls
- Start-game animations

## 👨‍💻 Author

**Nitin Verma**

Python Developer | AI/ML Enthusiast

---

⭐ If you like this project, consider giving it a star on GitHub!
