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

class StarBuzzCoffeeDisplay:
    """A class to represent the large computer screen showing customers the order queue.

    The StarBuzz Coffee shop has a large computer screen so customers can determine
    where in the queue their order is. 
    The driver of the computer screen is very basic. 
    The driver will use standard python operations to get info:
    - To get the entire queue ==> str(StarBuzzCoffeeDisplay)
    """

    def __init__(self, StarBuzzCoffeeOrders, num_staff_morning_coffees=0):
      self.order_queue = StarBuzzCoffeeOrders
      self.num_staff_morning_coffees = num_staff_morning_coffees

    # pattern 2 - exercise A
    def get_all_orders_in_queue(self):
        display_info = ""
        for idx, order in enumerate(self.order_queue):
            display_info += f"({idx}, '{order}')"
        return display_info

    # pattern 2 - exercise B
    def get_all_orders_excluding_tests(self):
        display_info = ""
        for idx, order in enumerate(self.order_queue, -1*self.num_staff_morning_coffees):
            if idx >= 0:
              display_info += f"({idx}, '{order}')"
        return display_info
    
    def __repr__(self) -> str:
        pass
        
        # pattern 2 - exercise A
        # return self.get_all_orders_in_queue()

        # pattern 2 - exercise B
        return self.get_all_orders_excluding_tests()
        

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
    
    # pattern 1 - exercise A
    def __len__(self):
        return len(self.orderq)
    
    # pattern 1 - exercise B
    def __iter__(self):
        return StarBuzzCoffeeOrdersIterator(self)
    
    # pattern 1 - exercise C
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