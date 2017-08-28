"""
所有页面元素,用例操作按照此为标准
"""
class BaseElement(object):
    # 元素定位方法
    find_element_by_id = "id"
    find_element_by_name = "name"
    find_element_by_class_name = "class_name"
    find_element_by_xpath = "xpath"

    # 元素定位等待时间
    WAIT_TIME = 5

    # 操作
    CLICK = "click"
    SET_VALUE = "set_value"
    SWIPE_LEFT = "swipe_left"
    SWIPE_RIGHT = "swipe_right"
    SWIPE_UP = "swipe_up"
    SWIPE_DOWN = "swipe_down"
    KEY_EVENT = "key_event" # 实体按键操作，用例中仍要写element_info、find_type

    TAP = "tap"