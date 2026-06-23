class Booking:
    def __init__(self):
        self.waiting_list = []
        self.booked = []
        self.counter = 1
    
    def add_customer(self):
        name = input("Enter customer name: ")
        show = input("Enter show name: ")
        
        ticket = {
            'number': self.counter,
            'name': name,
            'show': show,
            'status': 'Waiting'
        }
        
        self.waiting_list.append(ticket)
        self.counter += 1
        print(f"\nCustomer {name} added!")
        print(f"Ticket Number: {ticket['number']}")
        print(f"Position: {len(self.waiting_list)}\n")
    
    def book_ticket(self):
        if not self.waiting_list:
            print("\nNo customers waiting!\n")
            return
        
        customer = self.waiting_list.pop(0)
        customer['status'] = 'Booked'
        self.booked.append(customer)
        
        print(f"\nTicket booked for: {customer['name']}")
        print(f"Ticket Number: {customer['number']}\n")
    
    def view_next(self):
        if not self.waiting_list:
            print("\nNo customers waiting!\n")
            return
        
        customer = self.waiting_list[0]
        print(f"\nNext Customer: {customer['name']}")
        print(f"Ticket: #{customer['number']}")
        print(f"Show: {customer['show']}\n")
    
    def show_all(self):
        print("\nWAITING LIST")
        print("-" * 30)
        if not self.waiting_list:
            print("Empty")
        else:
            for i, c in enumerate(self.waiting_list, 1):
                print(f"{i}. {c['name']} - #{c['number']} - {c['show']}")
        print("-" * 30)
        
        print("\nBOOKED TICKETS")
        print("-" * 30)
        if not self.booked:
            print("Empty")
        else:
            for c in self.booked:
                print(f"{c['name']} - #{c['number']} - {c['show']}")
        print("-" * 30)
    
    def run_menu(self):
        while True:
            print("\n" + "=" * 30)
            print("TICKET BOOKING MENU")
            print("=" * 30)
            print("1. Add customer")
            print("2. Book ticket")
            print("3. View next customer")
            print("4. Show all tickets")
            print("5. Exit")
            print("=" * 30)
            
            choice = input("Choose option (1-5): ")
            
            if choice == "1":
                self.add_customer()
            elif choice == "2":
                self.book_ticket()
            elif choice == "3":
                self.view_next()
            elif choice == "4":
                self.show_all()
            elif choice == "5":
                print("\nThank you for using Ticket System!")
                break
            else:
                print("\nInvalid choice! Try again.")


if __name__ == "__main__":
    system = Booking()
    system.run_menu()