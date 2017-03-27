__author__ = 'khaile'
import os
from time import sleep

class Device(object):
    def __init__(self , driver=None):
        self.driver = driver

    def quit(self):
        self.driver.quit()

    def find_element(self, strategy, value):
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

    def find_elements(self, strategy, value):
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

    def is_ios(self):
        """
        :return: the boolean value of whether we are on an iOS platform
        """
        if self.driver.desired_capabilities['platformName'] == 'iOS':
            return True
        else:
            return False

    def is_android(self):
        """
        :return: the boolean value of whether we are on an Android platform
        """
        if self.is_mobile_web():
            if self.driver.desired_capabilities['platformName'] == 'Android':
                return True
            else:
                return False
        else:
            if self.driver.desired_capabilities['platformName'] == 'Android':
                return True
            else:
                return False

    def is_mobile_web(self):
        """
        :return: boolean value of the current automated target is a native app.
        False will be returned if it is a mobile web for example.
        """
        if self.driver.desired_capabilities.has_key('app'):
            return False
        else:
            return True

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
        size = self.get_window_size()
        height = size[0]
        width = size[1]
        startx = width*startx
        starty = height*starty
        endx = width*deltax
        endy = height*deltay

        if not self.is_current_context_native():
            self.switch_to_native()
        self.driver.swipe(startx, starty, endx, endy, duration)

    def swipe_up(self, startx=0.5, starty=0.8, deltax=0 , deltay=-0.5, duration=250):
        """
        Pre-defined swipe action starting near the bottom of the screen to the top
        """
        if self.is_android():
            deltay=deltay*(-1)

        self.swipe(startx, starty, deltax, deltay, duration)

    def swipe_down(self, startx=0.5, starty=0.3, deltax=0, deltay=0.5, duration=250):
        """
        Pre-defined swipe action starting from the top of the screen to the bottom
        """
        if self.is_android():
            deltay=deltay*(-1)

        self.swipe(startx, starty, deltax, deltay, duration)

    def swipe_left(self, startx=0.8, starty=0.5, deltax=-0.7, deltay=0, duration=250):
        """
        Pre-defined swipe action starting from left to right in the middle of the screen.
        """
        self.swipe(startx, starty, deltax, deltay, duration)

    def swipe_right(self, startx=0.2, starty=0.5, deltax=0.7, deltay=0, duration=250):
        """
        Pre-defined swipe action starting from right to left in the middle of the screen.
        """
        self.swipe(startx, starty, deltax, deltay, duration)


    def bezel_swipe_left(self, starty=None):
        """
        swipes in from left, halfway down the screen
        optional params: you can include starty to do a straight across swipe at that Y coord
        """
        if (starty==None):
            starty=.5
            deltay=0

        self.swipe(0.001, starty, .8, deltay)

    def bezel_swipe_right(self, starty=None):
        """
        swipes in from right, halfway down the screen
        optional params: you can include starty to do a straight across swipe at that Y coord
        """
        if (starty==None):
            starty=.5
            deltay=0

        self.swipe(.9999, starty, -.8, deltay)

    def bezel_swipe_top(self, startx=None):
        """
        swipes in from top, halfway across top of the screen
        optional params: you can include startx to do a straight vertical swipe at that x coord
        """
        if (startx==None):
            startx=.5
            deltax=0

        self.swipe(startx, 0.001, deltax, .8)

    def bezel_swipe_bottom(self, startx=None):
        """
        swipes in from bottom, halfway across top of the screen
        optional params: you can include startx to do a straight vertical swipe at that x coord

        """
        if (startx==None):
            startx=.5
            deltax=0

        self.swipe(startx, .9999, deltax, -.8)

    def tap_on_screen(self, *args):
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


    def get_current_orientation(self):
        """
        Returns the current orientation of the device.  Possible values
        are: LANDSCAPE or PORTRAIT.
        """
        return self.driver.orientation

    def __set_orientation(self, orientation):
        """
        Sets the current orientation of the device.
        :param orientation: LANDSCAPE or PORTRAIT.
        """

        current = self.driver.orientation
        if (current != orientation):
            self.driver.orientation = orientation
    def rotate_to_portrait(self):
        self.__set_orientation('PORTRAIT')

    def rotate_to_landscape(self):
        self.__set_orientation('LANDSCAPE')

    def dismiss_keyboard(self, key_name=None, key=None, strategy=None):
        """
        Hides the software keyboard on the device. In iOS, use `key_name` to press
        a particular key, or `strategy`. In Android, no parameters are used.
        :Args:
         - key_name - key to press
         - strategy - strategy for closing the keyboard (e.g., `tapOutside`)
        """
        self.driver.hide_keyboard(key_name, key, strategy)

    def tap_delete_key(self):
        if self.is_ios():
            self.driver.find_element_by_id('delete').click()
        else:
            self.driver.press_keycode(67)

    def tap_hardware_back_key(self):
        """
        Presses on the device's hardware back button Android only.
        """
        self.driver.press_keycode(4)

    def save_screenshot(self, filename):
        """
        Gets the screenshot of the current window. Returns False if there is
           any IOError, else returns True. Use full paths in your filename.

        :Args:
         - filename: The full path you wish to save your screenshot to.

        :Usage:
            driver.get_screenshot_as_file('/Screenshots/foo.png')
        """
        self.driver.save_screenshot(filename)

    def lock_device(self, seconds):
        """Lock the device for a certain period of time. Android and iOS 8.0 only.
        :Args:
         - the duration to lock the device, in seconds
        """
        if self.is_ios():
            self.driver.lock(seconds)
        else:
            os.system('adb shell input keyevent 26')
            sleep(seconds)
            os.system('adb shell input keyevent 26')


    def get_window_size(self):
        """
        Gets window size.
        :return: tuple of (height,width)
        """
        size=self.driver.get_window_size()
        self.height=size['height']
        self.width =size['width']

        return (self.height, self.width)

    def switch_to_native(self):
        if self.is_current_context_native():
            pass
        else:
            for context in self.driver.contexts:
                if (context.lower().find("native") > -1):
                    self.driver.switch_to.context(context)
                    return

            raise RuntimeError('Could not find the native app to switch to.  Aborting.')

    def switch_to_webview(self):
        if self.is_current_context_native():
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

    def get_contexts(self):
        """
        :return: the contexts within the current session.
        """
        return self.driver.contexts

    def get_current_context(self):
        """
        :return: the current context of the current session.
        """
        return self.driver.current_context

    def is_current_context_native(self):
        """
        :rtype : boolean
        :return:
        """
        current_context = self.get_current_context()
        if current_context.lower().find('native') > -1:
            return True
        else:
            return False