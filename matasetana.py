import pyxel
pyxel.init(160, 160)

class App:
    def __init__(self):
        self.position_x = 0
        self.position_y = 0

        self.frame_count = 0

        self.direction = 0

        """ self.direction
        0=right
        90=down
        180=left
        270=up
        """

        pyxel.load("./matasetana_assets.pyxres")




        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_DOWN):
            self.direction = 90
        if pyxel.btnp(pyxel.KEY_LEFT):
            self.direction = 180
        if pyxel.btnp(pyxel.KEY_UP):
            self.direction = 270
        if pyxel.btnp(pyxel.KEY_RIGHT):
            self.direction = 0
        print(self.direction)
        self.frame_count += 1
        if self.frame_count % 30 == 0:
            if self.direction == 0:
                self.position_x += 16
            if self.direction == 90:
                self.position_y += 16
            if self.direction == 180:
                self.position_x -= 16
            if self.direction == 270:
                self.position_y -= 16

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
            rotate=self.direction
        )
        # 画像を回転させたい場合：rotate 画像を拡大したい場合：scale の引数を追加できる

App()