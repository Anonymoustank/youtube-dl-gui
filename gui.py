import tkinter
from tkinter.simpledialog import askstring
import os

def Video_Download(): #Video formats are mp4, webm

def Audio_Download(): #Audio formats are mp3, m4a
	

def initialize():

	root.title("Youtube-dl GUI")

	root.geometry("600x600")

	root.deiconify()

	video_option = tkinter.Button(root, text = "Download video", command = lambda:[back_button.destroy(), sound_option.destroy(), video_option.destroy(), Video_Download()])
	
	video_option.pack()

	sound_option = tkinter.Button(root, text = "Download audio", command = lambda:[back_button.destroy(), sound_option.destroy(), video_option.destroy(), Audio_Download()])

	sound_option.pack()

	back_button = tkinter.Button(root, text = "Back", command = lambda:[root.destroy(),ask_link()])

	back_button.pack()

def ask_link():
	global root
	root = tkinter.Tk()

	root.withdraw()

	link = askstring("Link to the video", "Enter the link to the youtube video:")

	download = askstring("Enter your preferred download location:", "Enter your preferred download location:")

	os.system("cd " + download)

	initialize()
	





ask_link()
root.mainloop()