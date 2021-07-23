class Category:

  def __init__(self, category):
    self.category = category
    self.ledger = []

  def deposit(self, amount, description=''):
    self.ledger.append({'amount': amount, 'description': description})

  def check_funds(self, amount):
    if amount > self.get_balance():
      return False
    else:
      return True

  def withdraw(self, amount, description=''):
    if self.check_funds(amount) :
      self.ledger.append({'amount': 0-amount, 'description': description})
      return True
    else:
      return False

  def get_balance(self):
    balance = 0
    for item in self.ledger:
      balance = balance + item['amount']
    return balance

  def transfer(self, amount, b_category):
    if self.check_funds(amount):
      self.withdraw(amount, 'Transfer to '+ b_category.category)
      b_category.deposit(amount, 'Transfer from '+ self.category)
      return True
    else:
      return False
  
  def __str__(self):
    s = self.category.center(30, "*") + "\n"

    for item in self.ledger:
      temp = f"{item['description'][:23]:23}{item['amount']:7.2f}"
      s += temp + "\n"

    s += "Total: " + str(self.get_balance())
    return s


def create_spend_chart(categories):
  spend = []
  for category in categories:
    temp = 0
    for item in category.ledger:
      if item['amount'] < 0:
        temp += abs(item['amount'])
    spend.append(temp)
  
  total = sum(spend)
  percentage = [i/total * 100 for i in spend]

  title = "Percentage spent by category"
  for i in range(100, -1, -10):
    title += "\n" + str(i).rjust(3) + "|"
    for j in percentage:
      if j >= i:
        title += " o "
      else:
        title += "   "
    
    title += " "
  title += "\n    ----------"

  category_length = []
  for category in categories:
    category_length.append(len(category.category))
  max_length = max(category_length)

  for i in range(max_length):
    title += "\n    "
    for j in range(len(categories)):
      if i < category_length[j]:
        title += " " + categories[j].category[i] + " "
      else:
        title += "   "
    
    title += " "

  return title
