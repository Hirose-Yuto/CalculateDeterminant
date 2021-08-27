import Quotient
import Matrix
import numpy


class Determinant:
    @staticmethod
    def calc_det(matrix: Matrix) -> Quotient.Q:
        # 行列式を宣言
        det = Quotient.Q(1, 1)
        for i in range(1, matrix.size + 1):
            # (1, 1)成分が0でないようにする
            # 互換によって行列式の正負は入れ替わるのでそれを返す
            sign = matrix.check_diagonal_zero()

            # 1列について(1, 1)以外を掃き出す
            matrix.one_sweep_matrix()

            # 互換による正負と(1, 1)成分をかけていく．
            det = det * sign * matrix.element(1, 1)

            # どこかでdetが0となったら終了，
            if det.molecule == 0:
                return Quotient.Q(0, 1)

            # 一次行列までたどり着いたら小行列はつくらない
            if matrix.size > 1:
                # 1行，1列を除いた小行列を作る
                matrix = Determinant.make_sub_matrix(matrix)

        return det

    # 1行，1列を除いた小行列を作る
    @staticmethod
    def make_sub_matrix(matrix: Matrix) -> Matrix:
        # サイズが1小さい，小行列を宣言
        sub_matrix = Matrix.Matrix(numpy.zeros(matrix.size * matrix.size))

        # 列単位で代入していく
        for j in range(1, matrix.size):
            # 1行，1列ずらす
            for i in range(1, matrix.size):
                sub_matrix.set(i, j, matrix.element(i + 1, j + 1))
        return sub_matrix
