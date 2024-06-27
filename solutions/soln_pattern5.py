#    Copyright 2024 Google LLC

#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at

#        http://www.apache.org/licenses/LICENSE-2.0

#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

########################################################################################
# Display 
########################################################################################
class StarBuzzCoffeeDisplay:
    """A class to represent the large computer screen showing customers the order queue.

    The StarBuzz Coffee shop now sells both food & coffee.

    The StarBuzz Coffee shop has a large computer screen so customers can determine
    where in the queue their order is. 

    The driver of the computer screen is very basic. 
    The driver will use standard python operations to get info:
    - To get the entire queue ==> str(StarBuzzCoffeeDisplay)

    The display need to support displaying both coffee & food orders.
    """

    def __init__(self, order_system):
        self.order_system = order_system
    
    def __repr__(self) -> str:
        return str(self.order_system)

########################################################################################
# Central ordering system for both food & coffee
########################################################################################
class StarBuzzOrders:
    """ A class to represent a system that can take orders for both food & coffee.

    A single customer can order both coffe & food in one transaction.
    """

    def __init__(self):
      self.coffee_order_queue = StarBuzzCoffeeOrders()
      self.food_order_queue = StarBuzzFoodOrders()
    
    def new_order(self, food_order:str, coffee_order:str):
        self.food_order_queue.new_order(food_order)
        self.coffee_order_queue.new_order(coffee_order)  
    
    # pattern 5 - exercise A
    def get_all_orders(self):
        report = ""
        for food, coffee in zip(self.food_order_queue, self.coffee_order_queue):
            report += f"({food}, {coffee})"
        return report

    def __repr__(self) -> str:
        return self.get_all_orders()

########################################################################################
# Food orders
########################################################################################
class StarBuzzFoodOrders:
    """ A class to represent food orders at our new enterprise StarBuzz Coffee.
    """

    def __init__(self):
        self.orderq = []
        self.itr_idx = 0

    def new_order(self, order: str) -> None:
        self.orderq.append(order)
    
    def __len__(self):
        return len(self.orderq)
    
    def __iter__(self):
        return StarBuzzFoodOrdersIterator(self)
    
    def __getitem__(self, position):
        return self.orderq[position]
    
class StarBuzzFoodOrdersIterator:
    """ A class that is an iterator for StarBuzzFoodOrders.
    """

    def __init__(self, order_queue: StarBuzzFoodOrders):
        self.idx = 0
        self.order_queue = order_queue
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.idx >= len(self.order_queue):
            raise StopIteration
        order = self.order_queue.orderq[self.idx]
        self.idx +=1 
        return order        

########################################################################################
# Coffee orders
########################################################################################
class StarBuzzCoffeeOrders:
    """ A class to represent orders at our new enterprise StarBuzz Coffee.

    This order queue class needs to work with standard python operations:
    - To get total queue length ==> len(StarBuzzCoffeeOrders)
    - To get through all orders ==> for order in StarBuzzCoffeeOrders: 
    - To get an order at random ==> StarBuzzCoffeeOrders[idx]
    """

    def __init__(self):
        self.orderq = []
        self.itr_idx = 0

    def new_order(self, order: str) -> None:
        self.orderq.append(order)
    
    def was_this_order_perfect(self, order:str) -> bool:
        # [ ] check beans were correctly ground
        # [ ] check milk was heated correctly
        # [ ] check latte art was awesome
        # [ ] get customer got their portion of happiness in a cup
        return True
    
    def __len__(self):
        return len(self.orderq)
    
    def __iter__(self):
        return StarBuzzCoffeeOrdersIterator(self)
    
    def __getitem__(self, position):
        return self.orderq[position]
    
class StarBuzzCoffeeOrdersIterator:
    """ A class that is an iterator for StarBuzzCoffeeOrders.

    This class is required for pattern 1 - exercise B
    """

    def __init__(self, order_queue: StarBuzzCoffeeOrders):
        self.idx = 0
        self.order_queue = order_queue
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.idx >= len(self.order_queue):
            raise StopIteration
        order = self.order_queue.orderq[self.idx]
        self.idx +=1 
        return order