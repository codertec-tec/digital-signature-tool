# digital signature tool

import turtle
import tkinter as tk
from tkinter import colorchooser, filedialog, messagebox

# --- Config ---
BG_COLOR = "#050505"  # dark background
DEFAULT_PEN = "#00FF77"  # neon green
DEFAULT_SPEED = 5       # 1 slow - 10 fast
FANCY_FONT = "Edwardian Script ITC"  # change to "Great Vibes" or "Brush Script MT" if installed
FONT_SIZE = 72

class SignatureApp:
    def __init__(self, root):
        self.root = root
        root.title("Fancy Calligraphy Signature Tool")

        # Control bar
        frame = tk.Frame(root)
        frame.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)

        # Name entry
        tk.Label(frame, text="Name:").pack(side=tk.LEFT)
        self.name_var = tk.StringVar(value="signature")
        tk.Entry(frame, textvariable=self.name_var, width=20).pack(side=tk.LEFT, padx=5)

        # Color chooser
        self.pen_color = DEFAULT_PEN
        tk.Button(frame, text="Pen Color", command=self.choose_color).pack(side=tk.LEFT, padx=5)

        # Speed slider
        tk.Label(frame, text="Speed:").pack(side=tk.LEFT)
        self.speed_var = tk.IntVar(value=DEFAULT_SPEED)
        tk.Scale(frame, from_=1, to=10, orient=tk.HORIZONTAL, variable=self.speed_var).pack(side=tk.LEFT, padx=5)

        # Buttons
        tk.Button(frame, text="Sign", command=self.sign).pack(side=tk.LEFT, padx=5)
        tk.Button(frame, text="Clear", command=self.clear).pack(side=tk.LEFT, padx=5)
        tk.Button(frame, text="Save", command=self.save).pack(side=tk.LEFT, padx=5)

        # Turtle canvas
        self.canvas = tk.Canvas(root, width=900, height=300, bg=BG_COLOR)
        self.canvas.pack(padx=5, pady=5)
        self.screen = turtle.TurtleScreen(self.canvas)
        self.screen.bgcolor(BG_COLOR)
        self.t = turtle.RawTurtle(self.screen)
        self.t.hideturtle()
        self.t.pensize(3)

    def choose_color(self):
        c = colorchooser.askcolor(color=self.pen_color, title="Choose Pen Color")
        if c and c[1]:
            self.pen_color = c[1]

    def clear(self):
        self.t.clear()

    def save(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".ps",
                                                 filetypes=[("PostScript files", "*.ps")])
        if file_path:
            self.canvas.postscript(file=file_path, colormode='color')
            messagebox.showinfo("Saved", f"Signature saved to {file_path}")

    def sign(self):
        self.t.clear()
        self.t.penup()
        self.t.color(self.pen_color)
        self.t.speed(0)
        # Start position
        self.t.goto(-350, 0)

        name = self.name_var.get()
        speed = self.speed_var.get()

        for ch in name:
            self.t.write(ch, font=(FANCY_FONT, FONT_SIZE, "normal"))
            self.screen.update()
            self.t.forward(40)  # space between letters
            self.root.after(int(200 / speed))  # animation delay

def main():
    root = tk.Tk()
    app = SignatureApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
