from ursina import *
from perlin import Perlin, amplitude
import xlsxwriter


world = 1  # 1/2
xy_10 = []
xy_30 = []
xy_50 = []
xy_70 = []
xy_90 = []


class Terrain:
    def __init__(self):

        self.block = load_model('block.obj')
        self.world = world

        if self.world == 1:
            self.textures = 'textures org.png'
        else:
            self.textures = 'textures.png'

        self.subsets = []
        self.numSubsets = 1
        self.subWidth = 100

        self.dic = {}

        self.perlin = Perlin()

        for i in range(0, self.numSubsets):
            e = Entity(model=Mesh(), texture=self.textures)
            e.texture_scale *= 64 / e.texture.width
            self.subsets.append(e)

    def genblock(self, x, y, z):
        model = self.subsets[0].model
        model.vertices.extend([Vec3(x, y, z) + v for v in self.block.vertices])

        self.dic['x' + str(floor(x)) +
                 'y' + str(floor(y + 1)) +
                 'z' + str(floor(z))] = 't'

        if self.world == 1:
            # snow position
            uu = 9
            uv = 6
            if 3 <= y < 6:
                # grass position
                uu = 8
                uv = 7
            if 6 <= y < 9:
                # snowy dirt position
                uu = 8
                uv = 6
            if 1 <= y < 3:
                # stone position
                uu = 8
                uv = 5
        else:
            # red position
            uu = 8
            uv = 7
            if 8 <= y < 10:
                # orange position
                uu = 9
                uv = 7
            if 6 <= y < 8:
                # yellow position
                uu = 10
                uv = 7
            if y == 5:
                # green position
                uu = 11
                uv = 7
            if y == 4:
                # aqua position
                uu = 8
                uv = 6
            if y == 3:
                # light blue position
                uu = 9
                uv = 6
            if y == 2:
                # ocean blue position
                uu = 10
                uv = 6
            if y == 1:
                # purple position
                uu = 11
                uv = 6
            if y == amplitude + 2:
                # black line position
                uu = 8
                uv = 5

        model.uvs.extend([Vec2(uu, uv) + u for u in self.block.uvs])

    def genterrain(self):
        x = 0
        z = 0

        s = int(self.subWidth)

        for k in range(0, s):
            for j in range(0, s):

                y = floor(self.perlin.height(x + k, z + j)) + int(self.perlin.amplitude / 2) + (
                                              self.perlin.amplitude % 2) + 1

                self.genblock(x + k, y, z + j)

                if world == 2:
                    if k == 10:
                        self.genblock(x + k, amplitude + 2, z + j)
                        xy_10.append(y)

                    elif k == 30:
                        self.genblock(x + k, amplitude + 2, z + j)
                        xy_30.append(y)

                    elif k == 50:
                        self.genblock(x + k, amplitude + 2, z + j)
                        xy_50.append(y)

                    elif k == 70:
                        self.genblock(x + k, amplitude + 2, z + j)
                        xy_70.append(y)

                    elif k == 90:
                        self.genblock(x + k, amplitude + 2, z + j)
                        xy_90.append(y)

        if world == 2:
            wb = xlsxwriter.Workbook('noise.xlsx')

            ws = wb.add_worksheet('10')
            ws.write(0, 0, 'x')
            ws.write(0, 1, 'y')
            for i in range(0, 100):
                ws.write(i + 1, 0, i + 1)
                ws.write(i + 1, 1, xy_10[i])

            ws = wb.add_worksheet('30')
            ws.write(0, 0, 'x')
            ws.write(0, 1, 'y')
            for i in range(0, 100):
                ws.write(i + 1, 0, i + 1)
                ws.write(i + 1, 1, xy_30[i])

            ws = wb.add_worksheet('50')
            ws.write(0, 0, 'x')
            ws.write(0, 1, 'y')
            for i in range(0, 100):
                ws.write(i + 1, 0, i + 1)
                ws.write(i + 1, 1, xy_50[i])

            ws = wb.add_worksheet('70')
            ws.write(0, 0, 'x')
            ws.write(0, 1, 'y')
            for i in range(0, 100):
                ws.write(i + 1, 0, i + 1)
                ws.write(i + 1, 1, xy_70[i])

            ws = wb.add_worksheet('90')
            ws.write(0, 0, 'x')
            ws.write(0, 1, 'y')
            for i in range(0, 100):
                ws.write(i + 1, 0, i + 1)
                ws.write(i + 1, 1, xy_90[i])

            wb.close()

        self.subsets[0].model.generate()
