import unittest

from ConnectZ import Game, Player


class Test_ConnectZ(unittest.TestCase):

    def test_hori1(self):
        p1 = Player('1')
        p2 = Player('2')
        arena = Game(3, 3, 3, p1, p2)
        arena.make_move(p1, 1)
        arena.make_move(p1, 2)
        win = arena.check_win(p1, arena.make_move(p1, 3))

        self.assertEqual(win, True)

    def test_hori2(self):
        p1 = Player('1')
        p2 = Player('2')
        arena = Game(3, 3, 3, p1, p2)
        arena.make_move(p1, 1)
        arena.make_move(p1, 3)
        win = arena.check_win(p1, arena.make_move(p1, 2))

        self.assertEqual(win, True)

    def test_hori3(self):
        p1 = Player('1')
        p2 = Player('2')
        arena = Game(3, 3, 3, p1, p2)
        arena.make_move(p1, 2)
        arena.make_move(p1, 3)
        win = arena.check_win(p1, arena.make_move(p1, 1))

        self.assertEqual(win, True)

    def test_hori4(self):
        p1 = Player('1')
        p2 = Player('2')
        arena = Game(5, 5, 4, p1, p2)
        arena.make_move(p1, 4)
        arena.make_move(p1, 2)
        arena.make_move(p1, 5)
        win = arena.check_win(p1, arena.make_move(p1, 3))

        self.assertEqual(win, True)

    def test_vert1(self):
        p1 = Player('1')
        p2 = Player('2')
        arena = Game(3, 3, 3, p1, p2)
        arena.make_move(p1, 1)
        arena.make_move(p1, 1)
        win = arena.check_win(p1, arena.make_move(p1, 1))

        self.assertEqual(win, True)

    def test_vert2(self):
        p1 = Player('1')
        p2 = Player('2')
        arena = Game(3, 3, 3, p1, p2)
        arena.make_move(p1, 3)
        arena.make_move(p1, 3)
        win = arena.check_win(p1, arena.make_move(p1, 3))

        self.assertEqual(win, True)


    def test_vert3(self):
        p1 = Player('1')
        p2 = Player('2')
        arena = Game(3, 3, 3, p1, p2)
        arena.make_move(p1, 1)
        arena.make_move(p2, 3)
        arena.make_move(p1, 1)
        arena.make_move(p2, 3)

        win = arena.check_win(p1, arena.make_move(p1, 1))

        self.assertEqual(win, True)


    def test_loss(self):
        p1 = Player('1')
        p2 = Player('2')
        arena = Game(3, 3, 3, p1, p2)
        arena.make_move(p1, 1)
        arena.make_move(p2, 3)
        arena.make_move(p1, 1)
        arena.make_move(p2, 3)

        win = arena.check_win(p1, arena.make_move(p2, 3))

        self.assertEqual(win, False)



    def test_pd_win1(self):
        p1 = Player('1')
        p2 = Player('2')
        arena = Game(3, 3, 3, p1, p2)
        arena.make_move(p1, 1)
        arena.make_move(p1, 2)
        arena.make_move(p1, 2)
        arena.make_move(p2, 3)
        arena.make_move(p1, 3)
        win = arena.check_win(p1, (arena.make_move(p1, 3)))
        print(arena.board)

        self.assertEqual(win, True)

    def test_pd_win2(self):
        p1 = Player('1')
        p2 = Player('2')
        arena = Game(3, 3, 3, p1, p2)
        arena.make_move(p1, 2)
        arena.make_move(p1, 2)
        arena.make_move(p2, 3)
        arena.make_move(p1, 3)
        arena.make_move(p1, 3)
        win = arena.check_win(p1, (arena.make_move(p1, 1)))
        print(arena.board)

        self.assertEqual(win, True)

    def test_pd_win3(self):
        p1 = Player('1')
        p2 = Player('2')
        arena = Game(3, 3, 3, p1, p2)
        arena.make_move(p1, 1)
        arena.make_move(p1, 2)
        arena.make_move(p2, 3)
        arena.make_move(p1, 3)
        arena.make_move(p1, 3)
        win = arena.check_win(p1, (arena.make_move(p1, 2)))
        print(arena.board)

        self.assertEqual(win, True)

    def test_nd_win1(self):
        p1 = Player('1')
        p2 = Player('2')
        arena = Game(3, 3, 3, p1, p2)
        arena.make_move(p2, 1)
        arena.make_move(p2, 1)
        arena.make_move(p1, 1)
        arena.make_move(p2, 2)
        arena.make_move(p1, 2)

        win = arena.check_win(p1, arena.make_move(p1, 3))
        print(arena.board)

        self.assertEqual(win, True)

    def test_nd_win2(self):
        p1 = Player('1')
        p2 = Player('2')
        arena = Game(3, 3, 3, p1, p2)
        arena.make_move(p2, 1)
        arena.make_move(p2, 1)
        arena.make_move(p1, 1)
        arena.make_move(p1, 2)
        arena.make_move(p1, 3)

        win = arena.check_win(p1, (arena.make_move(p1, 2)))
        print(arena.board)

        self.assertEqual(win, True)


    def test_nd_win3(self):
        p1 = Player('1')
        p2 = Player('2')
        arena = Game(3, 3, 3, p1, p2)
        arena.make_move(p2, 1)
        arena.make_move(p2, 1)
        arena.make_move(p2, 2)
        arena.make_move(p1, 2)
        arena.make_move(p1, 3)

        win = arena.check_win(p1, (arena.make_move(p1, 1)))
        print(arena.board)

        self.assertEqual(win, True)

if __name__ == '__main__':
    unittest.main()
