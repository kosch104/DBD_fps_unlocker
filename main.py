import tkinter as tk
from tkinter import messagebox
import getpass
import os


DEFAULT_PATH = f"C:/Users/{getpass.getuser()}/AppData/Local/DeadByDaylight"
SECONDARY_PATH = f"Saved/Config/WindowsNoEditor"
USERSETTINGS_PATH = f"GameUserSettings.ini"

def main():
    window = tk.Tk(className=" Dead By Daylight FPS Unlocker")

    greeting = tk.Label(text="Welcome. Please enter the path to your Local appdata folder. The preset value \nshould work for most users.", width=70, height=4)
    greeting.pack()

    path = tk.Entry(width=70)
    path.insert(0, DEFAULT_PATH)
    path.pack()

    info_fps = tk.Label(text="Please enter a number to limit the fps to:", width=70, height=2)
    info_fps.pack()

    fps = tk.Entry(width=20)
    fps.insert(0, 60)
    fps.pack()

    button = tk.Button(text="Update File", command=lambda: click(path.get(), fps.get()), width=20, height=2)
    button.pack()

    window.mainloop()

def click(path, value):
    if not value.isnumeric():
        messagebox.showinfo(title="Error", message="Please enter a valid number")
        return
    try:
        usersettings_path = os.path.join(path, SECONDARY_PATH, USERSETTINGS_PATH)
        print(path)
        print(SECONDARY_PATH)
        print(USERSETTINGS_PATH)
        print("Path: " + usersettings_path)
        with open(usersettings_path, "r") as f:
            lines = f.readlines()
        #print(lines)

        vsync_changed = False
        for i in range(0, len(lines)):
            if "bUseVSync=False\n" in lines[i]:
                print("bUseVsync value OK")
            elif lines[i] == "bUseVSync=True\n":
                lines[i] = "bUseVSync=False\n"
                vsync_changed = True
                print("bUseVsync value updated")
            if "FrameRateLimit" in lines[i]:
                lines[i] = f"FrameRateLimit={value}.000000\n"

        with open(usersettings_path, "w") as f:
            f.writelines(lines)

        print("Success")
        messagebox.showinfo(title="Success", message="Your config was successfully updated")
    except Exception as e:
        messagebox.showinfo(title="Error", message=f"There was an error: {e}")



if __name__ == "__main__":
    main()