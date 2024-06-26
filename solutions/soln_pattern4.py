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

class StarBuzzCoffeeBilling:
    """ A class to represent billing logic at our new enterprise StarBuzz Coffee.
    """

    def __init__(self):
        self.order_system = StarBuzzCoffeeOrders()
        self.prices = {
            "latte": 1,
            "cappucino": 2,
            "americano": 3,
        }
        self.receipt_log = []
    
    def process_order(self, cusotmer_loyalty_id: str, order_item:str):
        self.order_system.new_order(order_item)
        self.receipt_log.append({
            "cust":cusotmer_loyalty_id,
            "order": order_item,
            "revenue": self.prices[order_item]
            })
    
    # pattern 4 - exercise A
    def report_total_revenue(self):
        total_revenue = 0
        for i in range(0,len(self.receipt_log)):
            total_revenue += self.receipt_log[i]["revenue"]
        return total_revenue
    
    # pattern 4 - exercise B
    def invite_customers_with_odd_sequence_slots_to_vip_program(self):
        invitee_list = ""
        for i in range(1, 20, 2):
            try:
                customer_to_invite = self.receipt_log[i]["cust"]
                invitee_list += f"({customer_to_invite})"
            except IndexError:
                invitee_list += "" #do nothing as we have not had this many customers
        return invitee_list


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