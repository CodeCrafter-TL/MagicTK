更新日志
===================

> [!TIP]  
> 此更新日志有以下 7 中类型的更新内容，分别用 7 中不同颜色来表示
>
> * 🟢 **新增**
> * 🔴 **移除**
> * 🟡 **变更**
> * 🔵 **优化**
> * 🟣 **修复**
> * 🟠 **弃用**
> * 🟤 **重构**

🔖 `1.0.0.beta1`
----------------

🕓 *发布日期 : 2024-08-09*

🟢 **新增**

- 为 `base.py` 新增 `Window` 类

- 为 `Window` 类添加 `place` `title` `titlebar` `position` `size` `alpha` `transparent` `transparentcolor` 方法

- 为 `tools.py` 添加 `create_image` `interpolate_color` 函数

- 为 `graphics.py` 新增 `TopRoundedRectangle` `RoundedButton` 类

- 为 `graphics.py` 中的 `Rectangle` 类添加 `alpha` 参数

- 为 `widgets.py` 新增 `Menu` 类

🟡 **变更**

- 将 `Rectangle` 中的 `create_rectangle` 部分移到 `if` 判断中，为适应 `alpha` 参数

### 重新匹配版本号

🔖 `1.0.1`
----------------

🕓 *发布日期 : 2024-08-01*

🟢 **新增**

- 为 `graphics.py` 中的 `RoundedRectangle` 类新增 `bind` 方法

- 为 `graphics.py` 中的 `Text` 类新增错误检测

- 添加 `tools.py`

- 为 `tools.py` 新增 `rgb_to_hex` `hex_to_rgb` 函数

- 为 `widgets.py` 新增 `RoundedButton` 类

🔖 `0.0.1.alpha4`
----------------

🕓 *发布日期 : 2024-07-22*

🟢 **新增**

- 为 `graphics.py` 中的 `Rectangle` 类新增 `_position` `_size` `_bg` 方法

- 为 `graphics.py` 中的 `Text` 类新增 `_usable` `_fg` 方法

- 为 `widgets.py` 中的 `Button` 类中的 `__start_click` 方法中的 `itemconfigure` 添加 `outline` 参数

- 为 `widgets.py` 添加 `BaseWidget` 类

- 为 `widgets.py` 中的 `BaseWidget` 类添加 `darken_color` 方法

- 为 `widgets.py` 中的 `BaseWidget` 类添加 `config` `create_shadow` 预设方法

- 为 `widgets.py` 中的 `Button` 类覆写 `config` `create_shadow` 方法

- 为 `widgets.py` 中的 `Label` 类覆写 `config` 方法

🟡 **变更**

- 将 `graphics.py` 中的类名称都改为 `PEP 8` 格式的单词首字母大写

- 将 `graphics.py` 中的 `Text` 类中的 `placemode` 改为 `self.placemode`

- 将 `graphics.py` 中的 `Text` 类中的 `coords` 改为调用 `_usable` 方法

- 将 `graphics.py` 中的 `Text` 类中的 `position` 方法改为 `_position`

- 将 `widgets.py` 中的 `Button` 类中的 `__start_click` 方法中的 `darkenColor` 改为 `darken_color`

🔖 `0.0.1.alpha3`
----------------

🕓 *发布日期 : 2024-06-20*

🟢 **新增**

- 为 `graphics.py` 添加 `text` 类

- 为 `graphics.py` 中的 `text` 类添加 `position` 方法

- 为 `widgets.py` 中的 `Button` 类添加一些赋值和基本绑定

- 为 `widgets.py` 中的 `Button` 类添加 `__start_click` `__end_click` 方法

🔖 `0.0.1.alpha2`
----------------

🕓 *发布日期 : 2024-06-20*

🟢 **新增**

- 为 `graphics.py` 添加 `rectangle` `perfectCircle` `ellipse` `roundedRectangle` 类

- 为 `graphics.py` 所有的类都添加 `canvasId` 属性

- 添加 `test.py`

🔖 `0.0.1 (.alpha1)`
----------------

🕓 *发布日期 : 2024-06-20*

🟢 **新增**

- 添加 `__init__.py` `base.py` `graphics.py` `widgets.py`
