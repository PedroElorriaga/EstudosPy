import os
import sys
file_path = os.path.dirname(__file__)
folder_pages_path = os.path.join(file_path, '..')
sys.path.append(folder_pages_path)

from BasePage import BasePage

class YoutubePage(BasePage):
    def __init__(self, webDriver):
        super().__init__(webDriver)

        