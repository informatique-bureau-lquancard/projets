from exchangelib import Credentials, Account

credentials = Credentials('j.martin@bureau-lquancard.fr', 'W<?Klblp_3s6kQe2')
account = Account('j.martin@bureau-lquancard.fr', credentials=credentials, autodiscover=True)

for item in account.inbox.all().order_by('-datetime_received')[:100]:
    print(item.subject, item.sender, item.datetime_received)
