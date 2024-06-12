import tkinter as tk
import re

class PasswordStrengthAssessor:
    def __init__(self):
        self.password = ""
        self.score = 0

    def set_password(self, password):
        self.password = password
        self.score = 0

    def assess_strength(self):
        feedback = ""

        # Check password length
        if len(self.password) < 8:
            feedback += "Password is too short. It should be at least 8 characters long.\n"
        elif len(self.password) >= 8 and len(self.password) <= 12:
            self.score += 1
        else:
            self.score += 2

        # Check for uppercase letters
        if re.search(r"[A-Z]", self.password):
            self.score += 1
        else:
            feedback += "Password should contain at least one uppercase letter.\n"

        # Check for lowercase letters
        if re.search(r"[a-z]", self.password):
            self.score += 1
        else:
            feedback += "Password should contain at least one lowercase letter.\n"

        # Check for numbers
        if re.search(r"\d", self.password):
            self.score += 1
        else:
            feedback += "Password should contain at least one number.\n"

        # Check for special characters
        if re.search(r"[!@#$%^&*()_+=-{};:'<>,./?]", self.password):
            self.score += 1
        else:
            feedback += "Password should contain at least one special character.\n"

        # Determine password strength
        if self.score < 3:
            feedback += "Password is weak. It should contain a mix of characters, numbers, and special characters.\n"
        elif self.score == 3 or self.score == 4:
            feedback += "Password is medium strength. It's a good start, but consider adding more complexity.\n"
        else:
            feedback += "Password is strong. Good job!\n"

        return feedback

def main():
    assessor = PasswordStrengthAssessor()
    root = tk.Tk()
    root.title("Password Strength Assessor")
    root.configure(bg="lightblue")

    frame = tk.Frame(root, bg="lightgray")
    frame.pack(fill=tk.BOTH, expand=True)

    password_label = tk.Label(frame, text="Enter a password:", bg="lightgray")
    password_label.pack()

    password_entry = tk.Entry(frame, bg="white")
    password_entry.pack()

    def assess_password():
        password = password_entry.get()
        assessor.set_password(password)
        feedback = assessor.assess_strength()
        result_label.config(text=feedback)

    assess_button = tk.Button(frame, text="Submit", command=assess_password, bg="lightblue")
    assess_button.pack()

    result_label = tk.Label(frame, text="", bg="lightgray")
    result_label.pack()

    root.mainloop()

if __name__ == "__main__":
    main()