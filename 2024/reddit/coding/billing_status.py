class BillingStatus:
    def __init__(self, user_id):
        self.user_id = user_id
        self.ad_delivery_pennies = 0
        self.payment_pennies = 0
        self.past_status = []
        self.undo_status = []

    def update_ad_metric(self, ad_metric):
        self.ad_delivery_pennies += ad_metric

    def update_payment_amount(self, payment):
        self.payment_pennies += payment

    def overwrite_status(self, new_ad_metric, new_payment):
        old_ad_metric, old_payment = self.ad_delivery_pennies, self.payment_pennies
        self.ad_delivery_pennies = new_ad_metric
        self.payment_pennies = new_payment
        self.past_status.append((new_ad_metric - old_ad_metric, new_payment - old_payment))
        self.undo_status.clear()

    def add_transaction(self, ad_metric_delta, payment_metric_delta):
        self.past_status.append((ad_metric_delta, payment_metric_delta))
        self.update_ad_metric(ad_metric_delta)
        self.update_payment_amount(payment_metric_delta)
        self.undo_status.clear()

    def undo_last_transaction(self):
        if self.past_status:
            ad_metric_delta, payment_metric_delta = self.past_status.pop()
            self.update_ad_metric(-ad_metric_delta)
            self.update_payment_amount(-payment_metric_delta)
            self.undo_status.append((ad_metric_delta, payment_metric_delta))

    def redo_last_transaction(self):
        if self.undo_status:
            ad_metric_delta, payment_metric_delta = self.undo_status.pop()
            self.update_ad_metric(ad_metric_delta)
            self.update_payment_amount(payment_metric_delta)

    def process_transaction_log(self, log):
        if log.get('undo_last', False):
            self.undo_last_transaction()
        elif log.get('redo_last', False):
            self.redo_last_transaction()
        elif log.get('overwrite', False):
            new_ad_metric = log.get('ad_delivery_pennies', self.ad_delivery_pennies)
            new_payment = log.get('payment_pennies', self.payment_pennies)
            self.overwrite_status(new_ad_metric, new_payment)
        else:
            ad_metric_delta = log.get('ad_delivery_pennies', 0)
            payment_metric_delta = log.get('payment_pennies', 0)
            self.add_transaction(ad_metric_delta, payment_metric_delta)


# Example usage:
log_entry = {
    'overwrite': True,
    'ad_delivery_pennies': 500,
    'payment_pennies': 1000
}
billing_status = BillingStatus(user_id=1)
billing_status.process_transaction_log(log_entry)