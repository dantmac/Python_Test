# Практическая работа 10
# Вариант 7

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Student #247397")
        self.root.geometry("500x400")

        # Вкладки
        self.tab_control = ttk.Notebook(self.root)

        # Вкладка 1: калькулятор
        self.tab1 = ttk.Frame(self.tab_control)
        self.tab_control.add(self.tab1, text="Калькулятор")

        # Вкладка 2: чекбоксы
        self.tab2 = ttk.Frame(self.tab_control)
        self.tab_control.add(self.tab2, text="Чекбоксы")

        # Вкладка 3: работа с текстом
        self.tab3 = ttk.Frame(self.tab_control)
        self.tab_control.add(self.tab3, text="Работа с текстом")

        self.tab_control.pack(expand=1, fill="both")

        self.create_calculator()
        self.create_checkboxes()
        self.create_text_operations()

    def create_calculator(self):
        self.num1_label = tk.Label(self.tab1, text="Первое число:")
        self.num1_label.pack(pady=5)

        self.num1_entry = tk.Entry(self.tab1)
        self.num1_entry.pack(pady=5)

        self.num2_label = tk.Label(self.tab1, text="Второе число:")
        self.num2_label.pack(pady=5)

        self.num2_entry = tk.Entry(self.tab1)
        self.num2_entry.pack(pady=5)

        self.operation_label = tk.Label(self.tab1, text="Операция:")
        self.operation_label.pack(pady=5)

        self.operation = ttk.Combobox(self.tab1, values=["+", "-", "*", "/"])
        self.operation.pack(pady=5)
        self.operation.set("+")

        self.result_label = tk.Label(self.tab1, text="Результат:")
        self.result_label.pack(pady=5)

        self.calculate_button = tk.Button(self.tab1, text="Вычислить", command=self.calculate)
        self.calculate_button.pack(pady=5)

    def calculate(self):
        try:
            num1 = float(self.num1_entry.get())
            num2 = float(self.num2_entry.get())
            operation = self.operation.get()

            if operation == "+":
                result = num1 + num2
            elif operation == "-":
                result = num1 - num2
            elif operation == "*":
                result = num1 * num2
            elif operation == "/":
                if num2 == 0:
                    messagebox.showerror("Ошибка", "На ноль делить нельзя!")
                    return
                result = num1 / num2

            self.result_label.config(text=f"Результат: {result}")

        except ValueError:
            messagebox.showerror("Ошибка", "Введите правильные числа.")

    def create_checkboxes(self):
        self.checkbox_var1 = tk.BooleanVar()
        self.checkbox_var2 = tk.BooleanVar()
        self.checkbox_var3 = tk.BooleanVar()

        self.checkbox1 = tk.Checkbutton(self.tab2, text="Первый", variable=self.checkbox_var1)
        self.checkbox1.pack(pady=5)

        self.checkbox2 = tk.Checkbutton(self.tab2, text="Второй", variable=self.checkbox_var2)
        self.checkbox2.pack(pady=5)

        self.checkbox3 = tk.Checkbutton(self.tab2, text="Третий", variable=self.checkbox_var3)
        self.checkbox3.pack(pady=5)

        self.submit_button = tk.Button(self.tab2, text="Выбрать", command=self.show_choice)
        self.submit_button.pack(pady=5)

    def show_choice(self):
        chosen_options = []
        if self.checkbox_var1.get():
            chosen_options.append("первый")
        if self.checkbox_var2.get():
            chosen_options.append("второй")
        if self.checkbox_var3.get():
            chosen_options.append("третий")

        if chosen_options:
            message = f"Вы выбрали: {', '.join(chosen_options)} чекбокс(ы)"
        else:
            message = "Ничего не выбрано"

        messagebox.showinfo("Выбор", message)

    def create_text_operations(self):
        self.load_button = tk.Button(self.tab3, text="Загрузить текст из файла", command=self.load_text)
        self.load_button.pack(pady=5)

        self.text_area = tk.Text(self.tab3, wrap="word", height=10)
        self.text_area.pack(pady=5)

        self.clear_button = tk.Button(self.tab3, text="Очистить текст", command=self.clear_text)
        self.clear_button.pack(pady=5)

    def load_text(self):
        filename = filedialog.askopenfilename(title="Выберите файл", filetypes=[("Text files", "*.txt")])
        if filename:
            with open(filename, "r", encoding="utf-8") as file:
                text = file.read()
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(tk.END, text)

    def clear_text(self):
        self.text_area.delete(1.0, tk.END)

root = tk.Tk()
app = App(root)
root.mainloop()

