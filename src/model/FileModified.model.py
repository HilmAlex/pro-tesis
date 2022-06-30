import os
import time
import traceback

class FileModified():
    def __init__(self, file_path, callback):
        self.file_path = file_path
        self.callback = callback
        self.modified_on = os.path.getmtime(file_path)
    
    def start(self):
        try:
            while (True):
                time.sleep(0.5)
                modified = os.path.getmtime(self.file_path)

                if modified != self.modified_on:
                    self.modified_on = modified
                    if self.callback():
                        break
        except Exception as e:
            print(traceback.format_exc())