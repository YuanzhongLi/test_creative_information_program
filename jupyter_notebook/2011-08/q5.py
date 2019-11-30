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

class Bullet(object):
    def __init__(self, x:int):
        self.x = int(x)
        self.y = int(14)
        self.mark = 'e'
    def __repr__(self):
        return 'x: {0}, y: {1}'.format(self.x, self.y)
    def move(self):
        self.y -= 1

class Gun(object):
    def __init__(self):
        self.x = int(4)
        self.mark = 'X'
        # 残弾数
        self.remain_bullet = 2
    def __repr__(self):
        return 'x: {0}, 残弾数: {1}'.format(self.x, self.remain_bullet)

class Game(object):
    def __init__(self):
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
            ['|', '-', '-', '-', '-', '-', '-', '-', '|'],
        ]
        self.enemy = Enemy()
        self.bullets = []
        self.gun = Gun()
        self.point = 0
        self.fail = 0
        # 初期段階
        self.phase = 0

    def print_board(self):
        row = len(self.board)
        print()
        col = len(self.board[0])
        for i in range(0, row):
            row_str = ''
            for j in range(0, col):
                row_str += self.board[i][j]
            print(row_str)

    def fire_gun(self, key):
        if (self.gun.remain_bullet > 0 and key == 'i'):
            self.bullets.append(Bullet(self.gun.x))
            self.gun.remain_bullet -= 1

    def move_enemy(self):
        # 移動
        self.enemy.move()
        if (self.enemy.y == 14):
            self.fail += 1
        # 初期位置にreset
        elif (self.enemy.y == 0):
            self.gun.remain_bullet = 2

    def move_bullets(self):
        for index, bullet in enumerate(self.bullets):
            if (bullet.y >= 0):
                bullet.move()

    def get_default_board_cell(self, x, y):
        if (x == 4 and y == 0):
            return 'V'
        elif (x == 0 or x == 8):
            return '|'
        elif (y == 0 or y == 14):
            return '-'
        else:
            return ' '
    def move_gun(self, key):
        if (key == 'j'):
            self.gun.x -= 1
            if (self.gun.x < 0):
                self.gun.x = 0
        if (key == 'l'):
            self.gun.x += 1
            if (self.gun.x > 8):
                self.gun.x = 8

    def update_board(self):
        tmp_board = cp.deepcopy(self.default_board)
        # enemyの移動後を更新
        tmp_board[self.enemy.y][self.enemy.x] = 'O'
        # enemyがresetした時にVに戻す
        tmp_board[0][4] = 'V'
        # gunの移動を更新
        tmp_board[14][self.gun.x] = 'X'
        # bulletの移動を更新
        for index, bullet in enumerate(self.bullets):
            if (bullet.y > 0 and bullet.y < 14):
                # enemyに当たった
                if (tmp_board[bullet.y][bullet.x] == 'O'):
                    tmp_board[bullet.y][bullet.x] = self.get_default_board_cell(bullet.x, bullet.y)
                    self.point += 1
                    self.gun.remain_bullet = 2
                    # reset enemy
                    self.enemy = Enemy()
                    # disable bullet
                    bullet.y = -1
                else:
                    tmp_board[bullet.y][bullet.x] = 'e'
        self.board = tmp_board

    def update_phase(self, key):
        if (key == 'i' or key == 'j' or key == 'k' or key == 'l'):
            self.phase += 1
            self.move_gun(key)
            self.fire_gun(key)
            self.move_enemy()
            self.move_bullets()
            self.update_board()

    def play_game_debug(self):
        print('phase: {0}, point: {1}, fail: {2}, 残弾数: {3}'.format(game.phase, game.point, game.fail, game.gun.remain_bullet))
        game.print_board()
        print('=' * 20)
        for i in range(0, 40):
            randn = random.randrange(4)
            key = 'k'
            if (randn == 0):
                key = 'i'
            if (randn == 1):
                key ='j'
            if (randn == 2):
                key = 'k'
            if (randn == 3):
                key = 'l'
            print('key: ', key)
            self.update_phase(key)
            print('phase: {0}, point: {1}, fail: {2}, 残弾数: {3}'.format(game.phase, game.point, game.fail, game.gun.remain_bullet))
            game.print_board()
            print('=' * 20)

    def play_game(self):
        print('phase: {0}, point: {1}, fail: {2}, 残弾数: {3}'.format(game.phase, game.point, game.fail, game.gun.remain_bullet))
        game.print_board()
        print('=' * 20)
        while (game.fail < 5):
            key = input()
            self.update_phase(key)
            print('phase: {0}, point: {1}, fail: {2}, 残弾数: {3}'.format(game.phase, game.point, game.fail, game.gun.remain_bullet))
            game.print_board()
            print('=' * 20)

game = Game()
game.play_game()
