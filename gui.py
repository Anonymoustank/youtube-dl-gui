from tkinter import *
from tkinter.simpledialog import askstring
import time
import subprocess
import os

def Video_Download(): #Video formats are mp4, webm
	clicked = StringVar(root) 
	#Add a back button here and at Audio_Download()
	clicked.set("mp4")

	menu = OptionMenu(root, clicked, "mp4", "webm")

	menu.pack()

	menu_label = Label(text = "Select what format you want to save your video as", font = ('Helvetica', 12), fg ='black')

	menu_label.pack()

	back_button = Button(root, text = "Back", command = lambda:[menu_label.destroy(), menu.destroy(), back_button.destroy(), initialize()])
	
	back_button.pack()

def Audio_Download(): #Audio formats are mp3, m4a
	clicked = StringVar(root)

	clicked.set("mp3")

	menu = OptionMenu(root, clicked, "mp3", "m4a")

	menu.pack()

	menu_label = Label(text = "Select what format you want to save your audio as", font = ('Helvetica', 12), fg ='black')

	menu_label.pack()

	back_button = Button(root, text = "Back", command = lambda:[menu_label.destroy(), menu.destroy(), back_button.destroy(), initialize()])
	
	back_button.pack()

def initialize():
	root.title("Youtube-dl GUI")

	root.geometry("600x600")

	root.deiconify()

	video_option = Button(root, text = "Download video", command = lambda:[back_button.destroy(), sound_option.destroy(), video_option.destroy(), Video_Download()])
	
	video_option.pack()

	sound_option = Button(root, text = "Download audio", command = lambda:[back_button.destroy(), sound_option.destroy(), video_option.destroy(), Audio_Download()])

	sound_option.pack()

	back_button = Button(root, text = "Back", command = lambda:[root.destroy(),ask_link()])

	back_button.pack()

def ask_link():
	global root
	root = Tk()

	root.withdraw()

	link = askstring("Link to the video", "Enter the link to the youtube video:")

	download = askstring("Enter your preferred download location:", "Enter your preferred download location:")

	while os.system("cd " + download) != 0:
		download = askstring("Enter your preferred download location:", "Please enter a location exists and you have access to")
	
	initialize()
	


ask_link()
root.mainloop()