# Hollow_Knight_RoomRando_Mapper
...To chart the world. What joy... If only ~~Iselda~~ other Hollow Knight room rando players could share the thrill...

Hollow Knight room randomizer is hard. I can never remember where things are, and what room transitions lead to where.
Well, why not just map it out?

# Dependency
Linux:
```
sudo apt-get install -y graphviz
pip install graphviz
```

Mac:
```
brew install graphviz
pip install graphviz
```

This script works with the following versions:
- Hollow Knight base game version 1.5.78.11833
- `Randomizer 4` version 4.1.6.0
- Python version 3.12

Compability with all other versions is untested.

# Installation
Just git clone this repo.

# Usage
1. In your current room rando run, open the helper log. It should be called `HelperLog.txt`. On my PC, the path to it is
```
C:\Users\<username>\AppData\LocalLow\Team Cherry\Hollow Knight\Randomizer 4\Recent\HelperLog.txt
```
Of course the path can be different depending on a bunch of things. But there should be a GUI button you can click in the rando startup menu.

2. Rename it to `data.txt` and put it in your cloned repo folder. Of course you can rename the target file in the source code too if you want to, or update the file read to take in arbitrary names. I'm too lazy to do that.

3. Just run
```
python draw_map.py
```
There's both an immediate display, and also the map will be saved to `map.pdf`.
The map should be self-explanatory.
Unchecked transitions in already visited rooms are marked with a bright red color, to distinguish themselves from all the existing area colors.

This is just a visualizer. Once you have the map, what you do with it is up to you.

To fully simulate the knight and Cornifer's experience, when you sit down on a bench in a room rando run, and the "Map Updated" icon is displaying, you can run this mapper. This way, it will feel like the "Map Updated" icon and quill animation is actually you (the player) recording new locations you visited on your map.

To simulate the experience even further, you can also consider not using the mapper until you found the quill in the run.

# Example
There's a sample `data.txt` in the repo, and a sample drawn `map.pdf`.
Enjoy.

<p align="center">
  <img src="https://raw.githubusercontent.com/paul0403/Hollow_Knight_RoomRando_Mapper/master/map.pdf#gh-light-mode-only" width="700px">
  <img src=".map" width="700px" onerror="this.style.display='none'" alt=""/>
</p>
