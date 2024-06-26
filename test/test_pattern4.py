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

from src.pattern4 import StarBuzzCoffeeBilling

class TestStarBuzzCoffeeBilling(unittest.TestCase):

    # pattern 4 - exercise A
    def test_total_revenue_report(self):
        """Your new start-up StarBuzz Coffee needs to report on all transactions! 
        
        This covers creating a billing system
        This test covers ordering some coffee
        This test covers calcuting the total revenue across all transactions.
        """
        cafe_billing = StarBuzzCoffeeBilling()
        cafe_billing.process_order(cusotmer_loyalty_id=1, order_item="latte")
        cafe_billing.process_order(cusotmer_loyalty_id=2, order_item="cappucino")
        expected_total_revenue = 3
        actual_total_revenue = cafe_billing.report_total_revenue()
        self.assertEqual(expected_total_revenue, actual_total_revenue)

    # pattern 4 - exercise B
    def test_vip_program_promotion(self):
        """A new promotion invites all odd numbered customers to a new VIP program! 
        
        To generate more business for StarBuzz Coffee you decide to run a promotion.
        You examine the sequence of customers buying coffee. 
        If in that sequence a customer occupies an odd slot, you invite them to a VIP program.
        Also, only the first 10 odd slots are eligible.
        Example customer sequence
        slot 0 - customer_loyalty_id=265
        slot 1 - customer_loyalty_id=555
        slot 2 - customer_loyalty_id=988
        slot 3 - customer_loyalty_id=333
        In this sequence the slot 1 & slot 3 slots are odd.
        So customer_loyalty_id=555 & customer_loyalty_id=333 are invited to the VIP program.
        customer_loyalty_id=265 is ignored because their sequence slot was even.
        customer_loyalty_id=988 is ignored because their sequence slot was even.
        """
        cafe_billing = StarBuzzCoffeeBilling()
        cafe_billing.process_order(cusotmer_loyalty_id=265, order_item="latte")
        cafe_billing.process_order(cusotmer_loyalty_id=555, order_item="latte")
        cafe_billing.process_order(cusotmer_loyalty_id=988, order_item="cappucino")
        cafe_billing.process_order(cusotmer_loyalty_id=333, order_item="americano")
        expected_vip_invitee_list = "(555)(333)"
        actual_vip_invitee_list = cafe_billing.invite_customers_with_odd_sequence_slots_to_vip_program()
        self.assertEqual(expected_vip_invitee_list, actual_vip_invitee_list)
    

