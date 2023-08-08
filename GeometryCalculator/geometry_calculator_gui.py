import tkinter as tk
from tkinter import ttk
from geometry_calculator import Rectangle, Circle

class GeometryCalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("2D Geometry Calculator")

        self.style = ttk.Style()
        self.style.theme_use("clam")

        self.label = tk.Label(root, text="2D Geometry Calculator", font=("Helvetica", 20, "bold"))
        self.label.pack(pady=10)

        self.shape_var = tk.StringVar()
        self.shape_label = tk.Label(root, text="Select Shape:", font=("Helvetica", 12))
        self.shape_label.pack()
        self.shape_combo = ttk.Combobox(root, textvariable=self.shape_var, values=["Rectangle", "Circle"])
        self.shape_combo.pack()

        self.dimension_frame = tk.Frame(root)
        self.dimension_frame.pack(pady=10)

        self.width_label = tk.Label(self.dimension_frame, text="Width:", font=("Helvetica", 12))
        self.width_label.grid(row=0, column=0, padx=5)
        self.width_entry = tk.Entry(self.dimension_frame)
        self.width_entry.grid(row=0, column=1, padx=5)

        self.height_label = tk.Label(self.dimension_frame, text="Height:", font=("Helvetica", 12))
        self.height_label.grid(row=1, column=0, padx=5)
        self.height_entry = tk.Entry(self.dimension_frame)
        self.height_entry.grid(row=1, column=1, padx=5)

        self.canvas = tk.Canvas(root, width=300, height=150, bg="white")
        self.canvas.pack()

        self.calculate_button = tk.Button(root, text="Calculate Area", font=("Helvetica", 12), command=self.calculate_area)
        self.calculate_button.pack(pady=15)

        self.result_label = tk.Label(root, text="", font=("Helvetica", 16, "bold"))
        self.result_label.pack()

        self.shape_var.trace("w", self.update_dimension_labels)

    def update_dimension_labels(self, *args):
        shape = self.shape_var.get()
        if shape == "Rectangle":
            self.width_label.config(text="Width:")
            self.height_label.config(text="Height:")
        elif shape == "Circle":
            self.width_label.config(text="Radius:")
            self.height_label.config(text="")

    def calculate_area(self):
        shape = self.shape_var.get()
        width = self.width_entry.get()
        height = self.height_entry.get()

        if not width or not height:
            self.result_label.config(text="Please enter dimensions.")
            return

        try:
            width = float(width)
            height = float(height)
        except ValueError:
            self.result_label.config(text="Invalid dimensions entered.")
            return

        if shape == "Rectangle":
            shape_obj = Rectangle(width, height)
        elif shape == "Circle":
            shape_obj = Circle(width)
        else:
            self.result_label.config(text="Invalid shape selected.")
            return

        area = shape_obj.calculate_area()
        result_text = f"{shape} Area: {area:.2f} square units"
        self.result_label.config(text=result_text)

        self.draw_shape(shape, width, height)

    
    def draw_shape(self, shape, width, height):
        self.canvas.delete("all")

        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()

        if shape == "Rectangle":
            rect_width = min(width * 10, canvas_width - 100)
            rect_height = min(height * 10, canvas_height - 100)
            self.canvas.create_rectangle(50, 50, 50 + rect_width, 50 + rect_height, outline="black", width=2)
        elif shape == "Circle":
           radius = min(width * 10, canvas_width // 2, canvas_height // 2)
           x = canvas_width // 2
           y = canvas_height // 2
           self.canvas.create_oval(x - radius, y - radius, x + radius, y + radius, outline="black", width=2)

if __name__ == "__main__":
    root = tk.Tk()
    app = GeometryCalculatorApp(root)
    root.mainloop()
