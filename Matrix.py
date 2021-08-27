import math
import numpy
import Quotient


# 行列クラス
class Matrix:
    # 一次元の配列を受け取り，行列に直す
    def __init__(self, a):
        # 行列の大きさ
        self.size = int(math.sqrt(len(a)))
        self.x = self.__make_matrix(a)

    # (i, j)成分を返す
    def element(self, i: int, j: int) -> Quotient.Q:
        return self.x[i - 1][j - 1]

    # (i, j)成分にelemを代入する
    def set(self, i: int, j: int, elem: Quotient.Q):
        self.x[i - 1][j - 1] = elem

    # 1列について(1, 1)以外を掃き出す
    def one_sweep_matrix(self):
        # 1列を(1, 1)成分を残して行変形により掃き出す
        for i in range(2, self.size+1):
            tmp = self.element(i, 1) / self.element(1, 1)
            for j in range(1, self.size + 1):
                self.set(i, j, self.element(i, j) - (tmp * self.element(1, j)))

    # (1, 1)成分が0でならなくなるように行を入れ替える
    # 互換によって行列式の正負は入れ替わるのでそれを返す
    def check_diagonal_zero(self) -> Quotient.Q:
        swap_count = 0
        for i in range(1, self.size + 1):
            # 0でないものが1列にあったら入れ替え
            # もしなかったらその後でdet = 0と求まるので放置
            if (self.element(i, 1)).molecule != 0:
                swap_count += self.swapRow(1, i)
                break

        if swap_count % 2 == 0:
            # 偶置換なら+1
            return Quotient.Q(1, 1)
        else:
            # 奇置換なら-1
            return Quotient.Q(-1, 1)

    # m行とn行を入れ替える．
    # 互換の個数を返す(0 or 1)
    def swapRow(self, m: int, n: int):
        # 互換が発生しないならそのまま
        if m == n:
            return 0

        # 入れ替え
        for j in range(1, self.size+1):
            tmp = Quotient.Q(-1, 1) * self.element(m, j)
            self.set(m, j, self.element(n, j))
            self.set(n, j, tmp)
        return 1

    # 行列を作る
    def __make_matrix(self, a):
        # 行列を宣言
        m = [[Quotient.Q(0, 1)] * self.size for i in range(self.size)]
        # 各成分を代入する
        for i in range(0, self.size):
            for j in range(0, self.size):
                m[i][j] = Quotient.Q(a[i * self.size + j], 1)
        return m


