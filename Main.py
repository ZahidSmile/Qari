import datetime, os, random, string

class Main:
    arguments = None
    file = None
    driver = None

    @staticmethod
    def __writeLog(message):
        '''Function to write logs'''
        try:
            if not Main.file:
                path = 'logs'

                if not os.path.exists(path):
                    os.makedirs(path)

                filename = 'qari-' + datetime.datetime.now().strftime('%Y-%m-%d-%H-%M') + '.log'
                Main.file = open(os.path.join(path, filename), 'w+')

            Main.file.write(message + os.linesep)
        except Exception as e:
            print("ERROR: " + str(e))

    @staticmethod
    def closeFile():
        '''Close log file'''
        if Main.file:
            Main.file.close()

    @staticmethod
    def __log(type, message):
        '''Function to Print and write logs'''
        try:
            message = "[" + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + "] qari." + type + ": " + str(
                message)

            if Main.arguments.verbose:
                print(message)

            Main.__writeLog(message)

        except Exception as e:
            Main.__log("ERROR", str(e))

    @staticmethod
    def info(message):
        '''Function to show and log info message'''
        Main.__log('INFO', message)

    @staticmethod
    def error(message):
        '''Function to show and log error message'''
        Main.__log('ERROR', message)

    @staticmethod
    def success(message):
        '''Function to show and log success message'''
        Main.__log('SUCCESS', message)

    @staticmethod
    def line():
        '''Function to show and log success message'''
        Main.__log('LINE', '__________________________________________________________________________________________')

    @staticmethod
    def element_exists_by_css_selector(css_selector):
        try:
            element = Main.driver.find_element_by_css_selector(css_selector)
            return True
        except Exception as e:
            Main.error('CSS Selector: ' + css_selector)
            Main.error(str(e))
            return False

    @staticmethod
    def random_string(string_length=10):
        '''Generate a random string of fixed length '''
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(string_length))
