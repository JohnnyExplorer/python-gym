from functional.cart.classes.customer import Customer


class Order:
  orders = []
  orderid = 0
  ship_add = ''
  expedited = False
  shipped = False
  customer = None
  backordered = False
  order_items = []



  def __init__(self, orderid, ship_add, expedited, shipped, customer, order_items,backordered) :
    super().__init__()
    self.orderid = orderid
    self.ship_add = ship_add
    self.expedited = expedited
    self.shipped = shipped
    self.customer = customer
    self.order_items = order_items
    self.backordered = backordered



  @staticmethod
  def v2_notify_backordered(orders, msg):
      Order.get_filtered_info(
        lambda o: any(i.backordered for i in o.order_items),
        lambda o: o.customer.notify(o.customer,msg),
        orders
      )

  # works from inside out
  @staticmethod
  def v2_notify_backordered(orders, msg):
    Order.map(lambda o : o.customer.notify(o.customer,msg),
      Order.filter(lambda o : Order.fileter(
        lambda i : i.backordered, o.order_items),
        orders
      ))

  @staticmethod
  def v1_notify_backordered(orders, msg):
      for o in orders:
          for i in o.order_items:
            if i.backordered:
                o.customer.notify(o.customer,msg)

  @staticmethod
  def filter(predicate, it):
    return list(filter(predicate,it))

  @staticmethod
  def map(func,it):
    return list(map(func,it))

  @staticmethod
  def get_filtered_info(predicate, func,orders):
      return Order.map(func,Order.filter(predicate,orders))


  @staticmethod
  def v1_get_filtered_info(predicate, func):
      output = []
      for order in Order.orders:
        if predicate(order):
          output.append(func(order))
      return output

  @staticmethod
  def test_expedited(order):
    return order.expedited

  @staticmethod
  def test_not_expedited(order):
    return not order.expedited



  @staticmethod
  def get_customer_address():
    return Order.customer.address

  @staticmethod
  def get_customer_name(order):
    return order.customer.name

  @staticmethod
  def get_customer_ship_add():
    return Order.customer.ship_add

  @staticmethod
  def get_expedited_orders_customer_name():
    return Order.get_filtered_info(Order.test_expedited,Order.get_customer_name())

  @staticmethod
  def get_expedited_orders_customer_addresses():
    return Order.get_filtered_info(Order.test_expedited,Order.get_customer_address)

  @staticmethod
  def get_expedited_orders_shipping_address():
      return Order.get_filtered_info(Order.test_expedited,Order.get_customer_ship_add)


  @staticmethod
  def get_order_by_id(orderid,orders):
    return list(filter(lambda order: order.orderid == orderid,orders))

  @staticmethod
  def v2_get_order_by_id(orderid):
      return Order.get_filtered_info(
        lambda order: order.orderid == orderid,
        lambda order: order
      )

  @staticmethod
  def v1_get_order_by_id(orderid):
    for order in Order.orders:
        if order.orderid == orderid:
          return order


  @staticmethod
  def v1_set_order_expedited(orderid):
    for order in Order.get_order_by_id(orderid):
      order.expedited = True

  @staticmethod
  def v1_set_order_expedited(orderid):
    for order in Order.orders:
      if order.orderid == orderid:
        order.expedited = True






  @staticmethod
  def v3_get_expedited_orders_customer_names():
    return Order.get_filtered_orders_customer_names(Order.test_expedited)

  @staticmethod
  def v2_get_expedited_orders_customer_names():
    return Order.get_filtered_info(
      lambda order: order.expedited,
      lambda order: order.customer.name
    )

  @staticmethod
  def v1_get_expedited_orders_customer_names():
    output = []
    for order in Order.orders:
      if order.expedited:
        output.append(order.customer.name)
    return output
  @staticmethod
  def v1_get_expedited_orders_customer_addresses():
    output = []
    for order in Order.orders:
      if order.expedited:
        output.append(order.customer.address)
      return output


  @staticmethod
  def v1_get_expedited_orders_shipping_address():
    output = []
    for order in Order.orders:
      if order.expedited:
        output.append(order.customer.ship_add)
      return output