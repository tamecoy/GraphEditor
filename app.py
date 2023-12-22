import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageDraw

class SimpleEditor:
     def __init__(self, root):
         self.root = root
         self.root.title("Simple graphic editor")

         self.canvas = tk.Canvas(root, bg="white", width=400, height=400)
         self.canvas.pack(expand=tk.YES, fill=tk.BOTH)

         self.setup_toolbar()
         self.setup_menu()

         self.image = Image.new("RGB", (400, 400), color="white")
         self.draw = ImageDraw.Draw(self.image)
         self.last_x = None
         self.last_y = None

         self.canvas.bind("<B1-Motion>", self.paint)
         self.canvas.bind("<ButtonRelease-1>", self.reset)

     def setup_toolbar(self):
         toolbar = tk.Frame(root, bg="gray")
         toolbar.pack(side=tk.BOTTOM, fill=tk.X)

         clear_button = tk.Button(toolbar, text="Clear", command=self.clear_canvas)
         clear_button.pack(side=tk.LEFT)

         save_button = tk.Button(toolbar, text="Save", command=self.save_image)
         save_button.pack(side=tk.RIGHT)

     def setup_menu(self):
         menubar = tk.Menu(root)
         root.config(menu=menubar)

         file_menu = tk.Menu(menubar, tearoff=0)
         menubar.add_cascade(label="File", menu=file_menu)

         file_menu.add_command(label="Save", command=self.save_image)
         file_menu.add_separator()
         file_menu.add_command(label="Exit", command=root.destroy)

     def paint(self, event):
         x, y = event.x, event.y
         if self.last_x and self.last_y:
             self.canvas.create_line(self.last_x, self.last_y, x, y, width=2, fill="black", capstyle=tk.ROUND, smooth=tk.TRUE)
             self.draw.line([self.last_x, self.last_y, x, y], fill="black", width=2)

         self.last_x = x
         self.last_y = y

     def reset(self, event):
         self.last_x = None
         self.last_y = None

     def clear_canvas(self):
         self.canvas.delete("all")
         self.image = Image.new("RGB", (400, 400), color="white")
         self.draw = ImageDraw.Draw(self.image)

     def save_image(self):
         file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
         if file_path:
             self.image.save(file_path)

if __name__ == "__main__":
     root = tk.Tk()
     editor = SimpleEditor(root)
     root.mainloop()
