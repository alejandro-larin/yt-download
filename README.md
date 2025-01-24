# Dowload YT python
Welcome to my project of download videos in python for initalitation this project is nesesary crear a virtaul enviroment:

## Installation
Clone the ropository with git:

```bash
git clone https://gitlab.com/personal8945746/python/download-list-music.git

```
### Virtual Enviroment
For create a virtual enviroment is nesesary this command and install dependece with pip:

```bash
# Linux
python3 -m venv ./download-list-music
cd download-list-music
source bin/activate
pip install -r requeriments.txt


# Windows
python -m venv download-list-music
cd download-list-music
Scripts\activate
pip install -r requirements.txt
```
## Configure Pytube

For  config they library of pytube is nesesary change this code:
![InnerTube Class Exemple 1](img/config_1.png)

The class cotain a attribute called `client` has to change the code to:
![InnerTube Class Exemple 1](img/config_2.png)

The class is locate in the file `Innertube.py`




