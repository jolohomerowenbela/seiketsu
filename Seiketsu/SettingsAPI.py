from PyQt5.QtCore import QSettings
import os

user_profile = os.path.expandvars("%userprofile%")
system_drive = user_profile[:3]
default_folders = [
    f"{user_profile}Downloads",
    f"{user_profile}OneDrive\Documents",
    f"{user_profile}Desktop",
    f"{user_profile}Videos",
    f"{user_profile}OneDrive\Pictures"
]

def init():
    default_folder = f"{user_profile}\Organized"
    
    if not os.path.exists(default_folder):
        os.mkdir(default_folder)
    
    settings = QSettings("JYOH Software Solutions", "Seiketsu")
    if "automatic" not in settings.allKeys():
        settings.setValue("automatic", False)
    
    if "organization_methods" not in settings.allKeys():
        settings.setValue("organization_methods", ["Filename Analysis"])
    
    if "rename_obscure" not in settings.allKeys():
        settings.setValue("rename_obscure", False)
    
    if "disable_quotes" not in settings.allKeys():
        settings.setValue("disable_quotes", False)
    
    if "interval" not in settings.allKeys():
        settings.setValue("interval", "1 week")
    
    if "folders" not in settings.allKeys():
        settings.setValue("folders", default_folders)
    
    if "default_output" not in settings.allKeys():
        settings.setValue("default_output", f"{user_profile}\Organized")
    
    return settings

def getScannableFolders():
    settings = QSettings("JYOH Software Solutions", "Seiketsu")
    return settings.value("folders", defaultValue=default_folders)

def setScannableFolders(folders: list[str]):
    settings = QSettings("JYOH Software Solutions", "Seiketsu")
    settings.setValue("folders", folders)

def getMethods():
    settings = QSettings("JYOH Software Solutions", "Seiketsu")
    return settings.value("organization_methods")

def setMethods(methods: list[str]):
    settings = QSettings("JYOH Software Solutions", "Seiketsu")
    settings.setValue("organization_methods", methods)

def getRenameObscure():
    settings = QSettings("JYOH Software Solutions", "Seiketsu")
    return settings.value("rename_obscure", defaultValue=False, type=bool)

def setRenameObscure(boolean: bool):
    settings = QSettings("JYOH Software Solutions", "Seiketsu")
    settings.setValue("rename_obscure", boolean)

def getQuotesDisabled():
    settings = QSettings("JYOH Software Solutions", "Seiketsu")
    return settings.value("disable_quotes", defaultValue=False, type=bool)

def setQuotesDisabled(boolean: bool):
    settings = QSettings("JYOH Software Solutions", "Seiketsu")
    settings.setValue("disable_quotes", boolean)

def getDefaultOutputFolder():
    settings = QSettings("JYOH Software Solutions", "Seiketsu")
    return settings.value("default_output", defaultValue=f"{user_profile}\Organized", type=str)

def setDefaultOutputFolder(output: str):
    settings = QSettings("JYOH Software Solutions", "Seiketsu")
    settings.setValue("default_output", output)

