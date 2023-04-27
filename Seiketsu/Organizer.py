import os
import time
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from Seiketsu.OutputView import *
from Seiketsu.Methods.FilenameAnalysis import *

class FileScanner(QThread):
    file_scanned = pyqtSignal(str, str)
    scan_finished = pyqtSignal()
    progress = pyqtSignal(str, str, str)
    user_profile = os.path.expandvars("%userprofile%")
    system_drive = user_profile[:3]
    invalid_files = [
        f"{system_drive}$Recycle.Bin",
        f"{system_drive}Documents and Settings",
        f"{system_drive}PerfLogs",
        f"{system_drive}Program Files",
        f"{system_drive}Program Files (x86)",
        f"{system_drive}ProgramData",
        f"{system_drive}Recovery",
        f"{system_drive}System Volume Information",
        f"{system_drive}Users/All Users",
        f"{system_drive}Users/Default",
        f"{system_drive}Users/Default User",
        f"{system_drive}Windows",
        f"{user_profile}/AppData",
        f"{user_profile}/Application Data",
        f"{user_profile}/Cookies",
        f"{user_profile}/Local Settings",
        f"{user_profile}/Documents/My Music",
        f"{user_profile}/Documents/My Pictures",
        f"{user_profile}/Documents/My Videos"
    ]

    def __init__(self, folders):
        super().__init__()
        self.folders = folders
        self.total_size = 0
        self.current_size = 0
        self.filename_analyzer = FilenameAnalyzer()

    def run(self):
        for folder in self.folders:
            self.enumerate_sortable_files(folder, self.get_size)

        for folder in self.folders:
            self.enumerate_sortable_files(folder, self.organize)

        self.scan_finished.emit()
    
    def enumerate_sortable_files(self, drive, func):
        try:
            for path in os.listdir(drive):
                file_path = os.path.join(drive, path)
                try:
                    if os.path.isfile(file_path) and file_path not in self.invalid_files and path[0] != ".":
                        func(file_path)
                    elif os.path.isdir(file_path) and file_path not in self.invalid_files and path[0] != ".":
                        self.enumerate_sortable_files(file_path, func)
                except PermissionError:
                    pass
        except (FileNotFoundError, FileExistsError):
            pass
    
    def get_size(self, file_path):
        size = int(self.total_size)
        size += os.path.getsize(file_path)
        self.total_size = str(size)
    
    def organize(self, file_path):
        self.current_size += os.path.getsize(file_path)
        self.progress.emit(str(self.current_size), self.total_size, file_path)
        category = self.categorize(file_path)
        self.move_file(file_path, category)
        self.file_scanned.emit(file_path, category)
    
    def categorize(self, path):
        category = ""
        if categ := self.filename_analyzer.scan(path):
            category = categ[1]
        return os.path.join(self.user_profile, category, os.path.basename(path))

    def move_file(self, path, category):
        pass

class Organizer():
    def __init__(self, outputview: OutputView) -> None:
        self.outputview = outputview
  
    def organize(self, folders):
        self.scanner = FileScanner(folders)
        self.scanner.file_scanned.connect(self.appediendo)
        self.scanner.progress.connect(self.printprog)
        self.scanner.start()
        
    def appediendo(self, file_path, category):
        self.outputview.table.append(f"{file_path} -->> {category}")
    
    def printprog(self, progress, max, current_file):
        self.outputview.progressbar.setValue(int((int(progress)/ int(max)) * 100))
        self.outputview.current_file.setText(current_file)