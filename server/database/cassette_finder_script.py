import sqlite3

from database.tables.eight_speed import insertEightSpeedData, createEightSpeedTable, get_speed_ratio_brand_8spd
from database.tables.nine_speed import insertNineSpeedData, createNineSpeedTable, get_speed_9spd, get_speed_9spd_all, get_speed_ratio_9spd
from database.tables.ten_speed import insertTenSpeedData, createTenSpeedTable, get_speed_10spd, get_speed_10spd_all, get_speed_ratio_10spd
from database.tables.eleven_speed import insertElevenSpeedData, createElevenSpeedTable, get_speed_11spd, get_speed_11spd_all, get_speed_ratio_11spd
from database.tables import distributor_table

createEightSpeedTable()
insertEightSpeedData()
# get_speed_8spd("*")
# get_speed_8spd_all()
get_speed_ratio_brand_8spd("*","*","*")

createNineSpeedTable()
insertNineSpeedData()
get_speed_9spd("*")
get_speed_9spd_all()
get_speed_ratio_9spd("*")

createTenSpeedTable()
insertTenSpeedData()
get_speed_10spd("*")
get_speed_10spd_all()
get_speed_ratio_10spd("*")

createElevenSpeedTable()
insertElevenSpeedData()
get_speed_11spd("*")
get_speed_11spd_all()
get_speed_ratio_11spd("*")
