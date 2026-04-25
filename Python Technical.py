import tkinter as tk

class ScrollOpen:
    def __init__(self, root):
        self.root = root
        self.root.title("Scroll Opening Prototype")
        self.root.geometry("700x500")
        self.root.configure(bg="#D8C7A1")

        self.closed_scroll = (
            "╭─────────────────────────────╮\n"
            "│                             │\n"
            "│         [ SCROLL ]          │\n"
            "│                             │\n"
            "╰─────────────────────────────╯"
        )

        self.half_closed_scroll = (
            "╭─────────────────────────────╮\n"
            "│╰───────────────────────────╯│\n"
            "│                             │\n"
            "│                             │\n"
            "│                             │\n"
            "│╭───────────────────────────╮│\n"
            "╰─────────────────────────────╯"
        )

        self.half_open_scroll = (
            "╭─────────────────────────────╮\n"
            "│╰───────────────────────────╯│\n"
            "│ Alexandria, scholars once   │\n"
            "│ gathered to study the stars │\n"
            "│ …                           │\n"
            "│                             │\n"
            "│                             │\n"
            "│                             │\n"
            "│                             │\n"
            "│                             │\n"
            "│╭───────────────────────────╮│\n"
            "╰─────────────────────────────╯"
        )

        self.full_open_scroll = (
            "╭─────────────────────────────╮\n"
            "│ Fragment 12 — Reconstructed │\n"
            "│                             │\n"
            "│ In the great halls of       │\n"
            "│ Alexandria, scholars once   │\n"
            "│ gathered to study the stars │\n"
            "│ …                           │\n"
            "│                             │\n"
            "│                             │\n"
            "│                             │\n"
            "│                             │\n"
            "│                             │\n"
            "│                             │\n"
            "│                             │\n"
            "│                             │\n"
            "╰─────────────────────────────╯"
        )

        self.label = tk.Label(
            root,
            text=self.closed_scroll,
            font=("Courier", 14),
            bg="#D8C7A1",
            fg="#2A241F",
            justify="left"
        )
        self.label.pack(expand=True)

        self.stage = 0
        root.bind("<Return>", self.start_animation)

    def start_animation(self, event=None):
      if self.stage == 0:
            self.stage = 1
            self.label.config(text=self.half_closed_scroll)
            self.root.after(250, self.show_half_open)

    def show_half_open(self):
        if self.stage == 1:
            self.stage = 2
            self.label.config(text=self.half_open_scroll)
            self.root.after(250, self.open_fully)

    def open_fully(self):
        if self.stage == 2:
            self.stage = 3
            self.label.config(text=self.full_open_scroll)

root = tk.Tk()
app = ScrollOpen(root)
root.mainloop()