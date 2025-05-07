Practical 1.py

class HashTableLP:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * size

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, name, number):
        i = self._hash(name)
        start = i
        while self.table[i] and self.table[i][0] != name:
            i = (i + 1) % self.size
            if i == start:
                print("Table full!")
                return
        self.table[i] = (name, number)
        print("Contact saved.")

    def search(self, name):
        i = self._hash(name)
        start = i
        while self.table[i]:
            if self.table[i][0] == name:
                print(f"{name}: {self.table[i][1]}")
                return
            i = (i + 1) % self.size
            if i == start:
                break
        print("Contact not found.")

    def delete(self, name):
        i = self._hash(name)
        start = i
        while self.table[i]:
            if self.table[i][0] == name:
                self.table[i] = None
                print("Contact deleted.")
                return
            i = (i + 1) % self.size
            if i == start:
                break
        print("Contact not found.")

    def display(self):
        for i, entry in enumerate(self.table):
            print(f"{i}: {entry if entry else 'Empty'}")


class HashTableChaining:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, name, number):
        i = self._hash(name)
        for idx, (k, _) in enumerate(self.table[i]):
            if k == name:
                self.table[i][idx] = (name, number)
                print("Contact updated.")
                return
        self.table[i].append((name, number))
        print("Contact saved.")

    def search(self, name):
        i = self._hash(name)
        for k, v in self.table[i]:
            if k == name:
                print(f"{name}: {v}")
                return
        print("Contact not found.")

    def delete(self, name):
        i = self._hash(name)
        for idx, (k, _) in enumerate(self.table[i]):
            if k == name:
                del self.table[i][idx]
                print("Contact deleted.")
                return
        print("Contact not found.")

    def display(self):
        for i, bucket in enumerate(self.table):
            print(f"{i}: {bucket if bucket else 'Empty'}")


def main():
    print("Select collision method:\n1. Linear Probing\n2. Chaining")
    choice = input("Enter 1 or 2: ")
    table = HashTableLP() if choice == '1' else HashTableChaining()

    while True:
        print("\n1. Insert\n2. Search\n3. Delete\n4. Display\n5. Exit")
        op = input("Select option: ")
        if op == '1':
            name = input("Name: ")
            num = input("Number: ")
            table.insert(name, num)
        elif op == '2':
            name = input("Name to search: ")
            table.search(name)
        elif op == '3':
            name = input("Name to delete: ")
            table.delete(name)
        elif op == '4':
            table.display()
        elif op == '5':
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
