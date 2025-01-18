# minesweeper

# principle
-  bombs are planted randomly in the grid
- check off all the none-bomb areas to win
- when discovering a bomb -> loss 
- spaces that are adjacent to a bombe get their counter + 1 starting from None (0) 
- revealing 
    - when the player reveals a 0-spot all adjacent 0-spots are revealed
    - when the number is higher than 0 only this spot will be revealed no matter what
    - adjacent numbers high than 0 are revealed also 

# layout
- keeping it simple: 10x10 board
- empty spots: ' ' 
- bombs: '*' 
- amount of bombs
    - easy: 10
    - medium: 20
    - hard: 30 
- undercover board & transperent board with bombs

plan
- [ ] a: reset the board for the next play
- [ ] add the marking function (maybe)
- [ ] add orientation for the board
- [x] a: fix the zero revelation algo
- [ ] c: changing is_win(): by counting down, reducing by bomb amount from the unrevealed spots
- [ ] a1: bug fixing
- [ ] 
- [ ] 
- [ ]  

Visited: Pros 
    You're absolutely right to question the need for a visited set if you're already checking whether a spot is empty (user_board[row][col] == ' ') before processing it. Technically, in your implementation, the user_board itself acts as a marker for whether a cell has been visited because:

    A cell that has been processed will no longer be ' '; it will contain a value from the init_board.
    However, there are still scenarios where having a visited set might be beneficial:

    Why Use visited?
    To Avoid Reprocessing During Recursion/BFS: If you have multiple paths leading to the same cell, a visited set ensures that you don’t accidentally re-add the same cell to the queue or revisit it unnecessarily. This is especially useful in densely interconnected zero regions, where recursion or BFS could otherwise repeatedly revisit cells.

    For Debugging/Clarity: Using a visited set can make your algorithm's flow more explicit, particularly when debugging or explaining your approach. You know that a cell has been visited because it is explicitly stored in visited.

    Future Extendability: If you later decide to implement features that rely on distinguishing visited but unrevealed cells (e.g., flagged cells), separating "visited" logic from the board's state might be useful.

    Handling Non-Empty Edge Cases: If, for some reason, your user_board logic changes (e.g., it contains states like flagged cells), a visited set ensures you avoid visiting already processed cells regardless of their display state.