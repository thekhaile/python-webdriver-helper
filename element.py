__author__ = 'khaile'

class Element(object):

    def __init__(self, ui_object=None):
        self.ui_object = ui_object

    def get_location(self):
        """
        :return: x,y coordinates (top-left) of the ui_element
        """
        return self.ui_object.location

    def get_name(self):
        """
        :return: displayed name of the ui_element
        """
        return self.ui_object.get_attribute('name')

    def get_size(self):
        """
        :return: size of the ui_element
        """
        return self.ui_object.size

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
        :param value: one of the available values in the picket
        """
        self.ui_object.send_keys(value)


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
