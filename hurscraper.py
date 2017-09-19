import feedparser
import time
from argparse import ArgumentParser
import sys

rss_link = "http://www.nhc.noaa.gov/gis-at.xml"



if __name__ == "__main__":
    parser = ArgumentParser(description="Options to parse RSS Feed")
    parser.add_argument("-t", "--time", dest="time_to_wait", type=int, default=10, help="In seconds how long do you want to wait between checking the rss feed.")

    argv = sys.argv[1:]
    try:
        argp = parser.parse_args(argv)
    except SystemExit as ex:
        print("Eception when parsing args because of => " + str(ex))
        sys.exit()

    try:
        time_to_wait = argp.time_to_wait
    except Exception as ex:
        print("Something went wrong because of => " + str(ex))

    try:
        d = feedparser.parse('http://www.nhc.noaa.gov/gis-at.xml')
    except Exception as ex:
        print("Cannot parse rss feed => " + str(ex))
    print(d.entries[0].title)

  #  for i in d.entries:
  #      if 'Summary' in i.title:
  #          print(i.title)
    for index, item in enumerate(d.entries):
        if 'Summary' in item.title:
            print(index, item.title)
