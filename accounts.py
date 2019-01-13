
import ccxt  # noqa: E402




class account():

	def __init__(self,exchange_name):
		self.coinbasepro = getattr(ccxt,exchange_name)()
		self.coinbasepro  = getattr(ccxt,exchange_name)({
    	'apiKey': "0e1354dd982e3469614e973122489b04",
    	'secret': "BlZ5JHt1rC6phWO2ZHWuPrHORv08r3ZCdH46f126OzdwRS+ze7P/CmW/NMbSvurV0EWGu/AyHhFR9Ou1BIf9Kw==",
    	'password': 'pw4vlmk5u9',
    	'verbose': False,  # switch it to False if you don't want the HTTP log
		})
	def my_order(self,name):
		return self.coinbasepro.fetchTrades(name)

	def order_id(self,order):
		return self.coinbasepro.parse_order(order)

	
	def order(self,name):
		return self.coinbasepro.fetchOpenOrders(symbol = name)

#-------------------------Get info on current holdings---------------------------------
	def total_USD(self,ticks):
		account_USD = self.coinbasepro.fetch_balance()['free']['USD']
		account_ETC = self.coinbasepro.fetch_balance()['free']['ETC']
		total = account_ETC*ticks + account_USD
		return total

	def balance_USD(self):
		account_USD = self.coinbasepro.fetch_balance()['free']['USD']
		return account_USD

	def balance_ETC(self):
		account_ETC = self.coinbasepro.fetch_balance()['free']['ETC']
		return account_ETC
#--------------------------------------------------------------------------------------

#-----Buy and Sell order placing functions with desired amount parameter---------------
	def buyAmount(self, amount, ticks):
		print("Buy: " + str(amount))
		buy_amount=amount/ticks
		try:
			self.coinbasepro.create_market_buy_order('ETC/USD', amount)
		except:
			print("Attempt to buy made")
			pass
	def sellAmount(self, amount, ticks):
		print("Sell: " + str(amount))
		sell_amount = amount/ticks
		if sell_amount >= 0.01:
			try:
				self.coinbasepro.create_market_sell_order('ETC/USD',  sell_amount)
			except:
				print("Attempt to sell made")
				pass
		else:
			print('Cannot Place Order, Minimun must be 0.01 ETC')
#--------------------------------------------------------------------------------------

#------------Checks on lastX orders paced by other traders and totals it---------------
	def orderTotal(self, lastX):
		order_data = self.coinbasepro.fetch_trades('ETC/USD')
		order_total = 0
		for i in range(lastX):
			if(order_data[i]['side']=='buy'):
				order_total += order_data[i]['amount']
			else:
				order_total -= order_data[i]['amount']
		return order_total
#--------------------------------------------------------------------------------------