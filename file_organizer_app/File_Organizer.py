# 📦 Import necessary tools (modules)
import os                      # This helps us work with folders and files
import shutil                  # This helps us move files
import tkinter as tk           # This helps us make the desktop window (GUI)
from tkinter import filedialog, messagebox  # These help us select folders and show messages

# 📁 Step 1: Define what types of files go into which folders
file_types = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif'],
    'Documents': ['.pdf', '.docx', '.txt', '.pptx'],
    'Videos': ['.mp4', '.mkv', '.avi'],
    'Music': ['.mp3', '.wav'],
    'Archives': ['.zip', '.rar'],
    'Others': []  # If file type doesn't match any above
}

# 🔁 Step 2: Function to sort and move files into folders
def organize_files(folder_path):
    if not folder_path:
        return  # If no folder is selected, do nothing

    # 📂 Create folders like Images, Documents, etc. if not already present
    for folder_name in file_types.keys():
        new_folder_path = os.path.join(folder_path, folder_name)
        if not os.path.exists(new_folder_path):
            os.mkdir(new_folder_path)  # Make folder

    # 📦 Now check each file in the folder
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if os.path.isdir(file_path):
            continue  # Skip if it's already a folder

        # 🧩 Get file extension (like .jpg, .pdf)
        _, ext = os.path.splitext(filename)
        ext = ext.lower()  # Make sure it's small letters
        moved = False  # This tracks if we moved the file

        # 📬 Try to move file into matching folder
        for folder_name, extensions in file_types.items():
            if ext in extensions:
                dest_path = os.path.join(folder_path, folder_name, filename)
                shutil.move(file_path, dest_path)  # Move the file
                moved = True
                break  # Stop checking more folders

        # 📦 If no folder matched, move file to 'Others'
        if not moved:
            dest_path = os.path.join(folder_path, 'Others', filename)
            shutil.move(file_path, dest_path)

    # ✅ Show a message when done
    messagebox.showinfo("Done", "Files organized successfully!")

# 📂 Step 3: Ask user to pick a folder from their computer
def choose_folder():
    folder_path = filedialog.askdirectory()  # Open folder picker
    organize_files(folder_path)              # Start sorting

# 🪟 Step 4: Create the main desktop window
app = tk.Tk()
app.title("📁 Auto File Organizer")  # App title
app.geometry("300x150")             # Window size

# ✉️ Step 5: Add a text label
label = tk.Label(app, text="Click to choose a folder to organize:")
label.pack(pady=10)  # Add space below the label

# 🔘 Step 6: Add a button that calls choose_folder
button = tk.Button(app, text="Choose Folder", command=choose_folder)
button.pack(pady=10)

# 🚀 Step 7: Run the app
app.mainloop()
