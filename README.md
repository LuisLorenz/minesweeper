# minesweeper

# principle
-  bombs are planted randomly in the grid
- check off all the none-bomb areas to win
- when discovering a bomb -> loss 
- spaces that are adjacent to a bombe get their counter + 1 starting from None (0) 
- revealing 
    - when the player reveals a 0-spot all adjacent 0-spots are revealed
    - when the number is higher than 0 only this spot will be revealed no matter what

# layout
- keeping it simple: 10x10 board
- empty spots: ' ' 
- bombs: '*' 
- amount of bombs
    - easy: 10
    - medium: 20
    - hard: 30 
- undercover board & transperent board with bombs