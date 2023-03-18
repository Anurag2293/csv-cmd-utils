import unittest
import main
import os
import csv


class TestCSVTool(unittest.TestCase):

	def setUp(self):
		self.filename = "sample.csv"
		self.data = [["Odd Numbers", "Even Numbers"], 
					 ['1', '12'], 
					 ['3', '4'],
		             ['5', '16'], 
					 ['7', '8'], 
					 ['9', '10']]

	def tearDown(self):
		if os.path.exists(self.filename):
			os.remove(self.filename)

	def test_load(self):
		with open(self.filename, 'w') as f:
			writer = csv.writer(f)
			writer.writerows(self.data)

		loaded_data = main.load(self.filename)
		self.assertEqual(loaded_data, self.data)

	def test_count_rows(self):
		count = main.count_rows(self.data)
		self.assertEqual(count, 5)

	def test_mean_column(self):
		mean_age = main.mean_column(self.data, "Even Numbers")
		self.assertAlmostEqual(mean_age, 10, places=2)

	def test_filter_rows(self):
		filtered_data = main.filter_rows(self.data, 'Even Numbers', '4')
		expected_data = [['3', '4']]
		self.assertEqual(filtered_data, expected_data)

	def test_std_dev(self):
		std_dev_age = main.std_dev(self.data, "Even Numbers")
		self.assertAlmostEqual(std_dev_age, 4.47, places=2)

if __name__ == '__main__':
	unittest.main()
