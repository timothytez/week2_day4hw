class ShoppingCart:
  
  def __init__(self):
   self.cart = {}
    
  def shopper(self):
      while self.check_shopper():
          user_input = self.get_user_input()
          if user_input == 'a':
              item = input("what are we adding to your cart?: ")
              while True:
                try:
                  price = float(input('What is price of item?: '))
                  break
                except:
                  print("Please enter price in digits. Ex: 10.99")
              while True:
                quantity = input("How many items are you adding? ")
                if quantity.isdigit():
                  quantity = int(quantity)
                  break
                else:
                  print("Please enter quantity in digits. Example: 10")
              self.add_to_cart( item, price, quantity)
          elif user_input == 'd':
              user_delete_option = input("what item/s are you deleting?: ")
              self.del_from_cart( user_delete_option )
          elif user_input != 's':
              print('please enter valid option')
          self.display_cart()

  def check_shopper(self):
      user_shopping = input('Are you shopping? [y]es/[n]o?: ').lower()
      return True if user_shopping in 'yes' else False

  def get_user_input(self):
      return input('What do you want to do? [a]dd,[d]elete,[s]how?: ').lower()
      
  def add_to_cart(self, item, price, quantity):
      if item not in self.cart:
        self.cart[item] = {
            'price': price,
            'quantity': quantity
        }
      else:
          self.cart[item]['quantity'] += quantity

  def del_from_cart(self, item):
      if item in self.cart:
        del self.cart[item]
      else:
          print('Item not in cart')

  def display_cart(self):
      total_price = 0
      for item, dict in self.cart.items():
        print(f'{item}\nquantity: {dict["quantity"]}\nprice: {dict["price"]}')
        total_price += dict["quantity"] * dict["price"]
      print(f'Total Price: {total_price:.2f}')

  
shopping_cart = ShoppingCart()

shopping_cart.shopper()