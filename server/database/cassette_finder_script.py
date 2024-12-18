import sqlite3

from database.tables.eight_speed import insertEightSpeedData, createEightSpeedTable
# from database.tables.nine_speed import insertNineSpeedData, createNineSpeedTable
# from database.tables.ten_speed import insertTenSpeedData, createTenSpeedTable
# from database.tables.eleven_speed import insertElevenSpeedData, createElevenSpeedTable
from database.tables import distributor_table

createEightSpeedTable()
insertEightSpeedData()

# createNineSpeedTable()
# insertNineSpeedData()
# 
# createTenSpeedTable()
# insertTenSpeedData()
# 
# createElevenSpeedTable()
# insertElevenSpeedData()
