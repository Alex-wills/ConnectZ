import sys

from Tic_Tac_Toe import Board, Player


def read_file():
    move_set = []
    dimensions = ''

    try:
        with open('banana.txt', 'r') as f:
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
            except ValueError:
                invalid_file()
            else:
                if dimensions[2] > dimensions[1] and dimensions[2] > dimensions[0]:
                    illegal_game()

    # need to check dimensions are valid

    return dimensions, move_set


class Game(Board):
    def __init__(self, row, column, z, player1, player2):
        Board.__init__(self, row, column, 0)
        self.z = z
        self.p1 = player1.sign
        self.p2 = player2.sign

        # what do we need to initialise here? what are the inputs
        # -- initialising the game means setting up the board full of zeroes

    # What functions? : check win which will have functions inside such as pd diag, vertical etc.,
    #                   check_valid_file

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

    # def make_subspace(self, move):
    #     for row in range(self.row):

    def check_win(self, player, move_made):
        # logic for each win here -- maybe separate types of results so only need to be checked when it is possible for
        # that type of win

        m = move_made

        def check_hori():
            print("\n\n\n\nChecking norm horizontal")
            reverse = False
            ctr = 1
            p = [0, 0]
            for inc in range(1, self.z):

                # searches horizontally right on the row until it does not
                # have the same sign or runs out of spaces in a direction
                try:
                    if self.board[m[0]][m[1] + inc] == player.sign:
                        ctr += 1
                        print("non reverse ctr = ", ctr)
                except IndexError:
                    print("Exception handled")
                    p = [m[0], m[1] + inc]
                    print("p = ", p)
                    reverse = True

                # when it has gone right across the horizontal row it then goes left
                # to see if the sequence of sign is completed
                if reverse:
                    try:
                        print("reverse")
                        print(p[0], p[1] - inc)
                        if self.board[p[0]][p[1] - inc] == player.sign:
                            ctr += 1
                            print("reverse ctr = ", ctr)

                    except IndexError:
                        print("reverse exception handled")
                        return False

            print("ctr = ", ctr)

            if ctr == self.z:
                return True
            else:
                return False

        def check_vert():

            reverse = False
            ctr = 1
            p = [0, 0]
            for inc in range(1, self.z):

                # searches down the vertical column until it does not
                # have the same sign or runs out of spaces in a direction
                try:
                    if self.board[m[0] - inc][m[1]] == player.sign:
                        ctr += 1
                        print("non reverse ctr = ", ctr)
                except IndexError:
                    print("Exception handled")
                    p = [m[0] - inc, m[1]]
                    reverse = True

                # when it has gone down the vertical it then goes up it to see if the sequence of sign is completed
                if reverse:
                    try:
                        print("reverse")
                        if self.board[p[0] + inc][p[1]] == player.sign:
                            ctr += 1
                            print("reverse ctr = ", ctr)

                    except IndexError:
                        print("reverse exception handled")
                        return False

            print("ctr = ", ctr)

            if ctr == self.z:
                return True
            else:
                return False

        def check_pd():

            reverse = False
            ctr = 1
            p = [0, 0]
            for inc in range(1, self.z):

                # searches up the positive diagonal until it does not
                # have the same sign or runs out of spaces in a direction
                try:
                    if self.board[m[0] - inc][m[1] + inc] == player.sign:
                        ctr += 1
                        print("non reverse ctr = ", ctr)
                except IndexError:
                    print("Exception handled")
                    p = [m[0] - inc, m[1] + inc]
                    reverse = True

                # when it has gone up the pd it then goes down it to see if the sequence of sign is completed
                if reverse:
                    try:
                        print("reverse")
                        if self.board[p[0] + inc][p[1] - inc] == player.sign:
                            ctr += 1
                            print("reverse ctr = ", ctr)

                    except IndexError:
                        print("reverse exception handled")
                        return False

            print("ctr = ", ctr)

            if ctr == self.z:
                return True
            else:
                return False

        def check_nd():

            reverse = False
            ctr = 1
            p = [0, 0]
            for inc in range(1, self.z):

                # searches up the negative diagonal until it does not
                # have the same sign or runs out of spaces in a direction
                try:
                    if self.board[m[0] + inc][m[1] + inc] == player.sign:
                        print("here")
                        ctr += 1
                        print("non reverse ctr = ", ctr)
                except IndexError:
                    print("Exception handled for nd")
                    p = [m[0] + inc, m[1] + inc]
                    print(p)
                    reverse = True

                # when it has gone down the nd it then goes up it to see if the sequence of sign is completed
                if reverse:
                    try:
                        print("reverse")
                        print(p[0] - inc, p[1] - inc)
                        if self.board[p[0] - inc][p[1] - inc] == player.sign:
                            ctr += 1
                            print("reverse ctr = ", ctr)

                    except IndexError:
                        print("reverse exception handled")
                        return False

            print("ctr = ", ctr)

            if ctr == self.z:
                return True
            else:
                return False

        ###########################################################################################################
        def check(c):
            print("Start of checking ", c)
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
                        print("m = ", m)
                        f = [m[0], m[1] + inc]

                    if c == 'vertical':
                        print("m = ", m)
                        f = [m[0] - inc, m[1]]

                    if c == 'pd':
                        print("m = ", m)

                        f = [m[0] - inc, m[1] + inc]

                    if c == 'nd':
                        print("m = ", m)

                        f = [m[0] + inc, m[1] + inc]

                    # searches up the negative diagonal until it does not
                    # have the same sign or runs out of spaces in a direction
                    try:
                        if self.board[f[0]][f[1]] == player.sign:
                            print("here")
                            ctr += 1
                            print("non reverse ctr = ", ctr)
                    except IndexError:
                        print("Exception handled")
                        p = [f[0], f[1]]
                        print("p = ", p)
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
                        print("reverse")
                        print(r[0], r[1])
                        print(self.board[r[0]][r[1]])
                        assert self.row-1 >= r[0] >= 0 and self.col-1 >= r[1] >= 0

                        if self.board[r[0]][r[1]] == player.sign:
                            ctr += 1
                            print("reverse ctr = ", ctr)

                    except IndexError:
                        print("reverse exception handled due to index")
                        return False
                    except AssertionError:
                        print("reverse exception handled due to assertion")
                        return False

            print("ctr = ", ctr)

            if ctr == self.z:
                return True
            else:
                return False
            ###########################################################################################################

        # if check_hori() or check_vert or check pd or check nd:
        # if check_pd() or check_nd() or check_hori() or check_vert():
        #     return True
        if check('pd') or check('nd') or check('horizontal') or check('vertical'):
            return True
        else:
            return False


# p1 = Player('1')
# p2 = Player('2')
# arena = Game(3, 3, 3, p1, p2, [1, 2, 3])
#
# arena.make_move(p1, 1)
# arena.make_move(p1, 2)
#
# win = arena.check_win(p1, arena.make_move(p1, 3))
#
# print(win)

# read_file()
# this will be in play loop iterating through every move set
#        for moves in player_moves
#           arena.make_move(player, move)


def draw():
    print(0)
    quit()


def p1_wins():
    print(1)
    quit()


def p2_wins():
    print(2)
    quit()


def incomplete_check():
    print(3)
    quit()


def illegal_continue_check():
    print(4)
    quit()


def illegal_row():
    print(5)
    quit()


def illegal_column():
    print(6)
    quit()


def illegal_game():
    print(7)
    quit()


def invalid_file():
    print(8)
    quit()


def file_error():
    print(9)
    quit()


if __name__ == '__main__':
    p1 = Player('1')
    p2 = Player('2')

    dim, move_set = read_file()

    print(dim)
    print(move_set)
    arena = Game(dim[0], dim[1], dim[2], p1, p2)

    complete = False
    win1 = False
    win2 = False

    # arena.make_move(p1, 1)
    # print(arena.board)
    # arena.make_move(p2, 2)
    # print(arena.board)
    # arena.make_move(p1, 3)
    # print(arena.board)
    # arena.check_win(p2,arena.make_move(p2, 1))
    # print(arena.board)

    for count in range(len(move_set)):
        # before z counters are placed there is no need to check for a win
        if count < arena.z:

            if count % 2 == 0:
                arena.make_move(p1, move_set[count])
            else:
                arena.make_move(p2, move_set[count])
            print("count = ", count)
            print(arena.board)



        else:
            print("count and check = ", count)

            if count % 2 == 0:
                if arena.check_win(p1, arena.make_move(p1, move_set[count])):
                    print("player one wins!")
                    complete = True
                    win1 = True
            else:
                if arena.check_win(p2, arena.make_move(p2, move_set[count])):
                    print("player two wins!")
                    complete = True
                    win2 = True
            print(arena.board)

        print("count =  ", count)
        # Illegal continue
        if complete == True and count != len(move_set) - 1:
            illegal_continue_check()

        # Draw
        if arena.list_of_valid_cols() == []:
            draw()

        # Incomplete
        if complete == False and count == len(move_set) - 1:
            incomplete_check()

        # Win for player 1
        if win1:
            p1_wins()

        # Win for player 2
        if win2:
            p2_wins()
