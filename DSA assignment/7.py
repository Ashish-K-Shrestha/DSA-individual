import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.total_posts = 0
        self.followers = 0
        self.following = 0

    def increment_total_posts(self):
        self.total_posts += 1

    def increment_followers(self):
        self.followers += 1

    def increment_following(self):
        self.following += 1

    def follow(self, user):
        print(f"Following user: {user.username}")

users = {}

class App:
    WINDOW_WIDTH = 400
    WINDOW_HEIGHT = 300
    BOX_WIDTH = 200
    BOX_HEIGHT = 30

    def __init__(self):
        self.current_user = None
        self.setup_ui()

    def setup_ui(self):
        self.root = tk.Tk()
        self.root.title("Instagram")

        self.create_login_page()

    def create_login_page(self):
        self.clear_frame()

        username_label = tk.Label(self.root, text="Username:")
        username_field = tk.Entry(self.root, width=self.BOX_WIDTH)

        password_label = tk.Label(self.root, text="Password:")
        password_field = tk.Entry(self.root, show="*", width=self.BOX_WIDTH)

        login_button = tk.Button(self.root, text="Login", command=lambda: self.login(username_field.get(), password_field.get()))
        register_button = tk.Button(self.root, text="Register", command=lambda: self.register(username_field.get(), password_field.get()))

        username_label.pack()
        username_field.pack()
        password_label.pack()
        password_field.pack()
        login_button.pack()
        register_button.pack()

    def create_profile_page(self):
        self.clear_frame()

        username_label = tk.Label(self.root, text=f"Username: {self.current_user.username}")

        total_posts_label = tk.Label(self.root, text=f"Total Posts: {self.current_user.total_posts}   ")
        followers_label = tk.Label(self.root, text=f"Followers: {self.current_user.followers}   ")
        following_label = tk.Label(self.root, text=f"Following: {self.current_user.following}   ")

        upload_image_button = tk.Button(self.root, text="Upload Image", command=self.upload_image)
        follow_button = tk.Button(self.root, text="Follow", command=self.follow_user)

        logout_button = tk.Button(self.root, text="Logout", command=self.logout)

        username_label.pack()
        total_posts_label.pack()
        followers_label.pack()
        following_label.pack()
        upload_image_button.pack()
        follow_button.pack()
        logout_button.pack()

    def upload_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.png;*.jpeg")])
        if file_path:
            messagebox.showinfo("Success", f"Image uploaded successfully: {file_path}")
            self.current_user.increment_total_posts()
            self.update_labels()

    def follow_user(self):
        follow_username = simpledialog.askstring("Follow User", "Enter the username to follow:")
        if follow_username:
            if follow_username in users:
                follow_user = users[follow_username]
                self.current_user.follow(follow_user)
                self.current_user.increment_following()
                follow_user.increment_followers()
                self.update_labels()
                messagebox.showinfo("Success", f"You are now following {follow_username}")
            else:
                messagebox.showerror("Error", f"User '{follow_username}' not found.")

    def logout(self):
        self.current_user = None
        self.create_login_page()

    def login(self, username, password):
        if username in users:
            user = users[username]
            if user.password == password:
                self.current_user = user
                self.create_profile_page()
            else:
                messagebox.showerror("Error", "Incorrect password!")
        else:
            messagebox.showerror("Error", "User not found! Please register.")

    def register(self, username, password):
        if username in users:
            messagebox.showerror("Error", "Username already exists!")
        else:
            new_user = User(username, password)
            users[username] = new_user
            messagebox.showinfo("Success", "Registration successful!")

    def clear_frame(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def update_labels(self):
        self.root.children["!label2"].config(text=f"Total Posts: {self.current_user.total_posts}   ")
        self.root.children["!label3"].config(text=f"Followers: {self.current_user.followers}   ")
        self.root.children["!label4"].config(text=f"Following: {self.current_user.following}   ")

    def run(self):
        self.root.geometry(f"{self.WINDOW_WIDTH}x{self.WINDOW_HEIGHT}")
        self.root.mainloop()

if __name__ == "__main__":
    app = App()
    app.run()
