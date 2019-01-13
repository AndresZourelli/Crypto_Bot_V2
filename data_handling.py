import pandas as pd
from candle_builder import candle_builder

class data_Handling():
	def __init__(self, exchange, candle_size):
		#Grabs Old Candles from exchange
		Old_candles = exchange.prev_Candles('1m')
		#Adds Candles to DataFrame
		self.candles = pd.DataFrame(Old_candles)
		#Adds new Header Row to decribe dataFrame columns
		self.candles.columns = ['Time','Open','High','Low','Close','Volume']
		#Builds candle
		self.building_candle = candle_builder(candle_size)
		#Set candle size to be used by entire class
		self.candle_size = candle_size
		#Flag for Clearing candle building function
		self.cleared_candle = False

	def candles_Add(self, new_candle):
		#Adds candle to dataFrame
		self.candles = self.candles.append([new_candle], ignore_index = True)
		#Triggers Candle to Clear after data is received
		self.cleared_candle = True
		print(new_candle)
		

	def candle_Builder(self, price, tick_stats, **kwargs):
		#Builds current candle
		self.building_candle.candle_tick(price, tick_stats)
		#Checks to see if candle is Done
		if self.building_candle.isClosed():
			#Adds candle to dataFrame
			self.candles_Add(self.building_candle.candle_tick(price, tick_stats))
			#Reads optional parameter to see if data received signal is sent
			if self.cleared_candle:
				#Starts New empty candle
				self.building_candle = candle_builder(self.candle_size)
				#Clears Candle Clear Flag
				self.cleared_candle = False
		else:
			return False