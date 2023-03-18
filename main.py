import csv
import argparse
import statistics
import pandas as pd
from termcolor import colored

ERROR_MESSAGE = "An error occurred.\nPlease make sure you provide all the required arguments correctly"

def load(filename):
	try:
		with open(filename, 'r') as file:
			reader = csv.reader(file)
			return list(reader)
	except:
		return ERROR_MESSAGE


def count_rows(data):
	try:
		return len(data) - 1
	except:
		return colored(ERROR_MESSAGE, "red")


def mean_column(data, column_name):
	try:
		header = data[0]
		column_index = header.index(column_name)
		column_data = [float(row[column_index]) for row in data[1:]]
		return statistics.mean(column_data)
	except:
		return colored(ERROR_MESSAGE, "red")
		

def filter_rows(data, column_name, value):
	try:
		header = data[0]
		column_index = header.index(column_name)
		filtered_data = [row for row in data if row[column_index] == value]
		return filtered_data
	except:
		return colored(ERROR_MESSAGE, "red")


def std_dev(data, column_name):
	try:
		header = data[0]
		column_index = header.index(column_name)
		column_data = [float(row[column_index]) for row in data[1:]]
		value = statistics.stdev(column_data)
		return round(value, 2)
	except:
		return colored(ERROR_MESSAGE, "red")


def sort_dataframe(df, colname):
	try:
		sorted_df = df.sort_values(by=colname)
		return sorted_df
	except:
		return colored(ERROR_MESSAGE, "red")


def parse_args():
	parser = argparse.ArgumentParser(description='CSV command-line tool')
	parser.add_argument('--load', help='Load the CSV file on which operations have to ber performed in format : file.csv')
	parser.add_argument(
	 '--command',
	 choices=['count', 'mean', 'filter', 'exit', 'std_dev', 'sort'],
	 help='Commands to execute')
	parser.add_argument('--column',
	                    help='Column to use for mean, filter or std_dev command')
	parser.add_argument('--value', help='Value to use for filter command')
	return parser.parse_args()


def main():
	args = parse_args()
	if (args.load == None):
		print("This is a Command line Utility for performing operations on CSV data.")
		print("Run 'python main.py -h' to get started.")
	elif (args.command == None):
		print(colored("No Commands provided.", "red"))
		print(colored("Run 'python main.py -h' to learn more.", "yellow"))
	else:
		data = load(args.load)
		data_pd = pd.read_csv(args.load)
	
		if args.command == 'count':
			print(count_rows(data))
		elif args.command == 'mean':
			print(mean_column(data, args.column))
		elif args.command == 'filter':
			filtered_data = filter_rows(data, args.column, args.value)
			if len(filtered_data) == 0:
				print("No matching values.")
			else:
				# print(data[0][0])
				for header in data[0]:
					print(header, end=", ")
				print()
				for row in filtered_data:
					print(','.join(row))
		elif args.command == 'std_dev':
			print(std_dev(data, args.column))
		elif args.command == 'sort':
			print("Sorted Data")
			print(sort_dataframe(data_pd, args.column))
		elif args.command == 'exit':
			return


if __name__ == '__main__':
	main()
