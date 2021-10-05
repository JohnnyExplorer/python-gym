class Order:

  orders = []
  orderid = 0
  ship_add = ''
  expedited = False
  shipped = False
  customer = None



  @staticmethod
  def test_expedited(order):
    return order.expedited

  @staticmethod
  def get_customer_name(order):
    return order.customer.name

  @staticmethod
  def get_filtered_info(predicate, func):
      output = []
      for order in Order.orders:
        if predicate(order):
          output.append(func(order))
      return output

  @staticmethod
  def get_filtered_orders_customer_names(predicate):
    output = []
    for order in Order.orders:
      if(predicate(order)):
        output.append(order.customer.name)
    return output
  @staticmethod

  def v4_get_expedited_orders_customer_name():
    return Order.get_filtered_info(Order.test_expedited,Order.get_customer_name())

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
  def get_expedited_orders_customer_addresses():
    output = []
    for order in Order.orders:
      if order.expedited:
        output.append(order.customer.address)
    return output
  @staticmethod
  def get_expedited_roders_shipping_address():
    output = []
    for order in Order.orders:
      if order.expedited:
        output.append(order.ship_add)
    return output