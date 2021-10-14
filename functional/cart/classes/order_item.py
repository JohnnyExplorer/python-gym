class OrderItem:
  name = ''
  itemnumber = ''
  quantity = 0
  price = 0
  backordered = False;

  def __init__(self,name, itemnumber, quantity, price,backordered) :
    self.name = name
    self.itemnumber = itemnumber
    self.quantity = quantity
    self.price = price
    self.backordered  = backordered

