import requests
from bs4 import BeautifulSoup
import random
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class InspirationPane(QWidget):
    def __init__(self, parent):
        super().__init__(parent)

        self.setStyleSheet(self.style())

        font = QFont()
        font.setFamily("Inter Medium")
        font.setPointSize(12)

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
            self.quotes = [
                "You're braver than you believe, and stronger than you seem, and smarter than you think.",
                "Be the change that you wish to see in the world.",
                "In the end, it's not the years in your life that count. It's the life in your years.",
                "Success is not final, failure is not fatal: it is the courage to continue that counts.",
                "Believe you can and you're halfway there.",
                "Happiness is not something ready made. It comes from your own actions.",
                "If you can't fly then run, if you can't run then walk, if you can't walk then crawl, but whatever you do you have to keep moving forward."
            ]

        self.label = QLabel(self, text=random.choice(self.quotes))
        self.label.setFont(font)
        self.label.setObjectName("inspirational")

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