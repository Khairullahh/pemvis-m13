import tkinter as tk

class DrawingApp:
    def __init__(self, master):
        self.master = master
        master.title("menggambar titik dan garis")

        self.canvas = tk.Canvas(master, width=600, height=400, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.color = "black"
        self.mode = "garis"  # Default mode is line drawing

        self.create_widgets()
        self.bind_events()

        # List to store item IDs for deletion (optional for future enhancements)
        self.items = []

    def create_widgets(self):
        # Color selection buttons (same as before)
        color_frame = tk.Frame(self.master)
        color_frame.pack(fill=tk.X)

        self.color_buttons = {}
        colors = ["red", "green", "blue", "black"]
        for color in colors:
            button = tk.Button(color_frame, text=color.capitalize(), bg=color,
                               command=lambda c=color: self.set_color(c))
            button.pack(side=tk.LEFT)
            self.color_buttons[color] = button

        # Mode selection buttons
        mode_frame = tk.Frame(self.master)
        mode_frame.pack(fill=tk.X)

        self.mode_buttons = {}
        modes = ["garis", "titik"]
        for mode in modes:
            button = tk.Button(mode_frame, text=mode.capitalize(),
                               command=lambda m=mode: self.set_mode(m))
            button.pack(side=tk.LEFT)
            self.mode_buttons[mode] = button

        # Clear button (optional for future enhancements)
        # clear_button = tk.Button(self.master, text="Hapus Semua", command=self.clear_canvas)
        # clear_button.pack()

    def bind_events(self):
        self.canvas.bind("<B1-Motion>", self.draw)
        self.canvas.bind("<ButtonRelease-1>", self.stop_drawing)

    def draw(self, event):
        if self.mode == "garis":
            self.x1, self.y1 = event.x, event.y
            self.canvas.create_line(self.x1, self.y1, event.x, event.y, fill=self.color)
        elif self.mode == "titik":
            x, y = event.x, event.y
            self.canvas.create_oval(x-2, y-2, x+2, y+2, fill=self.color)

    def stop_drawing(self, event):
        self.x1, self.y1 = None, None  # Reset starting coordinates

    def set_color(self, color):
        self.color = color
        for c, button in self.color_buttons.items():
            button.config(relief=tk.RAISED if c == color else tk.FLAT)

    def set_mode(self, mode):
        self.mode = mode
        for m, button in self.mode_buttons.items():
            button.config(relief=tk.RAISED if m == mode else tk.FLAT)

    def clear_canvas(self):
        # Delete all items from the canvas (optional for future enhancements)
        for item_id in self.items:
            self.canvas.delete(item_id)
        self.items = []  # Clear the list of item IDs

if __name__ == "__main__":
    root = tk.Tk()
    app = DrawingApp(root)
    root.mainloop()