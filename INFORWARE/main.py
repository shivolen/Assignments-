from PySide6.QtWidgets import QApplication
from ui import BillingApp
import sys
import database


class App(BillingApp):
    def __init__(self):
        super().__init__()


        self.add_customer_btn.clicked.connect(self.add_customer)
        self.add_bill_btn.clicked.connect(self.add_bill)
        self.view_customers_btn.clicked.connect(self.show_customers)
        self.view_bills_btn.clicked.connect(self.show_bills)

    def add_customer(self):
        name = self.name_input.text()
        email = self.email_input.text()
        phone = self.phone_input.text()
        if name and email and phone:
            database.insert_customer(name, email, phone)
            self.output_list.addItem(f"Added Customer: {name}")

    def add_bill(self):
        customer_id = 1
        amount = self.amount_input.text()
        if amount:
            database.insert_bill(customer_id, float(amount))
            self.output_list.addItem(f"Added Bill: ${amount}")

    def show_customers(self):
        self.output_list.clear()
        customers = database.fetch_customers()
        for c in customers:
            self.output_list.addItem(f"{c[0]} - {c[1]} - {c[2]} - {c[3]}")

    def show_bills(self):
        self.output_list.clear()
        bills = database.fetch_bills()
        for b in bills:
            self.output_list.addItem(f"{b[0]} - Customer ID: {b[1]} - ${b[2]}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec())
