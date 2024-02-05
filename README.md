# AutoClick
Neptun tárgyfelvétel könnyítő


1. Meg kell keresni a Python maga hol fut le, de ez benne szokott lenni az Environment variables -ben. Windows-ba írd be: " Environment variables " || (környezeti váltózók) azt hiszem

2. Adj hozzá új Path-et azt, ahol a Python Script-ek vannak. Alapértelmezett: C:\Users\%username%\AppData\Local\Programs\Python\Python39\Scripts
Ha nem tudod, hogy kell, nézd meg a sorrend képet.

Írd át a %username% -et vagy keress rá fájlkezelőben és onnan másold ki az elérési címet!

Environment variables -> Path -> New -> C:\Users\%username%\AppData\Local\Programs\Python\Python39\Scripts

4. Majd másold be a cmd-be:

	pip install pywin32
	pip install keyboard
	pip install mouse
	pip install pyautogui
	pip install opencv-python
