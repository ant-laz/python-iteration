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
        # TODO write your solution here
        pass
    
    # pattern 1 - exercise B
    def __iter__(self):
        # TODO write your solution here
        pass
    
    # pattern 1 - exercise C
    def __getitem__(self, position):
        # TODO write your solution here
        pass
    
class StarBuzzCoffeeOrdersIterator:
    """ A class that is an iterator for StarBuzzCoffeeOrders.

    This class is required for pattern 1 - exercise B
    """

    def __init__(self, order_queue: StarBuzzCoffeeOrders):
        self.idx = 0
        self.order_queue = order_queue
    
    def __iter__(self):
        # TODO write your solution here
        pass
    
    def __next__(self):
        # TODO write your solution here
        pass