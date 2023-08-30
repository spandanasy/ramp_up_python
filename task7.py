class ATM:
    def __init__(self):
        self.notes_available = [500, 200, 50]

    def validate_amount(self, amount):
        if amount <= 0 or amount % 50 != 0:
            return False
        return True

    def calculate_notes(self, amount):
        notes_count = {}
        remaining_amount = amount
        
        for available in self.notes_available:
            notes_count[available] = remaining_amount // available
            remaining_amount %= available
        return notes_count

    def run(self):
        while True:
            amount_input = input("Enter the amount to withdraw : ")
            
            
            if not amount_input:
                print("Please Enter the Amount Value (It Should Not Be Blank).")
                continue
            
            try:
                amount_ip = int(amount_input)
            except ValueError:
                print("Invalid input. Please Enter Amount In Numbers.")
                continue
            
            if not self.validate_amount(amount_ip):
                print("Invalid amount. Please enter a valid amount (multiple of 50).")
                continue
            
            notes_count = self.calculate_notes(amount_ip)
            print("Output:")
            for available, count in notes_count.items():
                print(f"{available} notes: {count}")

            user_input = input("Press 'C' to continue or 'ENTER' key to cancel: ").upper()
            if user_input == 'C':
                print("Transaction continued.")
            else:
                print("Transaction cancelled.")
                break


if __name__ == "__main__":
    atm = ATM()
    atm.run()
