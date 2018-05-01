__author__ = 'khaile'
import os
from time import sleep
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from appium.webdriver.common.mobileby import MobileBy

class Device(object):
    def __init__(self , driver=None):
        self.driver = driver
        self.action = TouchAction(self.driver)

    def quit(self):
        self.driver.quit()

    def findElement(self, strategy, value):
        """

        :param strategy: method such as ID, Class name, or xpath, etc...
        :param value: the search value that goes with the strategy
        :return: a web object
        """
        try:
            element = self.driver.find_element(strategy, value)
            return element
        except:
            return None

    def findElements(self, strategy, value):
        """

        :param strategy: method such as ID, Class name, or xpath, etc...
        :param value: the search value that goes with the strategy
        :return: a list of web objects
        """
        elements = []
        try:
            elements = self.driver.find_elements(strategy, value)
            return elements
        except:
            return elements
    def getStrategy(self):
        """
        :return: return proper strategy class based on whether tests run on desktop or mobile
        """
        if self.isMobile():
            return MobileBy
        else:
            return By

    def isIos(self):
        """
        :return: the boolean value of whether we are on an iOS platform
        """
        if self.driver.desired_capabilities['platformName'] == 'iOS':
            return True
        else:
            return False

    def isAndroid(self):
        """
        :return: the boolean value of whether we are on an Android platform
        """
        if self.driver.desired_capabilities['platformName'] == 'Android':
            return True
        else:
            return False

    def isWeb(self):
        """
        :return: boolean value if the current automated target is a native app.
        False will be returned if it is a web app for example.
        """
        if self.driver.desired_capabilities.has_key('app'):
            return False
        else:
            return True

    def isFirefox(self):
        """
        :return: boolean value if the current automated browser target is Firefox
        """
        if self.driver.desired_capabilities.get('browserName') == 'firefox':
            return True
        else:
            return False

    def isMicrosoftEdge(self):
        """
        :return: boolean value if the current automated browser target is Microsoft Edge
        """
        if self.driver.desired_capabilities.get('browserName') == 'MicrosoftEdge':
            return True
        else:
            return False

    def isSafari(self):
        """
        :return: boolean value if the current automated browser target is Safari
        """
        if self.driver.desired_capabilities.get('browserName') == 'safari':
            return True
        else:
            return False

    def isChromium(self):
        """
        :return: boolean value if the current automated browser target is Chrome on Android
        """
        if self.driver.current_context == 'CHROMIUM':
            return True
        else:
            return False

    def isInternetExplorer(self):
        """
        :return: boolean value if the current automated browser target is IE
        """
        if self.driver.desired_capabilities.get('browserName') == 'internet explorer':
            return True
        else:
            return False

    def isMobile(self):
        """
        :return: boolean value if the current automated target is a mobile.
        False will be returned if it is a desktop.
        """
        if self.driver.desired_capabilities.has_key('platformName'):
            if self.driver.desired_capabilities.get('platformName') in ['iOS', 'Android']:
                return True
            else:
                return False
        else:
            return False

    def isHybrid(self):
        """
        :return: boolean value if the current automated target is a hybrid app (webview inside a native app)
        """
        if not self.isWeb() and self.hasWebView():
            return True
        else:
            return False

    def swipe(self, startx, starty, deltax, deltay, duration=500):
        """
        Swipe across the screen or element.
        If phone rotates, x and y rotate with it.

        For the start and end points, if the values are less than one,
        then it is taken as a proportion of the element or screen.
        For example, 0.5 would be considered the center of the element or screen.

        duration is time in seconds.

        :param startx: Starting position on the horizontal axis.
        :param starty: Starting position on the vertical axis.
        :param deltax: change in position on the horizontal axis.
        :param deltay: change in position on the vertical axis.
        :param duration: (optional) Number of milisecond to do the swipe (shorter is faster).

        """
        size = self.getWindowSize()
        height = size[0]
        width = size[1]
        startx = width*startx
        starty = height*starty
        endx = width*deltax
        endy = height*deltay

        if not self.isCurrentContextNative():
            self.switchToNative()
        self.driver.swipe(startx, starty, endx, endy, duration)

    def swipeUp(self, startx=0.5, starty=0.8, deltax=0 , deltay=-0.5, duration=250):
        """
        Pre-defined swipe action starting near the bottom of the screen to the top
        """
        if self.isAndroid():
            deltay=deltay*(-1)

        self.swipe(startx, starty, deltax, deltay, duration)

    def swipeDown(self, startx=0.5, starty=0.3, deltax=0, deltay=0.5, duration=250):
        """
        Pre-defined swipe action starting from the top of the screen to the bottom
        """
        if self.isAndroid():
            deltay=deltay*(-1)

        self.swipe(startx, starty, deltax, deltay, duration)

    def swipeLeft(self, startx=0.8, starty=0.5, deltax=-0.7, deltay=0, duration=250):
        """
        Pre-defined swipe action starting from left to right in the middle of the screen.
        """
        self.swipe(startx, starty, deltax, deltay, duration)

    def swipeRight(self, startx=0.2, starty=0.5, deltax=0.7, deltay=0, duration=250):
        """
        Pre-defined swipe action starting from right to left in the middle of the screen.
        """
        self.swipe(startx, starty, deltax, deltay, duration)


    def bezelSwipeLeft(self, starty=None):
        """
        swipes in from left, halfway down the screen
        optional params: you can include starty to do a straight across swipe at that Y coord
        """
        if (starty==None):
            starty=.5
            deltay=0

        self.swipe(0.001, starty, .8, deltay)

    def bezelSwipeRight(self, starty=None):
        """
        swipes in from right, halfway down the screen
        optional params: you can include starty to do a straight across swipe at that Y coord
        """
        if (starty==None):
            starty=.5
            deltay=0

        self.swipe(.9999, starty, -.8, deltay)

    def bezelSwipeTop(self, startx=None):
        """
        swipes in from top, halfway across top of the screen
        optional params: you can include startx to do a straight vertical swipe at that x coord
        """
        if (startx==None):
            startx=.5
            deltax=0

        self.swipe(startx, 0.001, deltax, .8)

    def bezelSwipeBottom(self, startx=None):
        """
        swipes in from bottom, halfway across top of the screen
        optional params: you can include startx to do a straight vertical swipe at that x coord

        """
        if (startx==None):
            startx=.5
            deltax=0

        self.swipe(startx, .9999, deltax, -.8)

    def tapOnScreen(self, *args):
        """
        This method, on the WebDriver object, allows for tapping with multiple fingers, simply by passing in an array of x-y coordinates to tap.
        # set up array of two coordinates
        positions = []
        positions.append((0.5,0.7))
        positions.append((0.4, 0.8))

        self.driver.tap(positions)


        By default, this will be one finger tap in the middle of the screen
        """
        positions = []
        if not(args):
            positions.append((0.5, 0.5))

        else:
            for arg in args:
                positions.append(arg)

        self.driver.tap(positions)


    def scroll(self, origin_el, destination_el):
        """
        Scrolls from one element to another. Both elements need to be in view.
        :Args:
         - originalEl - the element from which to being scrolling
         - destinationEl - the element to scroll to
        :Usage:
            driver.scroll(el1, el2)
        """
        self.driver.scroll(origin_el, destination_el)


    def getCurrentOrientation(self):
        """
        Returns the current orientation of the device.  Possible values
        are: LANDSCAPE or PORTRAIT.
        """
        return self.driver.orientation

    def __setOrientation(self, orientation):
        """
        Sets the current orientation of the device.
        :param orientation: LANDSCAPE or PORTRAIT.
        """

        current = self.driver.orientation
        if (current != orientation):
            self.driver.orientation = orientation
    def rotateToPortrait(self):
        self.__setOrientation('PORTRAIT')

    def rotateToLandscape(self):
        self.__setOrientation('LANDSCAPE')

    def dismissKeyboard(self, key_name=None, key=None, strategy=None):
        """
        Hides the software keyboard on the device. In iOS, use `key_name` to press
        a particular key, or `strategy`. In Android, no parameters are used.
        :Args:
         - key_name - key to press
         - strategy - strategy for closing the keyboard (e.g., `tapOutside`)
        """
        if self.isAndroid():
            self.driver.hide_keyboard(key_name, key, strategy)
        if self.isIos():
            if self.isWeb():
                sleep(2)
                self.switchToNative()
                sleep(2)
                try:
                    self.driver.find_element(MobileBy.ACCESSIBILITY_ID, 'Done').click()
                except:
                    try:
                        self.driver.find_element(MobileBy.ACCESSIBILITY_ID, 'Hide keyboard').click()
                    except:
                        pass
                self.switchToWebview()
            else:
                self.driver.hide_keyboard(key_name="Done")
    def tapDeleteKey(self):
        if self.isIos():
            self.driver.find_element_by_id('delete').click()
        else:
            self.driver.press_keycode(67)

    def tapHardwareBackKey(self):
        """
        Presses on the device's hardware back button Android only.
        """
        self.driver.press_keycode(4)

    # def save_screenshot(self, filename):
    #     """
    #     Gets the screenshot of the current window. Returns False if there is
    #        any IOError, else returns True. Use full paths in your filename.
    #
    #     :Args:
    #      - filename: The full path you wish to save your screenshot to.
    #
    #     :Usage:
    #         driver.get_screenshot_as_file('/Screenshots/foo.png')
    #     """
    #     self.driver.save_screenshot(filename)

    def lockDevice(self, seconds):
        """Lock the device for a certain period of time. Android and iOS 8.0 only.
        :Args:
         - the duration to lock the device, in seconds
        """
        if self.isIos():
            self.driver.lock(seconds)
        else:
            os.system('adb shell input keyevent 26')
            sleep(seconds)
            os.system('adb shell input keyevent 26')


    def getWindowSize(self):
        """
        Gets window size.
        :return: tuple of (height,width)
        """
        size=self.driver.getWindowSize()
        self.height=size['height']
        self.width =size['width']

        return (self.height, self.width)

    def hasWebView(self):
        """
        :return: boolean value if the current target has webview context
        """
        try:
            for context in self.driver.contexts:
                if (context.lower().find("web") > -1) or (context.lower().find("chromium") > -1):
                    return True
                else:
                    return False
        except:
            return False
    def switchToNative(self):
        if self.isCurrentContextNative():
            pass
        else:
            for context in self.driver.contexts:
                if (context.lower().find("native") > -1):
                    self.driver.switch_to.context(context)
                    return

            raise RuntimeError('Could not find the native app to switch to.  Aborting.')

    def switchToWebview(self):
        if self.isCurrentContextNative():
            for context in self.driver.contexts:
                if (context.lower().find("web") > -1):
                    self.driver.switch_to.context(context)
                    return
                elif (context.lower().find("chromium") > -1):
                    self.driver.switch_to.context(context)
                    return
            raise RuntimeError('Could not find a webview to switch to.  Aborting.')
        else:
            pass

    def getContexts(self):
        """
        :return: the contexts within the current session.
        """
        return self.driver.contexts

    def getCurrentContext(self):
        """
        :return: the current context of the current session.
        """
        return self.driver.current_context

    def isCurrentContextNative(self):
        """
        :rtype : boolean
        :return:
        """
        current_context = self.getCurrentContext()
        if current_context.lower().find('native') > -1:
            return True
        else:
            return False

    def createScreenshotDir(self, path='../../screenshots/'):
        """
        Create the screenshot directory for the test run
        :param path: the relative or absolute path for the screenshot directory
        """
        try:
            from pathlib import Path
        except ImportError:
            from pathlib2 import Path  # python 2 backport
        Path(path).mkdir(exist_ok=True)

    def saveScreenshot(self,filename , path='./'):
        """
        Captures a screenshot and saves in the current directory with the filename given in png
        :param filename: name of the file
        :param path: default to be the current folder
        """
        self.driver.save_screenshot(path+filename+'.png')
        sleep(1)
