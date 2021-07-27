class Category:
    def __init__(self, name):
        self.category_name = name
        self.funds = 0
        self.ledger = []

    def check_funds(self, amount):
        if self.funds >= amount:
            return True
        else:
            return False

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})
        self.funds += amount

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            self.funds -= amount
            return True
        else:
            return False

    def get_balance(self):
        return self.funds

    def transfer(self, amount, transfer_category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {transfer_category.category_name}")

            transfer_category.deposit(amount, f"Transfer from {self.category_name}")
            return True
        else:
            return False

    def __str__(self):
        line1 = f"{self.category_name}".center(30, "*")
        line2 = ""

        for entry in self.ledger:
            desc = entry["description"][:23]
            amount = entry['amount']
            line2 += f"{desc}{amount: >{len(desc) - 30}.2f}\n"
        line_total = f"Total: {self.funds}"
        return f"{line1}\n{line2}{line_total}"

    def get_all_withdrawls(self):
        total = 0
        for entry in self.ledger:
            if entry["amount"] < 0:
                total += entry["amount"]

        return round(total, 2)


def create_spend_chart(categories):
    spent = []
    percentages = []
    for category in categories:
        spent.append(category.get_all_withdrawls())

    for amount in spent:
        percentage = round((amount / sum(spent)), 1) * 100
        percentages.append(percentage)

    title = "Percentage spent by category\n"

    graph = ""

    for interval in range(100, -10, -10):
        graph += str(interval).rjust(3) + "| "
        for percent in percentages:
            if int(percent) >= interval:
                graph += "o  "
            else:
                graph += " " * 3
        graph += "\n"

    graph += " " * 4 + "-" * ((len(categories) * 2) + 4)
    # graph += "\n" + " "*5

    # find max name len
    maxx_name_len = 0
    maxx_name = None
    # print(len(categories))
    for category in categories:
        name = category.category_name
        if len(name) > maxx_name_len:
            maxx_name_len = len(name)
            maxx_name = name

    # print(maxx_name_len)
    # print(maxx_name)

    vertical_names = ""
    for i in range(maxx_name_len):
        if i < maxx_name_len:
            vertical_names += "\n" + " " * 5
        for category in categories:
            name = category.category_name
            if len(name) > i:
                vertical_names += name[i] + " " * 2
            else:
                vertical_names += " " * 3

    # graph = graph.rstrip() + "\n"
    vertical_names = vertical_names.rstrip("\n")
    return f"{title}{graph}{vertical_names}"
