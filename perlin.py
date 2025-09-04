from Perlin_Noise import PerlinNoise
import random

seed = 362
#seed = random.randint(0, 1000)
frequency = 55
amplitude = 9
octaves = 7


class Perlin:
    def __init__(self):

        self.seed = seed
        self.octaves = octaves
        self.frequency = frequency
        self.amplitude = amplitude

        self.pNoise = PerlinNoise(seed=self.seed, octaves=self.octaves)

    def height(self, x, z):

        y = self.pNoise([x/self.frequency, z/self.frequency]) * self.amplitude

        return y
