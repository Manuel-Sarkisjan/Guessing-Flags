import tkinter as tk
import random
import os

class FlagQuiz(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Flag Quiz")
        self.geometry("300x300")

        self.flag_label = tk.Label(self, image=None)
        self.flag_label.pack(pady=10)

        self.question_label = tk.Label(self, text="", font=("Arial", 12))
        self.question_label.pack(pady=5)

        self.option_buttons = []
        for i in range(4):
            button = tk.Button(self, text="", width=20, command=lambda i=i: self.check_answer(i))
            button.pack(pady=5)
            self.option_buttons.append(button)

        self.result_label = tk.Label(self, text="", font=("Arial", 12))
        self.result_label.pack(pady=10)

        self.score_label = tk.Label(self, text=f"Score: 0", font=("Arial", 12))
        self.score_label.pack(pady=5)

        self.restart_button = tk.Button(self, text="Restart", command=self.restart_game)
        self.restart_button.pack(pady=10)

        self.countries = [
            ("United States", "us.png"),
            ("France", "fr.png"),
            ("Armenia", "am.png"),
            ("Japan", "jp.png"),
            ("Spain", "es.png"),
            ("Brazil", "br.png"),
            ("Ecuador", "ec.png"),
            ("Panama", "pa.png"),
            ("Russia", "ru.png"),
            ("China", "cn.png")
        ]

        self.current_question = 0
        self.score = 0
        self.used_countries = set()

        self.show_question()

    def show_question(self):
        while True:
            country, flag_file = random.choice(self.countries)
            if country not in self.used_countries:
                self.used_countries.add(country)
                break

        flag_path = os.path.join("D:\\Github\\Projects\\Guess The Flag", flag_file)

        try:
            self.flag_image = tk.PhotoImage(file=flag_path)
            self.flag_label.config(image=self.flag_image)
        except tk.TclError as e:
            print(f"Error loading image: {e}")
            # Handle the error, e.g., display a placeholder image or skip the question
            return

        self.question_label.config(text="Which country's flag is this?")

        options = [country]
        while len(options) < 4:
            new_country = random.choice(self.countries)[0]
            if new_country not in options and new_country not in self.used_countries:
                options.append(new_country)
        random.shuffle(options)

        for i in range(4):
            self.option_buttons[i].config(text=options[i], command=lambda i=i, country=country: self.check_answer(i, country))

    def check_answer(self, index, correct_country):
        selected_option = self.option_buttons[index]['text']

        if selected_option == correct_country:
            self.result_label.config(text="Correct!")
            self.score += 1
        else:
            self.result_label.config(text=f"Incorrect. The answer is {correct_country}")

        self.score_label.config(text=f"Score: {self.score}")

        self.current_question += 1

        if self.current_question < len(self.countries):
            self.show_question()
        else:
            self.result_label.config(text=f"Quiz completed. Your final score is {self.score}/{len(self.countries)}")
            self.restart_button.pack()

    def restart_game(self):
        self.current_question = 0
        self.score = 0
        self.used_countries.clear()
        self.restart_button.pack_forget()
        self.show_question()

if __name__ == "__main__":
    app = FlagQuiz()
    app.mainloop()