"""
所有页面元素
"""
class BaseElement(object):
    find_element_by_id = "id"
    find_element_by_name = "name"
    find_element_by_class_name = "class_name"
    find_element_by_xpath = "xpath"

    CLICK = "click"
    TAP = "tap"
    SWIPE_LEFT = "swipe_left"
    SET_VALUE = "set_value"
    WAIT_TIME = 5