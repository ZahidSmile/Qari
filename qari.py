# !/usr/bin/env python
from argparse import ArgumentParser
from selenium import webdriver
import os, importlib
from Main import Main
import time
from dotenv.main import load_dotenv
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.options import Options
import pathlib


class Qari:
    '''class variables'''
    __module = 'modules'
    __modules = None
    __failedModules = 0
    __executedModules = 0
    __arguments = None
    driver = None

    def __init__(self, arguments):
        '''constructor'''
        # setting arguments
        self.__arguments = arguments
        self.__setUp()
        self.__login()

    def __setUp(self):
        '''Function to set up initially'''
        # Load .ENV file
        load_dotenv()

        # Setting arguments to main class
        Main.arguments = self.__arguments

        # open selected browser
        self.__openBrowser()

        # register modules
        self.__registerModules()

    def __openBrowser(self):
        '''Opening Browser'''
        # Set Path For Chrome Driver
        Chrome = pathlib.Path("C:\chromedriver\chromedriver.exe")

        # Set Path For Gecko Driver
        FireFox = pathlib.Path("C:\geckodriver\geckodriver.exe")

        # Opening Chrome if Exist
        if Chrome.exists():
            op = webdriver.ChromeOptions()
            self.driver = webdriver.Chrome(service=Service("C:\chromedriver\chromedriver.exe"), options=op)

        # Opening Firefox if Exist
        elif FireFox.exists():
            options = Options()
            options.binary_location = r'C:\Users\zahid.ismail\AppData\Local\Mozilla Firefox\firefox.exe'
            self.driver = webdriver.Firefox(service=Service("C:\geckodriver\geckodriver.exe"), options=options)
            self.service = Service('C:\geckodriver\geckodriver.exe')
        # Closing the Script if both Does'nt Exist
        else:
            print("Chrome & Firefox Drivers Not Found")
            exit()

        self.driver.maximize_window()

    def __registerModules(self):
        '''Function To Register Modules'''
        m = self.__arguments.module_name + os.path.sep
        c = self.__arguments.class_name + '.py'
        self.__modules = [v if (v.find("__") < 0 and v.find(m) >= 0 and v.find(c) >= 0) else None for sl in
                        [[os.path.join(i[0], j) for j in i[2]] for i in os.walk(self.__module)] for v in sl]

    def __login(self):
        '''Function to login application'''
        self.driver.get(os.getenv("APP_URL"))
        # Opening Google
        time.sleep(3)
        try:
            time.sleep(1)
            self.driver.find_element(By.CSS_SELECTOR, 'div.Navigation div:nth-child(8)').click()
            time.sleep(5)
            self.driver.find_element(By.CSS_SELECTOR, 'div.Account.Teacher').click()
            # loading modules
            self.__loadModules()
            Main.line()
            Main.info("Module Execute " + str(self.__executedModules) + " & Fail " + str(self.__failedModules))
        except Exception as e:
            Main.error(str(e))

    def __loadModules(self):
        '''Function to load modules one b one and create'''
        try:
            if self.__modules:
                module = self.__modules.pop(0)
                if module and module.endswith(".py"):
                    try:
                        Main.info("Loading " + module)
                        getattr(importlib.import_module(module.replace('.py', '').replace(os.path.sep, '.')),
                                os.path.basename(module).replace('.py', ''))(self.driver)
                        Main.success("Module Execution Successful " + module)
                        self.__executedModules += 1
                    except Exception as e:
                        Main.error("Module Execution Failed " + module + " " + str(e))
                        self.__failedModules += 1
                    Main.line()
                self.__loadModules()
        except Exception as e:
            Main.error(e)

    def __del__(self):
        Main.closeFile()


if __name__ == '__main__':
    parser = ArgumentParser(description='This is Automation Life (qari) framework.')
    parser.add_argument("-m", "--module", dest="module_name", default='',
                        help="write a module name to perform automation only on that module.", metavar="MODULE NAME")
    parser.add_argument("-c", "--class", dest="class_name", default='',
                        help="write a class name to perform automation only on that class.", metavar="CLASS NAME")
    parser.add_argument("-q", "--quit", dest="verbose", default=True, action="store_false",
                        help="don't print status messages to standard output (stdout)")
    d = Qari(parser.parse_args())
