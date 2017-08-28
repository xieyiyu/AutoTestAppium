## 测试用例编写规范

* 熟悉yaml格式编写规范. [yaml语法学习地址](http://www.ruanyifeng.com/blog/2016/07/yaml.html)
* 用例编写 /yamls/testyaml/*.yaml
* 用例操作 /testcase/*_test.py ,与用例文件名称对应
  文件中的每个测试用例方法以test_开头，名称与yaml中一致

## 测试用例字段解释
####  1. 查找元素

| find_type      | 解释                | 对应元素                 | element_info
| -------------- | ------------------ | ----------------------- | ------------
| id             | 根据id查找元素       | resource-id             | com.cma.launcher.lite:id/preview_background
| name           | 根据name查找元素     | text                    | I'm Lucky
| class_name     | 根据class查找元素    | class                   | android.widget.ImageView
| xpath          | 根据xpath查找元素    | //class[@index='index'] | //android.widget.TextView[@index='2']

*  示例
```
element_info: com.cma.launcher.lite:id/add_btn
find_type: id
```

####  2.  用例操作
| operate_type   | 解释         | 配合字段                 | element_info是否必须
| -------------- | ----------- | ----------------------- | ------------
| click          | 点击         | resource-id             |  是
| set_value      | 设置值       | text 输入值              |  是
| swipe_left，swipe_right，swipe_up，swipe_down | 左滑，右滑，上滑，下滑   | times 滑动次数，swipe_time 滑动时间    | 是
| key_event      | 实体按键      | key_code 按键码          | 否

* 常用[按键码](http://blog.csdn.net/qq_22795513/article/details/53169593)
```
KEYCODE_BACK 返回键 4
KEYCODE_HOME 按键Home 3
KEYCODE_MENU 菜单键 82
KEYCODE_POWER 电源键 26
KEYCODE_ENTER 回车键 66
```


* 示例
```
- element_info: com.cma.launcher.lite:id/preview_background
  find_type: id
  operate_type: click
- operate_type: key_event
  key_code: 4
- element_info: com.cma.launcher.lite:id/search_button_container
  find_type: id
  operate_type: swipe_right
  times: 2
  swipe_time: 600
```
