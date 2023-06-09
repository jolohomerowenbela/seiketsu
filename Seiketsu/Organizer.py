import shutil
import os
import Seiketsu.SettingsAPI
from PyQt5.QtCore import *
from Seiketsu.OutputView import *
from Seiketsu.Methods.FilenameAnalysis import *
from Seiketsu.Methods.DocumentAnalysis import *

class FileScanner(QThread):
    file_scanned = pyqtSignal(str, str)
    scan_finished = pyqtSignal(str)
    progress = pyqtSignal(str, str, str)
    no_files = pyqtSignal(bool)
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
        self.file_count = 0
        self.filename_analyzer = FilenameAnalyzer()
        self.document_analyzer = DocumentAnalysis()

    def run(self):
        for folder in self.folders:
            self.enumerate_sortable_files(folder, self.get_size)
        
        if self.total_size == 0:
            self.no_files.emit(True)
            return

        for folder in self.folders:
            self.enumerate_sortable_files(folder, self.organize)

        self.scan_finished.emit(str(self.file_count))
    
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
        self.file_count += 1
    
    def organize(self, file_path):
        self.current_size += os.path.getsize(file_path)
        self.progress.emit(str(self.current_size), self.total_size, file_path)
        categorized_path = self.categorize(file_path)
        if categorized_path is not None:
            self.move_file(file_path, categorized_path)

        self.file_scanned.emit(file_path, categorized_path)
    
    def categorize(self, path):
        category = ""
        basename = os.path.basename(path)
        methods = Seiketsu.SettingsAPI.getMethods()
        if categ := self.filename_analyzer.scan(path):
            if "Filename Analysis" in methods:
                category = categ[1]
        elif categ := self.document_analyzer.scan(path):
            if "Document Analysis" in methods:
                category = categ[1]
                basename += category
                
                if Seiketsu.SettingsAPI.getRenameObscure():
                    basename = f"{category} - {basename}"
        else:
            return None
        
        
        default_folder = Seiketsu.SettingsAPI.getDefaultOutputFolder()
        return os.path.join(default_folder, category, basename)

    def move_file(self, path, categorized):
        folder = categorized.replace(os.path.basename(categorized), "")
        print(categorized)
        if not os.path.exists(folder):
            os.mkdir(folder)
        
        shutil.move(path, categorized)

class Organizer():
    def __init__(self, outputview: OutputView) -> None:
        self.outputview = outputview
  
    def organize(self, folders):
        self.scanner = FileScanner(folders)
        self.scanner.file_scanned.connect(self.append_to_updated_view)
        self.scanner.progress.connect(self.show_progress)
        self.scanner.scan_finished.connect(self.scan_finished)
        self.scanner.no_files.connect(self.no_files_found)
        self.scanner.start()
        
    def append_to_updated_view(self, file_path, category):
        self.outputview.table.append(f"{file_path} -->> {category}")
    
    def show_progress(self, progress, max, current_file):
        self.outputview.progressbar.setValue(int((int(progress)/ int(max)) * 100))
        self.outputview.current_file.setText(current_file)
    
    def scan_finished(self, file_count):
        self.outputview.progressbar.setFormat(f"Done! {file_count} files scanned.")
        self.outputview.current_file.setText("")
        self.outputview.save_button.setEnabled(True)
    
    def no_files_found(self, no_files: bool):
        if no_files:
            self.outputview.table.setText("No files found!")