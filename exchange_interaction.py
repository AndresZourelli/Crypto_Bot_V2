import ccxt


class Exchange_Access():
	def __init__(self, exchange_name, coin):
		#Uses inputed Exchange Name variable and gets the attribute from the ccxt Object
		#Allows function to be used with multiple exchanges
		#Instantiated class instance for ccxt
		self.exchange = getattr(ccxt, exchange_name)()
		#stores current tickm and price
		self.tick = 0
		self.price = 0
		#stores currency name 
		self.currency = coin

	def ticker(self):
		#Pings API and gets Latest Price and checks if function exists in exchange
		try:
			if self.exchange.has['fetchTicker']:

				self.tick = self.exchange.fetchTicker(self.currency)
				self.price = self.tick['close']
				return self.price, self.tick
			else:
				print( 'Does not have fetch_ticker function')
		#Catches any exchange errors and prevents bot from crashing
		except:
			 print("Error Occured")
			 print("Attempting to reconnect...")
			 
			 return self.price, self.tick

	def rateLimit(self):
		# exchange.rateLimit returns in miliseconds so need to change to seconds
		seconds = self.exchange.rateLimit/1000
		return seconds

	def prev_Candles(self,time_length):
		#pings api to check if it has candles and if it does returns values
		if self.exchange.has['fetchOHLCV']:
			#returns list of lists values at end of time period 
			return  self.exchange.fetchOHLCV(self.currency, time_length)
		else:
			print('No fetchOHLCV function exists')

