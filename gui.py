from tkinter import *
from tkinter.simpledialog import askstring
import os
import time
from subprocess import PIPE, run

times_ran = 0

error_label = None

result_label = None

def out(command):
        global times_ran
        
        global error_label

        global result_label
        
        if times_ran > 0:
                
                error_label.destroy()
                
                result_label.destroy()
                
        result = run(command, shell=True, capture_output=True, universal_newlines=True)
        
        time.sleep(2)
        
        error_label = Label(root,text=str(result.stderr))
        
        error_label.pack()
        
        result_label = Label(root,text=str(result.stdout))

        result_label.pack()

        times_ran = times_ran + 1
                
        
        

def Video_Download(): #Video formats are mp4, webm
	clicked = StringVar(root)
	
	clicked.set("mp4")

	menu = OptionMenu(root, clicked, "mp4", "webm")

	menu.pack()

	start_button = Button(root, text = "Start Download", command = lambda:[out("youtube-dl -f -q " + clicked.get() + " " + link + " -o " + "\"" + download + "/" + file_name + "." + clicked.get() + "\"")]) #Ask quotes to download and what comes after

	start_button.pack()

	back_button = Button(root, text = "Back", command = lambda:[menu.destroy(), back_button.destroy(), start_button.destroy(), error_label.destroy(), result_label.destroy(), initialize()])
	
	back_button.place(x=0,y=0)

def Audio_Download(): #Audio formats are mp3, m4a
	clicked = StringVar(root)

	clicked.set("m4a")

	menu = OptionMenu(root, clicked, "m4a", "mp3")

	menu.pack()

	start_button = Button(root, text = "Start Download", command = lambda:[out("youtube-dl -f -q " + clicked.get() + " " + link + " -o " + "\"" + download + "/" + file_name + "." + clicked.get() + "\"")]) #Add quotes to download and what comes after

	start_button.pack()

	back_button = Button(root, text = "Back", command = lambda:[menu.destroy(), back_button.destroy(), start_button.destroy(), error_label.destroy(), result_label.destroy(), initialize()])
	
	back_button.place(x=0,y=0)

def initialize():
	root.title("Youtube-dl GUI")

	root.geometry("600x600")

	root.deiconify()

	video_option = Button(root, text = "Download video", command = lambda:[back_button.destroy(), sound_option.destroy(), video_option.destroy(), Video_Download()])
	
	video_option.pack()

	sound_option = Button(root, text = "Download audio", command = lambda:[back_button.destroy(), sound_option.destroy(), video_option.destroy(), Audio_Download()])

	sound_option.pack()

	back_button = Button(root, text = "Back", command = lambda:[root.destroy(),ask_link()])

	back_button.place(x=0,y=0)

def ask_link():
	global root
	global link
	global download
	global file_name
	root = Tk()

	root.withdraw()

	link = askstring("Link to the video", "Enter the link to the youtube video:")

	download = askstring("Enter your preferred download location:", "Enter your preferred download location:")

	while os.system("cd " + download) != 0:
		download = askstring("Entered your preferred download location:", "Enter a location that exists and you have access to:")
	file_name = askstring("File Name? ", "File Name? ")  
	initialize()
	
        

ask_link()
root.mainloop()
