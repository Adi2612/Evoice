# E-voice

E-voice is a text-to-speech synthesizer for English and other languages,  developed in order to help the visually impaired people using computer generated voice which can read the text to the user.

# Use case

## Command -- For setup
```
sudo apt-get install python python-dev festival festival-dev
```
```
git clone git@github.com:Adi2612/Evoice.git
```
```
cd Evoice/
```
```
make clean 
make all
python2 setup.py build
```
## Command - For running 
```
python2 index.py
```
# Dependencies
1. festival - engine
2. festival - dev
