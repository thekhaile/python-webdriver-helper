__author__ = 'khaile'
from device import *
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoSuchElementException

class Type(object):
    """
    This class is mainly used as a middle man to provide auto-complete for UIType suggestion and
    return the selected class and pass on the webdriver to the individual classes.
    """
    def __init__(self , webdriver=None):
        """
        :param webdriver: the appium webdriver
        """
        self.driver = webdriver

    def Element(self, ui_obj):
        """
        :param ui_obj: the element object on which actions are being applied
        :return: the Element class
        """
        return Element(ui_obj, self.driver)

    def Button(self, ui_obj):
        """
        :param ui_obj: the element object on which actions are being applied
        :return: the Button class
        """
        return Button(ui_obj, self.driver)

    def Picker(self, ui_obj):
        """
        :param ui_obj: the element object on which actions are being applied
        :return: the Picker class
        """
        return Picker(ui_obj, self.driver)

    def TextField(self, ui_obj):
        """
        :param ui_obj: the element object on which actions are being applied
        :return: the TextField class
        """
        return TextField(ui_obj, self.driver)

    def CheckBox(self, ui_obj):
        """
        :param ui_obj: the element object on which actions are being applied
        :return: the CheckBox class
        """
        return CheckBox(ui_obj, self.driver)

    def Switch(self, ui_obj):
        """
        :param ui_obj: the element object on which actions are being applied
        :return: the Switch class
        """
        return Switch(ui_obj, self.driver)

    def RadioButton(self, ui_obj):
        """
        :param ui_obj: the element object on which actions are being applied
        :return: the RadioButton class
        """
        return RadioButton(ui_obj, self.driver)

    def Alert(self, ui_obj):
        """
        :param ui_obj: the element object on which actions are being applied
        :return: the RadioButton class
        """
        return Alert(ui_obj, self.driver)


class Element(object):
    """
    This class is the base class for all UI Elements and has basic methods shared across UI Types
    """
    def __init__(self, ui_object=None, driver =None):
        self.ui_object = ui_object
        self.driver = driver
        self.action = TouchAction(self.driver)
        self.device = Device(self.driver)

    def getLocation(self):
        """
        :return: x,y coordinates (top-left) of the ui_element
        """
        return self.ui_object.location

    def getSize(self):
        """
        :return: size (x pixels wide, y pixels high) of the ui_element
        """
        return self.ui_object.size

    def getName(self):
        """
        :return: displayed name of the ui_element
        """
        return self.ui_object.get_attribute('name')

    def getType(self):
        """
        :return: 'type' attribute of the ui_element
        """
        return self.ui_object.get_attribute('type')

    def getValue(self):
        """
        :return: 'value' attribute of the ui_element
        """
        return self.ui_object.get_attribute('value')

    def getLabel(self):
        """
        :return: 'label' attribute of the ui_element
        """
        if self.device.isWeb():
            return self.ui_object.text
        else:
            return self.ui_object.get_attribute('label')
        
    def tap(self):
        """
        Performs tap action on the element
        """
        if self.device.isMobile():
            if self.device.isChromium():
                self.ui_object.click()
            else:
                self.tapHybrid()
        else:
            self.ui_object.click()

    def tapHybrid(self):
        """
        Performs tap action on the element for hybrid apps
        """
        location = self.ui_object.location
        size = self.ui_object.size

        # Determine if we need to take into account the browser header of mobile web
        if self.device.isWeb():
            self.device.switchToNative()
            if self.device.isIos():
                #Assuming this is a placeholder for the URL Header Bar on iOS
                urlHeaderBar = self.driver.find_element(MobileBy.CLASS_NAME, 'UIAButton')
                urlHeaderBarSize = urlHeaderBar.size
                location['y'] = urlHeaderBarSize['height'] + location['y'] + size['height']/2
                location['x'] = location['x'] + size['width']/2
            else:
                webView = self.driver.find_element(MobileBy.CLASS_NAME, 'android.webkit.WebView')
                webViewLocation = webView.location
                location['y'] = webViewLocation['y'] + location['y'] + size['height']/2
                location['x'] = webViewLocation['x'] + location['x'] + size['width']/2
            self.device.switchToWebview()
        else:
            #This is simply native app wrapper
            location['x'] = location['x'] + size['width']/2
            location['y'] = location['y'] + size['height']/2
        if location['x'] < 0 or location['y'] < 0:
            print 'Either x or y coordinate is negative'
        else:
           self.action.tap(x=location['x'], y=location['y']).perform()

    def long_press(self):
        """
        performs long press action at the center of the element
        """
        coordinates = self.getLocation()
        size = self.getSize()
        coordinates['x'] = coordinates['x']+ size['width']/2
        coordinates['y'] = coordinates['y']+ size['height']/2

        self.action.long_press(x=coordinates['x'], y=coordinates['y']).perform()

class Button(Element):
    """
    This class is for the UI Element whose type is UIAButton for iOS and
    android.widget.Button for Android
    """
    def __init__(self, ui_obj, webdriver):
        Element.__init__(self, ui_object=ui_obj, driver=webdriver)

    def isEnabled(self):
        """
        :return: boolean whether or not the element is enabled
        """
        return self.ui_object.is_enabled()

class Picker(Element):
    def __init__(self, ui_obj, webdriver):
        Element.__init__(self, ui_object=ui_obj, driver=webdriver)


    def getCurrentValue(self):
        """
        :return: currently selected value
        """
        return self.ui_object.get_attribute('value')

    def scrollToValue(self, value):
        """
        Scroll the picker to the specified value
        :param value: one of the available values in the picker
        """
        # if Device().is_ios():
        self.ui_object.send_keys(value)
        # else:
        #     textView = self.ui_object.find_element(MobileBy.CLASS_NAME, 'android.widget.EditText')
        #     if textView.text == value:
        #         pass
        #     else:
        #         buttons = self.ui_object.find_elements(MobileBy.CLASS_NAME, 'android.widget.Button')
        #         if len(buttons) == 2:
        #             while len(buttons) == 2 or textView.text != value:
        #                 Device.scroll(buttons[1], textView)
        #             button = self.ui_object.find_element(MobileBy.CLASS_NAME, 'android.widget.Button')
        #             count = 0
        #             while textView.text != value or count < 150:
        #                 Device.scroll(button, textView)
        #                 count += 1
        #             if textView.text != value:
        #                 raise
        #         elif len(buttons) == 1:
        #             button = self.ui_object.find_element(MobileBy.CLASS_NAME, 'android.widget.Button')
        #             count = 0
        #             while textView.text != value or count < 150:
        #                 Device.scroll(button, textView)
        #                 count += 1
        #             if textView.text != value:
        #                 raise

class TextField(Element):
    """
    This class is for the UI Element whose type is UIATextField or UIASecureField for iOS and android.widget.EditText
    for Android
    """
    def __init__(self, ui_obj, webdriver):
        Element.__init__(self, ui_object=ui_obj, driver=webdriver)


    def getDisplayedText(self):
        """
        :return: the displayed text or placeholder
        """
        return self.ui_object.text

    def enterText(self, text):
        """
        Inserts the text into the field
        :param text: the text that needs to go into the field
        """
        self.ui_object.send_keys(text)

    def clearText(self):
        """
        Deletes the current text in the field
        """
        self.ui_object.clear()

        # ## The method below could be applied to iOS app only ##
        # self.driver.find_element_by_xpath('//UIAButton[@name="Clear text"]').click()

    def goToNextField(self):
        """
        Similar to hitting tab
        """
        self.ui_object.send_keys('\n')

class CheckBox(Element):
    """
    Tested on Android
    """
    def __init__(self, ui_obj, webdriver):
        Element.__init__(self, ui_object=ui_obj, driver=webdriver)

    def isEnabled(self):
        """
        :return: boolean whether or not the element is enabled
        """
        return self.ui_object.is_enabled()

    def isChecked(self):
        """
        :return: boolean whether or not the checkbox is checked
        """
        if self.device.isWeb():
            return self.ui_object.is_selected()
        elif self.device.isIos():
            if self.ui_object.get_attribute('value') == 1:
                return True
            else:
                return False

        else:
            return self.ui_object.get_attribute('checked')

    def check(self):
        if self.isChecked():
            pass
        else:
            self.ui_object.click()

    def unCheck(self):
        if not self.isChecked():
            self.ui_object.click()
        else:
            pass

class Switch(Element):
    """
    Tested on Android
    This class is for the UI Element whose type is UIASwitch for iOS and
    android.widget.Switch for Android
    """
    def __init__(self, ui_obj, webdriver):
        Element.__init__(self, ui_object=ui_obj, driver=webdriver)

    def isEnabled(self):
        """
        :return: boolean whether or not the element is enabled
        """

        return self.ui_object.is_enabled()

    def isOn(self):
        """
        :return: boolean whether or not the Switch is on
        """
        if self.device.isWeb():
            return self.ui_object.is_selected()
        elif self.device.isIos():
            if self.ui_object.get_attribute('value') == 1:
                return True
            else:
                return False
        else:
            return self.ui_object.get_attribute('checked')

    def toggle(self):
        self.ui_object.click()

class RadioButton(Element):
    """
    Tested on Android
    """
    def __init__(self, ui_obj, webdriver):
        Element.__init__(self, ui_object=ui_obj, driver=webdriver)

    def isEnabled(self):
        """
        :return: boolean whether or not the element is enabled
        """
        return self.ui_object.is_enabled()

    def isSelected(self):
        """
        :return: boolean whether or not the checkbox is checked
        """
        return self.ui_object.get_attribute('checked')

class Cell(Element):
     def __init__(self, ui_obj, webdriver):
        Element.__init__(self, ui_object=ui_obj, driver=webdriver)


class Alert(Element):
    def __init__(self, ui_obj, webdriver):
        Element.__init__(self, ui_object=ui_obj, driver=webdriver)

    def accept(self):
        """
        Try interacting with the positive action of Allow first, If not try OK, and finally try Yes
        """
        try:
            el = self.ui_object.find_element(MobileBy.ID, 'Allow')
            el.click()
        except NoSuchElementException:
            try:
                el = self.ui_object.find_element(MobileBy.ID, 'OK')
                el.click()
            except NoSuchElementException:
                el = self.ui_object.find_element(MobileBy.ID, 'Yes')
                el.click()


    def dismiss(self):
        """
        Try interacting with the negative action of Don't Allow first, If not try Cancel, and finally try No
        """
        try:
            el = self.ui_object.find_element(MobileBy.ID, "Don't Allow")
            el.click()
        except NoSuchElementException:
            try:
                el = self.ui_object.find_element(MobileBy.ID, 'Cancel')
                el.click()
            except NoSuchElementException:
                el = self.ui_object.find_element(MobileBy.ID, 'No')
                el.click()


    def getTitle(self):
        """
        :return: the header of the alert
        """
        el = self.ui_object.find_element(MobileBy.CLASS_NAME, 'UIAStaticText')
        return el.text

    def getBody(self):
        """
        :return: the body of the alert
        """
        els = self.ui_object.find_elements(MobileBy.CLASS_NAME, 'UIAStaticText')
        el = els[1]
        return el.text

