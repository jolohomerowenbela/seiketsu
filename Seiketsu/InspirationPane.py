import requests
from bs4 import BeautifulSoup
import random
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from Seiketsu.SettingsAPI import getQuotesDisabled
from Seiketsu.Quotes import get_local_quotes

class InspirationPane(QWidget):
    def __init__(self, parent):
        super().__init__(parent)

        self.setStyleSheet(self.style())
        self.quotes = []
        self.text = ""
        font = QFont()
        font.setFamily("Inter Medium")
        font.setPointSize(12)

        # Check if quotes are enabled in settings
        if getQuotesDisabled():
            self.quotes = []
            self.text=""
            self.setStyleSheet("background:none;")
        else:
            # Retrieve quotes from the web page
            try:
                page = requests.get("https://www.brainyquote.com/topics/motivational-quotes")
                soup = BeautifulSoup(page.content, 'html.parser')
                quotes = soup.select(".m-brick")

                self.quotes = [quote.select_one("a").text for quote in quotes]
                
            except:
                self.quotes = []

            # Set a default quote if no quotes are found
            if not self.quotes:
                self.quotes = get_local_quotes()
            self.text=random.choice(self.quotes)

        self.label = QLabel(self, text=self.text)
        self.label.setFont(font)
        self.label.setObjectName("inspirational")
        self.label.setWordWrap(True)

        self.simpleLayout = QVBoxLayout(self)
        self.simpleLayout.addWidget(self.label)

    def style(self):
        return """
        #inspirational {
            background:none;
            color: #ffffff;
            border: 2px solid #666666;
            padding-top: 10px;
            padding-bottom: 10px;
            qproperty-alignment: AlignCenter;
        }
        """
