# import tkinter as tk
# import random
# import math
# import pygame

# WIDTH = 800
# HEIGHT = 600

# difficulty_settings = {
#     "Easy": {"speed": 2, "spawn": 1500},
#     "Medium": {"speed": 3, "spawn": 1000},
#     "Hard": {"speed": 4, "spawn": 700}
# }

# challenge_modes = [
#     "Normal",
#     "Speed Runner",
#     "No Escape",
#     "Sharp Shooter"
# ]

# class BalloonGame:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("🎈 Pop It Like It's Hot 🔥")
#         self.root.geometry(f"{WIDTH}x{HEIGHT}")
#         self.root.resizable(False, False)

#         pygame.mixer.init()
#         try:
#             pygame.mixer.music.load("bg_music.mp3")
#             pygame.mixer.music.play(-1)
#         except:
#             pass

#         self.show_splash()

#     # ---------------- SPLASH ----------------
#     def show_splash(self):
#         self.splash = tk.Frame(self.root, bg="#6ec6ff")
#         self.splash.pack(fill="both", expand=True)

#         self.splash_canvas = tk.Canvas(self.splash,
#                                        bg="#6ec6ff",
#                                        width=WIDTH,
#                                        height=HEIGHT,
#                                        highlightthickness=0)
#         self.splash_canvas.pack()

#         self.title_text = self.splash_canvas.create_text(
#             WIDTH//2, 80,
#             text="🎈 POP IT LIKE IT'S HOT 🔥",
#             font=("Comic Sans MS", 30, "bold"),
#             fill="#ff006e"
#         )

#         self.animate_title()
#         self.animate_background()

#         tk.Label(self.splash,
#                  text="Select Difficulty:",
#                  font=("Arial", 14),
#                  bg="#6ec6ff").place(relx=0.5,
#                                      rely=0.35,
#                                      anchor="center")

#         self.mode = tk.StringVar(value="Easy")
#         tk.OptionMenu(self.splash,
#                       self.mode,
#                       *difficulty_settings.keys()).place(
#                           relx=0.5,
#                           rely=0.42,
#                           anchor="center")

#         tk.Label(self.splash,
#                  text="Select Challenge:",
#                  font=("Arial", 14),
#                  bg="#6ec6ff").place(relx=0.5,
#                                      rely=0.52,
#                                      anchor="center")

#         self.challenge_choice = tk.StringVar(value="Normal")
#         tk.OptionMenu(self.splash,
#                       self.challenge_choice,
#                       *challenge_modes).place(
#                           relx=0.5,
#                           rely=0.59,
#                           anchor="center")

#         tk.Button(self.splash,
#                   text="🚀 START GAME",
#                   font=("Comic Sans MS", 16, "bold"),
#                   bg="#ff006e",
#                   fg="white",
#                   command=self.start_game).place(
#                       relx=0.5,
#                       rely=0.75,
#                       anchor="center")

#     # -------- SPLASH ANIMATIONS --------
#     def animate_title(self):
#         colors = ["#ff006e", "#ffbe0b", "#3a86ff", "#8338ec"]
#         self.splash_canvas.itemconfig(
#             self.title_text,
#             fill=random.choice(colors))
#         self.root.after(500, self.animate_title)

#     def animate_background(self):
#         r = random.randint(100, 200)
#         g = random.randint(150, 220)
#         b = random.randint(200, 255)
#         color = f'#{r:02x}{g:02x}{b:02x}'
#         self.splash_canvas.config(bg=color)
#         self.root.after(2000, self.animate_background)

#     # ---------------- START ----------------
#     def start_game(self):
#         self.splash.destroy()

#         self.canvas = tk.Canvas(self.root,
#                                 bg="#caf0f8",
#                                 width=WIDTH,
#                                 height=HEIGHT)
#         self.canvas.pack()

#         self.score = 0
#         self.display_score = 0
#         self.time_left = 30
#         self.running = True
#         self.balloons = []
#         self.particles = []

#         self.challenge = self.challenge_choice.get()
#         self.challenge_timer = 20

#         self.score_label = tk.Label(self.root,
#                                     text="Score: 0",
#                                     font=("Arial", 14))
#         self.score_label.place(x=10, y=10)

#         self.timer_label = tk.Label(self.root,
#                                     text="Time: 30",
#                                     font=("Arial", 14))
#         self.timer_label.place(x=700, y=10)

#         self.challenge_label = tk.Label(self.root,
#             text=f"Mode: {self.challenge}",
#             font=("Arial", 12, "bold"),
#             fg="purple")
#         self.challenge_label.place(x=320, y=10)

#         self.canvas.bind("<Button-1>", self.shoot)

#         self.spawn_balloon()
#         self.update_game()
#         self.countdown()

#     # ---------------- SPAWN ----------------
#     def spawn_balloon(self):
#         if not self.running:
#             return

#         x = random.randint(50, WIDTH-50)
#         r = 25

#         balloon = self.canvas.create_oval(
#             x-r, HEIGHT-r, x+r, HEIGHT+r,
#             fill=random.choice(["#ff4d6d",
#                                 "#4cc9f0",
#                                 "#80ed99",
#                                 "#000000"]),
#             outline=""
#         )

#         self.balloons.append({
#             "id": balloon,
#             "dx": random.choice([-2,-1,1,2]),
#             "swing": random.uniform(0, math.pi)
#         })

#         delay = difficulty_settings[
#             self.mode.get()]["spawn"]
#         self.root.after(delay, self.spawn_balloon)

#     # ---------------- UPDATE ----------------
#     def update_game(self):
#         if not self.running:
#             return

#         speed = difficulty_settings[
#             self.mode.get()]["speed"]

#         for balloon in self.balloons[:]:
#             balloon["swing"] += 0.1
#             swing_offset = math.sin(
#                 balloon["swing"]) * 2

#             self.canvas.move(balloon["id"],
#                              balloon["dx"] + swing_offset,
#                              -speed)

#             coords = self.canvas.coords(
#                 balloon["id"])

#             if coords[3] < 0:
#                 self.canvas.delete(balloon["id"])
#                 self.balloons.remove(balloon)

#                 if self.challenge == "No Escape":
#                     self.game_over(
#                         "A Balloon Escaped!")
#                     return

#         for p,dx,dy,life in self.particles[:]:
#             self.canvas.move(p,dx,dy)
#             life -= 1
#             if life <= 0:
#                 self.canvas.delete(p)
#                 self.particles.remove(
#                     (p,dx,dy,life+1))
#             else:
#                 self.particles[
#                     self.particles.index(
#                         (p,dx,dy,life+1)
#                     )
#                 ] = (p,dx,dy,life)

#         if self.display_score < self.score:
#             self.display_score += 1
#             self.score_label.config(
#                 text=f"Score: {self.display_score}")

#         self.root.after(30,self.update_game)

#     # ---------------- SHOOT ----------------
#     def shoot(self, event):
#         if not self.running:
#             return

#         hit = False
#         for balloon in self.balloons[:]:
#             x1,y1,x2,y2 = self.canvas.coords(
#                 balloon["id"])
#             if x1 < event.x < x2 and y1 < event.y < y2:
#                 hit = True
#                 self.pop_balloon(balloon)
#                 break

#         if not hit:
#             self.shake()
#             if self.challenge == "Sharp Shooter":
#                 self.game_over("Missed Click!")

#     # ---------------- POP ----------------
#     def pop_balloon(self, balloon):
#         self.explosion(balloon)
#         self.canvas.delete(balloon["id"])
#         self.balloons.remove(balloon)
#         self.score += 1

#     # ---------------- EXPLOSION ----------------
#     def explosion(self, balloon):
#         x1,y1,x2,y2 = self.canvas.coords(
#             balloon["id"])
#         cx = (x1+x2)/2
#         cy = (y1+y2)/2

#         for _ in range(15):
#             angle = random.uniform(0,2*math.pi)
#             speed = random.uniform(2,5)
#             dx = math.cos(angle)*speed
#             dy = math.sin(angle)*speed
#             p = self.canvas.create_oval(
#                 cx, cy, cx+5, cy+5,
#                 fill="orange", outline="")
#             self.particles.append((p,dx,dy,20))

#     # ---------------- TIMER ----------------
#     def countdown(self):
#         if not self.running:
#             return

#         self.time_left -= 1
#         self.timer_label.config(
#             text=f"Time: {self.time_left}")

#         if self.time_left <= 5:
#             current = self.timer_label.cget("fg")
#             self.timer_label.config(
#                 fg="red" if current=="black"
#                 else "black")

#         if self.time_left <= 0:
#             self.game_over("Time Up")
#         else:
#             self.root.after(1000,
#                             self.countdown)

#     # ---------------- SHAKE ----------------
#     def shake(self):
#         for _ in range(8):
#             x = random.randint(-5,5)
#             y = random.randint(-5,5)
#             self.root.geometry(
#                 f"{WIDTH}x{HEIGHT}+{x}+{y}")
#             self.root.update()
#         self.root.geometry(
#             f"{WIDTH}x{HEIGHT}")

#     # ---------------- GAME OVER ----------------
#     def game_over(self, reason):
#         self.running = False
#         self.canvas.delete("all")

#         comment = "🔥 Advanced Pop Master!" \
#             if self.score >= 15 \
#             else "🎯 Skilled Player!" \
#             if self.score >= 5 \
#             else "🌱 Beginner! Keep practicing!"

#         self.canvas.create_text(
#             WIDTH//2, HEIGHT//2 - 60,
#             text=reason,
#             font=("Comic Sans MS", 22, "bold"),
#             fill="red")

#         self.canvas.create_text(
#             WIDTH//2, HEIGHT//2,
#             text=f"Final Score: {self.score}",
#             font=("Comic Sans MS", 26, "bold"),
#             fill="blue")

#         self.canvas.create_text(
#             WIDTH//2, HEIGHT//2 + 60,
#             text=comment,
#             font=("Comic Sans MS", 18),
#             fill="green")

#         tk.Button(self.root,
#                   text="🔄 Play Again",
#                   font=("Comic Sans MS", 14),
#                   bg="#06d6a0",
#                   fg="white",
#                   command=self.restart).place(
#                       relx=0.5,
#                       rely=0.75,
#                       anchor="center")

#     def restart(self):
#         self.canvas.destroy()
#         self.score_label.destroy()
#         self.timer_label.destroy()
#         self.challenge_label.destroy()
#         self.start_game()


# root = tk.Tk()
# game = BalloonGame(root)
# root.mainloop()
















import tkinter as tk
import random
import math

# Constants
WIDTH = 800
HEIGHT = 600

difficulty_settings = {
    "Easy": {"speed": 2, "spawn": 1500},
    "Medium": {"speed": 3, "spawn": 1000},
    "Hard": {"speed": 4, "spawn": 700}
}

challenge_modes = ["Normal", "Speed Runner", "No Escape", "Sharp Shooter"]

class BalloonGame:
    def __init__(self, root):
        self.root = root
        self.root.title("🎈 Pop It Like Arathy 🔥")
        self.root.geometry(f"{WIDTH}x{HEIGHT}")
        self.root.resizable(False, False)
        
        self.show_splash()

    # ================= SPLASH SCREEN =================
    def show_splash(self):
        # Create a container frame to hold all splash widgets
        self.splash_frame = tk.Frame(self.root, bg="#6ec6ff")
        self.splash_frame.pack(fill="both", expand=True)

        self.splash_canvas = tk.Canvas(self.splash_frame, bg="#6ec6ff", 
                                      width=WIDTH, height=HEIGHT, highlightthickness=0)
        self.splash_canvas.pack()

        self.title_text = self.splash_canvas.create_text(
            WIDTH//2, 100,
            text="🎈 POP IT LIKE Arathy 🔥",
            font=("Comic Sans MS", 32, "bold"),
            fill="#ff006e"
        )

        # UI Controls
        tk.Label(self.splash_frame, text="Select Difficulty:", font=("Arial", 12), bg="#6ec6ff").place(relx=0.5, rely=0.35, anchor="center")
        self.diff_var = tk.StringVar(value="Medium")
        tk.OptionMenu(self.splash_frame, self.diff_var, *difficulty_settings.keys()).place(relx=0.5, rely=0.42, anchor="center")

        tk.Label(self.splash_frame, text="Select Challenge:", font=("Arial", 12), bg="#6ec6ff").place(relx=0.5, rely=0.52, anchor="center")
        self.chall_var = tk.StringVar(value="Normal")
        tk.OptionMenu(self.splash_frame, self.chall_var, *challenge_modes).place(relx=0.5, rely=0.59, anchor="center")

        tk.Button(self.splash_frame, text="🚀 START GAME", font=("Arial", 16, "bold"), 
                  bg="#ff006e", fg="white", command=self.start_game).place(relx=0.5, rely=0.75, anchor="center")

        self.animate_splash()

    def animate_splash(self):
        if hasattr(self, 'splash_frame') and self.splash_frame.winfo_exists():
            colors = ["#ff006e", "#ffbe0b", "#3a86ff", "#8338ec"]
            self.splash_canvas.itemconfig(self.title_text, fill=random.choice(colors))
            self.root.after(500, self.animate_splash)

    # ================= START GAME =================
    def start_game(self):
        # Get settings before destroying splash
        self.difficulty = self.diff_var.get()
        self.challenge = self.chall_var.get()
        
        # Clean up splash
        self.splash_frame.destroy()

        # Game Setup
        self.canvas = tk.Canvas(self.root, width=WIDTH, height=HEIGHT, bg="#caf0f8", highlightthickness=0)
        self.canvas.pack()

        self.score = 0
        self.time_left = 30
        self.running = True
        self.balloons = []
        self.particles = []

        # UI Overlay
        self.score_text = self.canvas.create_text(70, 30, text="Score: 0", font=("Arial", 16, "bold"), fill="black")
        self.timer_text = self.canvas.create_text(WIDTH-80, 30, text="Time: 30", font=("Arial", 16, "bold"), fill="black")
        self.mode_text = self.canvas.create_text(WIDTH//2, 30, text=f"Mode: {self.challenge}", font=("Arial", 12, "italic"), fill="purple")

        self.canvas.bind("<Button-1>", self.on_click)

        self.spawn_loop()
        self.update_loop()
        self.timer_loop()

    # ================= MIDPOINT CIRCLE ALGORITHM =================
    def midpoint_circle(self, xc, yc, r):
        x, y = 0, r
        p = 1 - r
        pts = []
        while x <= y:
            pts += [(xc+x, yc+y), (xc-x, yc+y), (xc+x, yc-y), (xc-x, yc-y),
                    (xc+y, yc+x), (xc-y, yc+x), (xc+y, yc-x), (xc-y, yc-x)]
            x += 1
            if p < 0: p += 2*x + 1
            else:
                y -= 1
                p += 2*(x-y) + 1
        return pts

    def fill_circle_manual(self, xc, yc, r, color):
        items = []
        for y_off in range(-r, r):
            x_lim = int(math.sqrt(r*r - y_off*y_off))
            line = self.canvas.create_line(xc-x_lim, yc+y_off, xc+x_lim, yc+y_off, fill=color)
            items.append(line)
        return items

    # ================= BALLOON LOGIC =================
    def create_balloon(self):
        x = random.randint(60, WIDTH-60)
        y = HEIGHT + 40
        r = 25
        color = random.choice(["#ff4d6d", "#4cc9f0", "#80ed99", "#7209b7", "#ffbe0b"])

        fill_ids = self.fill_circle_manual(x, y, r, color)
        outline_pts = self.midpoint_circle(x, y, r)
        outline_ids = [self.canvas.create_rectangle(px, py, px+1, py+1, fill="black", outline="") for px, py in outline_pts]

        return {
            "x": x, "y": y, "r": r,
            "items": fill_ids + outline_ids,
            "dx": random.choice([-1.5, -0.5, 0.5, 1.5]),
            "swing": random.uniform(0, math.pi)
        }

    def spawn_loop(self):
        if not self.running: return
        self.balloons.append(self.create_balloon())
        delay = difficulty_settings[self.difficulty]["spawn"]
        self.root.after(delay, self.spawn_loop)

    def update_loop(self):
        if not self.running: return

        speed = difficulty_settings[self.difficulty]["speed"]

        for b in self.balloons[:]:
            b["swing"] += 0.1
            oscillation = math.sin(b["swing"]) * 2
            
            dx = b["dx"] + oscillation
            dy = -speed
            
            b["x"] += dx
            b["y"] += dy
            
            for item in b["items"]:
                self.canvas.move(item, dx, dy)

            if b["y"] < -50:
                self.remove_balloon(b)
                if self.challenge == "No Escape":
                    self.game_over("A Balloon Escaped!")
                    return

        # Particle Update
        for p_data in self.particles[:]:
            obj, dx, dy, life = p_data
            self.canvas.move(obj, dx, dy)
            new_life = life - 1
            if new_life <= 0:
                self.canvas.delete(obj)
                self.particles.remove(p_data)
            else:
                idx = self.particles.index(p_data)
                self.particles[idx] = (obj, dx, dy, new_life)

        self.root.after(30, self.update_loop)

    # ================= INTERACTION =================
    def on_click(self, event):
        if not self.running: return
        hit = False
        for b in self.balloons[:]:
            dist = math.sqrt((event.x - b["x"])**2 + (event.y - b["y"])**2)
            if dist <= b["r"]:
                self.pop_balloon(b)
                hit = True
                break
        
        if not hit:
            self.shake_screen()
            if self.challenge == "Sharp Shooter":
                self.game_over("Missed Click!")

    def pop_balloon(self, b):
        self.create_explosion(b["x"], b["y"])
        self.remove_balloon(b)
        self.score += 1
        self.canvas.itemconfig(self.score_text, text=f"Score: {self.score}")

    def remove_balloon(self, b):
        for item in b["items"]:
            self.canvas.delete(item)
        if b in self.balloons:
            self.balloons.remove(b)

    def create_explosion(self, cx, cy):
        for _ in range(12):
            angle = random.uniform(0, 2*math.pi)
            spd = random.uniform(2, 6)
            dx = math.cos(angle) * spd
            dy = math.sin(angle) * spd
            p = self.canvas.create_oval(cx-2, cy-2, cx+2, cy+2, fill="orange", outline="")
            self.particles.append((p, dx, dy, 15))

    def shake_screen(self):
        orig_geo = self.root.geometry()
        for _ in range(5):
            x_sh = random.randint(-4, 4)
            y_sh = random.randint(-4, 4)
            self.root.geometry(f"{WIDTH}x{HEIGHT}+{x_sh}+{y_sh}")
            self.root.update()
        self.root.geometry(f"{WIDTH}x{HEIGHT}+0+0")

    # ================= TIMER & END =================
    def timer_loop(self):
        if not self.running: return
        self.time_left -= 1
        self.canvas.itemconfig(self.timer_text, text=f"Time: {self.time_left}")
        
        if self.time_left <= 5:
            curr_color = self.canvas.itemcget(self.timer_text, "fill")
            self.canvas.itemconfig(self.timer_text, fill="red" if curr_color == "black" else "black")

        if self.time_left <= 0:
            self.game_over("Time Up!")
        else:
            self.root.after(1000, self.timer_loop)

    def game_over(self, reason):
        self.running = False
        self.canvas.delete("all")
        
        self.canvas.create_text(WIDTH//2, HEIGHT//2 - 80, text=reason, font=("Arial", 30, "bold"), fill="#ff006e")
        self.canvas.create_text(WIDTH//2, HEIGHT//2 - 20, text=f"Final Score: {self.score}", font=("Arial", 24), fill="blue")
        
        msg = "🔥 Legend!" if self.score > 20 else "👏 Great Job!" if self.score > 10 else "💪 Keep Practicing!"
        self.canvas.create_text(WIDTH//2, HEIGHT//2 + 30, text=msg, font=("Arial", 18), fill="green")

        tk.Button(self.root, text="🔄 RESTART", font=("Arial", 14, "bold"), bg="#06d6a0", fg="white", 
                  command=self.restart_game).place(relx=0.5, rely=0.75, anchor="center")

    def restart_game(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        self.show_splash()

if __name__ == "__main__":
    root = tk.Tk()
    game = BalloonGame(root)
    root.mainloop()