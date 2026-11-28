class TicketStack:
    def __init__(self):
        self.tickets = []          # The list acts as the stack
        self.last_cancelled = None

    def is_empty(self):
        return len(self.tickets) == 0

    # 1. Push a ticket ID when it is booked
    def book(self, ticket_id):
        self.tickets.append(ticket_id)
        print(f"Ticket {ticket_id} booked.")

    # 2. Display all booked ticket IDs (latest first)
    def display(self):
        if self.is_empty():
            print("No tickets booked.")
            return
        print("Booked tickets (latest first):")
        for ticket_id in reversed(self.tickets):
            print(ticket_id)

    # 3. Cancel the most recently booked ticket
    def cancel(self):
        if self.is_empty():
            print("No tickets to cancel.")
            return
        self.last_cancelled = self.tickets.pop()
        print(f"Ticket {self.last_cancelled} cancelled.")

    # 4. Display the cancelled ticket ID
    def show_cancelled(self):
        if self.last_cancelled is None:
            print("No ticket has been cancelled yet.")
        else:
            print(f"Last cancelled ticket: {self.last_cancelled}")

    # 5. Search for a particular ticket ID
    def search(self, ticket_id):
        if ticket_id in self.tickets:
            position = len(self.tickets) - self.tickets.index(ticket_id)
            print(f"Ticket {ticket_id} found at position {position} from the top.")
        else:
            print(f"Ticket {ticket_id} not found.")

    # 6. Display the total number of booked tickets
    def count(self):
        print(f"Total booked tickets: {len(self.tickets)}")


railway = TicketStack()

while True:
    print("\n1.Book  2.Display  3.Cancel  4.Show Cancelled  5.Search  6.Count  0.Exit")
    ch = input("Choice: ")

    if ch == "1":
        railway.book(input("Ticket ID: "))
    elif ch == "2":
        railway.display()
    elif ch == "3":
        railway.cancel()
    elif ch == "4":
        railway.show_cancelled()
    elif ch == "5":
        railway.search(input("Ticket ID: "))
    elif ch == "6":
        railway.count()
    elif ch == "0":
        break
    else:
        print("Invalid choice.")