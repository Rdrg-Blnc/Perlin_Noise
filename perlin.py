from Perlin_Noise import PerlinNoise
import random

# use a chosen or random seed
#seed = 001
seed = random.randint(0, 1000)
frequency = 55
amplitude = 5
octaves = 1


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

