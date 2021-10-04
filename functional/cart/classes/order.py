class Order:

  orders = []
  orderid = 0
  ship_add = ''
  expedited = False
  shipped = False
  customer = None
  
  def get_expedited_orders_customer_names(self):
    output = []
    for order in Order.orders:
      if order.expedited:
        output.append(order.customer.name)
    return output

  def get_expedited_orders_customer_addresses(self):
    output = []
    for order in Order.orders:
      if order.expedited:
        output.append(order.customer.address)
    return output

  def get_expedited_roders_shipping_address(self):
    output = []
    for order in Order.orders:
      if order.expedited:
        output.append(order.ship_add)
    return output