# 有理数クラス
class Q:
    def __init__(self, m: int, d: int):
        # 分子
        self.molecule: int = m
        # 分母
        self.denominator: int = d

    # 四則演算を定義
    # 和
    def __add__(self, other):
        # 通分してから足す
        den_gcd = self.__abs_gcd(self.denominator, other.denominator)
        # (by/ax) + (bs/at) = (by*t + x*bs)/(x*at)のような計算
        add_molecule = self.molecule * (other.denominator // den_gcd) + (self.denominator // den_gcd) * other.molecule
        add_denominator = (self.denominator // den_gcd) * other.denominator

        add = Q(add_molecule, add_denominator)
        # 約分
        add.__reduceQ()
        return add

    # 差
    def __sub__(self, other):
        return self + (Q(-1, 1) * other)

    # 積
    def __mul__(self, other):
        # 約分しながら掛ける
        gcd_a = self.__abs_gcd(self.molecule, other.denominator)
        gcd_b = self.__abs_gcd(self.denominator, other.molecule)
        # (by /ax) * (as/bt) = (ys/xt)のような計算
        mul_molecule = (self.molecule // gcd_a) * (other.molecule // gcd_b)
        mul_denominator = (self.denominator // gcd_b) * (other.denominator // gcd_a)

        mul = Q(mul_molecule, mul_denominator)
        # 念の為約分
        mul.__reduceQ()
        return mul

    # 商
    def __truediv__(self, other):
        return self * Q(other.denominator, other.molecule)

    # 有理数の表示
    def print(self):
        print(self.molecule / self.denominator)
        if self.molecule % self.denominator == 0:
            print("整数です")

    # 約分
    def __reduceQ(self):
        # 最大公約数を求めて割る
        gcd = self.__abs_gcd(self.molecule, self.denominator)
        self.molecule = self.molecule // gcd
        self.denominator = self.denominator // gcd

    # ユークリッドの互除法
    def __abs_gcd(self, a: int, b: int) -> int:
        # 絶対値の最大公約数を求める
        x = abs(a)
        y = abs(b)
        return int(self.__gcd(max(x, y), min(x, y)))

    def __gcd(self, a: int, b: int) -> int:
        # どちらかが0なら1を返す
        if a == 0 or b == 0:
            return 1

        # 互除法の操作
        if a % b != 0:
            return self.__gcd(b, a % b)
        else:
            return b
