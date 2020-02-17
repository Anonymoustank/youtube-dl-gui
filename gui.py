import tkinter
from tkinter.simpledialog import askstring

root = tkinter.Tk()

root.withdraw()

link = askstring("Link to the video", "Enter the link to the youtube video:")

def Video_Download():
	print("hi")

def Audio_Download():
	print("hola")

def initialize():

	root.title("Youtube-dl GUI")

	root.geometry("600x600")

	root.deiconify()

	video_option = tkinter.Button(root, text = "Download video", command = Video_Download)
	
	video_option.pack()

	sound_option = tkinter.Button(root, text = "Download audio", command = Audio_Download)

	sound_option.pack()
	





initialize()
root.mainloop()