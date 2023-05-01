import requests
from bs4 import BeautifulSoup
import random
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import Seiketsu.SettingsAPI as SettingAPI
import Seiketsu.Quotes as quote_library

class QuoteScraper(QThread):
    text_chosen = pyqtSignal(str)
    def __init__(self):
         super().__init__()
         self.quotes = []
    def run(self):
        # Retrieve quotes from the web page
        try:
            page = requests.get("https://www.brainyquote.com/topics/motivational-quotes")
            soup = BeautifulSoup(page.content, 'html.parser')
            quotes = soup.select(".m-brick")

            self.quotes = [quote.select_one("a").text for quote in quotes]
        except :
            self.quotes = []

        # Set a default quote if no quotes are found
        if not self.quotes:
            self.quotes = quote_library.get_local_quotes()

        self.text_chosen.emit(random.choice(self.quotes))

class InspirationPane(QWidget):
    def __init__(self, parent):
        super().__init__(parent)

        self.setStyleSheet(self.style())
        self.quotes = []
        self.text = ""
        font = QFont()
        font.setFamily("Inter Medium")
        font.setPointSize(12)

        self.label = QLabel(self, text="Loading quote for a while...")
        self.label.setFont(font)
        self.label.setObjectName("inspirational")
        self.label.setWordWrap(True)
        
        self.quote_scraper = QuoteScraper()
        self.quote_scraper.text_chosen.connect(lambda text: self.label.setText(text))
        self.quote_scraper.start()
        
        # Check if quotes are enabled in settings
        self.hide_quote(SettingAPI.getQuotesDisabled())

        self.simpleLayout = QVBoxLayout(self)
        self.simpleLayout.addWidget(self.label)

    def hide_quote(self, state: bool):
        self.label.setHidden(state)

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
