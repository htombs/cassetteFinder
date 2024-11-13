import sqlite3
from .database import connect_database, response

def createEightSpeedTable():
    connect = connect_database()
    cursor = connect.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS cassettes_8spd
               (id INT PRIMARY KEY,
               brand VARCHAR(255),
               model VARCHAR(255),
               partNumber VARCHAR(255),
               speed INT,
               ratio VARCHAR(10),
               distributor VARCHAR(255),
               rrp DECIMAL(10,2),
               distributor_id INT,
               FOREIGN KEY (distributor_id) REFERENCES distributor_table (distributor_id))''')
    connect.commit()
    connect.close()


def insertEightSpeedData():
    connect = connect_database()
    cursor = connect.cursor()
    data = [
        (1, "Shimano", "HG400", "CSHG4008145", 8, "11-45", "Madison", 36.99, 6),
        (2, "Shimano", "HG400", "CSHG4008140", 8, "11-40", "Madison", 34.99, 6),
        (3, "Shimano", "HG50", "CSHG508128", 8, "11-28", "Madison", 22.99, 6),
        (4, "Shimano", "HG50", "CSHG508130", 8, "11-30", "Madison", 22.99, 6),
        (5, "Shimano", "HG50", "CSHG508132", 8, "11-32", "Madison", 22.99, 6),
        (6, "Shimano", "HG50", "CSHG508134", 8, "11-34", "Madison", 22.99, 6),
        (7, "Shimano", "HG50", "CSHG508225", 8, "12-25", "Madison", 34.99, 6),
        (8, "Shimano", "HG41", "CSHG418130", 8, "11-30", "Madison", 21.99, 6),
        (9, "Shimano", "HG41", "CSHG418132", 8, "11-32", "Madison", 21.99, 6),
        (10, "Shimano", "HG41", "CSHG418134", 8, "11-34", "Madison", 22.99, 6),
        (11, "Shimano", "HG31", "CSHG318132", 8, "11-32", "Madison", 20.99, 6),
        (12, "Shimano", "HG31", "CSHG318134", 8, "11-34", "Madison", 20.99, 6),
        (13, "SRAM", "PG820", "FW821130", 8, "11-30", "ZyroFisher", 18.00, 8),
        (14, "SRAM", "PG820", "FW821132", 8, "11-32", "ZyroFisher", 18.00, 8),
        (15, "SRAM", "PG850", "FW851128", 8, "11-28", "ZyroFisher", 26.00, 8),
        (16, "SRAM", "PG850", "FW851130", 8, "11-30", "ZyroFisher", 26.00, 8),
        (17, "SRAM", "PG850", "FW851132", 8, "11-32", "ZyroFisher", 26.00, 8),
        (18, "SRAM", "PG850", "FW851223", 8, "12-23", "ZyroFisher", 35.00, 8),
        (19, "SRAM", "PG850", "FW851226", 8, "12-26", "ZyroFisher", 35.00, 8),
        (20, "SRAM", "PG830", "FW831128", 8, "11-28", "ZyroFisher", 20.00, 8),
        (21, "SRAM", "XG", "FW075000", 8, "11-48", "ZyroFisher", 480.00, 8),
        (22, "Shimano", "HG41", "25113", 8, "11-34", "Bob Elliot", 22.99, 1),
        (23, "Shimano", "HG51", "25149", 8, "11-30", "Bob Elliot", 28.99, 1),
        (24, "Shimano", "HG51", "25150", 8, "11-32", "Bob Elliot", 28.99, 1),
        (25, "Sunrace", "M66", "50232", 8, "11-32", "Bob Elliot", 19.99, 1),
        (26, "Sunrace", "M66", "50340", 8, "11-34", "Bob Elliot", 20.99, 1),
        (27, "Sunrace", "R86", "50283", 8, "11-28", "Bob Elliot", 22.99, 1),
        (28, "Sunrace", "M55", "50337", 8, "11-34", "Bob Elliot", 19.99, 1),
        (29, "Shimano", "HG200", "25265", 8, "12-32", "Bob Elliot", 24.99, 1),
        (30, "Box", "FOUR", "CSBX48142K", 8, "11-42", "Ison Distribution", 59.99, 4),
        (31, "Box", "FOUR", "CSBX48242K", 8, "12-42", "Ison Distribution", 59.99, 4),
        (32, "Sunrace", "R86", "CSSR6832", 8, "11-32", "Ison Distribution", 21.99, 4),
        (33, "Sunrace", "R86", "CSSR8825", 8, "12-25", "Ison Distribution", 24.99, 4),
        (34, "GTB", "N/A", "ESP1031N", 8, "11-28", "Greyville", 25.96, 3),
        (35, "GTB", "N/A", "ESP1032N", 8, "11-32", "Greyville", 27.95, 3),
        (36, "Geardrive", "N/A", "GD0823", 8, "11-23", "Greyville", 16.96, 3),
        (37, "Geardrive", "N/A", "GD0825", 8, "11-25", "Greyville", 17.95, 3),
        (38, "Geardrive", "N/A", "GD0828", 8, "11-28", "Greyville", 18.54, 3),
        (39, "Geardrive", "N/A", "GD0832", 8, "11-32", "Greyville", 18.54, 3),
        (40, "Geardrive", "N/A", "GD0832OE", 8, "11-32", "Greyville", 16.96, 3),
        (41, "KMC", "REACT X8", "KX20", 8, "11-32", "Chicken Cyclekit", 26.00, 2),
        (42, "Miche", "PRIMATO 8X", "MCX501", 8, "11-28", "Chicken Cyclekit", 32.99, 2),
        (43, "Miche", "PRIMATO 8X", "MCX502", 8, "12-25", "Chicken Cyclekit", 32.99, 2),
        (44, "Miche", "PRIMATO 8X", "MCX503", 8, "12-27", "Chicken Cyclekit", 32.99, 2),
        (45, "Tifosi", "8X HG", "TIF708A", 8, "11-28", "Chicken Cyclekit", 18.99, 2),
        (46, "Tifosi", "8X HG", "N/A", 8, "11-32", "Chicken Cyclekit", 18.99, 2),
        (47, "Shimano", "HG50", "25261", 8, "11-28", "Bob Elliot", 22.99, 1),
        (48, "Shimano", "HG50", "25262", 8, "11-30", "Bob Elliot", 22.99, 1),
        (49, "Shimano", "HG50", "25263", 8, "11-32", "Bob Elliot", 22.99, 1),
        (50, "Shimano", "HG50", "25264", 8, "11-34", "Bob Elliot", 22.99, 1),
        (51, "Shimano", "HG50", "25137", 8, "12-25", "Bob Elliot", 34.99, 1),
        (52, "Shimano", "HG41", "25124", 8, "11-30", "Bob Elliot", 21.99, 1),
        (53, "Shimano", "HG41", "25122", 8, "11-32", "Bob Elliot", 21.99, 1),
        (54, "Shimano", "HG31", "25252", 8, "11-32", "Bob Elliot", 20.99, 1),
        (55, "Sunrace", "M66", "CSM668AU", 8, "11-32", "Greyville", 19.99, 3),
        (56, "Sunrace", "R86", "CSSR6828", 8, "11-28", "Ison Distribution", 22.99, 4),
        (57, "Sunrace", "R86", "CSR868AS", 8, "11-28", "Greyville", 22.99, 3),
        (58, "Shimano", "HG200", "HG200832", 8, "12-32", "Greyville", 24.99, 3),
        (59, "SRAM", "PG850", "FW851128", 8, "11-28", "Mackadams", 26.00, 5),
        (60, "SRAM", "PG850", "FW851130", 8, "11-30", "Mackadams", 26.00, 5),
        (61, "SRAM", "PG850", "FW851132", 8, "11-32", "Mackadams", 26.00, 5),
        (62, "SRAM", "PG850", "FW851223", 8, "12-23", "Mackadams", 35.00, 5),
        (63, "SRAM", "PG850", "FW851226", 8, "12-26", "Mackadams", 35.00, 5),
        (64, "Shimano", "HG200", "HG200832", 8, "12-32", "Mackadams", 24.99, 5),
        (65, "Undranded", "N/A", "CSESP1032", 8, "12-32", "Mackadams", 23.99, 5),
        (66, "Sunrace", "CSR86", "CSR868AO", 8, "11-23", "Mackadams", 19.99, 5),
        (67, "Sunrace", "CSR86", "CSR868AS", 8, "11-28", "Mackadams", 21.99, 5),
        (68, "Sunrace", "CSR86", "CSR868BQ", 8, "12-25", "Mackadams", 22.99, 5),
        (69, "Sunrace", "CSM66", "CSM668AU", 8, "11-32", "Mackadams", 22.99, 5),
        (70, "SRAM", "PG830", "FW831128", 8, "11-28", "Mackadams", 20.00, 5),
        (71, "Undranded", "N/A", "CSESP1031", 8, "11-28", "Mackadams", 20.00, 5),
        (72, "SRAM", "PG820", "FW821128", 8, "11-28", "Mackadams", 18.00, 5),
        (73, "SRAM", "PG820", "FW821130", 8, "11-30", "Mackadams", 18.00, 5),
        (74, "SRAM", "PG820", "FW821132", 8, "11-32", "Mackadams", 18.00, 5),
        (75, "Tektro", "ED-8", "TK-ABCS000001", 8, "11-42", "Upgrade", 70.00, 7),
        (76, "Microshift", "R8", "CSMSH8128", 8, "11-28", "Ison Distribution", 24.99, 4),
        (77, "Microshift", "Mezzo", "CSMSH8132", 8, "11-32", "Ison Distribution", 24.99, 4),
        (78, "Microshift", "Mezzo", "CSMSH8134", 8, "11-34", "Ison Distribution", 24.99, 4),
        (79, "Microshift", "Acolyte", "CSMSH8138", 8, "11-38", "Ison Distribution", 29.99, 4),
        (80, "Microshift", "Acolyte", "CSMSH8242", 8, "12-42", "Ison Distribution", 34.99, 4),
        (81, "Microshift", "Acolyte", "CSMSH8246", 8, "12-46", "Ison Distribution", 39.99, 4)]

    cursor.executemany("REPLACE INTO cassettes_8spd VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)", data)

    connect.commit()
    connect.close()

eightspdSQL = '''SELECT cassettes_8spd.brand, cassettes_8spd.model, cassettes_8spd.partNumber, cassettes_8spd.speed, cassettes_8spd.ratio, distributor_table.distributor_name, cassettes_8spd.rrp, distributor_table.distributor_link_url 
        FROM cassettes_8spd, distributor_table WHERE cassettes_8spd.distributor_id = distributor_table.distributor_id '''

def get_speed_8spd_all():
    connect = connect_database()
    cursor = connect.cursor()
    result = cursor.execute(eightspdSQL)
    
    rows = result.fetchall()
    connect.close()
 
    return response(rows)

def get_speed_8spd(speed: int):
    connect = connect_database()
    cursor = connect.cursor()
    print(speed)
    result = cursor.execute(eightspdSQL + "AND speed=?", [speed])

    rows = result.fetchall()
    connect.close()
    return response(rows)

# def get_speed_ratio_8spd(ratio: str):
#     connect = connect_database()
#     cursor = connect.cursor()
#     print(ratio)
#     cursor = connect.cursor()
#     result = cursor.execute(eightspdSQL + "AND speed=8 AND ratio=?", [ratio])
        
#     rows = result.fetchall()
#     connect.close()
#     return response(rows)

# I've commented this function out as it's been made redundant with the below fundtion

def get_speed_ratio_brand_8spd(ratio: str, brand: str):
    connect = connect_database()
    cursor = connect.cursor()
    print(brand)
    result = cursor.execute(eightspdSQL + "AND speed=8 AND ratio=? AND brand=?", [ratio], [brand])

    rows = result.fetchall()
    connect.close()
    return response(rows)