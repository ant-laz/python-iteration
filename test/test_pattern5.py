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

from src.pattern5 import StarBuzzOrders, StarBuzzCoffeeDisplay

class TestStarBuzzDisplayCoffeeAndFood(unittest.TestCase):

    # pattern 5 - exercise A
    def test_display_all_orders(self):
        """Customers need to see both their food & coffee orders on the big screen!
        
        This test covers created some coffee orders.
        This test covers creating some food orders
        """
        cafe = StarBuzzOrders()
        cafe.new_order(food_order="croissant", coffee_order="latte")
        cafe.new_order(food_order="muffin", coffee_order="cappucino")
        cafe_display = StarBuzzCoffeeDisplay(cafe)
        expected_display_info = "(croissant, latte)(muffin, cappucino)"
        actual_display_info = str(cafe_display)
        self.assertEqual(expected_display_info, actual_display_info)
