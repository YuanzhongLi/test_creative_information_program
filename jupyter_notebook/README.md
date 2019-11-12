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
````

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
