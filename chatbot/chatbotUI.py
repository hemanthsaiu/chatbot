import tkinter as tk
from tkinter import ttk

def on_translate_click():
    english_text = english_input.get()
    french_text = translate_english_to_french(english_text)
    french_output.delete(0, tk.END)
    french_output.insert(tk.END, french_text)

# Main application window
app = tk.Tk()
app.title("English to French Translator")

# Create the input frame
input_frame = ttk.Frame(app, padding="10")
input_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Create the output frame
output_frame = ttk.Frame(app, padding="10")
output_frame.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Create the widgets
english_label = ttk.Label(input_frame, text="English Text:")
english_input = ttk.Entry(input_frame, width=50)

translate_button = ttk.Button(input_frame, text="Translate", command=on_translate_click)

french_label = ttk.Label(output_frame, text="French Text:")
french_output = ttk.Entry(output_frame, width=50)

# Layout the widgets
english_label.grid(row=0, column=0)
english_input.grid(row=0, column=1)

translate_button.grid(row=1, column=0, columnspan=2)

french_label.grid(row=2, column=0)
french_output.grid(row=2, column=1)

# Run the application
app.mainloop()
