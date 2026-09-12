import pyxel
pyxel.init(160, 160)

class App:
    def __init__(self):
        self.position_x = 20
        self.position_y = 20

        pyxel.load("./matasetana_assets.pyxres")


        pyxel.run(self.update, self.draw)

    def update(self):
        self.position_x +=1

    def draw(self):
        pyxel.cls(0)
        pyxel.blt(
            self.position_x,
            self.position_y,
            0,
            0,
            0,
            16,
            16,
            0,
        )
        # 画像を回転させたい場合：rotate 画像を拡大したい場合：scale の引数を追加できる

App()