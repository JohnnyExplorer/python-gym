class Customer:
  name = ''
  adderess = ''
  enterprise = False;


  def __init__(self,name,adderess,enterprise):
    super().__init__();
    self.name = name
    self.adderess = adderess
    self.enterprise = enterprise

  @staticmethod
  def notify(cust: object,msg: str):
    print('Sending ""{}"" to ""{}"" at ""{}""'.format(msg,cust.name,cust.address))