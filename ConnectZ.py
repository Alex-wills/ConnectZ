import sys

from Tic_Tac_Toe import Board, Player


def read_file(file):
    move_set = []
    dimensions = ''

    try:
        with open(file, 'r') as f:
            contents = f.readlines()
    except FileNotFoundError:
        file_error()

    else:
        for line in contents:

            try:
                # only triggered on first iteration
                if line == contents[0]:
                    dimensions = list(line.replace(" ", "").replace("\n", ""))
                    dimensions[0] = int(dimensions[0])
                    dimensions[1] = int(dimensions[1])
                    dimensions[2] = int(dimensions[2])
                    continue

                mov = int(line.replace("\n", ""))
                move_set.append(mov)
            except (ValueError, IndexError):
                invalid_file()
            else:
                if dimensions[2] > dimensions[1] and dimensions[2] > dimensions[0]:
                    illegal_game()

    if len(contents) == 1:
        illegal_game()

    return dimensions, move_set


class Game(Board):
    def __init__(self, row, column, z, player1, player2):
        Board.__init__(self, row, column, 0)
        self.z = z
        self.p1 = player1.sign
        self.p2 = player2.sign

    # target possible fields
    def list_of_valid_cols(self):
        valid_cols = []

        # if top row of column is empty then valid column
        for column in range(self.col):
            if self.board[0][column] == 0:
                valid_cols.append(column)

        return valid_cols

    def list_of_empty_cols(self):
        empty_cols = []

        # if bottom row of column is empty then empty column
        for column in range(self.col):
            if self.board[self.row - 1][column] == 0:
                empty_cols.append(column)

        return empty_cols

    def make_move(self, player, move):

        # Illegal column
        if move < 1 or move > self.col:
            illegal_column()

        move = move - 1
        # make the move on the board and make the relevant checks after the move
        valid_cols = self.list_of_valid_cols()
        empty_cols = self.list_of_empty_cols()

        if move in empty_cols:
            self.board[self.row - 1][move] = player.sign
            move = (self.row - 1, move)

        elif move in valid_cols:

            # find topmost available row
            for row in range(self.row):

                # last empty space in column is the valid space
                if self.board[row][move] != 0:
                    self.board[row - 1][move] = player.sign
                    move = (row - 1, move)
                    break
        else:
            illegal_row()

        return move

    def check_win(self, player, move_made):

        m = move_made

        def check(c):
            reverse = False
            ctr = 1

            # previous point 'p'
            p = [0, 0]
            # forward search 'f'
            f = [0, 0]
            # reverse search 'r'
            r = [0, 0]

            for inc in range(1, self.z):

                if not reverse:
                    if c == 'horizontal':
                        f = [m[0], m[1] + inc]

                    if c == 'vertical':
                        f = [m[0] - inc, m[1]]

                    if c == 'pd':
                        f = [m[0] - inc, m[1] + inc]

                    if c == 'nd':
                        f = [m[0] + inc, m[1] + inc]

                    # searches up the negative diagonal until it does not
                    # have the same sign or runs out of spaces in a direction
                    try:
                        if self.board[f[0]][f[1]] == player.sign:
                            ctr += 1
                        else:
                            p = [f[0], f[1]]
                            reverse = True

                    except IndexError:
                        p = [f[0], f[1]]
                        reverse = True

                # when it has gone down the nd it then goes up it to see if the sequence of sign is completed
                if reverse:

                    if c == 'horizontal':
                        r = [p[0], p[1] - inc - 1]

                    if c == 'vertical':
                        r = [p[0] + inc + 1, p[1]]

                    if c == 'pd':
                        r = [p[0] + inc + 1, p[1] - inc - 1]

                    if c == 'nd':
                        r = [p[0] - inc - 1, p[1] - inc - 1]
                    try:

                        assert self.row - 1 >= r[0] >= 0 and self.col - 1 >= r[1] >= 0

                        if self.board[r[0]][r[1]] == player.sign:
                            ctr += 1
                        else:
                            break

                    except IndexError:
                        return False
                    except AssertionError:
                        return False


            if ctr == self.z:
                return True
            else:
                return False


        if check('pd') or check('nd') or check('horizontal') or check('vertical'):
            return True
        else:
            return False




def draw():
    print(0)


def p1_wins():
    print(1)


def p2_wins():
    print(2)


def incomplete_check():
    print(3)


def illegal_continue_check():
    print(4)


def illegal_row():
    print(5)
    raise TypeError


def illegal_column():
    print(6)
    raise TypeError


def illegal_game():
    print(7)
    raise TypeError


def invalid_file():
    print(8)
    raise TypeError


def file_error():
    print(9)
    raise TypeError


if __name__ == '__main__':
    p1 = Player('1')
    p2 = Player('2')

    for file in sys.argv[1:]:

        try:
            dim, move_set = read_file(file)
        except TypeError:
            continue

        arena = Game(dim[0], dim[1], dim[2], p1, p2)

        complete = False
        win1 = False
        win2 = False


        for count in range(len(move_set)):

            try:

                # before z counters are placed there is no need to check for a win
                if count < arena.z:

                    if count % 2 == 0:
                        arena.make_move(p1, move_set[count])
                    else:
                        arena.make_move(p2, move_set[count])


                else:

                    # player one wins
                    if count % 2 == 0:
                        if arena.check_win(p1, arena.make_move(p1, move_set[count])):
                            complete = True
                            win1 = True
                    else:
                        # player two wins
                        if arena.check_win(p2, arena.make_move(p2, move_set[count])):
                            complete = True
                            win2 = True

            # if any of the errors are raised 5-9 then the correct return is outputted and the next file is checked
            except TypeError:
                break

            # Illegal continue
            if complete == True and count != len(move_set) - 1:
                illegal_continue_check()
                break

            # Draw
            if arena.list_of_valid_cols() == []:
                draw()
                break

            # Win for player 1
            if win1:
                p1_wins()
                break

            # Win for player 2
            if win2:
                p2_wins()
                break

            # Incomplete
            if complete == False and count == len(move_set) - 1:
                incomplete_check()
                break
