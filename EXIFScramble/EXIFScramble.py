import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import os
import random

class MetadataEditor:
    def __init__(self, master):
        self.master = master
        self.master.title("Metadaten-Editor")
        self.master.geometry("300x150")

        self.path_label = tk.Label(self.master, text="Dateipfad:")
        self.path_label.pack()

        self.path_entry = tk.Entry(self.master)
        self.path_entry.pack()

        self.load_button = tk.Button(self.master, text="Datei laden", command=self.load_file)
        self.load_button.pack()

        self.delete_button = tk.Button(self.master, text="Metadaten löschen", command=self.delete_metadata)
        self.delete_button.pack()

        self.edit_button = tk.Button(self.master, text="Metadaten bearbeiten", command=self.edit_metadata)
        self.edit_button.pack()

    def load_file(self):
        file_path = filedialog.askopenfilename()
        self.path_entry.delete(0, tk.END)
        self.path_entry.insert(0, file_path)

    def delete_metadata(self):
        file_path = self.path_entry.get()
        if os.path.isfile(file_path):
            os.system(f"exiftool -all= {file_path}")
            messagebox.showinfo("Information", "Metadaten wurden entfernt.")
        else:
            messagebox.showerror("Fehler", "Ungültiger Dateipfad.")

    def edit_metadata(self):
        file_path = self.path_entry.get()
        if os.path.isfile(file_path):
            random_metadata = self.generate_random_metadata()
            os.system(f"exiftool {random_metadata} {file_path}")
            messagebox.showinfo("Information", "Metadaten wurden bearbeitet.")
        else:
            messagebox.showerror("Fehler", "Ungültiger Dateipfad.")

    def generate_random_metadata(self):
        metadata = [
            "-EXIF:ImageWidth=" + str(random.randint(100, 2000)),
            "-EXIF:ImageHeight=" + str(random.randint(100, 2000)),
            "-EXIF:Make=" + random.choice(["Apple", "Canon", "Nikon", "Sony", "Samsung"]),
            "-EXIF:Model=" + random.choice(["iPhone", "EOS5D", "D850", "Alpha7", "GalaxyS21"]),
            "-EXIF:Software=" + random.choice(["Photoshop", "Lightroom", "GIMP", "Snapseed", "Canva"]),
            "-XMP:CreatorTool=" + random.choice(["AdobePhotoshop", "LightroomClassic", "CaptureOne", "GIMP", "Canva"]),
            "-XMP:Rating=" + str(random.randint(0, 5)),
            "-IPTC:Keywords=" + ",".join([random.choice(["Nature", "Travel", "Food", "Portrait", "Abstract"]) for _ in range(3)])
        ]
        return " ".join(metadata)

root = tk.Tk()
app = MetadataEditor(root)
root.mainloop()