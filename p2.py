class Node:
    def __init__(self, bid, title, avb):
        self.bid = bid
        self.title = title
        self.avb = avb
        self.next = None


class Library:
    def __init__(self):
        self.head = None

    def search(self, bid):
        temp = self.head
        while temp:
            if temp.bid == bid:
                return temp
            temp = temp.next
        return None

    def add(self, bid, title, avb=True):
        if self.search(bid):
            print("Book ID already exists.")
            return
        new = Node(bid, title, avb)
        if self.head is None:
            self.head = new
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new
        print("Book added.")

    def display(self):
        if self.head is None:
            print("No books available!")
            return
        temp = self.head
        while temp:
            status = "Yes" if temp.avb else "No"
            print(f"Book ID: {temp.bid}\nTitle: {temp.title}\nAvailable: {status}\n")
            temp = temp.next

    def search_book(self, bid):
        s = self.search(bid)
        if s:
            status = "Yes" if s.avb else "No"
            print(f"Book Found! ID: {s.bid}, Title: {s.title}, Available: {status}")
        else:
            print("Book Not Found!")

    def issue(self, bid):
        s = self.search(bid)
        if s is None:
            print("Book Not Found!")
        elif not s.avb:
            print("Book already issued.")
        else:
            s.avb = False
            print("Book issued.")

    def return_book(self, bid):
        s = self.search(bid)
        if s is None:
            print("Book Not Found!")
        elif s.avb:
            print("Book was not issued.")
        else:
            s.avb = True
            print("Book returned.")


library = Library()

while True:
    print("\n1.Add  2.Display All  3.Search  4.Issue  5.Return  0.Exit")
    ch = input("Choice: ")

    if ch == "1":
        bid = int(input("Book ID: "))
        title = input("Title: ")
        library.add(bid, title)
    elif ch == "2":
        library.display()
    elif ch == "3":
        library.search_book(int(input("Book ID: ")))
    elif ch == "4":
        library.issue(int(input("Book ID: ")))
    elif ch == "5":
        library.return_book(int(input("Book ID: ")))
    elif ch == "0":
        break
    else:
        print("Invalid choice.")