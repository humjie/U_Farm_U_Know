import random
import tkinter as tk
from PIL import Image, ImageTk
import pygame
import os
import time
import threading
import imageio
import re
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import webbrowser
from data import A_type, R_type, S_type, I_type, E_type, C_type, books, flower, language_of_flower, famous_example, mystery_document, riasec_description


### window
window = tk.Tk()
window.configure(bg="green")
window.title("U FARM U KNOW")
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window.geometry(f"{screen_width}x{screen_height}")
window.attributes("-fullscreen", True)
window.resizable()

def exit_fullscreen(event):
    window.attributes("-fullscreen", False)
window.bind("<Escape>", exit_fullscreen)



### background_music
def play_music():
    pygame.mixer.init()
    pygame.mixer.music.set_volume(0.05)
    pygame.mixer.music.load(os.path.join(os.getcwd(), "resources/background_music.mp3"))
    pygame.mixer.music.play()
play_music()



### page 2
## page 2 frame
frame_page_2 = tk.Frame(master=window)
page_2_background_label = tk.Label(master=frame_page_2, bg="chartreuse4")
def page_2():
    page_2_background_label.pack(fill=tk.BOTH, expand=True)
    frame_page_2.pack(fill=tk.BOTH, expand=True)
    tk.Frame.tkraise(frame_page_2)
    frame_page_2.place(x=0, y=0, relwidth=1, relheight=1)

class Game_discription():
    def __init__(self):
        self.background = Image.open('resources/image/other_image/discription_background.png').resize((screen_width, screen_height), Image.Resampling.LANCZOS)
        self.resized_background = ImageTk.PhotoImage(self.background)

        self.frame_discription = tk.Frame(master=window, bg='chartreuse4')
        self.label = tk.Label(self.frame_discription, text="", justify='center', font=("Comic Sans MS", 48), bg="chartreuse4", image=self.resized_background, compound="center")
        self.close_button = tk.Button(self.frame_discription, text="Close", font=("Comic Sans MS", 20), bd=1, width=8, height=2, command=self.close)
        self.next_button = tk.Button(self.frame_discription, text="Next", font=("Comic Sans MS", 20), bd=1, width=8, height=2, command=self.next)



        self.file_content = ['QUICK!!!!!', 'EASY!!!!!', 'Knowing yourself by farming in just 10 minutes!!!!!',
        'What you need to do is.....', 'Discover how to play this game by yourselves!', 'Here’s what you do:',
        'Farming', 'Solve mystery events', 'and Accumulate your total asset to $6000!', 'Finally.....',
        'We’ll apply John Holland Self-Directed Search', 'To delve deeper into your personality traits!']
        self.repeat_num = 0
        self.update_content_word_num = 0
        self.update_content_word_show = ""

    def loading_then_show_next_page(self):
        self.frame_discription.pack(fill=tk.BOTH, expand=True)
        tk.Frame.tkraise(self.frame_discription)
        self.frame_discription.place(x=0, y=0, relwidth=1, relheight=1)
        play_loading = Video_player(self.frame_discription, "resources/video/loading.mp4")
        self.frame_discription.after(5000, play_loading.close_video)
        self.frame_discription.after(0, self.show_game_discription_page)

    def show_game_discription_page(self):
        self.label.place(relx=0.5, rely=0.5, anchor="center")
        self.update_content()

    def update_content(self):
        if self.repeat_num == 0:
            self.label.config(text="")
            self.update_content_word()
            self.next_button.place(relx=0.9, rely=0.85, anchor="center")
        elif self.repeat_num <= 11 and self.repeat_num > 0:
            self.next_button.place(relx=0.9, rely=0.85, anchor="center")
        else:
            self.close_button.place(relx=0.9, rely=0.85, anchor="center")

    def next(self):
        self.next_button.place_forget()
        self.label.config(text="")
        self.update_content_word()

    def update_content_word(self):
        if self.update_content_word_num < len(self.file_content[self.repeat_num]):
            self.update_content_word_show += self.file_content[self.repeat_num][self.update_content_word_num]
            self.label.config(text=self.update_content_word_show)
            self.update_content_word_num += 1
            self.frame_discription.after(20, self.update_content_word)
        else:
            self.repeat_num += 1
            self.update_content_word_show = ""
            self.update_content_word_num = 0
            self.update_content()

    def close(self):
        self.frame_discription.place_forget()
        page_2()

game_discription = Game_discription()

### page 1
## page 1 frame
frame_page_1 = tk.Frame(master=window)
frame_page_1.pack(fill=tk.BOTH, expand=True)


## background video
class Video_player():
    def __init__(self, master, video_path):
        self.master = master
        self.video_path = video_path
        self.video_label = tk.Label(self.master)
        self.video_label.pack(fill=tk.BOTH, expand=True)
        self.video_can_play = True

        self.start_video_thread()

    def play_video(self):
        while self.video_can_play:
            video_reader = imageio.get_reader(self.video_path)
            for frame in video_reader.iter_data():
                video_image = Image.fromarray(frame)
                video_photo = ImageTk.PhotoImage(video_image)

                self.master.after(0, self.update_video_label, video_photo)
                time.sleep(2 / video_reader.get_meta_data()['fps'])
    def update_video_label(self, photo):
        self.video_label.configure(image=photo)
        self.video_label.image = photo

    def start_video_thread(self):
        self.video_thread = threading.Thread(target=self.play_video)
        self.video_thread.daemon = True
        self.video_thread.start()

    def close_video(self):
        self.video_can_play = False
        self.video_label.pack_forget()


Video_player(frame_page_1, "resources/video/page_1_background.mp4")


## page 1 title
title_image = ImageTk.PhotoImage(Image.open("resources/image/other_image/title.png"))
title = tk.Label(master=window, image=title_image, bg="azure2", relief="solid", borderwidth=6, highlightbackground="black", highlightthickness=2)
title.place(relx=0.5, rely=0.25, anchor="center")


## page 1 start button
start_button = tk.Button(master=frame_page_1, text="Start", bg="white", fg="black", width=15, height=3, font=("Comic Sans MS", 15), command=game_discription.loading_then_show_next_page)
start_button.place(relx=0.5, rely=0.5, anchor="center")


##page 1 setting button
class Setting_menu():
    def __init__(self, button, master, relx, rely):
        self.button = button
        self.master = master
        self.relx = relx
        self.rely = rely
        self.current_volume = 0.05
        self.can_open_volume = 1

        self.setting_button_menu = tk.Menu(self.button)
        button.config(menu=self.setting_button_menu)

        self.setting_button_menu.add_command(label="Language", command=self.language, font=("Comic Sans MS", 10))
        self.setting_button_menu.add_command(label="Volume", command=self.volume, font=("Comic Sans MS", 10))
        self.setting_button_menu.add_command(label="Quit", command=self.quit, font=("Comic Sans MS", 10))

    def language(self):
        pass

    def set_volume(self, val):
        volume = float(val) / 100
        pygame.mixer.music.set_volume(volume)
        self.current_volume = float(val)

    def volume(self):
        if self.can_open_volume == 1:
            self.can_open_volume = 0
            self.volume_slider = tk.Scale(master=self.master, from_=0, to=100, orient='horizontal', command=self.set_volume)
            self.volume_slider.set(self.current_volume)
            self.volume_slider.place(relx=self.relx, rely=self.rely, anchor="center")
            self.volume_slider.bind("<ButtonRelease-1>", self.destroy_volume_slider)

    def quit(self):
        pygame.mixer.music.stop()
        pygame.quit()
        window.destroy()

    def destroy_volume_slider(self, event):
        if event.widget == self.volume_slider:
            self.volume_slider.destroy()
            self.can_open_volume = 1

setting_button_1 = tk.Menubutton(master=frame_page_1, text="Setting", bg="white", fg="black", width=15, height=3, font=("Comic Sans MS", 15))
setting_button_1.place(relx=0.5, rely=0.7, anchor="center")
Setting_menu(setting_button_1, frame_page_1, 0.5, 0.8)



### page 2
## plant image
image_size_x = 80
image_size_y = 80
arableland_image = Image.open('resources/image/plant_image/arableland.png').resize((image_size_x, image_size_y), Image.Resampling.LANCZOS)
arableland_image = ImageTk.PhotoImage(arableland_image)
paddy1 = Image.open('resources/image/plant_image/paddy1.png').resize((image_size_x, image_size_y), Image.Resampling.LANCZOS)
paddy2 = Image.open('resources/image/plant_image/paddy2.png').resize((image_size_x, image_size_y), Image.Resampling.LANCZOS)
potato1 = Image.open('resources/image/plant_image/potato1.png').resize((image_size_x, image_size_y), Image.Resampling.LANCZOS)
potato2 = Image.open('resources/image/plant_image/potato2.png').resize((image_size_x, image_size_y), Image.Resampling.LANCZOS)
cabbage1 = Image.open('resources/image/plant_image/cabbage1.png').resize((image_size_x, image_size_y), Image.Resampling.LANCZOS)
cabbage2 = Image.open('resources/image/plant_image/cabbage2.png').resize((image_size_x, image_size_y), Image.Resampling.LANCZOS)
greentea1 = Image.open('resources/image/plant_image/greentea1.png').resize((image_size_x, image_size_y), Image.Resampling.LANCZOS)
greentea2 = Image.open('resources/image/plant_image/greentea2.png').resize((image_size_x, image_size_y), Image.Resampling.LANCZOS)
pea1 = Image.open('resources/image/plant_image/pea1.png').resize((image_size_x, image_size_y), Image.Resampling.LANCZOS)
pea2 = Image.open('resources/image/plant_image/pea2.png').resize((image_size_x, image_size_y), Image.Resampling.LANCZOS)
ladyfinger1 = Image.open('resources/image/plant_image/ladyfinger1.png').resize((image_size_x, image_size_y), Image.Resampling.LANCZOS)
ladyfinger2 = Image.open('resources/image/plant_image/ladyfinger2.png').resize((image_size_x, image_size_y), Image.Resampling.LANCZOS)
pear1 = Image.open('resources/image/plant_image/pear1.png').resize((image_size_x, image_size_y), Image.Resampling.LANCZOS)
pear2 = Image.open('resources/image/plant_image/pear2.png').resize((image_size_x, image_size_y), Image.Resampling.LANCZOS)
grape1 = Image.open('resources/image/plant_image/grape1.png').resize((image_size_x, image_size_y), Image.Resampling.LANCZOS)
grape2 = Image.open('resources/image/plant_image/grape2.png').resize((image_size_x, image_size_y), Image.Resampling.LANCZOS)
rose1 = Image.open('resources/image/plant_image/rose1.png').resize((image_size_x, image_size_y), Image.Resampling.LANCZOS)
rose2 = Image.open('resources/image/plant_image/rose2.png').resize((image_size_x, image_size_y), Image.Resampling.LANCZOS)
durian1 = Image.open('resources/image/plant_image/durian1.png').resize((image_size_x, image_size_y), Image.Resampling.LANCZOS)
durian2 = Image.open('resources/image/plant_image/durian2.png').resize((image_size_x, image_size_y), Image.Resampling.LANCZOS)
plant_image = [
    [
        ImageTk.PhotoImage(paddy1),
        ImageTk.PhotoImage(paddy2)
    ], [
        ImageTk.PhotoImage(potato1),
        ImageTk.PhotoImage(potato2)
    ], [
        ImageTk.PhotoImage(cabbage1),
        ImageTk.PhotoImage(cabbage2)
    ], [
        ImageTk.PhotoImage(greentea1),
        ImageTk.PhotoImage(greentea2)
    ], [
        ImageTk.PhotoImage(pea1),
        ImageTk.PhotoImage(pea2)
    ], [
        ImageTk.PhotoImage(ladyfinger1),
        ImageTk.PhotoImage(ladyfinger2)
    ], [
        ImageTk.PhotoImage(pear1),
        ImageTk.PhotoImage(pear2)
    ], [
        ImageTk.PhotoImage(grape1),
        ImageTk.PhotoImage(grape2)
    ], [
        ImageTk.PhotoImage(rose1),
        ImageTk.PhotoImage(rose2)
    ], [
        ImageTk.PhotoImage(durian1),
        ImageTk.PhotoImage(durian2)
    ]
    ]

image_size_x = 65
image_size_y = 65
paddy1 = Image.open('resources/image/plant_image/paddy1.png').resize((image_size_x, image_size_y), Image.Resampling.LANCZOS)
paddy2 = Image.open('resources/image/plant_image/paddy2.png').resize((image_size_x, image_size_y), Image.Resampling.LANCZOS)
potato1 = Image.open('resources/image/plant_image/potato1.png').resize((image_size_x, image_size_y), Image.Resampling.LANCZOS)
potato2 = Image.open('resources/image/plant_image/potato2.png').resize((image_size_x, image_size_y), Image.Resampling.LANCZOS)
cabbage1 = Image.open('resources/image/plant_image/cabbage1.png').resize((image_size_x, image_size_y), Image.Resampling.LANCZOS)
cabbage2 = Image.open('resources/image/plant_image/cabbage2.png').resize((image_size_x, image_size_y), Image.Resampling.LANCZOS)
greentea1 = Image.open('resources/image/plant_image/greentea1.png').resize((image_size_x, image_size_y), Image.Resampling.LANCZOS)
greentea2 = Image.open('resources/image/plant_image/greentea2.png').resize((image_size_x, image_size_y), Image.Resampling.LANCZOS)
pea1 = Image.open('resources/image/plant_image/pea1.png').resize((image_size_x, image_size_y), Image.Resampling.LANCZOS)
pea2 = Image.open('resources/image/plant_image/pea2.png').resize((image_size_x, image_size_y), Image.Resampling.LANCZOS)
ladyfinger1 = Image.open('resources/image/plant_image/ladyfinger1.png').resize((image_size_x, image_size_y), Image.Resampling.LANCZOS)
ladyfinger2 = Image.open('resources/image/plant_image/ladyfinger2.png').resize((image_size_x, image_size_y), Image.Resampling.LANCZOS)
pear1 = Image.open('resources/image/plant_image/pear1.png').resize((image_size_x, image_size_y), Image.Resampling.LANCZOS)
pear2 = Image.open('resources/image/plant_image/pear2.png').resize((image_size_x, image_size_y), Image.Resampling.LANCZOS)
grape1 = Image.open('resources/image/plant_image/grape1.png').resize((image_size_x, image_size_y), Image.Resampling.LANCZOS)
grape2 = Image.open('resources/image/plant_image/grape2.png').resize((image_size_x, image_size_y), Image.Resampling.LANCZOS)
rose1 = Image.open('resources/image/plant_image/rose1.png').resize((image_size_x, image_size_y), Image.Resampling.LANCZOS)
rose2 = Image.open('resources/image/plant_image/rose2.png').resize((image_size_x, image_size_y), Image.Resampling.LANCZOS)
durian1 = Image.open('resources/image/plant_image/durian1.png').resize((image_size_x, image_size_y), Image.Resampling.LANCZOS)
durian2 = Image.open('resources/image/plant_image/durian2.png').resize((image_size_x, image_size_y), Image.Resampling.LANCZOS)
plant_image_shop = [
    [
        ImageTk.PhotoImage(paddy1),
        ImageTk.PhotoImage(paddy2)
    ], [
        ImageTk.PhotoImage(potato1),
        ImageTk.PhotoImage(potato2)
    ], [
        ImageTk.PhotoImage(cabbage1),
        ImageTk.PhotoImage(cabbage2)
    ], [
        ImageTk.PhotoImage(greentea1),
        ImageTk.PhotoImage(greentea2)
    ], [
        ImageTk.PhotoImage(pea1),
        ImageTk.PhotoImage(pea2)
    ], [
        ImageTk.PhotoImage(ladyfinger1),
        ImageTk.PhotoImage(ladyfinger2)
    ], [
        ImageTk.PhotoImage(pear1),
        ImageTk.PhotoImage(pear2)
    ], [
        ImageTk.PhotoImage(grape1),
        ImageTk.PhotoImage(grape2)
    ], [
        ImageTk.PhotoImage(rose1),
        ImageTk.PhotoImage(rose2)
    ], [
        ImageTk.PhotoImage(durian1),
        ImageTk.PhotoImage(durian2)
    ]
    ]

setting_image = Image.open("resources/image/other_image/setting_image.png").resize((50, 50), Image.Resampling.LANCZOS)
resize_setting_image = ImageTk.PhotoImage(setting_image)
shop_image = Image.open("resources/image/other_image/shop_image.png").resize((50, 50), Image.Resampling.LANCZOS)
resize_shop_image = ImageTk.PhotoImage(shop_image)
close_shop_arrow_image = Image.open('resources/image/other_image/close_shop_arrow_image.png').resize((20, 10), Image.Resampling.LANCZOS)
resized_close_shop_arrow_image = ImageTk.PhotoImage(close_shop_arrow_image)
money_image = Image.open('resources/image/other_image/money.png').resize((50, 50), Image.Resampling.LANCZOS)
resized_money_image = ImageTk.PhotoImage(money_image)
stone_image = Image.open('resources/image/other_image/stone.png').resize((50, 50), Image.Resampling.LANCZOS)
resized_stone_image = ImageTk.PhotoImage(stone_image)
tree_image = Image.open('resources/image/other_image/tree.png').resize((50, 100), Image.Resampling.LANCZOS)
resized_tree_image = ImageTk.PhotoImage(tree_image)
bel_tree_image = Image.open('resources/image/other_image/bel_tree.png').resize((50, 100), Image.Resampling.LANCZOS)
resized_bel_tree_image = ImageTk.PhotoImage(bel_tree_image)


## page 2 setting button
setting_button_2_frame = tk.Frame(master=frame_page_2, width=50, height=50, bg="grey80", borderwidth=2, relief=tk.RAISED)
setting_button_2_frame.place(relx=0.08, rely=0.055, anchor="center")
setting_button_2 = tk.Menubutton(master=setting_button_2_frame, image=resize_setting_image, bg="grey80", width=50, height=50)
setting_button_2.pack()
Setting_menu(setting_button_2, frame_page_2, 0.097, 0.115)


## shop and plant and money
def random_money(first, second):
    return random.randint(first, second)
seed_number = [0 for i in range(10)]
seed_price = [200, 250, 250, 700, 700, 700, 800, 2000, 3000, 4000]
seed_profit = [[224, 251], 287, [221, 346], 778, [684, 852], [653, 905], 950, 2340, 3340, [2890, 5010]]
thing_price = [50, 20]

class Shop_button():
    def __init__(self):
        shop_frame = tk.Frame(master=frame_page_2, width=50, height=50, bg="grey", bd=1, relief=tk.RAISED)
        shop_frame.place(relx=0.03, rely=0.055, anchor="center")
        self.shop_button = tk.Button(master=shop_frame, command=self.open_shop, image=resize_shop_image, bg="grey80")
        self.shop_button.pack()
        self.frame = frame_page_2
        self.plant_list = ["paddy", "potato", "cabbage", "greentea", "pea", "ladyfinger", "pear", "grape", "rose", "durian"]
        self.objects_list = ["remove\nstone", "remove\ntree"]
        self.frame_expand = tk.Frame(master=self.frame, bg="grey", borderwidth=1, relief=tk.RAISED)
        self.expand_shop()

    def open_shop(self):
        self.frame_expand.place(relx=0.01, rely=0.02)

    def expand_shop(self):
        self.plant_image_reference = []
        for index, plant in enumerate(self.plant_list):
            option_image = plant_image_shop[index][1]
            self.plant_image_reference.append(option_image)

            self.option_image_button = tk.Button(master=self.frame_expand, image=option_image, height=60, width=60, command=lambda i=index: self.add_seed_number(i))
            self.option_image_button.grid(row=(index // 2) * 4, column=index % 2, padx=25, pady=(5, 0))

            self.option_text_label = tk.Label(master=self.frame_expand, text=plant, font=("Comic Sans MS", 9), bg="grey")
            self.option_text_label.grid(row=1 + (index // 2) * 4, column=index % 2)

            self.option_price_label = tk.Label(master=self.frame_expand, text="price: " + str(seed_price[index]), font=("Comic Sans MS", 9), bg="grey")
            self.option_price_label.grid(row=2 + (index // 2) * 4, column=index % 2)

            current_seed_profit = seed_profit[index]
            if isinstance(current_seed_profit, list):
                seed_profit_shown = "profit: " + str(current_seed_profit[0]) + "~" + str(current_seed_profit[1])
            else:
                seed_profit_shown = "profit: " + str(current_seed_profit)
            self.option_profit_label = tk.Label(master=self.frame_expand, text=seed_profit_shown, font=("Comic Sans MS", 9), bg="grey")
            self.option_profit_label.grid(row=3 + (index // 2) * 4, column=index % 2)

        for num, item in enumerate(self.objects_list):
            self.option_remove_thing = tk.Button(master=self.frame_expand, height=3, width=6, text=str(self.objects_list[num]), command=lambda i=num: generate_stone_tree.count_treeandstone(i), bg="grey80")
            self.option_remove_thing_label = tk.Label(master=self.frame_expand, text="price: " + str(thing_price[num]), font=("Comic Sans MS", 9), bg="grey")

            self.option_remove_thing.grid(row=20, column=num, padx=10, pady=(5, 0))
            self.option_remove_thing_label.grid(row=21, column=num)

        self.option_close_shop_button = tk.Button(master=self.frame_expand, image=resized_close_shop_arrow_image, bg="grey70", height=10, width=50, command=self.close_shop)
        self.option_close_shop_button.grid(row=22, column=0, columnspan=2, padx=10, pady=(5, 5))

    def close_shop(self):
        self.frame_expand.place_forget()

    def add_seed_number(self, index):
        generate_stone_tree.reset_remove_mode()
        if Money.money >= seed_price[index]:
            for a in range(10):
                seed_number[a] = 0
            seed_number[index] = 1
        else:
            Money.start_warning()


class Generate_stone_tree():
    def __init__(self, avoid_zone):
        self.avoid_zone = avoid_zone
        self.avoid_overlap = []
        self.tree_frames = []
        self.stone_frames = []
        self.bel_tree_frames = []
        self.stone_labels = []
        self.tree_labels = []
        self.bel_tree_labels = []
        self.remove_mode = [False, False]


        for tr in range(10):
            self.tree_frame = tk.Frame(master=frame_page_2, bg="grey", width=50, height=100)
            self.tree_label = tk.Label(master=self.tree_frame, image=resized_tree_image, width=50, height=100, bg="chartreuse4")
            x, y = self.get_valid_position(50, 100)
            self.tree_frame.place(x=x, y=y)
            self.tree_label.pack()
            self.tree_frames.append(self.tree_frame)
            self.tree_labels.append(self.tree_label)

        for tr in range(10):
            self.stone_frame = tk.Frame(master=frame_page_2, bg="white", width=50, height=50)
            self.stone_label = tk.Label(master=self.stone_frame, image=resized_stone_image, width=50, height=50, bg="chartreuse4")
            x, y = self.get_valid_position(50, 50)
            self.stone_frame.place(x=x, y=y)
            self.stone_label.pack()
            self.stone_frames.append(self.stone_frame)
            self.stone_labels.append(self.stone_label)

        for tr in range(10):
            self.bel_tree_frame = tk.Frame(master=frame_page_2)
            self.bel_tree_label = tk.Label(master=self.bel_tree_frame, image=resized_bel_tree_image, bg="chartreuse4")
            x, y = self.get_valid_position(50, 100)
            self.bel_tree_frame.place(x=x, y=y)
            self.bel_tree_label.pack()
            self.bel_tree_frames.append(self.bel_tree_frame)
            self.bel_tree_labels.append(self.bel_tree_label)


    def click(self, event):
        if self.remove_mode[0]:
            label = event.widget

            if label in self.stone_labels:
                frame = self.stone_frames[self.stone_labels.index(label)]
                label.pack_forget()
                frame.place_forget()
                self.stone_labels.remove(label)
                self.stone_frames.remove(frame)
                Money.decrease_money_by_delete(0)
                rsieac_points.add_rsieac_obstacle_number(0)
                self.remove_mode = [False, False]

        elif self.remove_mode[1]:
            label = event.widget

            if label in self.tree_labels:
                frame = self.tree_frames[self.tree_labels.index(label)]
                label.pack_forget()
                frame.place_forget()
                self.tree_labels.remove(label)
                self.tree_frames.remove(frame)
                Money.decrease_money_by_delete(1)
                rsieac_points.add_rsieac_obstacle_number(1)
                self.remove_mode = [False, False]

            elif label in self.bel_tree_labels:
                frame = self.bel_tree_frames[self.bel_tree_labels.index(label)]
                label.pack_forget()
                frame.place_forget()
                self.bel_tree_labels.remove(label)
                self.bel_tree_frames.remove(frame)
                Money.decrease_money_by_delete(1)
                rsieac_points.add_rsieac_obstacle_number(2)
                self.remove_mode = [False, False]

    def count_treeandstone(self, index):
        self.remove_mode = [False, False]
        for a in range(10):
            seed_number[a] = 0
        if Money.money >= thing_price[index]:
            if index == 0:
                self.remove_mode[index] = True
                for stone_label in self.stone_labels:
                    stone_label.bind("<Button-1>", self.click)
            elif index == 1:
                self.remove_mode[index] = True
                for tree_label in self.tree_labels:
                    tree_label.bind("<Button-1>", self.click)

                for bel_tree_label in self.bel_tree_labels:
                    bel_tree_label.bind("<Button-1>", self.click)
        else:
            Money.start_warning()

    def check_avoid_zone(self, x, y, width, height):
        for a in range(a):
            ax1, ax2, ay1, ay2 = self.avoid_zone[a]
            if x + width >= ax1 and x <= ax2:
                if y + height >= ay1 and y <= ay2:
                    return False
            for i in self.avoid_overlap:
                if x + width >= i[0] and x <= i[1]:
                    if y + height >= i[2] and y <= i[3]:
                        return False
        return True

    def get_valid_position(self, width, height):
        while True:
            x = random.randint(250, screen_width - width)
            y = random.randint(70, screen_height - height)
            if self.check_avoid_zone(x, y, width, height):
                self.avoid_overlap.append([x, x + width, y, y + height])
                return x, y

    def reset_remove_mode(self):
        self.remove_mode = [False, False]

def create_arableland():
    numbers = {0, 88, 176, 264}
    for x in numbers:
        for y in numbers:
            Switch_Plant_Image(frame_page_2, x, y)


class Switch_Plant_Image():
    def __init__(self, master, x, y):
        self.master = master
        self.can_harvest = 0

        self.farm = tk.Frame(master=master, bg="#8B4513", height=70, width=70)
        self.farm.place(x=(screen_width/2 - 172) + x, y=(screen_height/2 - 172) + y)
        self.image_label = tk.Label(master=self.farm, image=arableland_image, height=80, width=80, bg="grey75")
        self.image_label.pack()
        self.bind_click()

    def switch_image(self, event, index):
        Money.decrease_money(index)
        self.image_label.config(image=plant_image[index][0])
        self.start_timer(index)
        self.master.after(0000, self.bind_harvest(index))
        self.master.after(0000, self.reset_seed_number(index))

    def bind_click(self):
        self.image_label.bind('<Button-1>', self.on_click)

    def on_click(self, event):
        for ind, num in enumerate(seed_number):
            if num == 1:
                self.switch_image(event, ind)

    def start_timer(self, index):
        self.timer_thread = threading.Thread(target=self.run_timer, args=(index, ))
        self.timer_thread.start()

    def run_timer(self, index):
        time.sleep(3)
        self.image_label.config(image=plant_image[index][1])
        self.can_harvest = 1

    def harvest(self, index):
        if self.can_harvest == 1:
            Money.increase_money(index)
            rsieac_points.add_rsieac_plant_number(index)
            self.image_label.config(image=arableland_image)
            self.can_harvest = 0
            self.bind_click()

    def bind_harvest(self, index):
            self.image_label.bind("<Button-1>", lambda event, idx=index: self.harvest(idx))

    def reset_seed_number(self, index):
        seed_number[index] = 0



class Money():
    def __init__(self):
        self.money = 300
        self.page_3 = 0

        self.money_frame = tk.Frame(master=frame_page_2, width=100, height=100, bg="chartreuse4")
        self.money_frame.place(relx=0.95, rely=0.055, anchor="center")

        self.money_label = tk.Label(master=self.money_frame, image=resized_money_image, text=self.money, compound="left", font=("Comic Sans MS", 20), bg="grey70", relief="solid", borderwidth=2, highlightbackground="black", highlightthickness=1)
        self.money_label.grid()

        self.money_spawn = tk.Frame(frame_page_2, width=30, height=30, bg="chartreuse4")

        self.no_money_warning_frame = tk.Frame(master=frame_page_2, bg="chartreuse4")
        self.no_money_warning_label = tk.Label(master=self.no_money_warning_frame, text="", font=("Comic Sans MS", 20), bg="chartreuse4", fg="red3")
        self.no_money_warning_label.pack()

        self.end_button_frame = tk.Frame(master=window)
        self.end_button = tk.Button(master=self.end_button_frame, text="End", bg="white", fg="black", width=6, height=1, font=("Comic Sans MS", 15), command=self.open_page_3)


    def decrease_money_by_delete(self, index):
        self.money -= thing_price[index]
        self.money_label.config(text=self.money)
        self.temp_money = "-" + str(thing_price[index])
        self.saw_money()
        self.trigger_mystery()
        self.go_page_3()

    def mystery_modify_money(self, modify_money):
        self.money += modify_money
        self.money_label.config(text=self.money)
        if modify_money < 0:
            self.temp_money = str(modify_money)
            self.saw_money()
        elif modify_money > 0:
            self.temp_money = "+" + str(modify_money)
            self.saw_money()
        self.trigger_mystery()
        self.go_page_3()

    def decrease_money(self, index):
        self.money -= seed_price[index]
        self.money_label.config(text=self.money)
        self.temp_money = "-" + str(seed_price[index])
        self.saw_money()
        self.trigger_mystery()
        self.go_page_3()

    def increase_money(self, index):
        current_seed_money = seed_profit[index]
        if isinstance(current_seed_money, list):
            increase_profit = random_money(current_seed_money[0], current_seed_money[1])
        else:
            increase_profit = current_seed_money
        self.money += increase_profit
        self.money_label.config(text=self.money)
        self.temp_money = "+" + str(increase_profit)
        self.saw_money()
        self.trigger_mystery()
        self.go_page_3()

    def saw_money(self):
        self.money_spawn.place(relx=0.89, rely=0.055, anchor="center")
        self.money_temp_label = tk.Label(self.money_spawn, text=self.temp_money, font=("Comic Sans MS", 12), bg="chartreuse4", fg="yellow")
        self.money_temp_label.pack()
        self.money_spawn.after(1000, self.money_temp_label.pack_forget)
        frame_page_2.after(1000, self.money_spawn.place_forget)

    def start_warning(self):
        self.warning_timer_thread = threading.Thread(target=self.run_warning)
        self.warning_timer_thread.start()

    def run_warning(self):
        self.no_money_warning_frame.place(relx=0.8, rely=0.055, anchor="center")
        self.no_money_warning_label.config(text="no enough money")
        time.sleep(2)
        self.no_money_warning_label.config(text="")
        frame_page_2.after(0, self.no_money_warning_frame.place_forget)

    def trigger_mystery(self):
        for i in mystery_document:
            if i[6] == 1 and self.money >= i[5]:
                i[6] = 0
                Mystery_events(i[0], i[1], i[2], i[3], i[4], i[7], i[8], i[9], i[10])

    def go_page_3(self):
        if self.money >= 6000:
            self.end_button_frame.place(relx=0.93, rely=0.9, anchor="se")
            tk.Frame.tkraise(self.end_button_frame)
            self.end_button.pack()
    def open_page_3(self):
        frame_page_2.pack_forget()
        self.page_3 = Page_3()

## mystery events
class Mystery_events():
    def __init__(self, mystery_text, yes_reply_text, no_reply_text, yes_money_modify, no_money_modify, yes_RSIEAC, no_RSIEAC, yes_video, no_video):
        self.mystery_frame = tk.Frame(master=frame_page_2, bg="#458b00", relief="solid", borderwidth=2, highlightbackground="black", highlightthickness=1)
        self.mystery_label = tk.Label(master=self.mystery_frame, text="", font=("Comic Sans MS", 20), wraplength=500, bg="#458b00")
        self.mystery_choice_yes = tk.Button(master=self.mystery_frame, text="YES", font=("Comic Sans MS", 20), command=self.mystery_yes_react, bg="grey70")
        self.mystery_choice_no = tk.Button(master=self.mystery_frame, text="NO", font=("Comic Sans MS", 20), command=self.mystery_no_react, bg="grey70")

        self.mystery_text = mystery_text
        self.mystery_text_show = ""
        self.yes_reply_text = yes_reply_text
        self.no_reply_text = no_reply_text
        self.yes_money_modify = yes_money_modify
        self.no_money_modify = no_money_modify
        self.yes_RSIEAC = yes_RSIEAC
        self.no_RSIEAC = no_RSIEAC
        self.mystery_text_index = 0
        self.show_mystery()

        self.yes_video_path = yes_video
        self.no_video_path = no_video
        self.mystery_video_frame = tk.Frame(master=frame_page_2, bg="#458b00", relief="solid", borderwidth=2, highlightbackground="black", highlightthickness=1)
        self.video_label = tk.Label(self.mystery_video_frame)
        self.video_path = 0

    def show_mystery(self):
        self.mystery_frame.place(relx=0.8, rely=0.3, anchor="center")
        self.mystery_label.grid(row=0, column=0, columnspan=2)
        if self.mystery_text_index < len(self.mystery_text):
            self.mystery_text_show += self.mystery_text[self.mystery_text_index]
            self.mystery_label.config(text=self.mystery_text_show)
            self.mystery_frame.after(10, self.show_mystery)
            self.mystery_text_index += 1
        else:
            self.show_mystery_choice()

    def show_mystery_choice(self):
        self.mystery_choice_yes.grid(row=1, column=0)
        self.mystery_choice_no.grid(row=1, column=1)

    def mystery_yes_react(self):
        self.hide_choice()
        self.mystery_label.config(text="")
        self.mystery_text_index = 0
        self.mystery_text_show = ""
        rsieac_points.add_points(self.yes_RSIEAC)
        self.video_path = self.yes_video_path
        self.trigger_play_video()
        self.update_reply_text(self.yes_reply_text, self.yes_money_modify)

    def mystery_no_react(self):
        self.hide_choice()
        self.mystery_label.config(text="")
        self.mystery_text_index = 0
        self.mystery_text_show = ""
        rsieac_points.add_points(self.no_RSIEAC)
        self.video_path = self.no_video_path
        self.trigger_play_video()
        self.update_reply_text(self.no_reply_text, self.no_money_modify)

    def update_reply_text(self, reply_text, money_modify):
        if self.mystery_text_index < len(reply_text):
            self.mystery_text_show += reply_text[self.mystery_text_index]
            self.mystery_label.config(text=self.mystery_text_show)
            self.mystery_text_index += 1
            self.mystery_frame.after(10, self.update_reply_text(reply_text, money_modify))
        else:
            Money.mystery_modify_money(money_modify)
            self.mystery_frame.after(5000, self.hide_mystery)

    def hide_choice(self):
        self.mystery_choice_yes.grid_forget()
        self.mystery_choice_no.grid_forget()

    def hide_mystery(self):
        self.mystery_frame.place_forget()
        self.close_video()

    def trigger_play_video(self):
        if self.video_path == 0:
            pass
        else:
            self.mystery_video_frame.place(relx=0.8, rely=0.7, anchor="center", width=400, height=400)
            self.video_label.pack()
            self.video_can_play = True

            self.start_video_thread()

    def play_video(self):
        while self.video_can_play:
            video_reader = imageio.get_reader(self.video_path)
            for frame in video_reader.iter_data():
                video_image = Image.fromarray(frame)
                resized_video_image = video_image.resize((400, 400))
                video_photo = ImageTk.PhotoImage(resized_video_image)

                self.mystery_video_frame.after(0, self.update_video_label, video_photo)
                time.sleep(2 / video_reader.get_meta_data()['fps'])

    def update_video_label(self, photo):
        self.video_label.configure(image=photo)
        self.video_label.image = photo

    def start_video_thread(self):
        self.video_thread = threading.Thread(target=self.play_video)
        self.video_thread.daemon = True
        self.video_thread.start()

    def close_video(self):
        self.video_can_play = False
        self.video_label.pack_forget()
        self.mystery_video_frame.place_forget()


## RSIEAC points
class RSIEAC_points():
    def __init__(self):
        self.RSIEAC_temp_points = [0 for i in range(6)]  # R, I, A, S, E, C

        self.rsieac_plant_number = [0 for j in range(10)]
        self.rsieac_obstacle_number = [10, 10, 10]  # stone, tree, bel_tree
        self.add_rsieac_plant = ["1E2I1R", "3C1I2R", "2E", "2C2R1I", "1E", "2E2I", "0", "2C3I1R", "4A", "3E1A"]

        self.pattern = re.compile(r"\d[RSIEAC]")
        self.points = 0
        self.type = ""

        self.categories = ["R", "I", "A", "S", "E", "C"]
        self.max_points = [14, 11, 10, 16, 15, 10]
        self.points_percentage = [0 for k in range(6)]

    def add_points(self, points_and_type):
        matches = self.pattern.findall(points_and_type)
        for match in matches:
            self.points = int(match[0])
            self.type = match[1]

            for i in self.categories:
                if self.type == i:
                    self.RSIEAC_temp_points[self.categories.index(i)] += self.points

    def add_rsieac_plant_number(self, index):
        self.rsieac_plant_number[index] += 1

    def add_rsieac_obstacle_number(self, index):
        self.rsieac_obstacle_number[index] -= 1

    def plant_add_points(self, a, b, c):
        if self.rsieac_plant_number[a] > self.rsieac_plant_number[b]:
            if self.rsieac_plant_number[a] > self.rsieac_plant_number[c]:
                self.add_points(self.add_rsieac_plant[a])
            elif self.rsieac_plant_number[a] < self.rsieac_plant_number[c]:
                self.add_points(self.add_rsieac_plant[c])
            else:
                self.add_points(self.add_rsieac_plant[a])
                self.add_points(self.add_rsieac_plant[c])
        elif self.rsieac_plant_number[b] > self.rsieac_plant_number[a]:
            if self.rsieac_plant_number[b] > self.rsieac_plant_number[c]:
                self.add_points(self.add_rsieac_plant[b])
            elif self.rsieac_plant_number[b] < self.rsieac_plant_number[c]:
                self.add_points(self.add_rsieac_plant[c])
            else:
                self.add_points(self.add_rsieac_plant[b])
                self.add_points(self.add_rsieac_plant[c])
        elif self.rsieac_plant_number[a] == self.rsieac_plant_number[b]:
            if self.rsieac_plant_number[a] > self.rsieac_plant_number[c]:
                self.add_points(self.add_rsieac_plant[a])
                self.add_points(self.add_rsieac_plant[b])
            elif self.rsieac_plant_number[a] < self.rsieac_plant_number[c]:
                self.add_points(self.add_rsieac_plant[c])
            else:
                self.add_points(self.add_rsieac_plant[a])
                self.add_points(self.add_rsieac_plant[b])
                self.add_points(self.add_rsieac_plant[c])

    def obstacle_add_points(self):
        if self.rsieac_obstacle_number[1] == 0:
            self.add_points("3A")

    def create_radar_chart(self):
        self.points_percentage = [0 for k in range(6)]
        for i in range(6):
            self.points_percentage[i] = round((self.RSIEAC_temp_points[i] / self.max_points[i]) * 100)

        angles = np.linspace(0, 2 * np.pi, 6, endpoint=False).tolist()
        self.points_percentage += self.points_percentage[:1]
        angles += angles[:1]
        fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
        ax.set_yticks(self.points_percentage)
        ax.set_ylim(0, 100)
        ax.plot(angles, self.points_percentage, linewidth=1, linestyle='solid')
        ax.fill(angles, self.points_percentage, 'b', alpha=0.1)
        ax.set_xticks(angles[:-1])
        ax.set_xticklabels(self.categories, fontsize=20, weight='bold', fontname="Comic Sans MS")
        ax.set_rgrids([20, 40, 60, 80])
        ax.grid(linewidth=1)
        ax.yaxis.grid(color='#161819', linestyle='--', linewidth=0.7)

        ax.set_facecolor('#BEC2C3')
        fig.patch.set_facecolor('#E1EEF2')

        return fig

    def create_bar_chart(self):
        self.points_percentage = [0 for k in range(6)]
        for i in range(6):
            self.points_percentage[i] = round(self.RSIEAC_temp_points[i] / self.max_points[i] * 100)
        bar_dict = dict(zip(self.categories, self.points_percentage))
        items = list(bar_dict.items())
        sorted_items = sorted(items, key=lambda x: x[1], reverse=True)
        bar_dict = {k: v for k, v in sorted_items}
        bar_keys_list = list(bar_dict.keys())
        bar_values_list = list(bar_dict.values())

        fig = Figure(figsize=(3, 10), dpi=100)
        ax = fig.add_subplot(111)
        ax.bar(bar_keys_list, bar_values_list, color='#737373', edgecolor="#808080", width=0.5)
        ax.set_facecolor("#E1EEF2")
        fig.patch.set_facecolor("#E1EEF2")
        ax.set_xticks(range(len(bar_keys_list)))
        ax.set_xticklabels(bar_keys_list, fontname='Comic Sans MS', fontsize=15)
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['left'].set_visible(False)
        ax.spines['bottom'].set_visible(False)
        ax.yaxis.set_visible(False)
        ax.tick_params(axis='x', which='both', bottom=False)

        for i, value in enumerate(bar_values_list):
            ax.text(i, value + 1, str(value), ha='center', va='bottom')

        return fig

    def get_summary_code(self):
        self.points_percentage = [0 for k in range(6)]
        for i in range(6):
            self.points_percentage[i] = round(self.RSIEAC_temp_points[i] / self.max_points[i] * 100)
        bar_dict = dict(zip(self.categories, self.points_percentage))
        items = list(bar_dict.items())
        sorted_items = sorted(items, key=lambda x: x[1], reverse=True)
        bar_dict = {k: v for k, v in sorted_items}
        bar_keys_list = list(bar_dict.keys())
        summary_code = f"{bar_keys_list[0]}{bar_keys_list[1]}{bar_keys_list[2]}"

        return summary_code



## page 3

class Page_3():
    def __init__(self):
        self.c = "#E1EEF2"
        self.frame_page_3 = tk.Frame(master=window, bg=self.c)
        self.frame_page_3.pack(fill=tk.BOTH, expand=True)
        tk.Frame.tkraise(self.frame_page_3)
        self.frame_page_3.place(x=0, y=0, relwidth=1, relheight=1)

        rsieac_points.plant_add_points(0, 1, 2)
        rsieac_points.plant_add_points(3, 4, 5)
        rsieac_points.plant_add_points(7, 8, 9)
        rsieac_points.obstacle_add_points()

        self.contributor_background_trans = self.change_transparency("resources/image/other_image/contributor_background.png", 0.5)
        self.contributor_background = ImageTk.PhotoImage(self.contributor_background_trans)
        self.reference_background_trans = self.change_transparency("resources/image/other_image/reference_background.png", 0.5)
        self.reference_background = ImageTk.PhotoImage(self.reference_background_trans)
        self.contributor_1 = Image.open('resources/image/other_image/contributor_1.png').resize((300, 300), Image.Resampling.LANCZOS)
        self.resized_contributor_1 = ImageTk.PhotoImage(self.contributor_1)
        self.contributor_2 = Image.open('resources/image/other_image/contributor_2.png').resize((320, 250), Image.Resampling.LANCZOS)
        self.resized_contributor_2 = ImageTk.PhotoImage(self.contributor_2)
        self.line_4 = Image.open('resources/image/other_image/line_vertical.png').resize((10, 700), Image.Resampling.LANCZOS)
        self.resized_line_4 = ImageTk.PhotoImage(self.line_4)


        self.frame_page_3_1 = tk.Frame(master=self.frame_page_3, width=screen_width, height=screen_height, bg=self.c)
        self.other_description_1 = tk.Label(master=self.frame_page_3_1, text="Self-Directed Search", font=("Comic Sans MS", 25, "bold"), bg="grey70", relief="solid", borderwidth=5, highlightbackground="black", highlightthickness=1)
        self.other_description_2 = tk.Label(master=self.frame_page_3_1, text="Here's your result!", bg=self.c, font=("Comic Sans MS", 20))
        self.next_button_1 = tk.Button(master=self.frame_page_3_1, text="Next", bg="white", fg="black", width=6, height=1, font=("Comic Sans MS", 15), command=self.page_3_2)
        self.riasec_position = [[0.01, 0.06, 0.01, 0.11], [0.01, 0.39, 0.01, 0.44], [0.01, 0.73, 0.01, 0.78], [0.99, 0.06, 0.99, 0.11], [0.99, 0.39, 0.99, 0.44], [0.99, 0.73, 0.99, 0.78]]
        self.riasec_index = 0
        self.more_description_list = []


        self.frame_page_3_2 = tk.Frame(master=self.frame_page_3, width=screen_width, height=screen_height, bg=self.c)
        self.next_button_2 = tk.Button(master=self.frame_page_3_2, text="Next", bg="white", fg="black", width=6, height=1, font=("Comic Sans MS", 15), command=self.page_3_3)
        self.back_button_2 = tk.Button(master=self.frame_page_3_2, text="Back", bg="white", fg="black", width=6, height=1, font=("Comic Sans MS", 15), command=self.page_3_1)
        self.summary_code = rsieac_points.get_summary_code()

        self.random_flower_path, self.random_flower_name = self.get_random_flower()
        self.label_width = 400
        self.label_height = 700
        self.original_flower = Image.open(self.random_flower_path)
        self.original_width, self.original_height = self.original_flower.size
        ratio = min(self.label_width / self.original_width, self.label_height / self.original_height)
        self.new_width = int(self.original_width * ratio)
        self.new_height = int(self.original_height * ratio)
        self.flower = self.original_flower.resize((self.new_width, self.new_height), Image.Resampling.LANCZOS)
        self.resized_flower = ImageTk.PhotoImage(self.flower)


        self.frame_page_3_3 = tk.Frame(master=self.frame_page_3, width=screen_width, height=screen_height, bg=self.c)
        self.next_button_3 = tk.Button(master=self.frame_page_3_3, text="Next", bg="white", fg="black", width=6, height=1, font=("Comic Sans MS", 15), command=self.page_3_4)
        self.back_button_3 = tk.Button(master=self.frame_page_3_3, text="Back", bg="white", fg="black", width=6, height=1, font=("Comic Sans MS", 15), command=self.page_3_2)

        self.random_fam_index = random.sample(range(0, len(famous_example)), 2)
        self.fam_name_1, self.fam_des_1, self.fam_name_2, self.fam_des_2 = self.get_random_fam(self.random_fam_index[0], self.random_fam_index[1])
        self.language_of_flower = language_of_flower[flower.index(self.random_flower_name)]


        self.frame_page_3_4 = tk.Frame(master=self.frame_page_3, width=screen_width, height=screen_height, bg=self.c)
        self.end_button_4 = tk.Button(master=self.frame_page_3_4, text="End", bg="white", fg="black", width=6, height=1, font=("Comic Sans MS", 15), command=self.page_3_5)
        self.back_button_4 = tk.Button(master=self.frame_page_3_4, text="Back", bg="white", fg="black", width=6, height=1, font=("Comic Sans MS", 15), command=self.page_3_3)

        self.partner_code = ["R", "S", "I", "E", "A", "C"]
        self.partner_summary_code = random.sample(self.partner_code, 3)

        self.random_flower_path_2, self.random_flower_name_2 = self.get_random_flower()
        self.label_width_2 = 400
        self.label_height_2 = 500
        self.original_flower_2 = Image.open(self.random_flower_path_2)
        self.original_width_2, self.original_height_2 = self.original_flower_2.size
        ratio_2 = min(self.label_width_2 / self.original_width_2, self.label_height_2 / self.original_height_2)
        self.new_width_2 = int(self.original_width_2 * ratio_2)
        self.new_height_2 = int(self.original_height_2 * ratio_2)
        self.flower_2 = self.original_flower_2.resize((self.new_width_2, self.new_height_2), Image.Resampling.LANCZOS)
        self.resized_flower_2 = ImageTk.PhotoImage(self.flower_2)

        self.random_books_index = random.sample(range(0, len(books)), 2)
        self.random_book_name_1, self.random_book_author_1, self.random_book_description_1, self.random_book_name_2, self.random_book_author_2, self.random_book_description_2 = self.get_random_books(self.random_books_index[0], self.random_books_index[1])


        self.frame_page_3_5 = tk.Frame(master=self.frame_page_3, width=screen_width, height=screen_height, bg=self.c)


        self.frame_page_3_6 = tk.Frame(master=self.frame_page_3, width=screen_width, height=screen_height, bg=self.c)
        self.background_3_6 = tk.Label(master=self.frame_page_3_6, image=self.contributor_background)
        self.next_button_6 = tk.Button(master=self.frame_page_3_6, text="Next", bg="white", fg="black", width=6, height=1, font=("Comic Sans MS", 15), command=self.page_3_7)
        self.back_button_6 = tk.Button(master=self.frame_page_3_6, text="Back", bg="white", fg="black", width=6, height=1, font=("Comic Sans MS", 15), command=self.page_3_5)


        self.frame_page_3_7 = tk.Frame(master=self.frame_page_3, width=screen_width, height=screen_height, bg=self.c)
        self.background_3_7 = tk.Label(master=self.frame_page_3_7, image=self.reference_background)
        self.end_button_7 = tk.Button(master=self.frame_page_3_7, text="End", bg="white", fg="black", width=6, height=1, font=("Comic Sans MS", 15), command=self.page_3_5)
        self.back_button_7 = tk.Button(master=self.frame_page_3_7, text="Back", bg="white", fg="black", width=6, height=1, font=("Comic Sans MS", 15), command=self.page_3_6)

        self.page_3_1()

    def page_3_1(self):
        self.frame_page_3_5.pack_forget()
        self.frame_page_3_2.pack_forget()
        self.frame_page_3_1.pack()
        self.show_radar_chart()
        self.show_riasec_description()
        self.other_description_1.place(relx=0.5, rely=0.05, anchor="center")
        self.other_description_2.place(relx=0.5, rely=0.19, anchor="center")
        self.next_button_1.place(relx=0.5, rely=0.95, anchor="center")

    def show_radar_chart(self):
        fig = rsieac_points.create_radar_chart()
        canvas = FigureCanvasTkAgg(fig, master=self.frame_page_3_1)
        canvas.draw()
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.config(width=500, height=500, bg=self.c)
        canvas_widget.place(x=screen_width/2-250, y=screen_height/2-250)

    def show_riasec_description(self):
        if self.riasec_index < 3:
            self.riasec_type_label = tk.Label(master=self.frame_page_3_1, text=riasec_description[self.riasec_index][0], justify="left", bg=self.c, font=("Comic Sans MS", 20, "bold"), wraplength=500)
            self.riasec_explain_label = tk.Label(master=self.frame_page_3_1, text=riasec_description[self.riasec_index][1], justify="left", bg=self.c, font=("Comic Sans MS", 15), wraplength=500)
            self.riasec_type_label.place(relx=self.riasec_position[self.riasec_index][0], rely=self.riasec_position[self.riasec_index][1], anchor="nw")
            self.riasec_explain_label.place(relx=self.riasec_position[self.riasec_index][2], rely=self.riasec_position[self.riasec_index][3], anchor="nw")
            self.riasec_index += 1
            self.show_riasec_description()
        elif self.riasec_index < 6:
            self.riasec_type_label = tk.Label(master=self.frame_page_3_1, text=riasec_description[self.riasec_index][0], justify="right", bg=self.c, font=("Comic Sans MS", 20, "bold"), wraplength=500)
            self.riasec_explain_label = tk.Label(master=self.frame_page_3_1, text=riasec_description[self.riasec_index][1], justify="right", bg=self.c, font=("Comic Sans MS", 15), wraplength=500)
            self.riasec_type_label.place(relx=self.riasec_position[self.riasec_index][0], rely=self.riasec_position[self.riasec_index][1], anchor="ne")
            self.riasec_explain_label.place(relx=self.riasec_position[self.riasec_index][2], rely=self.riasec_position[self.riasec_index][3], anchor="ne")
            self.riasec_index += 1
            self.show_riasec_description()

    def page_3_2(self):
        self.frame_page_3_1.pack_forget()
        self.frame_page_3_3.pack_forget()
        self.frame_page_3_2.pack()
        self.show_bar_chart()
        self.show_more_description()
        self.next_button_2.place(relx=0.55, rely=0.95, anchor="center")
        self.back_button_2.place(relx=0.45, rely=0.95, anchor="center")

    def show_bar_chart(self):
        fig = rsieac_points.create_bar_chart()
        canvas = FigureCanvasTkAgg(fig, master=self.frame_page_3_2)
        canvas.draw()
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.config(width=400, height=800, bg=self.c)
        canvas_widget.place(relx=0, rely=0.5, anchor="w")

    def show_more_description(self):
        summary_code_label_1 = tk.Label(master=self.frame_page_3_2, text="Your summary code is", bg=self.c, font=("Comic Sans MS", 20))
        summary_code_label_2 = tk.Label(master=self.frame_page_3_2, text=self.summary_code, bg=self.c, font=("Comic Sans MS", 30, "bold"))
        summary_code_label_1.place(relx=0.25, rely=0.15, anchor="w")
        summary_code_label_2.place(relx=0.438, rely=0.15, anchor="w")

        more_description_code = [self.summary_code[0], self.summary_code[2], self.summary_code[1]]
        for i in more_description_code:
            self.get_sentence(i, more_description_code.index(i))
        more_description = tk.Label(master=self.frame_page_3_2, text=f"{self.more_description_list[0]}{self.more_description_list[1]}{self.more_description_list[2]}", bg=self.c, font=("Comic Sans MS", 20), wraplength=700, justify="left")
        more_description.place(relx=0.25, rely=0.25, anchor="nw")

        flower_image = tk.Label(master=self.frame_page_3_2, bg=self.c, image=self.resized_flower, width=self.label_width, height=self.label_height+200, text=f"\nYour representative flower is:\n{self.random_flower_name}", font=("Comic Sans MS", 20), compound=tk.TOP)
        flower_image.place(relx=0.85, rely=0.47, anchor="center")

    def get_sentence(self, type, index):
        if type == "R":
            random_index = random.randint(0, (len(R_type) - 1))
            self.more_description_list.append(R_type[random_index][index])
        elif type == "S":
            random_index = random.randint(0, (len(S_type) - 1))
            self.more_description_list.append(S_type[random_index][index])
        elif type == "I":
            random_index = random.randint(0, (len(I_type) - 1))
            self.more_description_list.append(I_type[random_index][index])
        elif type == "E":
            random_index = random.randint(0, (len(E_type) - 1))
            self.more_description_list.append(E_type[random_index][index])
        elif type == "A":
            random_index = random.randint(0, (len(A_type) - 1))
            self.more_description_list.append(A_type[random_index][index])
        elif type == "C":
            random_index = random.randint(0, (len(C_type) - 1))
            self.more_description_list.append(C_type[random_index][index])

    def get_random_flower(self):
        png_files = [f for f in os.listdir('resources/image/flower_image/') if f.endswith('.png')]
        random_flower_filename = random.choice(png_files)
        random_flower_path = 'resources/image/flower_image/' + random_flower_filename
        random_flower_name = os.path.splitext(random_flower_filename)[0]
        return random_flower_path, random_flower_name

    def page_3_3(self):
        self.frame_page_3_2.pack_forget()
        self.frame_page_3_4.pack_forget()
        self.frame_page_3_3.pack()

        famous_title = tk.Label(master=self.frame_page_3_3, text=f"Famous example of {self.summary_code}:", bg=self.c, font=("Comic Sans MS", 22))
        famous_title.place(relx=0.05, rely=0.1, anchor="nw")
        fam_name_1 = tk.Label(master=self.frame_page_3_3, text=self.fam_name_1, bg=self.c, font=("Comic Sans MS", 20, "bold"), justify="left", wraplength=650)
        fam_name_1.place(relx=0.05, rely=0.25, anchor="nw")
        fam_detail_1 = tk.Label(master=self.frame_page_3_3, text=self.fam_des_1, bg=self.c, font=("Comic Sans MS", 18), justify="left", wraplength=650)
        fam_detail_1.place(relx=0.05, rely=0.3, anchor="nw")
        fam_name_2 = tk.Label(master=self.frame_page_3_3, text=self.fam_name_2, bg=self.c, font=("Comic Sans MS", 20, "bold"), justify="left", wraplength=650)
        fam_name_2.place(relx=0.05, rely=0.5, anchor="nw")
        fam_detail_2 = tk.Label(master=self.frame_page_3_3, text=self.fam_des_2, bg=self.c, font=("Comic Sans MS", 18), justify="left", wraplength=650)
        fam_detail_2.place(relx=0.05, rely=0.55, anchor="nw")
        line_3_label = tk.Label(master=self.frame_page_3_3, image=self.resized_line_4, bg=self.c)
        line_3_label.place(relx=0.3, rely=0.5, anchor="center")

        flower_image = tk.Label(master=self.frame_page_3_3, bg=self.c, image=self.resized_flower, width=self.label_width+500, height=self.label_height, text=self.language_of_flower, font=("Comic Sans MS", 20), compound=tk.RIGHT, wraplength=500)
        flower_image.place(relx=0.65, rely=0.47, anchor="center")

        self.next_button_3.place(relx=0.55, rely=0.95, anchor="center")
        self.back_button_3.place(relx=0.45, rely=0.95, anchor="center")

    def get_random_fam(self, i1, i2):
        return famous_example[i1][0], famous_example[i1][1], famous_example[i2][2], famous_example[i2][3]

    def page_3_4(self):
        self.frame_page_3_3.pack_forget()
        self.frame_page_3_5.pack_forget()
        self.frame_page_3_4.pack()
        self.show_partner_and_book()
        self.end_button_4.place(relx=0.55, rely=0.95, anchor="center")
        self.back_button_4.place(relx=0.45, rely=0.95, anchor="center")

    def show_partner_and_book(self):
        summary_code_label_1 = tk.Label(master=self.frame_page_3_4, text="Your most suitable partner's summary code is", bg=self.c, font=("Comic Sans MS", 20))
        summary_code_label_2 = tk.Label(master=self.frame_page_3_4, text=f"{self.partner_summary_code[0]}{self.partner_summary_code[1]}{self.partner_summary_code[2]}", bg=self.c, font=("Comic Sans MS", 30, "bold"))
        summary_code_label_1.place(relx=0.05, rely=0.1, anchor="w")
        summary_code_label_2.place(relx=0.43, rely=0.1, anchor="w")
        flower_image_2 = tk.Label(master=self.frame_page_3_4, bg=self.c, image=self.resized_flower_2, width=self.label_width_2, height=self.label_height_2+200, text=f"\nRepresentative flower:\n{self.random_flower_name_2}", font=("Comic Sans MS", 20), compound=tk.TOP)
        flower_image_2.place(relx=0.25, rely=0.55, anchor="center")

        line_4_label = tk.Label(master=self.frame_page_3_4, image=self.resized_line_4, bg=self.c)
        line_4_label.place(relx=0.5, rely=0.5, anchor="center")
        book_title = tk.Label(master=self.frame_page_3_4, text="Books that you should read:", bg=self.c, font=("Comic Sans MS", 22))
        book_title.place(relx=0.55, rely=0.1, anchor="nw")
        book_name_1 = tk.Label(master=self.frame_page_3_4, text=self.random_book_name_1, bg=self.c, font=("Comic Sans MS", 20, "bold"), justify="left", wraplength=650)
        book_name_1.place(relx=0.55, rely=0.2, anchor="nw")
        book_detail_1 = tk.Label(master=self.frame_page_3_4, text=f"{self.random_book_author_1}\n\n{self.random_book_description_1}", bg=self.c, font=("Comic Sans MS", 18), justify="left", wraplength=650)
        book_detail_1.place(relx=0.55, rely=0.25, anchor="nw")
        book_name_2 = tk.Label(master=self.frame_page_3_4, text=self.random_book_name_2, bg=self.c, font=("Comic Sans MS", 20, "bold"), justify="left", wraplength=650)
        book_name_2.place(relx=0.55, rely=0.55, anchor="nw")
        book_detail_2 = tk.Label(master=self.frame_page_3_4, text=f"{self.random_book_author_2}\n\n{self.random_book_description_2}", bg=self.c, font=("Comic Sans MS", 18), justify="left", wraplength=650)
        book_detail_2.place(relx=0.55, rely=0.6, anchor="nw")

    def get_random_books(self, i1, i2):
        return books[i1][0], books[i1][1], books[i1][2], books[i2][0], books[i2][1], books[i2][2]

    def page_3_5(self):
        self.frame_page_3_4.pack_forget()
        self.frame_page_3_6.pack_forget()
        self.frame_page_3_7.pack_forget()
        self.frame_page_3_5.pack()



        thank_you_label = tk.Label(master=self.frame_page_3_5, text="Thank you for playing!", bg=self.c, font=("Comic Sans MS", 50))
        thank_you_label.place(relx=0.5, rely=0.2, anchor="center")

        contributors_and_references = tk.Button(master=self.frame_page_3_5, text="Contributors &\nReferences", bg="white", fg="black", width=15, height=3, font=("Comic Sans MS", 16), command=self.page_3_6)
        contributors_and_references.place(relx=0.35, rely=0.4, anchor="nw")
        feedback_button = tk.Button(master=self.frame_page_3_5, text="Feedback", bg="white", fg="black", width=15, height=3, font=("Comic Sans MS", 16), command=self.open_website)
        feedback_button.place(relx=0.65, rely=0.4, anchor="ne")
        back_button = tk.Button(master=self.frame_page_3_5, text="Back", bg="white", fg="black", width=15, height=3, font=("Comic Sans MS", 16), command=self.page_3_1)
        back_button.place(relx=0.35, rely=0.7, anchor="sw")
        quit_button = tk.Button(master=self.frame_page_3_5, text="Quit", bg="white", fg="black", width=15, height=3, font=("Comic Sans MS", 16), command=self.quit)
        quit_button.place(relx=0.65, rely=0.7, anchor="se")

    def open_website(self):
        webbrowser.open("https://forms.gle/DLdnScLQ3K3gzqPAA")

    def quit(self):
        pygame.mixer.music.stop()
        pygame.quit()
        window.destroy()

    def page_3_6(self):
        self.frame_page_3_5.pack_forget()
        self.frame_page_3_7.pack_forget()
        self.frame_page_3_6.pack()
        self.background_3_6.pack()

        contributor_image_1 = tk.Label(master=self.frame_page_3_6, image=self.resized_contributor_1, bg="grey70", relief="solid", borderwidth=3, highlightbackground="black", highlightthickness=1)
        contributor_image_1.place(relx=0.06, rely=0.1, anchor="nw")
        contributor_image_2 = tk.Label(master=self.frame_page_3_6, image=self.resized_contributor_2, relief="solid", borderwidth=3, highlightbackground="black", highlightthickness=1)
        contributor_image_2.place(relx=0.06, rely=0.5, anchor="nw")

        contributor_description_1 = tk.Label(master=self.frame_page_3_6, text="Contributor 1: Huuuuu\nQuote: chipi chipi chapa chapa\n            dubi dubi daba daba", font=("Comic Sans MS", 30), bg="grey70", relief="solid", borderwidth=3, highlightbackground="black", highlightthickness=1, anchor="w", justify="left")
        contributor_description_1.place(relx=0.3, rely=0.28, anchor="w")
        contributor_description_2 = tk.Label(master=self.frame_page_3_6, text="Contributor 2: Kuuuuu\nQuote: Saving others as a passerby, \n            being saved by others.", font=("Comic Sans MS", 30), bg="grey70", relief="solid", borderwidth=3, highlightbackground="black", highlightthickness=1, anchor="w", justify="left")
        contributor_description_2.place(relx=0.3, rely=0.65, anchor="w")

        self.next_button_6.place(relx=0.55, rely=0.95, anchor="center")
        self.back_button_6.place(relx=0.45, rely=0.95, anchor="center")

    def page_3_7(self):
        self.frame_page_3_6.pack_forget()
        self.frame_page_3_7.pack()
        self.background_3_7.pack()

        reference_label = tk.Label(master=self.frame_page_3_7, text=reference, font=("Comic Sans MS", 25), bg="grey70", relief="solid", borderwidth=3, highlightbackground="black", highlightthickness=1, anchor="w", justify="left", wraplength=1000)
        reference_label.place(relx=0.1, rely=0.25, anchor="w")

        tools_label = tk.Label(master=self.frame_page_3_7, text=tools, font=("Comic Sans MS", 25), bg="grey70", relief="solid", borderwidth=3, highlightbackground="black", highlightthickness=1, anchor="w", justify="left", wraplength=1000)
        tools_label.place(relx=0.1, rely=0.65, anchor="w")

        self.end_button_7.place(relx=0.55, rely=0.95, anchor="center")
        self.back_button_7.place(relx=0.45, rely=0.95, anchor="center")

    def change_transparency(self, image_path, transparency):
        image = Image.open(image_path).convert("RGBA")
        alpha = image.split()[3]
        alpha = alpha.point(lambda p: p * transparency)
        image.putalpha(alpha)
        image.resize((screen_width, screen_height), Image.Resampling.LANCZOS)

        return image

reference = "Reference:\n\nhttps://self-directed-search.com/riasec-theory/\nhttps://www.acer.org/files/SDS_Sample_Report.pdf\nhttps://boardgamedesignlab.com/wp-content/uploads/2020/11/Playtest-Feedback-Form.pdf\nhttps://www.youtube.com/watch?v=zPyg4N7bcHM\n"
tools = "Tools:\n\nPython, Tkinter, ChatGPT, Paint, FlipaClip, Canvas, Runway, etc.\n"
avoid_zone = [(screen_width/2 - 175, screen_width/2 + 175, screen_height/2 - 175, screen_height/2 + 175), (screen_width*0.9, screen_height*0.4, 150, 150)]



if __name__ == "__main__":
    create_arableland()
    Shop_button()
    Money = Money()
    generate_stone_tree = Generate_stone_tree(avoid_zone)
    rsieac_points = RSIEAC_points()

    window.mainloop()


