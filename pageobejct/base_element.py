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
    # 设置值
    SET_VALUE = "set_value"
    # 左滑
    SWIPE_LEFT = "swipe_left"
    # 右滑
    SWIPE_RIGHT = "swipe_right"
    # 上滑
    SWIPE_UP = "swipe_up"
    # 下滑
    SWIPE_DOWN = "swipe_down"
    # 实体按键操作，用例中仍要写element_info、find_type
    KEY_EVENT = "key_event"
    # 在元素上执行放大操作
    ZOOM = "zoom"
    # 在元素上执行模拟双指捏（缩小操作）
    PINCH = "pinch"

    TAP = "tap"