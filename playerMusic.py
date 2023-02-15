import tkinter as tk
import fnmatch
import os
from pygame import mixer
from tkinter import filedialog
from tkinter import messagebox
from pathlib import Path

mixer.init()

player = tk.Tk()
player.title("Lecteur de Musique")
player.geometry("600x800")
player.config(background='#ee85b5')


rootpath = "C:\\Users\\amari\Desktop\music"
pattern = "*.mp3"


prev_img = tk.PhotoImage(file = "prev.png")
next_img = tk.PhotoImage(file = "next.png")
play_img = tk.PhotoImage(file = "play.png")
pause_img = tk.PhotoImage(file = "pause.png")
stop_img = tk.PhotoImage(file = "stop.png")
volup_img = tk.PhotoImage(file = "volup.png")
voldown_img = tk.PhotoImage(file = "voldown.png")
loop_png = tk.PhotoImage(file = "loop.png")

def select():
    label.config(text = listBox.get("anchor"))
    mixer.music.load(rootpath + "\\" + listBox.get("anchor"))
    mixer.music.play()

def stop():
    mixer.music.stop()
    listBox.select_clear('active')

def play_next():
    next_song = listBox.curselection()
    next_song = next_song[0] + 1
    next_song_name = listBox.get(next_song)
    label.config(text = next_song_name)

    mixer.music.load(rootpath + "\\" + next_song_name)
    mixer.music.play()

    listBox.select_clear(0, 'end')
    listBox.activate(next_song)
    listBox.select_set(next_song)

def play_prev():
    next_song = listBox.curselection()
    next_song = next_song[0] - 1
    next_song_name = listBox.get(next_song)
    label.config(text = next_song_name)

    mixer.music.load(rootpath + "\\" + next_song_name)
    mixer.music.play()

    listBox.select_clear(0, 'end')
    listBox.activate(next_song)
    listBox.select_set(next_song)

def pause_song():
    if pauseButton["text"] == "Pause":
        mixer.music.pause()
        pauseButton["text"] = "Play"
    else: 
        mixer.music.unpause()
        pauseButton["text"] = "Pause"

def volume_up():
    volume = mixer.music.get_volume()
    mixer.music.set_volume(min(volume + 0.1, 1))

def volume_down():
    volume = mixer.music.get_volume()
    mixer.music.set_volume(max(volume - 0.1, 0))

def loop_music():
    mixer.music.play(-1)

def add_song():
    file_path = tk.filedialog.askopenfilename(initialdir=rootpath, title="Select File", filetypes=(("Audio Files", "*.mp3"), ("All Files", "*.*")))
    if file_path:
        filename = os.path.basename(file_path)
        if filename not in listBox.get(0, 'end'):
            listBox.insert('end', filename)
        else:
            tk.messagebox.showerror("Erreur", "Cette musique existe déjà!")

def remove_song():
    selected_song = listBox.curselection()
    if selected_song:
        song_name = listBox.get(selected_song[0])
        os.remove(os.path.join(rootpath, song_name))
        listBox.delete(selected_song)


listBox = tk.Listbox(player, fg='#6D5A72', bg='#FFFFFF', width = 100, font =('poppins', 14))
listBox.pack(padx = 15, pady = 15)

label = tk.Label(player, text = '', bg = '#ee85b5', fg = '#6D5A72', font = ('poppins', 18))
label.pack(pady = 15)

top = tk.Frame(player, bg = '#ee85b5')
top.pack(padx = 10, pady = 5, anchor = 'center')

voldownButton = tk.Button(player, text = "Down", image = voldown_img, bg = '#ee85b5', borderwidth = 0, command = volume_down)
voldownButton.pack(pady = 15, in_ = top, side = 'left')

prevButton = tk.Button(player, text ="Prev", image = prev_img, bg = '#ee85b5', borderwidth = 0, command = play_prev)
prevButton.pack(pady = 15, in_ = top, side = 'left')

stopButton = tk.Button(player, text ="Stop", image = stop_img, bg = '#ee85b5', borderwidth = 0, command = stop)
stopButton.pack(pady = 15, in_ = top, side = 'left')

playButton = tk.Button(player, text ="Play", image = play_img, bg = '#ee85b5', borderwidth = 0, command = select)
playButton.pack(pady = 15, in_ = top, side = 'left')

pauseButton = tk.Button(player, text ="Pause", image = pause_img, bg = '#ee85b5', borderwidth = 0, command = pause_song)
pauseButton.pack(pady = 15, in_ = top, side = 'left')

nextButton = tk.Button(player, text ="Next", image = next_img, bg = '#ee85b5', borderwidth = 0, command = play_next)
nextButton.pack(pady = 15, in_ = top, side = 'left')

volupButton = tk.Button(player, text = "Up", image = volup_img, bg = '#ee85b5', borderwidth = 0, command = volume_up)
volupButton.pack(pady = 15, in_ = top, side = 'left')

loopButton = tk.Button(player, text="Loop", image = loop_png , bg = '#ee85b5', borderwidth = 0, command=loop_music)
loopButton.pack()

addButton = tk.Button(player, text="Add", bg='#ee85b5', command=add_song)
addButton.pack(pady=15, in_=top, side='left')

removeButton = tk.Button(player, text ="Remove", bg = '#ee85b5', command = remove_song)
removeButton.pack(pady = 15, in_ = top, side = 'left')

for root, dirs, files in os.walk(rootpath):
    for filename in fnmatch.filter(files, pattern):
        listBox.insert('end', filename)


player.mainloop()