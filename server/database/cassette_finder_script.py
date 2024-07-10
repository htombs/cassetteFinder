import sqlite3

from database.tables.eight_speed import insertEightSpeedData, createEightSpeedTable, get_distributor_8spd, get_brand_8spd, get_speed_8spd, get_ratio_8spd, get_distributor_8spd_all, get_brand_8spd_all, get_speed_8spd_all, get_ratio_8spd_all
from database.tables.nine_speed import insertNineSpeedData, createNineSpeedTable, get_distributor_9spd, get_brand_9spd, get_speed_9spd, get_ratio_9spd, get_distributor_9spd_all, get_brand_9spd_all, get_speed_9spd_all, get_ratio_9spd_all
from database.tables.ten_speed import insertTenSpeedData, createTenSpeedTable, get_distributor_10spd, get_brand_10spd, get_speed_10spd, get_ratio_10spd, get_distributor_10spd_all, get_brand_10spd_all, get_speed_10spd_all, get_ratio_10spd_all
from database.tables.eleven_speed import insertElevenSpeedData, createElevenSpeedTable, get_distributor_11spd, get_brand_11spd, get_speed_11spd, get_ratio_11spd, get_distributor_11spd_all, get_brand_11spd_all, get_speed_11spd_all, get_ratio_11spd_all
from database.tables import distributor_table

createEightSpeedTable()
insertEightSpeedData()
get_distributor_8spd("*")
get_brand_8spd("*")
get_speed_8spd("*")
get_ratio_8spd("*")
get_distributor_8spd_all("*")
get_brand_8spd_all("*")
get_speed_8spd_all("*")
get_ratio_8spd_all("*")

createNineSpeedTable()
insertNineSpeedData()
get_distributor_9spd("*")
get_brand_9spd("*")
get_speed_9spd("*")
get_ratio_9spd("*")
get_distributor_9spd_all("*")
get_brand_9spd_all("*")
get_speed_9spd_all("*")
get_ratio_9spd_all("*")

createTenSpeedTable()
insertTenSpeedData()
get_distributor_10spd("*")
get_brand_10spd("*")
get_speed_10spd("*")
get_ratio_10spd("*")
get_distributor_10spd_all("*")
get_brand_10spd_all("*")
get_speed_10spd_all("*")
get_ratio_10spd_all("*")

createElevenSpeedTable()
insertElevenSpeedData()
get_distributor_11spd("*")
get_brand_11spd("*")
get_speed_11spd("*")
get_ratio_11spd("*")
get_distributor_11spd_all("*")
get_brand_11spd_all("*")
get_speed_11spd_all("*")
get_ratio_11spd_all("*")
