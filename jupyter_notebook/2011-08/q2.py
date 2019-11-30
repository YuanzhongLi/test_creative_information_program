import copy as cp
class Enemy(object):
    def __init__(self):
        self.x = int(4)
        self.y = int(0)
        self.mark = 'O'
        self.vector = [1, 1]

    def __repr__(self):
        return 'x: {0}, y: {1}, vec: {2}'.format(self.x, self.y, self.vector)

    def move(self):
        self.x += self.vector[0]
        self.y += self.vector[1]
        if (self.y > 14):
            self.x = int(4)
            self.y = int(0)
            self.vector = [1, 1]
        elif (self.x == 0):
            self.vector[0] = 1
        elif (self.x == 8):
            self.vector[0] = -1

class Game(object):
    def __init__(self):
        self.default_board = [
            ['|', '-', '-', '-', 'V', '-', '-', '-', '|'],
            ['|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|'],
            ['|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|'],
            ['|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|'],
            ['|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|'],
            ['|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|'],
            ['|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|'],
            ['|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|'],
            ['|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|'],
            ['|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|'],
            ['|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|'],
            ['|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|'],
            ['|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|'],
            ['|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|'],
            ['|', '-', '-', '-', 'X', '-', '-', '-', '|'],
        ]
        self.board = [
            ['|', '-', '-', '-', 'V', '-', '-', '-', '|'],
            ['|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|'],
            ['|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|'],
            ['|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|'],
            ['|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|'],
            ['|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|'],
            ['|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|'],
            ['|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|'],
            ['|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|'],
            ['|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|'],
            ['|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|'],
            ['|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|'],
            ['|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|'],
            ['|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|'],
            ['|', '-', '-', '-', 'X', '-', '-', '-', '|'],
        ]
        self.enemy = Enemy()
        # 初期段階
        self.phase = 0

    def print_board(self):
        row = len(self.board)
        col = len(self.board[0])
        for i in range(0, row):
            row_str = ''
            for j in range(0, col):
                row_str += self.board[i][j]
            print(row_str)

    def move_enemy(self):
        # 移動
        self.enemy.move()

    def update_board(self):
        tmp_board = cp.deepcopy(self.default_board)
        # enemyの移動後を更新
        tmp_board[self.enemy.y][self.enemy.x] = 'O'
        self.board = tmp_board
        # enemyがresetした時にVに戻す
        self.board[0][4] = 'V'

    def update_phase(self):
        self.phase += 1
        self.move_enemy()
        self.update_board()

    def play_game_debug(self):
        print('phase: {0}'.format(game.phase))
        game.print_board()
        print('=' * 20)
        for i in range(0, 20):
            self.update_phase()
            print('phase: {0}'.format(game.phase))
            game.print_board()
            print('=' * 20)

    def play_game(self):
        print('phase: {0}'.format(game.phase))
        game.print_board()
        print('=' * 20)
        for i in range(0, 20):
            self.update_phase()
            print('phase: {0}'.format(game.phase))
            game.print_board()
            print('=' * 20)

game = Game()
game.play_game()
