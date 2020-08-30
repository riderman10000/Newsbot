"""
** Personal Project **
This is a personal project for providing updates regarding the COVID-19 outbreak.
Date: 21st March, 2020
Coded by: Abiskar Timsina

"""
from classes.corona_data import *
import sys

obj_corona_data = corona_data_scrapper()
obj_corona_news = corona_news_scrapper()

if '-h' in sys.argv:
	print("# usage of the script ")
	print("$ python main.py 			\n-- takes you to main program for news and update features.")
	print("$ python main.py country <county_name>\n -- print the data of the country entered.")
	print("also\n$ python main.py county <county_name1> <county_name2> <county_name3> ...")
	print("-- prints the data of multiple countries.")

if len(sys.argv) == 1: 
	while (1):
		a = input ("Welcome to Webscrepper: ")
		if (a == "!news"):
			obj_corona_news.main()
		elif (a == "!update"):
			obj_corona_data.main()
		else:
			continue
elif len(sys.argv) > 1:
	if 'country' in sys.argv[1].lower():
		obj_corona_data.main(sys.argv[2:]) 