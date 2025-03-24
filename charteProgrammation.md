# Programming Charter for Monopoly school edition in Python

This charter defines the best practices and guidelines to follow when developing the **Monopoly school edition in Python** project. The aim is to ensure consistency, readability, and maintainability of the code throughout the project.

---

## 1. Naming Conventions

- **Variables**: Use descriptive names in **snake_case** (e.g., `player_name`, `property_price`).
- **Functions**: Function names should be descriptive and also use **snake_case** (e.g., `roll_dice()`, `calculate_rent()`).
- **Classes**: Use **PascalCase** for class names (e.g., `Player`, `Board`).
- **Constants**: Constants should be written in **UPPERCASE** and separated by underscores (e.g., `MAX_PLAYERS`, `BOARD_SIZE`).

---

### Examples:
```python
# Good naming practices
MAX_PLAYERS = 4
class Player:
    def __init__(self, name):
        self.name = name

def roll_dice():
    return random.randint(1, 6)
```

---

## 2. Identation and Spacing

- Leave a **blank line** before and after **class and function definitions**.
- Use **spaces around operators** (=, +, -, ==, etc.) to improve readability.

---

## 3. Code Documentation

- **comments**: Add comments to explain the "why" behind the code, especially in complex blocks or sections that are not immediately obvious.
- **Docstrings**: Every function and class should have a docstring explaining its purpose, parameters, and return values.

---

## 4. Clean and Readable Code

- **Avoid "puzzle" code**: The code should be readable, even for someone who didn’t write it. Prefer descriptive names for variables and functions.
- **Avoid overly long functions**: A function should be small enough to understand and test easily. If it becomes too complex, break it into smaller functions.

---

## 5. Code Review

- **Pull requests must be reviewed**before being merged into the dev branch and after the main branch for security
- Code should be reviewed for **readability**, **clarity**, and **adherence** to this programming charter.
