import sublime
import sublime_plugin
import os
import sys
import time

''' Change this directory name by your python directory '''
pathToPython = "/home/light/.local/lib/python3.6/site-packages/"
sys.path.append(pathToPython)

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

def process(string):

	# Get active file name
	filename = sublime.active_window().active_view().file_name()
	contestid, problem = string.strip().split()

	# Change executor_url according to your preference
	executor_url = "127.0.0.1:9222" # change 9222 to the port you have used.
	url = "codeforces.com/contest/" + contestid + "/problem/" + problem
	
	_chrome_options = Options()
	_chrome_options.add_argument('disable-infobars')
	_chrome_options.add_argument("--start-maximized")
	_chrome_options.add_experimental_option("debuggerAddress", executor_url)
	try:
		driver = webdriver.Chrome(chrome_options = _chrome_options)
		driver.implicitly_wait(30)

		try:
			driver.get("http://" + url.rstrip())
			driver.find_element_by_name("sourceFile")
			driver.find_element_by_css_selector('input[type="file"]').clear()
			driver.find_element_by_css_selector('input[type="file"]').send_keys(filename.rstrip()) # Send File to Codeforces
			driver.find_element_by_class_name("submit").click() # Click on submit button
		except Exception as e:
			''' In case Codeforces is too busy or File is untitled.'''
			sublime.error_message('Either Codeforces is too busy or File is Untitled.')
	except Exception as e:
		''' In case Server is not active. '''
		sublime.error_message('Server is not active.')
class SolveItCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		window = self.view.window()
		''' Input Panel to get Contest ID and Problem Id from the user '''
		window.show_input_panel("Enter ContestID & ProblemID : ", "", self.on_done, self.on_change, self.on_cancel)

	def on_done(self, input_data):	
		process(input_data)		
		pass

	def on_change(self, input_data):
		pass

	def on_cancel(self):
		pass
