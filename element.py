__author__ = 'khaile'


class Element(object):

    def __init__(self, ui_object=None):
        self.ui_object = ui_object

    def location(self):
        ##Returns the x, y coordinates of the element
        return self.ui_object.location

    def name(self):
        ##Returns the displayed name of the element
        return self.ui_object.get_attribute('name')

    def tap(self):
        self.ui_object.click()

class Button(Element):
    def __init__(self, ui_obj):
        Element.__init__(self, ui_object=ui_obj )
        self.driver = Mobile.driver

    def is_enabled(self):
        ##Returns boolean whether or not the element is enabled
        return self.ui_object.is_enabled()

class Picker(Element):
    def __init__(self, ui_obj):
        Element.__init__(self, ui_object=ui_obj)
        self.driver = Mobile.driver

    def currentValue(self):
        return self.ui_object.get_attribute('value')

    def flickToValue(self, value):
        self.ui_object.send_keys(value)

    def dismiss(self):
        self.driver.hide_keyboard()

class Textfield(Element):
    def __init__(self, ui_obj):
        Element.__init__(self, ui_object=ui_obj)
        self.driver = Mobile.driver

    def displayedText(self):
        return self.ui_object.text

    def enterText(self, text):
        self.ui_object.send_keys(text)

    def clearText(self):
        self.ui_object.clear()

        # ## The method below could be applied to iOS app only ##
        # self.driver.find_element_by_xpath('//UIAButton[@name="Clear text"]').click()

    def goToNextField(self):
        self.ui_object.send_keys('\n')
