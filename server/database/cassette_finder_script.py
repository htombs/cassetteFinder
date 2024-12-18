import sqlite3

from tables.cassettes_table import createCassettesTable, insertCassettesData, dropCassTable
# from database.tables.nine_speed import insertNineSpeedData, createNineSpeedTable
# from database.tables.ten_speed import insertTenSpeedData, createTenSpeedTable
# from database.tables.eleven_speed import insertElevenSpeedData, createElevenSpeedTable
# from database.tables import distributor_table

dropCassTable()

createCassettesTable()
insertCassettesData()

# createNineSpeedTable()
# insertNineSpeedData()
# 
# createTenSpeedTable()
# insertTenSpeedData()
# 
# createElevenSpeedTable()
# insertElevenSpeedData()
