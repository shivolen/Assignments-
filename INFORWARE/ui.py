from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLineEdit, QLabel, QListWidget

class BillingApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Billing System")
        self.setGeometry(100, 100, 400, 300)
        layout = QVBoxLayout()

        # Input fields
        self.name_input = QLineEdit(self)
        self.name_input.setPlaceholderText("Enter Name")
        self.email_input = QLineEdit(self)
        self.email_input.setPlaceholderText("Enter Email")
        self.phone_input = QLineEdit(self)
        self.phone_input.setPlaceholderText("Enter Phone")
        self.amount_input = QLineEdit(self)
        self.amount_input.setPlaceholderText("Enter Amount")

        # Buttons
        self.add_customer_btn = QPushButton("Add Customer", self)
        self.add_bill_btn = QPushButton("Add Bill", self)
        self.view_customers_btn = QPushButton("View Customers", self)
        self.view_bills_btn = QPushButton("View Bills", self)

        # Output field
        self.output_list = QListWidget()

        # Add widgets to layout
        layout.addWidget(self.name_input)
        layout.addWidget(self.email_input)
        layout.addWidget(self.phone_input)
        layout.addWidget(self.add_customer_btn)
        layout.addWidget(self.amount_input)
        layout.addWidget(self.add_bill_btn)
        layout.addWidget(self.view_customers_btn)
        layout.addWidget(self.view_bills_btn)
        layout.addWidget(self.output_list)

        self.setLayout(layout)
