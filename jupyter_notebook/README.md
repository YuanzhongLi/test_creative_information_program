## 実行環境pypy3
### 実行環境に入る
```
$pyenv activate test_pypy
$pypy3 <file_path>
```

## 2006-02
### theme
- 真理値問題
- リスト

## 2007-08
### theme
- 経路問題
#### (4)
- 配列作りかた
```
[' ' for _ in range(4)]
[' ', ' ', ' ', ' ']

# 二次元配列
[[' ' for _ in range(3)] for _ in range(4)]
# 3row, 4col

[i for i in range(3)]
[0, 1, 2]
```
- 二次元配列でx, y座標の注意点
```
array = \
[[1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]]

# array[x][y]にしないように注意!
array[y][x]
```

### (5)
- queue, stack
```
from collections import deque
l = [0,1,2,3]
q = deque(l)
# O(1)でいか四つができ、stackとしてもqueueとしても使用できる
q.append(4) # 後ろから4を挿入, l=deque([0,1,2,3,4])
q.appendleft(5)#前から5を挿入, l=deque([5,0,1,2,3,4])
x = q.pop() #後ろの要素を取り出す, x=4, l=deque([5,0,1,2,3])
y = q.popleft() # 前の要素を取り出す, y=5, l = deque([0,1,2,3])
```

### (7)
- set
```
s = set()
s.add(<setに入れたい要素>)
<setに存在するか確認したい要素> in s
# booleanを返す
s.discard(<削除したい要素>)
```

## 2010-02
### theme
- グラフ問題z

## 2011-08
### theme
- ゲーム作成

#### (3)
- 入力受付
```
# test.py
import sys
inp = sys.argv[1]
print(inp)

# teminal
$pypy3 test.py abc
$abc
```
```
#test.py
for i in range(0, 5):
  inp = input()
  print(input)

# terminal
$pypy3 test.py
1
1
ab
ab
...
```

- copy
```
import copy as cp
# shallow copy
cp.copy(x)
# deepcopy(完全に別なオブジェクトを作る)
cp.deepcopy(x)
```

#### (4)
- random
```
import random
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]からランダムに一つ
a = random.randrange(10)
# [10, 20, 30, 40, 50, 60, 70, 80, 90]からランダムに一つ
a = random.randrange(10, 100, 10)
- time
```
import time
```
# 現在のunix時間をfloatで取得
a = time.time()
```


## 2012-08
### theme
- アセンブリ

#### (1)
- asciiファイルの開き方
```
with open(file_path, encoding='ascii') as f:
```

#### (3)
- 末尾の\nを削除
```
string.rstrip('\n')
```

## 2013-02
### theme
- 論理式

#### (4)
- マクロ
```
exec('a = 1; b = 2; c = a + b')
c
3

d = 1
e = 2
f = eval(d + e)
f
3
```

- replace
```
'aba'.replace('a', 'b')
'bbb'
```

## 2013-08
### theme
- 再帰
- 点の内包

#### (5),(6)
- 配列結合
```
a = [1, 2, 3]
b = [4, 5]
c = a.extend(b) # [1, 2, 3, 4, 5]
```
- array要素削除(index指定)
```
array.pop(index)
array.pop(-1) # 最後尾削除
```

## 2014-08
### theme
- 文字列探索

### (3)
- 行ごとにファイル読み込みのとき'\n'のみを削除する
```
with open(file_path, 'r') as f:
        text = f.readlines()
        txts = []
        for index, txt in enumerate(text):
            if txt[-1] == '\n':
                txts.append(txt[:-1])
            else:
                txts.append(txt)
```

## 2015-08
### theme
- N進数
#### (4)
- 文字列reverse
```
string[::-1]
```
#### (7)
- 文字列分割
```
string.split() # 空白で分割
string.split('文字') # 指定文字で分割
```
- array結合して文字列
```
'文字'.join(array) # 要素間に文字を追加して文字列にする
```

## 2016-08
### theme
- キャンバス描画
#### (2)
- 配列比較で全要素比較
```
a = [['a', 'c'], ['b', 'd']]
b = [['a', 'c'], ['b', 'd']]
a == b
True
```

#### (4)
- stripは前だけでなく後ろのスペースも削除してしまう
```
a = '    abc def ghi  \n'
a.strip()
'abc def ghi'
```
- '\n'で1文字分
```
b = 'a\n'
len(b)
2
```

## 2017-08
### theme
- キャッシュミス

## 2018-08
### theme
- 画像圧縮
- byte書き出し
#### (3)
- compare(key)でのsort cf) l.41
```
def cmp():
sorted_list = sorted(list, key=cmp)
```
#### (6)
- 配列でindexを使いたい
```
for index, ele in enumerate(list):
```
- byteにする
```
(number).to_bytes(<何バイトか>, beteorder='big(or littel)')
# typeはbyteになる
```
- バイナリ書き出し
```
# 上書き
whith open('file_name', 'wb') as fout:
# 追加
whith open('file_name', 'ab') as fout:
```

## Divisors
- 末尾追加(append)
```
array.append(a)
```
- 途中追加(insert)
```
array = [1, 2, 3]
array.insert(2, 2.5)
array # [1, 2, 2.5, 3]
```

## Cordinate
- swap
```
a, b = b, a
```
- objectとnp.array
```
a = np.empty((2, 3), dtype=Point)
p = Point(1, 1)
a[0][0] = p
```

## その他
- classをsetに入れる
```
class T(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def __eq__(self, t):
        return (self.x == self.x) and (self.y == self.y) and (self.z == self.z)
    def __hash__(self):
        string = '{0}, {1}, {2}'.format(self.x, self.y, self.z)
        return hash(string)
    def __repr__(self):
        return '{0}, {1}, {2}'.format(self.x, self.y, self.z)

a = T(1,[1],'a')
b = T(1,[1, 2], 'b')
s = set()
s.add(b)
s.add(a)
s.add(b)
```

- 割り算切り捨て
```
4 // 3
1
```
