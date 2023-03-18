# CSV Command-Line Tool 

This is a command-line utility for performing operations on CSV data. It uses `argparse` module to manage command line arguments. The tool supports the following commands:

`count`: count the number of rows in a CSV file  
`mean`: calculate the mean value of a specified column in the CSV file  
`filter`: filter the CSV data by a specified value in a specified column  
`std_dev`: calculate the Standard Deviation of a specified column in the CSV file  
`sort`: sort the CSV data by a specified column  

## Getting Started

1. Clone the repository to your local machine:  
   ```
   git clone https://github.com/<username>/csv-command-line-tool.git
	```
3. Install the required Python packages:
	```
	pip install pandas
	pip install termcolor
	```
4. Run the tool:
	```
	python main.py --load <path_to_csv_file> --command <command> --column <column_name> --value <filter_value>
	```


Replace `<path_to_csv_file>` with the path to your CSV file, `<command>` with one of the supported commands, `<column_name>` with the name of the column you want to operate on (required for `mean`, `filter`, `std_dev`, and `sort` commands), and `<filter_value>` with the value you want to filter by (required for filter command).  

## Example Usage

To count the number of rows in the example `data.csv` CSV file:  

````
python main.py --load data.csv --command count  
````

To find the Standard Deviation of Even Numbers in the given `data.csv` file:

````
python main.py --load data.csv --command std_dev --column 'Even Numbers'
````

## Unit Tests

To run the tests, enter the following command:

```
python test_main.py
```

This will execute all of the unit tests contained in the `test_main.py file.
