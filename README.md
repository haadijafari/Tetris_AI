# Tetris AI
My University AI Project (Tetris AI) using Python. It uses greedy algorithm.


The score for each move is computed by assessing the grid the move would result in. This assessment is based on four heuristics: **aggregate height**, **complete lines**, **holes**, and **bumpiness**, each of which the AI will try to either minimize or maximize.



![Tetris AI GamePlay](/src/tetris_ai_gameplay.gif)
## API Reference

#### Install Requirements

```bash
  pip install -r requirements.txt
```
p.s: It only requires [PyGame](https://pypi.org/project/pygame/)

#### Run Greedy AI

```bash
  python main.py greedy
```

#### Play Yourself

```bash
  python main.py
```

| Action    | Key      | Description                       |
| :-------- | :------- | :-------------------------------- |
| Left      | `A`      | Moves tetromino to the left       |
| Right     | `D`      | Moves tetromino to the right      |
| Rotate    | `W`      | Rotates tetromino clockwise       |
| Fall      | `S`      | Moves tetromino to the bottem     |



## Definition of game

Perhaps the most interesting observation I made in the course of developing the AI was this: despite the existence of the “standard” Tetris guideline, there are still many variants of the game. If you were to play a game of Tetris online, chances are that it won’t be the “standard” one.

For this AI, I’ve stuck to the “official” guideline as closely as possible. For the sake of reducing ambiguity, here are the rules I’ve adhered to:

- The Tetris grid is 10 cells wide and 22 cells tall, with the top 2 rows hidden.
- All Tetrominoes (Tetris pieces) will start in the middle of the top 2 rows.
- There are 7 Tetrominoes : “I”, “O”, “J”, “L”, “S”, “Z”, “T”.
- The Super Rotation System is used for all rotations.
- The “7 system” random generator is used to randomize the next pieces.
- One lookahead piece is allowed (the player knows what the next piece will be).

But I have igmored the last rule for this code.


#### Read More

You can read more about how the code works [here](https://codemyroad.wordpress.com/2013/04/14/tetris-ai-the-near-perfect-player/).(I wrote my code based on this article :D)
