__author__ = 'khaile'
# from device import *
# from appium.webdriver.common.mobileby import MobileBy

class Element(object):

    def __init__(self, ui_object=None):
        self.ui_object = ui_object

    def get_location(self):
        """
        :return: x,y coordinates (top-left) of the ui_element
        """
        return self.ui_object.location

    def get_size(self):
        """
        :return: size (x pixels wide, y pixels high) of the ui_element
        """
        return self.ui_object.size

    def get_name(self):
        """
        :return: displayed name of the ui_element
        """
        return self.ui_object.get_attribute('name')

    def get_type(self):
        """
        :return: 'type' attribute of the ui_element
        """
        return self.ui_object.get_attribute('type')

    def get_value(self):
        """
        :return: 'value' attribute of the ui_element
        """
        return self.ui_object.get_attribute('value')

    def get_label(self):
        """
        :return: 'label' attribute of the ui_element
        """
        return self.ui_object.get_attribute('label')

    def tap(self):
        """
        Performs tap action on the element
        """
        self.ui_object.click()

class Button(Element):
    def __init__(self, ui_obj):
        Element.__init__(self, ui_object=ui_obj )

    def is_enabled(self):
        """
        :return: boolean whether or not the element is enabled
        """
        return self.ui_object.is_enabled()

class Picker(Element):
    def __init__(self, ui_obj):
        Element.__init__(self, ui_object=ui_obj)


    def get_current_value(self):
        """
        :return: currently selected value
        """
        return self.ui_object.get_attribute('value')

    def scroll_to_value(self, value):
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

class Textfield(Element):
    def __init__(self, ui_obj):
        Element.__init__(self, ui_object=ui_obj)


    def get_displayed_text(self):
        """
        :return: the displayed text or placeholder
        """
        return self.ui_object.text

    def enter_text(self, text):
        """
        Inserts the text into the field
        :param text: the text that needs to go into the field
        """
        self.ui_object.send_keys(text)

    def clear_text(self):
        """
        Deletes the current text in the field
        """
        self.ui_object.clear()

        # ## The method below could be applied to iOS app only ##
        # self.driver.find_element_by_xpath('//UIAButton[@name="Clear text"]').click()

    def go_to_next_field(self):
        """
        Similar to hitting tab
        """
        self.ui_object.send_keys('\n')

class CheckBox(Element):
    """
    Tested on Android
    """
    def __init__(self, ui_obj):
        Element.__init__(self, ui_object=ui_obj)

    def is_enabled(self):
        """
        :return: boolean whether or not the element is enabled
        """
        return self.ui_object.is_enabled()

    def is_checked(self):
        """
        :return: boolean whether or not the checkbox is checked
        """
        return self.ui_object.get_attribute('checked')

    def check(self):
        if self.ui_object.get_attribute('checked'):
            pass
        else:
            self.ui_object.click()

    def unCheck(self):
        if not self.ui_object.get_attribute('checked'):
            self.ui_object.click()
        else:
            pass

class Switch(Element):
    """
    Tested on Android
    """
    def __init__(self, ui_obj):
        Element.__init__(self, ui_object=ui_obj)

    def is_enabled(self):
        """
        :return: boolean whether or not the element is enabled
        """
        return self.ui_object.is_enabled()

    def is_on(self):
        """
        :return: boolean whether or not the checkbox is checked
        """
        return self.ui_object.get_attribute('checked')

    def toggle(self):
        self.ui_object.click()

class RadioButton(Element):
    """
    Tested on Android
    """
    def __init__(self, ui_obj):
        Element.__init__(self, ui_object=ui_obj)

    def is_enabled(self):
        """
        :return: boolean whether or not the element is enabled
        """
        return self.ui_object.is_enabled()

    def is_selected(self):
        """
        :return: boolean whether or not the checkbox is checked
        """
        return self.ui_object.get_attribute('checked')