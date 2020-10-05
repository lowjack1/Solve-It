from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import sublime
import sublime_plugin

'''
Copy and Paste selinium module and urllib3 module of Python in
"sublime-text-3/Lib/Python3.3" folder of sublime-text3
'''


def process(string):

    # Get active file name
    filename = sublime.active_window().active_view().file_name()
    contestid, problem = string.strip().split()

    # Change executor_url according to your preference
    executor_url = "127.0.0.1:9222"  # change 9222 to the port you have used.
    url = "codeforces.com/contest/" + contestid + "/problem/" + problem

    _chrome_options = Options()
    _chrome_options.add_argument('disable-infobars')
    _chrome_options.add_argument("--start-maximized")
    _chrome_options.add_experimental_option("debuggerAddress", executor_url)
    try:
        driver = webdriver.Chrome(chrome_options=_chrome_options)
        driver.implicitly_wait(30)

        try:
            driver.get("http://" + url.rstrip())
            driver.find_element_by_name("sourceFile")
            driver.find_element_by_css_selector('input[type="file"]').clear()
            # Send File to Codeforces
            driver.find_element_by_css_selector(
                'input[type="file"]').send_keys(filename.rstrip())
            # Click on submit button
            driver.find_element_by_class_name("submit").click()
        except Exception:
            # In case Codeforces is too busy or File is untitled.
            sublime.error_message('Either Codeforces is too busy or File is Untitled.')
    except Exception:
        # In case Server is not active.
        sublime.error_message('Server is not active.')


class SolveItCommand(sublime_plugin.TextCommand):
    """
    Submit solution from sublime by getting contest ID and problem ID
    from the user
    """
    def run(self, edit):
        window = self.view.window()
        # Input Panel to get Contest ID and Problem ID from the user
        window.show_input_panel("Enter ContestID & ProblemID : ", "", self.on_done, self.on_change, self.on_cancel)

    def on_done(self, input_data):
        process(input_data)

    def on_change(self, input_data):
        pass

    def on_cancel(self):
        pass
