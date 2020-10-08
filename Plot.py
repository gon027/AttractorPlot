import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import tkinter as tk

# グラフの描画を担当するクラス
class Plot:
    # 初期パラメータ
    alpha = 0.0
    sigma= 0.0
    mu = 0.0

    def __init__(self):
        self.reset()

    # root(master)ウインドウに描画するグラフを追加する
    def addPlotCanvas(self, master):
        self.fig = plt.Figure()
        self.ax = self.fig.add_subplot(111)

        # キャンバスの作成
        self.canvas = FigureCanvasTkAgg(self.fig, master=master)
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH)

        # この関数を呼び出し時に描画しておく
        self.plot()

    # 初期化
    def init(self):
        x = 0.1
        y = 0.1

        for _ in range(5000):
            x, y = self.next(x, y)
            self.X.append(x)
            self.Y.append(y)

    # 配列をからにする
    def reset(self):
        self.X = []
        self.Y = []

    # クリアする
    def clear(self):
        self.reset()
        self.ax.clear()

    # パラメータを設定する
    def setParameter(self, _alpha, _sigma, _mu):
        self.alpha = _alpha
        self.sigma= _sigma
        self.mu = _mu

    # プロットする
    def plot(self):
        self.clear()
        self.init()
        self.ax.scatter(self.X, self.Y, s=0.5, alpha=0.75)
        self.canvas.draw()

    # 漸化式の次の項を計算する
    def next(self, _x, _y):
        nx = _y + self.alpha * _y * (1 - self.alpha - self.sigma* _y * _y) + self.g(_x)
        ny = -_x + self.g(nx)
        return (nx, ny)

    # g(x)の値を計算する
    def g(self, _x):
        return self.mu * _x + (2 * (1 - self.mu) * _x * _x) / (1 + _x * _x)
