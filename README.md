# Building 石垣 (Stone Wall) with Machine Learning

The current project attempts to use a neural network to create a "solid looking" stone wall.

## Usage

This project uses `poetry` to handle dependencies. It also provides the `start` script to run the program.

```bash
poetry run start
```

for now this script runs a `pygame` script that will contain the simulation of wall building in the form of a game.

## Program Flow

The finished project will have several scripts

-   Starting the game/simulation and play as a person (start-demo)
-   Train the Neural Network
-   Load a previously trained NN and see it play the simulation
-   Show NN metrics
