from tkinter import *
from tkinter.simpledialog import askstring
from subprocess import PIPE, run

def out(command, video_format):

        result = run(command, shell=True, capture_output=True, universal_newlines=True)

        complete = Tk()

        complete.title("Download Results for " + file_name + "." + str(video_format))

        global error_label

        error_label = Label(complete,text=str(result.stderr))

        error_label.pack()

        global result_label

        result_label = Label(complete,text=str(result.stdout))

        result_label.pack()

        success_notify = Label(complete,text="Download completed successfully!")

        if str(result.returncode) == "0":

                success_notify.pack()

        else:
                error_notify = Label(complete,text="Download unsuccessful. Process exited with code " + str(result.returncode) + ".")
                error_notify.pack()




def Video_Download(): #Video formats are mp4, webm
        clicked = StringVar(root)

        clicked.set("mp4")

        menu = OptionMenu(root, clicked, "mp4", "webm")

        menu.pack()

        start_button = Button(root, text = "Start Download", command = lambda:[out("youtube-dl -q -f " + clicked.get() + " " + link + " -o " + "\"" + download + "/" + file_name + "." + clicked.get() + "\"", clicked.get())])

        start_button.pack()

        back_button = Button(root, text = "Back", command = lambda:[menu.destroy(), back_button.destroy(), start_button.destroy(), initialize()])

        back_button.place(x=0,y=0)

def Audio_Download(): #Audio formats are mp3, m4a
        clicked = StringVar(root)

        clicked.set("m4a")

        menu = OptionMenu(root, clicked, "m4a", "mp3")

        menu.pack()

        start_button = Button(root, text = "Start Download", command = lambda:[out("youtube-dl -q -f " + clicked.get() + " " + link + " -o " + "\"" + download + "/" + file_name + "." + clicked.get() + "\"", clicked.get())]) 

        start_button.pack()

        back_button = Button(root, text = "Back", command = lambda:[menu.destroy(), back_button.destroy(), start_button.destroy(), initialize()])

        back_button.place(x=0,y=0)

def initialize():
        root.title("Youtube-dl GUI")

        root.geometry("300x75")

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

        if link == None:
                exit()

        download = askstring("Enter the video download location","Enter the video download location")

        while str(run("cd " + download, shell=True, capture_output=True, universal_newlines=True).returncode) != "0":
                download = askstring("Invalid location","Enter a location that exists and you have access to")
                

        file_name = askstring("File Name? ", "File Name? ")
        
        initialize()



ask_link()
root.mainloop()
