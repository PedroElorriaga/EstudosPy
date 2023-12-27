import os
import sys
file_path = os.path.dirname(__file__)
folder_pages_path = os.path.join(file_path, '..')
sys.path.append(folder_pages_path)

from selenium import webdriver
from Pages.YoutubePage import YoutubePage
import unittest


class YoutubeTest(unittest.TestCase):

    def setUp(self):
        self.webdriver = webdriver.Chrome()
        