import sqlite3

from tables import eight_speed

mydb = sqlite3.connect("cassette_finder.db")

eight_speed.get_distributor_8spd(mydb,"Madison")