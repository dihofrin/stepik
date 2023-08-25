"""
https://stepik.org/lesson/958398/step/15?unit=964840

Класс OrderStatus
Реализуйте класс OrderStatus, описывающий флаг с состояниями интернет-заказов. Флаг должен иметь три элемента:

ORDER_PLACED
PAYMENT_RECEIVED
SHIPPING_COMPLETE
"""

from enum import Flag, auto

class OrderStatus(Flag):

    ORDER_PLACED = auto()
    PAYMENT_RECEIVED = auto()
    SHIPPING_COMPLETE = auto()