import random
import datetime

# -----------------------------------------------

# Programmer : Peyton John Hall

# Date       : 05/13/2026

# Description: Mama Papa Shop Point-of-Sale (POS) 
#              System

# -----------------------------------------------

class POSSystem:
    """
    POSSystem is the progenitor class, from
    which all other classes inherit data.

    @inherits None
    """
    def __init__(self):
        """
        The presumption, is that, the only objects which should be accessed by
        child classes, viz. globally accessable objects, are objects where it 
        would not be a grave matter for them to be, for whatever reason, 
        corrupted. If a corruption should occur, of which its consequence would
        be a trivial matter, refinements to the program could be made, or, if 
        the corruption were brought about through maliscious intent, the 
        programmer(s) held liable could be fired or even become (a) 
        defendant(s) in what would be a breach of contract lawsuit.
        However, for highly sensitive data, like usernames and passwords, 
        if private objects are made of them, then that would imply, that, 
        not only would those objects not be able to be inherited, accessed,
        and, therefore, potentially corrupted by child classes, but, 
        if, in the progenitor class, perhaps, for example, might I say, chunks
        of code were furnished with restricted visual access through access 
        modifiers, whereby, if a subordinate programmer even had the privilege
        to access the uneditable progenitor class, then that programmer 
        would be incapable of discovering sensitive information like a 
        dictionary of usernames and passwords from protected chunks, 
        then the users whose usernames and passwords are lodged 
        into the system would be secure. 
        """
        self.__users = {}
        self.inventory = {}
        self.sales_log = {}
        self.current_user = None
        self.current_sale = None

    def load_inventory(self):
        """
        Negative indexing is used here because some item descriptions
        contain commas, which makes it impossible to know which column
        the numeric fields start at when counting from the left.
        """
        with open("""RetailStoreItemData.txt""", """r""") as myFile:
            next(myFile)
            for eachLine in myFile:
                parts = eachLine.strip().split(""",""")
                Item_UPC = parts[0]
                Item_Description = """,""".join(parts[1:-5])
                Item_Max_Qty = parts[-5]
                Item_Order_Threshold = parts[-4]
                Item_Replenishment_Order_Qty = parts[-3]
                Item_On_Hand = parts[-2]
                Item_Unit_Price = parts[-1]
                itemObject = Item(Item_UPC, Item_Description,
                                  Item_Max_Qty, Item_Order_Threshold,
                                  Item_Replenishment_Order_Qty,
                                  Item_On_Hand, Item_Unit_Price)
                self.inventory[Item_UPC] = itemObject

    def runPOSSystem(self):
        self.load_inventory()
        print("""\n"""
              """The POS system is running. """)

        self.__users["""c1"""] = User("""c1""", """pass123""", """Ali Naqvi""")
        self.__users["""c2"""] = User("""c2""", """pass222""", """Ana""")
        self.__users["""admin"""] = User("""admin""", """admin123""",
                                         """Store Manager""")

        while True:
            userID = input("""Enter a valid UserID: """)
            password = input("""Enter a valid password: """)

            if (userID in self.__users):
                user = self.__users[userID]
                if (user.locked):
                    print("""Your account has been locked. """)
                    return

                if (user.verify_credentials(password)):
                    print("""\n"""
                          """You have entered the system. """)
                    while True:
                        print("""Declare what you intend to do by """
                              """furnishing the program with an integer. """
                              """\n"""
                              """Each integer represents the following:"""
                              """\n"""
                              """0. Exit. """
                              """\n"""
                              """1. New Sale. """
                              """\n"""
                              """2. Return Item(s). """
                              """\n"""
                              """3. Backroom Operations. """)
                        selection = input()
                        try:
                            selectInt = int(selection)
                        except ValueError:
                            print("""Your selection is insufficient. """)
                            continue
                        if (selectInt == 0):
                            return
                        elif (selectInt == 1):
                            NewSale().run(self.inventory, self.sales_log)
                        elif (selectInt == 2):
                            ReturnItems().run(self.inventory, self.sales_log)
                        elif (selectInt == 3):
                            BackroomOperations().run(self.inventory, 
                                                     self.sales_log)
                        else:
                            print("""Invalid input. """)
                else:
                    print("""An improper userid or """
                          """password has been furnished. """)
                    user.failed_attempts = user.failed_attempts + 1
                    if (user.failed_attempts >= 3):
                        user.locked = True
                    continue

class Item(POSSystem):
    """
    A representation of a single item of merchandise, furnished with
    a universal product code, a description of its nature, quantities
    controlling its presence upon the shelf and in the storeroom, a price
    set upon it, and the faculty of determining whether replenishment
    is warranted.

    @inherits inventory (POSSystem)
    @inherits current_user (POSSystem)
    @inherits current_sale (POSSystem)
    """

    def __init__(self, Item_UPC, Item_Description, Item_Max_Qty,
                 Item_Order_Threshold, Item_Replenishment_Order_Qty,
                 Item_On_Hand, Item_Unit_Price):
        # super invokes the parent; nothing exists without the POSSystem
        super().__init__()
        self.__Item_UPC = Item_UPC
        self.__Item_Description = Item_Description
        self.__Item_Max_Qty = Item_Max_Qty
        self.__Item_Order_Threshold = Item_Order_Threshold
        self.__Item_Replenishment_Order_Qty = Item_Replenishment_Order_Qty
        self.__Item_On_Hand = Item_On_Hand
        self.__Item_Unit_Price = Item_Unit_Price

    def get_Item_UPC(self):
        return self.__Item_UPC
    def get_Item_Description(self):
        return self.__Item_Description
    def get_Item_Max_Qty(self):
        return self.__Item_Max_Qty
    def get_Item_Order_Threshold(self):
        return self.__Item_Order_Threshold
    def get_Item_Replenishment_Order_Qty(self):
        return self.__Item_Replenishment_Order_Qty
    def get_Item_On_Hand(self):
        return self.__Item_On_Hand
    def get_Item_Unit_Price(self):
        return self.__Item_Unit_Price

    def set_Item_UPC(self, Item_UPC):
        self.__Item_UPC = Item_UPC
    def set_Item_Description(self, Item_Description):
        self.__Item_Description = Item_Description
    def set_Item_Max_Qty(self, Item_Max_Qty):
        self.__Item_Max_Qty = Item_Max_Qty
    def set_Item_Order_Threshold(self, Item_Order_Threshold):
        self.__Item_Order_Threshold = Item_Order_Threshold
    def set_Item_Replenishment_Order_Qty(self, Item_Replenishment_Order_Qty):
        self.__Item_Replenishment_Order_Qty = Item_Replenishment_Order_Qty
    def set_Item_On_Hand(self, Item_On_Hand):
        self.__Item_On_Hand = Item_On_Hand
    def set_Item_Unit_Price(self, Item_Unit_Price):
        self.__Item_Unit_Price = Item_Unit_Price
    def update_on_hand(self, quantity):
        """
        Adjusts on-hand quantity by the given amount.
        Negative values reflect sales; positive values reflect restocking.
        """
        self.__Item_On_Hand = float(self.__Item_On_Hand) + float(quantity)
    def needs_reorder(self):
        """
        Returns a boolean.
        It is True if on-hand quantity is at or below the order threshold.
        """
        reorder = float(self.__Item_On_Hand) <= float(self.__Item_Order_Threshold)
        return reorder

class User(POSSystem):
    """
    A representation of a person lawfully admitted to operate the 
    system, bearing credentials by which their identity may be confirmed 
    and their access either granted or withheld upon repeated failure.

    @inherits inventory (POSSystem)
    @inherits current_user (POSSystem)
    @inherits current_sale (POSSystem)
    """
    def __init__(self, uid, pw, name):
        """ defines instance variables """
        # super invokes the parent; nothing exists without the POSSystem
        super().__init__()
        self.user = uid
        self.password = pw
        self.name = name
        self.failed_attempts = 0
        self.locked = False

    def verify_credentials(self, password):
        # the user alone knows if the password is correct
        return self.password == password

class Sale(POSSystem):
    """
    A representation of a completed transaction, bearing a receipt number
    by which it may be retrieved, the items exchanged, the total tendered,
    the moment of its occurrence, and a designation of whether it
    constitutes a sale or a return.
    Claude was used for help in the implementation.
 
    @inherits inventory (POSSystem)
    @inherits current_user (POSSystem)
    @inherits current_sale (POSSystem)
    """
    def __init__(self, receipt_number, items, total, timestamp,
                 is_return=False):
        # super invokes the parent; nothing exists without the POSSystem
        super().__init__()
        self.__receipt_number = receipt_number
        self.__items = items
        self.__total = total
        self.__timestamp = timestamp
        self.__is_return = is_return
 
    def get_receipt_number(self):
        return self.__receipt_number
    def get_items(self):
        return self.__items
    def get_total(self):
        return self.__total
    def get_timestamp(self):
        return self.__timestamp
    def get_is_return(self):
        return self.__is_return

class NewSale(POSSystem):
    """
    The means by which a new transaction is
    initiated and brought to its conclusion.
    Claude was used for help in the implementation.
 
    @inherits inventory (POSSystem)
    @inherits current_user (POSSystem)
    @inherits current_sale (POSSystem)
    """
    def run(self, inventory, sales_log):
        sale_items = []
        total = 0.0
        while True:
            upc = input("""Enter UPC (or "0" to finish): """)
            if (upc == """0"""):
                break
            if (upc not in inventory):
                print("""Item not found. """)
                continue
            item = inventory[upc]
            qty_input = input("""Enter quantity: """)
            try:
                qty = int(qty_input)
            except ValueError:
                print("""Invalid quantity. """)
                continue
            if (qty <= 0):
                print("""Quantity must be greater than zero. """)
                continue
            if (float(item.get_Item_On_Hand()) < qty):
                print("""Insufficient stock. """)
                continue
            price = float(item.get_Item_Unit_Price())
            subtotal = price * qty
            total += subtotal
            sale_items.append((item, qty, subtotal))
            item.update_on_hand(-qty)
            print(item.get_Item_Description()
                  + """ | Qty: """ + str(qty)
                  + """ | Price: $""" + str(round(price, 2))
                  + """ | Subtotal: $""" + str(round(subtotal, 2)))
 
        if (not sale_items):
            print("""No items were sold. """)
            return
 
        print("""\n"""
              """Total: $""" + str(round(total, 2)))
 
        while True:
            cash_input = input("""Enter cash tendered: $""")
            try:
                cash = float(cash_input)
            except ValueError:
                print("""Invalid amount. """)
                continue
            if (cash < total):
                print("""Insufficient cash. Total is $"""
                      + str(round(total, 2)))
                continue
            break
 
        change = cash - total
        receipt_number = random.randint(10000000, 99999999)
        while (receipt_number in sales_log):
            receipt_number = random.randint(10000000, 99999999)
 
        timestamp = datetime.datetime.now()
        sale = Sale(receipt_number, sale_items, total, timestamp,
                    is_return=False)
        sales_log[receipt_number] = sale
 
        print("""Change: $""" + str(round(change, 2)))
        print("""Receipt number: """ + str(receipt_number))

class ReturnItems(POSSystem):
    """
    The means by which goods previously exchanged for tender
    are received back into the possession of the establishment.
    Claude was used for help in the implementation.
 
    @inherits inventory (POSSystem)
    @inherits current_user (POSSystem)
    @inherits current_sale (POSSystem)
    """
    def run(self, inventory, sales_log):
        receipt_input = input("""Enter receipt number: """)
        try:
            receipt_number = int(receipt_input)
        except ValueError:
            print("""Invalid receipt number. """)
            return
 
        if (receipt_number not in sales_log):
            print("""Receipt not found. """)
            return
 
        sale = sales_log[receipt_number]
 
        if (sale.get_is_return()):
            print("""That receipt number belongs to a return, """
                  """not a sale. """)
            return
 
        print("""1. Return Single Item"""
              """\n"""
              """2. Return All Items""")
        sub = input("""Select option: """)
 
        if (sub == """1"""):
            upc = input("""Enter UPC of item to return: """)
            found = None
            for (item, qty, subtotal) in sale.get_items():
                if (item.get_Item_UPC() == upc):
                    found = (item, qty, subtotal)
                    break
            if (found is None):
                print("""Item not found on that receipt. """)
                return
            item, sold_qty, sold_subtotal = found
            print("""You entered: """ + item.get_Item_Description())
            qty_input = input("""Enter quantity to return: """)
            try:
                qty = int(qty_input)
            except ValueError:
                print("""Invalid quantity. """)
                return
            if (qty <= 0):
                print("""Quantity must be greater than zero. """)
                return
            if (qty > sold_qty):
                print("""Cannot return more than was sold. """)
                return
            item.update_on_hand(qty)
            refund = float(item.get_Item_Unit_Price()) * qty
            print("""Return Amount: $""" + str(round(refund, 2)))
            ret_receipt = random.randint(10000000, 99999999)
            while (ret_receipt in sales_log):
                ret_receipt = random.randint(10000000, 99999999)
            timestamp = datetime.datetime.now()
            ret_sale = Sale(ret_receipt, [(item, qty, refund)],
                            refund, timestamp, is_return = True)
            sales_log[ret_receipt] = ret_sale
 
        elif (sub == """2"""):
            confirm = input("""Are you sure you want to return """
                            """all items? Y = yes, N = No: """)
            if (confirm.upper() != """Y"""):
                print("""Return cancelled. """)
                return
            total_refund = 0.0
            for (item, qty, subtotal) in sale.get_items():
                item.update_on_hand(qty)
                total_refund += subtotal
                print("""You entered: """
                      + item.get_Item_Description()
                      + """ Returned""")
            print("""Return Amount: $""" + str(round(total_refund, 2)))
            ret_receipt = random.randint(10000000, 99999999)
            while (ret_receipt in sales_log):
                ret_receipt = random.randint(10000000, 99999999)
            timestamp = datetime.datetime.now()
            ret_sale = Sale(ret_receipt, sale.get_items(),
                            total_refund, timestamp, is_return = True)
            sales_log[ret_receipt] = ret_sale
 
        else:
            print("""Invalid selection. """)

class BackroomOperations(POSSystem):
    """
    The means by which the affairs of the storeroom are
    administered, which includes the inspection and management
    of stock not yet advertised on the floor of trade, and the
    production of daily reports pertaining to sales, shifts,
    orders, and returns.
    Claude was used for help in the implementation.
 
    @inherits inventory (POSSystem)
    @inherits current_user (POSSystem)
    @inherits current_sale (POSSystem)
    """
    def run(self, inventory, sales_log):
        print("""\n"""
              """Backroom Operations:"""
              """\n"""
              """1. Daily Sales Report"""
              """\n"""
              """2. Daily Shift Report"""
              """\n"""
              """3. Daily Order Report"""
              """\n"""
              """4. Daily Returns Report"""
              """\n"""
              """0. Exit""")
        selection = input("""Select option: """)
 
        if (selection == """0"""):
            return
        elif (selection == """1"""):
            self.daily_sales_report(sales_log)
        elif (selection == """2"""):
            self.daily_shift_report(sales_log)
        elif (selection == """3"""):
            self.daily_order_report(inventory)
        elif (selection == """4"""):
            self.daily_returns_report(sales_log)
        else:
            print("""Invalid selection. """)
 
    def daily_sales_report(self, sales_log):
        """
        Produces a 24-hour report of all completed sales,
        enumerating each transaction and its total, with a
        grand total appended at the conclusion.
        """
        print("""\n"""
              """Daily Sales Report:""")
        grand_total = 0.0
        found = False
        for receipt, sale in sales_log.items():
            if (not sale.get_is_return()):
                found = True
                ts = sale.get_timestamp().strftime("""%H:%M:%S""")
                print("""Receipt: """ + str(receipt)
                      + """ | Total: $""" + str(round(sale.get_total(), 2))
                      + """ | Time: """ + ts)
                grand_total += sale.get_total()
        if (not found):
            print("""No sales recorded. """)
        else:
            print("""Grand Total: $""" + str(round(grand_total, 2)))
 
    def daily_shift_report(self, sales_log):
        """
        Partitions all sales into two eight-hour shifts:
        Shift A covers midnight through noon;
        Shift B covers noon through midnight.
        """
        print("""\n"""
              """Daily Shift Report:""")
        shift_a = []
        shift_b = []
        for receipt, sale in sales_log.items():
            if (not sale.get_is_return()):
                if (sale.get_timestamp().hour < 12):
                    shift_a.append(sale)
                else:
                    shift_b.append(sale)
 
        print("""Shift A (12:00 AM - 11:59 AM):""")
        shift_a_total = 0.0
        for sale in shift_a:
            ts = sale.get_timestamp().strftime("""%H:%M:%S""")
            print("""  Receipt: """ + str(sale.get_receipt_number())
                  + """ | Total: $""" + str(round(sale.get_total(), 2))
                  + """ | Time: """ + ts)
            shift_a_total += sale.get_total()
        print("""  Shift A Total: $""" + str(round(shift_a_total, 2)))
 
        print("""Shift B (12:00 PM - 11:59 PM):""")
        shift_b_total = 0.0
        for sale in shift_b:
            ts = sale.get_timestamp().strftime("""%H:%M:%S""")
            print("""  Receipt: """ + str(sale.get_receipt_number())
                  + """ | Total: $""" + str(round(sale.get_total(), 2))
                  + """ | Time: """ + ts)
            shift_b_total += sale.get_total()
        print("""  Shift B Total: $""" + str(round(shift_b_total, 2)))
 
    def daily_order_report(self, inventory):
        """
        Enumerates all items whose on-hand quantity has descended
        to or below the order threshold, which is to say, those
        items for which a replenishment order is warranted.
        """
        print("""\n"""
              """Daily Order Report (items below threshold):""")
        found = False
        for upc, item in inventory.items():
            if (item.needs_reorder()):
                found = True
                print(upc
                      + """ | """ + item.get_Item_Description()
                      + """ | On Hand: """
                      + str(item.get_Item_On_Hand())
                      + """ | Threshold: """
                      + str(item.get_Item_Order_Threshold()))
        if (not found):
            print("""No items require reorder. """)
 
    def daily_returns_report(self, sales_log):
        """
        Produces a report of all returns processed within
        the day, enumerating each return receipt and the
        refund issued, with a total of all refunds appended
        at the conclusion.
        """
        print("""\n"""
              """Daily Returns Report:""")
        total_refund = 0.0
        found = False
        for receipt, sale in sales_log.items():
            if (sale.get_is_return()):
                found = True
                ts = sale.get_timestamp().strftime("""%H:%M:%S""")
                print("""Return Receipt: """ + str(receipt)
                      + """ | Refund: $"""
                      + str(round(sale.get_total(), 2))
                      + """ | Time: """ + ts)
                total_refund += sale.get_total()
        if (not found):
            print("""No returns recorded. """)
        else:
            print("""Total Refunds: $""" + str(round(total_refund, 2)))

class Main(POSSystem):
    """
    The principal means of execution. It is here that the system 
    is set into motion, for the implementation of the class(es) it
    inherits is separated from the calling of their functions.

    @inherits inventory (POSSystem)
    @inherits current_user (POSSystem)
    @inherits current_sale (POSSystem)
    """
    def main(self):
            pos = POSSystem()
            pos.runPOSSystem()

if __name__ == """__main__""":
    Main().main()