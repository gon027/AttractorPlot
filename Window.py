import tkinter as tk
from Plot import Plot

# スライダーを作成するクラス
class ParameterScale:
    # スライダーの長さと値の振り幅のパラメータ
    length = 500
    _from = -1.000
    _to = 1.000

    def __init__(self, frame):
        self.value = tk.DoubleVar()
        self.scale = tk.Scale(
            frame,
            variable=self.value,
            orient=tk.HORIZONTAL,
            length=self.length,
            from_=self._from,
            to=self._to,
            resolution=0.001
        )
    
    # スライダーを配置する
    def pack(self):
        self.scale.pack()

    # スライダーの値を取得する
    def get(self):
        return self.scale.get()

# パラメータの管理を担当するクラス
class Window:
    def __init__(self, plot):
        # master
        self.root = tk.Tk()
        self.root.title("Window")
        self.root.geometry("900x750")

        # plotオブジェクトを作成してrootウインドウを登録
        self.plot = plot
        self.plot.addPlotCanvas(self.root)
        self.plot.init()

        # フレームの作成
        self.frame = tk.Frame(self.root)

        # タイトル、alpha、sigma、muのラベルを作成
        self.titleLable = tk.Label(self.frame, text="Parameters")
        self.alpha = tk.Label(self.frame, text="alpha")
        self.sigma = tk.Label(self.frame, text="sigma")
        self.mu = tk.Label(self.frame, text="mu")

        # alpha、sigma、muの値を操作するscaleを作成
        self.alphaScale = ParameterScale(self.frame)
        self.sigmaScale = ParameterScale(self.frame)
        self.muScale = ParameterScale(self.frame)

        # 描画するボタンを作成
        self.drawButton = tk.Button(
            self.frame,
            text="Plot",
            command=self.clickButton,
            width=10,
            height=2
        )

    # ボタンがクリックされた時のイベント
    def clickButton(self):
        # スケールからそれぞれのパラメータの値を取得してくる
        alpha = self.alphaScale.get()
        sigma = self.sigmaScale.get()
        mu = self.muScale.get()

        # 取得したパラメータをセットする
        self.plot.setParameter(alpha, sigma, mu)
        self.plot.plot()

    # 作成したラベルやボタンの配置
    def pack(self):
        self.frame.pack()
        self.titleLable.pack()
        self.alpha.pack()
        self.alphaScale.pack()
        self.sigma.pack()
        self.sigmaScale.pack()
        self.mu.pack()
        self.muScale.pack()
        self.drawButton.pack()

    # ウインドウのメインループ
    def show(self):
        self.root.mainloop()
