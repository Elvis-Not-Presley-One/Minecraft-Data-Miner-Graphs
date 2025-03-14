# Minecraft-Data-Miner-Graphs

![GitHub Downloads (all assets, all releases)](https://img.shields.io/github/downloads/Elvis-Not-Presley-One/Minecraft-Data-Miner-Graphs/total?style=for-the-badge&logo=Github&labelColor=black&color=cyan)
![GitHub commits since latest release](https://img.shields.io/github/commits-since/Elvis-Not-Presley-One/Minecraft-Data-Miner-Graphs/latest?style=for-the-badge&logo=Github&labelColor=black&color=pink)
![GitHub Repo stars](https://img.shields.io/github/stars/Elvis-Not-Presley-One/Minecraft-Data-Miner-Graphs?style=for-the-badge&labelColor=black&color=yellow)



Minecraft-Data-Miner-Graphs is a Python program that creates interactive visual graphs for data from CSV files with Minecraft data within. This program is an offshoot and specifically made for ```lawnguy1201/GoneAxolotl``` Minecraft region data miner, for Maxdog006's 25k End world download (wdl). Interactability and shareable graphs were the main priority of this program. Also, the graphs had to be able to be placed on websites with little hassle causing us to focus on making the graphs .HTML files.
- [The Data Miner](https://github.com/Elvis-Not-Presley-One/LostCassowary)

We first considered making this program in ```Matlab```, but the Matlab file share system is atrocious, so we made the program in ```Python```, using mainly the Plotly API and Matplotlib API.

Minecraft-Data-Miner-Graphs was made over the course of 1 1/2 months, with multiple iterations. I spent a lot of time making this program as optimized as possible. For example, the previous iteration would create graphs about 780k KB in size with larger datasets, and with this current iteration, it's now creating about 5K KB with the same large dataset.

We ran into many problems and challenges throughout the development of the program, one of which was making the graphs as optimized as possible. The main issue we ran into was the ```Biomes.py``` class not working properly. We were using ```sqlite``` to handle the 300Gb CSV file of all biome info. However, we ran into limitations of Plotly at that point with how we were creating graphs with millions of data points that needed to be shown.  

**You will need basic coding knowledge to use this program**


![Screenshot_2025-01-13_191819](https://github.com/user-attachments/assets/05a5f454-4315-49e8-92e1-85f44812e4ad)


# Features
- Create 3d Graphs **(Interactive)**
  - ![9gwzfg](https://github.com/user-attachments/assets/412d2832-d557-498a-8838-5d523fa62f1b)
- Create 3d Animated Graphs **(Interactive)**
  - ![9gwzfg](https://github.com/user-attachments/assets/6d880326-52ba-4712-8892-222d4813375c)
- Create 2d Graphs **(Interactive)**
  - ![Screenshot_2025-01-13_191819](https://github.com/user-attachments/assets/05a5f454-4315-49e8-92e1-85f44812e4ad)
- Create Heatmaps **(Interactive)**
  - ![newplot](https://github.com/user-attachments/assets/ab2ea884-5079-4370-b914-ed2490cc7536)
- Create Mesh Graphs **(Interactive)**
  - ![newplot (2)](https://github.com/user-attachments/assets/a0d63cc6-306e-4dff-8591-c910043371cc)
- Create Pi Charts Based On Percentage
- Create Bar Charts **(Interactive only for Plotly one)**
  - ![newplot (3)](https://github.com/user-attachments/assets/a3d4d81a-121d-4fc3-938d-c1310e3e4c49)
- Find How Many Unique Items There are
- Count How Many Times a Unique Item was placed
- Create .html Files For The Graphs
- Create .html Data Frames To Manually See All Data
- Search For Codysmile11 Signs (Or any other player) **(Interactive)**
  - Create Sorted Data Frame (html)
  - Sort Codysmile11 Signs by date Oldest To Newest
  - Create an Animated Graph of The signs placed Day by Day or Cumulative **(Interactive)**
  - Create 3d, 2d, heatmap, mesh Graph of all the signs together **(Interactive)**

NOTE* I do have a Matlab program that can create an animated graph of the path that was taken to download the world from time chunk data

# How to Use
- Make sure you have all dependencies
- Add your csv files into your directory
- Change the the path in  ```main```
- Comment in the data you would like to use i.e. banner data, signs data (Change the file name to what ever the csv name is)
- Go through the classes and change the name of the graphs or any small details you would like to change

# dependencies
- Python 3.10.0
- Any ide of your choice (made in pycharm)
- Need to download Matplotlib, Plotly, Pandas, datashader, sqlite3 or
  - use the Anaconda Python Interpreter

# Known Bugs
- ```Biome.py``` class not working

# How To Contribute
- Create a fork
- Add your code
- Create a pull request with detailed comments on the changes


# Future Plans
I don't plan on adding to this program anymore

