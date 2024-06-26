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

import unittest

from src.pattern1 import StarBuzzCoffeeOrders

class TestStarBuzzCoffeeOrders(unittest.TestCase):

    # pattern 1 - exercise A
    def test_ordering_a_coffee(self):
        """Your new start-up StarBuzz Coffee needs to take orders! 
        
        This test covers ordering a latte and checking that
        the order made it into the order queue.
        """
        cafe_orders = StarBuzzCoffeeOrders()
        cafe_orders.new_order("latte")
        expected_num_orders = 1
        actual_num_orders: int = len(cafe_orders)
        self.assertEqual(expected_num_orders, actual_num_orders)
    
    # pattern 1 - exercise B
    def test_looping_through_all_orders(self):
        """You need to loop through all orders.

        You hired a second barista at StarBuzz Coffee.
        With two baristas you can really whip through orders.
        Check that you can loop throgh all orders in the queue.
        Check for quality too, those lattes need to be perfect.
        """
        cafe_orders = StarBuzzCoffeeOrders()
        cafe_orders.new_order("latte")
        cafe_orders.new_order("cappuccino")
        cafe_orders.new_order("americano")
        expected_perfect_coffee_cnt = 3
        actual_perfect_coffee_cnt = 0
        for order in cafe_orders:
            if cafe_orders.was_this_order_perfect(order):
                actual_perfect_coffee_cnt += 1                     
        self.assertEqual(expected_perfect_coffee_cnt, actual_perfect_coffee_cnt)

    # pattern 1 - exercise C
    def test_checking_order_queue_at_idx(self):
        """Your baristra needs to checks orders at random.

        You hired a new barista at StarBuzz Coffee. 
        The barista needs to check the order queue randomly.
        Sometimes a customers need to jump the queue. 
        Sometimes a customers forgot what they ordered.
        """
        cafe_orders = StarBuzzCoffeeOrders()
        cafe_orders.new_order("latte")
        cafe_orders.new_order("cappuccino")
        expected_order_retreived = "latte"
        actual_order_retreived  = cafe_orders[0]
        self.assertEqual(expected_order_retreived, actual_order_retreived)
    

