class Node:
    def __init__(self, pid, name, qty, price):
        self.pid = pid
        self.name = name
        self.qty = qty
        self.price = price
        self.next = None


class ProductList:
    def __init__(self):
        self.head = None

    def search(self, pid):
        temp = self.head
        while temp:
            if temp.pid == pid:
                return temp
            temp = temp.next
        return None

    def add_product(self, pid, name, qty, price):
        if self.search(pid):
            print("Product ID already exists.")
            return
        new = Node(pid, name, qty, price)
        if self.head is None:
            self.head = new
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new
        print("Product added.")

    def search_product(self, pid):
        p = self.search(pid)
        if p:
            print(f"ID: {p.pid}, Name: {p.name}, Qty: {p.qty}, Price: {p.price}")
        else:
            print("Product not found.")

    def update_quantity(self, pid, qty):
        p = self.search(pid)
        if p:
            p.qty = qty
            print("Quantity updated.")
        else:
            print("Product not found.")

    def delete_product(self, pid):
        temp, prev = self.head, None
        while temp and temp.pid != pid:
            prev, temp = temp, temp.next
        if temp is None:
            print("Product not found.")
            return
        if prev is None:
            self.head = temp.next
        else:
            prev.next = temp.next
        print("Product deleted.")

    def display_all(self):
        if self.head is None:
            print("No products.")
            return
        temp = self.head
        while temp:
            print(f"ID: {temp.pid}, Name: {temp.name}, Qty: {temp.qty}, Price: {temp.price}")
            temp = temp.next

    def highest_price(self):
        if self.head is None:
            print("No products.")
            return
        best = self.head
        temp = self.head.next
        while temp:
            if temp.price > best.price:
                best = temp
            temp = temp.next
        print(f"Highest price: {best.name} (ID: {best.pid}) - {best.price}")

    def low_stock(self, limit):
        temp = self.head
        found = False
        while temp:
            if temp.qty < limit:
                print(f"ID: {temp.pid}, Name: {temp.name}, Qty: {temp.qty}")
                found = True
            temp = temp.next
        if not found:
            print("No products below the limit.")


store = ProductList()

while True:
    print("\n1.Add  2.Search  3.Update Qty  4.Delete  5.Display All  6.Highest Price  7.Low Stock  0.Exit")
    ch = input("Choice: ")

    if ch == "1":
        store.add_product(int(input("ID: ")), input("Name: "), int(input("Qty: ")), float(input("Price: ")))
    elif ch == "2":
        store.search_product(int(input("ID: ")))
    elif ch == "3":
        store.update_quantity(int(input("ID: ")), int(input("New Qty: ")))
    elif ch == "4":
        store.delete_product(int(input("ID: ")))
    elif ch == "5":
        store.display_all()
    elif ch == "6":
        store.highest_price()
    elif ch == "7":
        store.low_stock(int(input("Limit: ")))
    elif ch == "0":
        break
    else:
        print("Invalid choice.")