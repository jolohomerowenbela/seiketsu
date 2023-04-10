import os
from multiprocessing import Process

class Organizer():
    def __init__(self) -> None:
        user_profile = os.path.expandvars("%userprofile%")
        system_drive = user_profile[:3]
        self.invalid_files = [f"{system_drive}$Recycle.Bin",
                              f"{system_drive}Documents and Settings",
                              f"{system_drive}PerfLogs",
                              f"{system_drive}Program Files",
                              f"{system_drive}Program Files (x86)",
                              f"{system_drive}ProgramData",
                              f"{system_drive}Recovery",
                              f"{system_drive}System Volume Information",
                              f"{system_drive}Users\\All Users",
                              f"{system_drive}Users\\Default",
                              f"{system_drive}Users\\Default User",
                              f"{system_drive}Windows",
                              f"{user_profile}\\AppData",
                              f"{user_profile}\\Application Data",
                              f"{user_profile}\\Cookies",
                              f"{user_profile}\\Local Settings",
                              f"{user_profile}\\Documents\\My Music",
                              f"{user_profile}\\Documents\\My Pictures",
                              f"{user_profile}\\Documents\\My Videos"]

    def check_files(self, drives):
        self.done = False
        for drive in drives:
            self.enumerate_sortable_files(drive)
    
    def enumerate_sortable_files(self, drive):
        for path in os.listdir(drive):
            file_path = os.path.join(drive, path)
            try:
                if os.path.isfile(file_path) and file_path not in self.invalid_files and path[0] != ".":
                    with open("mess.txt", 'a', encoding="utf-8") as f:
                        f.write(file_path + "\n")
                elif os.path.isdir(file_path) and file_path not in self.invalid_files and path[0] != ".":
                    self.enumerate_sortable_files(file_path)
            except PermissionError:
                pass
        self.done = True
    
    def organize(self, drive_array):
        self.process = Process(target=self.check_files, args=(drive_array,), daemon=True)
        self.process.start()
        