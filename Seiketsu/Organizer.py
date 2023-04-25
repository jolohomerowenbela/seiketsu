import os
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class FileScanner(QThread):
    file_scanned = pyqtSignal(str, str)
    user_profile = os.path.expandvars("%userprofile%")
    system_drive = user_profile[:3]
    invalid_files = [f"{system_drive}$Recycle.Bin",
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
    def __init__(self, folders):
        super().__init__()
        self.folders = folders
    def run(self):
        for folder in self.folders:
            self.enumerate_sortable_files(folder)
    
    def enumerate_sortable_files(self, drive):
        for path in os.listdir(drive):
            file_path = os.path.join(drive, path)
            try:
                if os.path.isfile(file_path) and file_path not in self.invalid_files and path[0] != ".":
                    category = self.categorize(file_path)
                    self.file_scanned.emit(file_path, category)
                elif os.path.isdir(file_path) and file_path not in self.invalid_files and path[0] != ".":
                    self.enumerate_sortable_files(file_path)
            except PermissionError:
                pass
    
    def categorize(self, path):
        print(path)
        return path

class Organizer():   
    def organize(self, folders, outputview):
        self.outputview = outputview
        self.scanner = FileScanner(folders)
        self.scanner.file_scanned.connect(self.appediendo)
        self.scanner.start()
        
    def appediendo(self, file_path, category):
        self.outputview.table.append(f"{file_path} -->> {category}")