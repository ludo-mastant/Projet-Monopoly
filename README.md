# Monopoly Project school (edition) in Python

Welcome to the **Monopoly in Python** project! This project recreates the famous **Monopoly** board game in a Python environment, allowing you to play against other players in a digital format. **Realised by ludo-mastant, EvanSurGit and Rylight2512 ( physically absent but mentally present )**

## Table of Contents

1. [Project Description](#project-description)
2. [Features](#features)
3. [Prerequisites](#prerequisites)
4. [Usage](#usage)
5. [Project Structure](#project-structure)

---

## Project Description

This project implements a digital version of the **Monopoly** board game using Python. The objective of the game is to buy properties, collect rent, build houses and hotels, and bankrupt the other players.

The project is designed to work in local multiplayer mode, with a turn-based system, Chance and Community Chest cards, and classic Monopoly rules.

---

## Features

- **Turn-based gameplay**: Each player takes turns rolling the dice, moving around the board, and making decisions.
- **Property management**: Players can buy properties, collect rent, and build houses or hotels.
- **Chance and Community Chest cards**: The game includes Chance and Community Chest cards, which affect the game randomly.
- **Local multiplayer**: The game can be played by multiple players on the same device.
- **End of game**: The game ends when a player goes bankrupt, and the winner is the player with the most money left.

---

## Prerequisites

Before running this project, make sure you have Python extension installed on Visual Code.

- **Python extension on Visual Code**

Additionally, the project uses the following libraries that can be installed via `pip`:

- **pygame** (if you have a graphical interface)
- **random** (for generating random game events)

---

## Usage

Once the installation is complete, you can start the game by running the main file. Use the following command to start the game:

Python main.py

The game will launch in the console, and you'll be able to play Monopoly with multiple players taking turns.

---

## Project Structure

Projet-Monopoly/
* ├── img/                       # Contains images used in the game (e.g., cards, board images, player pieces)
* ├── main.py                    # Main entry point for the game (starts the game loop and initializes the game)
* ├── test.py                    # Test file (contains unit tests for various components of the game)
* ├── plateau.py                 # Game board logic (defines the board, spaces, and interactions between them)
* ├── joueur.py                  # Player management (handles player properties, actions, and states)
* ├── partie.py                  # Game mechanics (controls the flow of the game, turns, and game rules)
* ├── case.py                    # Game space logic (defines individual spaces on the board and their behavior)
* ├── terrain.py                 # Property spaces (manages properties, rents, and building mechanics)
* ├── case_speciale.py           # Special space logic (defines special spaces like Chance or Community Chest)
* ├── README.md                  # Project documentation (provides an overview of the project, installation, and usage)
* ├── chartre_prog.md            # Coding rules (sets the guidelines for coding practices and conventions in the project)
* └──                            # (optional: other files or directories, such as for future features, assets, or documentation)
