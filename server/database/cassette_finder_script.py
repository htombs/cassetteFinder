import sqlite3

from tables.cassettes_table import createCassettesTable, insertCassettesData, dropCassTable

dropCassTable()

createCassettesTable()
insertCassettesData()