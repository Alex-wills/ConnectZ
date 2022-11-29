# ConnectZ

## Prerequisite knowledge

A program that reads a file that is in the format of a completed generalised 
'connect4' game, then outputs the corresponding result.

An example of the input file is: test.txt

7 6 4  
1 \
2 \
1 \
2 \
1 \
2 \
1 

In the first line, 7 or X represents the number of rows, 6 or Y represents the number of columns and 
4 or Z represents the number of the player's counters next to each other needed to win.

In the lines that follow every other line is that of the player's move (dropping 
the counter down that particular column).

## Outputs

| Code |      Reason      | 
|------|:----------------:|
 | 0    |       Draw       | 
 | 1    | Win for player 1 | 
 | 2    | Win for player 2 | 
 | 3    |    Incomplete    | 
 | 4    | Illegal continue | 
 | 5    |   Illegal row    | 
 | 6    |  Illegal column  | 
 | 7    |   Illegal game   | 
 | 8    |   Invalid file   | 
 | 9    |    File error    | 

<br>
<br>
Descriptions: <br>

0: This happens when every possible space in the frame was filled
with a counter, but neither player achieved a line of the required
length.

1: The first player achieved a line of the required length.

2: The second player achieved a line of the required length.

3: The file conforms to the format and contains only legal moves,
but the game is neither won nor drawn by either player and there
are remaining available moves in the frame. Note that a file with
only a dimensions line constitues an incomplete game.

4: All moves are valid in all other respects but the game has already
been won on a previous turn so continued play is considered an
illegal move.

5: The file conforms to the format and all moves are for legal
columns but the move is for a column that is already full due to
previous moves.

6: The file conforms to the format but contains a move for a column
that is outside the dimensions of the board. i.e. the column
selected is greater than X

7: The file conforms to the format but the dimensions describe a game that can never be won.

8: The file is opened but does not conform the format.

9: The file can not be found, opened or read for some reason.
<br>
<br>

## Intuition

The idea behind the search for the victory condition is to only scan the last move's
possible victory sequence to make it efficient and only scan a minimum amount of 
necessary squares. For example for the horizontal search; wherever the move is made 
the check_win() method will scan right to see if it encounters consecutive player's
signs/counters, until it reaches outside the board or to a space where one of their 
counters is not present. Then it will scan in the opposite direction of the original 
move to see if it can find the remaining consecutive counters needed for a win.
If it does not find the necessary amount, it will check the other directions 
(vertical, positive diagonal, etc.) and finally return True or False.



<br>

## Excecution
To run this program type into the terminal of the ConnectZ file:

use either 
```bash
python 
```
or
```bash
python3 
```

and then type for a file named test1.txt:
```bash
python3 ConnectZ.py test1.txt
``` 

For testing multiple files at once type them consecutively separated by a space:
```bash
python3 ConnectZ.py test1.txt test2.txt test3.txt
``` 