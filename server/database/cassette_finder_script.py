import sqlite3

from database.tables.eight_speed import insertCassettesData, createCassettesTable
# from database.tables.nine_speed import insertNineSpeedData, createNineSpeedTable
# from database.tables.ten_speed import insertTenSpeedData, createTenSpeedTable
# from database.tables.eleven_speed import insertElevenSpeedData, createElevenSpeedTable
from database.tables import distributor_table

insertCassettesData()
createCassettesTable()

# createNineSpeedTable()
# insertNineSpeedData()
# 
# createTenSpeedTable()
# insertTenSpeedData()
# 
# createElevenSpeedTable()
# insertElevenSpeedData()
