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

from src.pattern3 import StarBuzzCoffeeInventory

class TestStarBuzzInventory(unittest.TestCase):

    # pattern 3 - exercise A
    def test_full_inventory_report(self):
        """The manager needs to know everything in the inventory ! 
        
        This test covers creating an inventory. 
        This test covers adding items to the inventory.
        This test covers getting a view of all (item, quantity) pairs in the inventory.
        """
        cafe_inventory = StarBuzzCoffeeInventory()
        cafe_inventory.add_item(item_name="milk", item_quantity=3)
        cafe_inventory.add_item(item_name="coffee_beans", item_quantity=10)
        expected_inventory_report = "(milk, 3)(coffee_beans, 10)"
        actual_inventory_report = str(cafe_inventory)
        self.assertEqual(expected_inventory_report, actual_inventory_report)

    # pattern 3 - exercise B
    def test_out_of_stock_inventory_report(self):
        """The manager needs to know what out of stock items to re-order ! 
        
        This test covers creating an inventory. 
        This test covers adding items to the inventory.
        This test covers getting a view of the (item, quantity) pairs with quantity=0
        """
        cafe_inventory = StarBuzzCoffeeInventory()
        cafe_inventory.add_item(item_name="milk", item_quantity=3)
        cafe_inventory.add_item(item_name="coffee_beans", item_quantity=10)
        cafe_inventory.add_item(item_name="cream", item_quantity=1)
        cafe_inventory.use_item(item_name="cream")
        expected_inventory_report = "(cream)"
        actual_inventory_report = cafe_inventory.list_all_items_for_reorder()
        self.assertEqual(expected_inventory_report, actual_inventory_report)

