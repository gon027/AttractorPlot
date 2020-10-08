from Plot import Plot
from Window import Window

# PlotとWindowを作成して実行する
def main():
    plt = Plot()
    window = Window(plt)
    window.pack()
    window.show()

if __name__ == "__main__":
    main()

