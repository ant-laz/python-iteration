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

class StarBuzzCoffeeInventory:
    """A class to represent the inventory at Star Buzz Coffee..

    It takes a lot of ingredients to make all the kinds of coffee Star Buzz sells. 
    This class represents the inventory management system.
    """

    def __init__(self):
        self.inventory = {}

    def add_item(self, item_name: str, item_quantity: int):
        if item_name not in self.inventory.keys():
            self.inventory[item_name] = item_quantity
        else:
            self.inventory[item_name] += item_quantity

    def use_item(self, item_name: str) -> bool:
        if item_name in self.inventory.keys():
            if self.inventory[item_name] > 0:
                self.inventory[item_name] -= 1
                return True
            else:
                return False #out of stock, quantity = 0
        else:
            return False #item does not exist

    # pattern 3 - exercise A
    def __repr__(self) -> str:            
        return self.list_all_invetory()

    # pattern 3 - exercise A
    def list_all_invetory(self):
        report = ""
        for item, quantity in self.inventory.items():
            report += f"({item}, {quantity})"
        return report

    # pattern 3 - exercise B
    def list_all_items_for_reorder(self):
        report = ""
        for item,quantity in self.inventory.items():
            if quantity == 0:
                report += f"({item})"
        return report

    