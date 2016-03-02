from collections import defaultdict

prices = {"APPL": [1,2,3,4,5,6,7,8,9,20],
		  "GOOG": [1,2,3,4,5,6,7,8,9,22]
		 }

profit = {} 

def maxProfit(prices):
	for stock in prices:
		for i in range(len(prices[stock])):
			profit[stock] = defaultdict(list)
			for i in range(i+1, range(len(prices[stock]))):
