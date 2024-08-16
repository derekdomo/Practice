from collections import defaultdict
from dataclasses import dataclass
TTL = 10
@dataclass
class Transfer:
    transfer_id: str
    from_acc: str
    to_acc: str
    timestamp: int
    amount: int
    complete: bool

class BankSystem:
    def __init__(self):
        self.accounts = set()
        self.balance = defaultdict(int)
        self.activity_value = defaultdict(dict)
        self.pending_activities = []
        self.transfer_id = 0

    def _add_money(self, account, value):
        if account not in self.accounts:
            return "false"
        self.balance[account] += value
        self.activity_value[account] += value
        return "true", self.balance[account]

    def _withdraw_money(self, account, value):
        if account not in self.accounts:
            return "false"
        if self.balance[account] < value:
            return "false"
        self.balance[account] -= value
        self.activity_value[account] += value
        return "true"
    
    def process_query(self, query):
        action = query[0]
        timestamp = int(query[1])
        params = query[2:]
        if action == 'CREATE_ACCOUNT':
            account = params[0]
            if account in self.accounts:
                return "false", "an accouont with this identifier already exists"
            self.accounts.add(account)
            self.activity_value[account] = 0
            return "true"
        elif action == "DEPOSIT":
            account, amount = params 
            success, amount = self._add_money(account, int(amount))
            if success == 'true':
                return amount
            return success
        elif action == 'PAY':
            account, amount = params
            return self._withdraw_money(account, int(amount))
        elif action == 'TOP_ACTIVITY':
            k = int(params[0])
            sorted_activities = sorted(self.activity_value.items(), key=lambda x: x[1], reverse=True)
            return [f'{key}({value})' for key, value in sorted_activities[:k]]
        elif action == 'TRANSFER':
            amount = int(params[2])
            from_acc = params[0]
            to_acc = params[1]

            if from_acc == to_acc:
                return "same account"

            success = self._withdraw_money(from_acc, amount)
            if success == 'true':
                self.transfer_id += 1
                self.pending_activities.append(Transfer(
                        f"transfer{self.transfer_id}",
                        from_acc,
                        to_acc,
                        timestamp + TTL,
                        amount,
                        False
                        ))
                return f"transfer{self.transfer_id}"
            else:
                return "" 
        elif action == 'ACCEPT_TRANSFER':
            to_account = params[0]
            transfer_id = params[1]
            for t in self.pending_activities:
                if transfer_id == t.transfer_id:
                    if to_account == t.to_acc:
                        if t.complete:
                            return "false"
                        elif timestamp <= t.timestamp:
                            t.complete = True
                            return self._add_money(to_account, t.amount)
                        else:
                            self._add_money(t.from_acc, t.amount)
                            return "false"
                    else:
                        return "false"
            return "false"

queries = [
    ['CREATE_ACCOUNT', '1', 'account1'],
    ['CREATE_ACCOUNT', '2', 'account2'],
    ['DEPOSIT', '3', 'account1', '2000'],
    ['DEPOSIT', '4', 'account2', '3000'],
    ['TRANSFER', '5', 'account1', 'account2', '5000'],
    ['TRANSFER', '6', 'account1', 'account2', '1000'],
    ['ACCEPT_TRANSFER', '7', 'account1', 'transfer1'],
    ['ACCEPT_TRANSFER', '8', 'account2', 'transfer1'],
    ['ACCEPT_TRANSFER', '8', 'account2', 'transfer1'],
    ['TRANSFER', '9', 'account1', 'account2', '1000'],
    ['ACCEPT_TRANSFER', '30', 'account2', 'transfer2']
]

bank_system = BankSystem()
for query in queries:
    print(bank_system.process_query(query))


            







