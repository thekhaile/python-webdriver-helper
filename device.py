__author__ = 'khaile'


class Device(object):
    def __init__(self , driver=None):
        self.driver = driver


    def find_element(self, by, locator):
        try:
            element = self.driver.find_element(by, locator)
            return element
        except:
            return None

    def find_elements(self, by, locator):
        elements = []
        try:
            elements = self.driver.find_elements(by, locator)
            return elements
        except:
            return elements


    def swipe(self, startx, starty, endx, endy, duration=None):
        """
        Swipe across the screen or element.
        If phone rotates, x and y rotate with it.

        For the start and end points, if the values are less than one,
        then it is taken as a proportion of the element or screen.
        For example, 0.5 would be considered the center of the element or screen.

        duration is time in seconds.

        :param startx: Starting position on the horizontal axis.
        :param starty: Starting position on the vertical axis.
        :param endx: Ending position on the horizontal axis.
        :param endy: Ending position on the vertical axis.
        :param duration: (optional) Number of seconds to do the swipe (shorter is faster).

        """

        self.driver.swipe(startx, starty, endx, endy, duration)

    def swipe_up(self, startx=0.5, starty=0.7, endx=0.5, endy=0.3, duration=None):
        """
        Pre-defined swipe action starting near the bottom of the screen to the top
        """
        self.driver.swipe(startx, starty, endx, endy, duration)

    def swipe_down(self, startx=0.5, starty=0.3, endx=0.5, endy=0.7, duration=None):
        """
        Pre-defined swipe action starting from the top of the screen to the bottom
        """
        self.driver.swipe(startx, starty, endx, endy, duration)

    def swipe_left(self, startx=0.8, starty=0.5, endx=0.2, endy=0.5, duration=None):
        """
        Pre-defined swipe action starting from left to right in the middle of the screen.
        """
        self.driver.swipe(startx, starty, endx, endy, duration)

    def swipe_right(self, startx=0.2, starty=0.5, endx=0.8, endy=0.5, duration=None):
        """
        Pre-defined swipe action starting from right to left in the middle of the screen.
        """
        self.driver.swipe(startx, starty, endx, endy, duration)


    def bezel_swipe_left(self, starty=None, endy=None):
        """
        swipes in from left, halfway down the screen
        optional params: you can include starty to do a straight across swipe at that Y coord
          or you can include starty and endy to do a diagonal bezel swipe
        """
        if (starty==None):
            starty=endy=.5
        elif (endy==None):
            endy=starty

        self.driver.swipe(0.001, starty, .8, endy)

    def bezel_swipe_right(self, starty=0, endy=None):
        """
        swipes in from right, halfway down the screen
        optional params: you can include starty to do a straight across swipe at that Y coord
          or you can include starty and endy to do a diagonal bezel swipe
        """
        if (starty==None):
            starty=endy=.5
        elif (endy==None):
            endy=starty

        self.driver.swipe(.9999, starty, .2, endy)

    def bezel_swipe_top(self, startx=None, endx=None):
        """
        swipes in from top, halfway across top of the screen
        optional params: you can include startx to do a straight vertical swipe at that x coord
          or you can include startx and endx to do a diagonal bezel swipe
        """
        if (startx==None):
            startx=endx=.5
        elif (endx==None):
            endx=startx

        self.driver.swipe(startx, 0.001, endx, .8)

    def bezel_swipe_bottom(self, startx=None, endx=None):
        """
        swipes in from bottom, halfway across top of the screen
        optional params: you can include startx to do a straight vertical swipe at that x coord
          or you can include startx and endx to do a diagonal bezel swipe
        """
        if (startx==None):
            startx=endx=.5
        elif (endx==None):
            endx=startx

        self.driver.swipe(startx, .9999, endx, .2)

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

    def set_orientation(self, orientation):
        """
        Sets the current orientation of the device.
        :param orientation: LANDSCAPE or PORTRAIT.
        """

        current = self.driver.orientation
        if (current != orientation):
            self.driver.orientation = orientation

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
        self.driver.find_element_by_id('delete').click()

    def tap_hardware_back_key(self):
        """
        Presses on the device's hardware back button
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
        """Lock the device for a certain period of time. iOS only.
        :Args:
         - the duration to lock the device, in seconds
        """

        self.driver.lock(seconds)

    def get_window_size(self):
        """
        Gets window size.
        :return: tuple of (height,width)
        """
        size=self.driver.get_window_size()
        self.height=size['height']
        self.width =size['width']

        return (self.height, self.width)

