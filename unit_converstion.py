import tkinter as tk
def cm_to_feet():
    try:
        cm = float(cm_entry.get())
        feet = cm * 0.0328084
        result_label.config(text=f"{feet} feet")
    except ValueError:
        result_label.config(text="Invalid input")

def feet_to_inches():
    try:
        feet = float(feet_entry.get())
        inches = feet * 12
        result_label.config(text=f"{inches} inches")
    except ValueError:
        result_label.config(text="Invalid input")

def sqft_to_sqm():
    try:
        sqft = float(sqft_entry.get())
        sqm = sqft * 0.092903
        result_label.config(text=f"{sqm} square meters")
    except ValueError:
        result_label.config(text="Invalid input")

def sqft_to_hectares():
    try:
        sqft = float(sqft_entry.get())
        hectares = sqft * 0.0000092903
        result_label.config(text=f"{hectares} hectares")
    except ValueError:
        result_label.config(text="Invalid input")

root = tk.Tk()
root.title("Unit Conversion Tool")

cm_label = tk.Label(root, text="Centimeters:")
cm_label.grid(row=0, column=0)
cm_entry = tk.Entry(root)
cm_entry.grid(row=0, column=1)
convert_cm_button = tk.Button(root, text="Convert to Feet", command=cm_to_feet)
convert_cm_button.grid(row=0, column=2)

feet_label = tk.Label(root, text="Feet:")
feet_label.grid(row=1, column=0)
feet_entry = tk.Entry(root)
feet_entry.grid(row=1, column=1)
convert_feet_button = tk.Button(root, text="Convert to Inches", command=feet_to_inches)
convert_feet_button.grid(row=1, column=2)

sqft_label = tk.Label(root, text="Square Feet:")
sqft_label.grid(row=2, column=0)
sqft_entry = tk.Entry(root)
sqft_entry.grid(row=2, column=1)
convert_sqft_button = tk.Button(root, text="Convert to Sqm", command=sqft_to_sqm)
convert_sqft_button.grid(row=2, column=2)

convert_hectare_button = tk.Button(root, text="Convert to Hectares", command=sqft_to_hectares)
convert_hectare_button.grid(row=3, column=0)

result_label = tk.Label(root, text="")
result_label.grid(row=4, column=0, columnspan=3)

root.mainloop()
