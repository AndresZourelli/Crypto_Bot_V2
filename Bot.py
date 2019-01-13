
import time
from exchange_interaction import Exchange_Access
from data_handling import data_Handling
from accounts import account
from candle_builder import candle_builder
# Enter Desired Coin Pairings here
desired_Coin = 'ETC/USD' 
desired_Exchange = 'coinbasepro'

def Bot(Crypto_Name):
	#set candle how long it takes to build candle
	candle_size = 10
	#Calling initial functions
	#Calls excange functions
	exchange = Exchange_Access(desired_Exchange, Crypto_Name)
	#Stores data from old candles in data frame
	data_Handlings = data_Handling(exchange, candle_size)

	#account function to get account information
	accounts = account(desired_Exchange)

	while True:
		#Gets Crypto Curreny information from Exchange
		price, tick_stats = exchange.ticker()

		#takes in information from Exchange to Build Candle
		data_Handlings.candle_Builder(price, tick_stats)

		print(price)
		
		#Limits API calling to exchange limit
		time.sleep(exchange.rateLimit())





#----------------Run Function------------------------------
Bot(desired_Coin)