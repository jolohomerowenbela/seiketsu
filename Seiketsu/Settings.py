from PyQt5.QtCore import QSettings

def init():
    settings = QSettings("JYOH Software Solutions", "Seiketsu")
    if "automatic" not in settings.allKeys():
        settings.setValue("automatic", False)
    
    if "organization_methods" not in settings.allKeys():
        settings.setValue("organization_methods", ["Filename Analysis"])
    
    if "disable_quotes" not in settings.allKeys():
        settings.setValue("disable_quotes", False)
    
    return settings

def getAutomatic():
    settings = QSettings("JYOH Software Solutions", "Seiketsu")
    return settings.value("automatic", defaultValue=False, type=bool)

def setAutomatic(boolean: bool):
    settings = QSettings("JYOH Software Solutions", "Seiketsu")
    settings.setValue("automatic", boolean)

def getMethods():
    settings = QSettings("JYOH Software Solutions", "Seiketsu")
    return settings.value("organization_methods")

def setMethods(methods: list[str]):
    settings = QSettings("JYOH Software Solutions", "Seiketsu")
    settings.setValue("organization_methods", methods)

def getQuotesDisabled():
    settings = QSettings("JYOH Software Solutions", "Seiketsu")
    return settings.value("disable_quotes", defaultValue=False, type=bool)

def setQuotesDisabled(boolean: bool):
    settings = QSettings("JYOH Software Solutions", "Seiketsu")
    settings.setValue("disable_quotes", boolean)
