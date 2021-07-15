from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import mimetypes

import os
import json
import time

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(location_folder):
            src = location_folder + "/" + filename
            if os.path.isfile(src):
                a_list = filename.split(".")
                new_destination = location_folder + "/" + a_list[-1]
                if os.path.isdir(new_destination):
                    os.rename(src, f"{new_destination}/{filename}")
                else:
                    os.mkdir(new_destination)
                    os.rename(src, f"{new_destination}/{filename}")


username = str(input("Enter your computers username(you can type whoami in cmd.exe if you're not sure):"))
location_folder = f"/Users/{username}/Downloads"
folder_destinations = f"/Users/{username}/Downloads"
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, location_folder, recursive=True)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()

