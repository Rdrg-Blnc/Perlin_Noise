# 🎮 Perlin Noise

This experiment focused on finding the optimal parameters for Perlin Noise to recreate a Minecraft-like world.

During the experiment I used 4 python files together with the block textures found in the assets folder.

I also wrote a 4000 word essay explaining the entire research process, experiment methodoly and results.

## 🐍 Python Files
### Main
Creates app and player properties.

Continuously checks the height of terrain to update the value of the player when going up and down the terrain.

### Terrain
Generates every block in the terrain.

Adds specific textures to blocks depending on the height.

Saves heights of the 5 data lines into a spreadsheet.

### Perlin
Contains the parameters for the noise function.

### Perlin_Noise
Contains the algorithm for Perlin Noise.

## ⚠️ Dependencies
The program works in Python v3.11+

Two external libraries are requiered, ***ursina*** and ***xlsxwriter***.
