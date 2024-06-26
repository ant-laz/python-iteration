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

from src.pattern2 import StarBuzzCoffeeOrders, StarBuzzCoffeeDisplay

class TestStarBuzzCoffeeDisplay(unittest.TestCase):

    # pattern 2 - exercise A
    def test_display_all_orders(self):
        """Customers need to know their place in the queue at StarBuzz Coffee ! 
        
        This test covers create a number of test orders.
        This test covers checking the output to the display driver matches 
        the actual sequeue of orders in the queue.
        """
        cafe_orders = StarBuzzCoffeeOrders()
        cafe_orders.new_order("latte")
        cafe_orders.new_order("espresso")
        cafe_display = StarBuzzCoffeeDisplay(cafe_orders)
        expected_display_info = "(0, 'latte')(1, 'espresso')"
        actual_display_info = str(cafe_display)
        self.assertEqual(expected_display_info, actual_display_info)

    # pattern 2 - exercise B
    def test_hiding_initial_test_orders(self):
        """Hide the 2 coffees the baristas have before opening time ! 
        
        StarBuzz Coffee has two amazing baristas. 
        Why are they amazing ? 
        Because they have 1 coffee each before opening time
        Your in-store display should hide these 2 morning coffes
        """
        cafe_orders = StarBuzzCoffeeOrders()
        cafe_orders.new_order("barista_1_morning_latte")
        cafe_orders.new_order("barista_2_morning_americano")
        cafe_orders.new_order("latte")
        cafe_orders.new_order("espresso")
        cafe_display = StarBuzzCoffeeDisplay(cafe_orders, 
                                             num_staff_morning_coffees=2)
        expected_display_info = "(0, 'latte')(1, 'espresso')"
        actual_display_info = str(cafe_display)
        self.assertEqual(expected_display_info, actual_display_info)
    

