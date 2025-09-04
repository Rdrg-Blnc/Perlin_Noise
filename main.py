from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from terrain import Terrain
from terrain import world
from perlin import seed, frequency, amplitude, octaves

app = Ursina()

window.color = color.rgb(0, 205, 255)
indra = Sky()
indra.color = window.color
player = FirstPersonController()
player.gravity = 0.0
player.cursor.visible = False
player.y = 100

txt = Text(text=f'Seed: {seed}\n'
                f'Frequency: {frequency}\n'
                f'Amplitude: {amplitude}\n'
                f'Octaves: {octaves}',
           x=-.85, y=.45, scale=3)

terrain = Terrain()


def update():
    blockfound = False

    if world == 1:
        step = 4
        height = 1
    else:
        step = 4
        height = 100

    x = str(floor(player.x + 0.5))
    z = str(floor(player.z + 0.5))
    y = floor(player.y + 0.5)

    for i in range(-step, step):
        if terrain.dic.get('x' + x + 'y' + str(y + i) + 'z' + z) == 't':
            target = y + i + height
            blockfound = True
            break

    if blockfound:
        player.y = lerp(player.y, target, 6 * time.dt)
    else:
        if world == 1:
            player.y -= 9.8 * time.dt
        else:
            player.y -= 0 * time.dt

    # updateTerrain()


terrain.genterrain()

app.run()
