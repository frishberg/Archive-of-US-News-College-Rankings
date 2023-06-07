import json
import csv

f = open("data.csv", "r")
reader = csv.reader(f)
data = list(reader)
f.close()

years = [2023, 2022, 2021, 2020, 2019, 2018, 2017, 2016, 2015, 2014, 2013, 2012, 2011, 2010, 2009, 2008, 2007, 2006, 2005, 2004, 2003, 2002, 2001, 2000, 1999, 1998, 1997, 1996, 1995, 1994, 1993, 1992, 1991, 1990, 1989, 1988, 1986, 1984]
json_data = {}

for x in data:
    name = x[0]
    ranks = x[1:]
    json_data[name] = {}
    for i in range(len(years)):
        json_data[name][str(years[i])] = ranks[i]

f = open("data.json", "w")
f.write(json.dumps(json_data))