import sqlite3
from .database import connect_database, response

def createTenSpeedTable():
    connect = connect_database()
    cursor = connect.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS cassettes_10spd 
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
    connect.commit()

def insertTenSpeedData():
    connect = connect_database()
    cursor = connect.cursor()
    data = [
        (1, "Shimano", "5700", "21590", 10, "11-28", "Bob-Elliot", 54.99, 1),
        (2, "Shimano", "M4100", "25269", 10, "11-46", "Bob-Elliot", 59.99, 1),
        (3, "Shimano", "M4100", "25206", 10, "11-42", "Bob-Elliot", 49.99, 1),
        (4, "Shimano", "HG50", "25253", 10, "11-36", "Bob-Elliot", 45.99, 1),
        (5, "Shimano", "HG500", "25238", 10, "11-28", "Bob-Elliot", 34.99, 1),
        (6, "Sunrace", "M1", "50374", 10, "11-36", "Bob-Elliot", 46.99, 1),
        (7, "Sunrace", "MS1", "50236", 10, "11-36", "Bob-Elliot", 46.99, 1),
        (8, "Sunrace", "MS3", "50237", 10, "11-40", "Bob-Elliot", 64.99, 1),
        (9, "Sunrace", "MS3", "50238", 10, "11-40", "Bob-Elliot", 64.99, 1),
        (10, "Sunrace", "MS3", "50239", 10, "11-42", "Bob-Elliot", 64.99, 1),
        (11, "Sunrace", "MS3", "50240", 10, "11-42", "Bob-Elliot", 64.99, 1),
        (12, "Sunrace", "MS3", "50341", 10, "11-46", "Bob-Elliot", 72.99, 1),
        (13, "Sunrace", "MS3", "50342", 10, "11-46", "Bob-Elliot", 72.99, 1),
        (14, "Sunrace", "MX0", "50249", 10, "11-36", "Bob-Elliot", 81.99, 1),
        (15, "Sunrace", "MX0", "50250", 10, "11-36", "Bob-Elliot", 68.99, 1),
        (16, "Sunrace", "MX3", "50253", 10, "11-42", "Bob-Elliot", 99.99, 1),
        (17, "Sunrace", "MX3", "50254", 10, "11-42", "Bob-Elliot", 86.99, 1),
        (18, "Sunrace", "MX3", "50255", 10, "11-46", "Bob-Elliot", 107.99, 1),
        (19, "Sunrace", "MX3", "50256", 10, "11-46", "Bob-Elliot", 95.99, 1),
        (20, "Sunrace", "RS0", "50270", 10, "11-25", "Bob-Elliot", 54.99, 1),
        (21, "Sunrace", "RS0", "50271", 10, "11-28", "Bob-Elliot", 54.99, 1),
        (22, "Sunrace", "RS0", "50272", 10, "11-32", "Bob-Elliot", 54.99, 1),
        (23, "Sunrace", "RS1", "50275", 10, "11-28", "Bob-Elliot", 35.99, 1),
        (24, "Sunrace", "RS1", "50276", 10, "11-32", "Bob-Elliot", 35.99, 1),
        (25, "Sunrace", "RX0", "50345", 10, "11-28", "Bob-Elliot", 73.99, 1),
        (26, "Sunrace", "RX0", "50348", 10, "11-32", "Bob-Elliot", 60.99, 1),
        (27, "Sunrace", "RX0", "50346", 10, "11-28", "Bob-Elliot", 60.99, 1),
        (28, "Sunrace", "RX0", "50347", 10, "11-32", "Bob-Elliot", 73.99, 1),
        (29, "Campagnolo", "Centuar", "CPB528A", 10, "14-23", "Chicken Cyclekit", 98.99, 2),
        (30, "Campagnsolo", "Veloce", "CPB533", 10, "11-25", "Chicken Cyclekit", 71.24, 2),
        (31, "Campagnolo", "Veloce", "CPB539", 10, "12-23", "Chicken Cyclekit", 52.99, 2),
        (32, "Campagnolo", "Veloce", "CPB535", 10, "12-25", "Chicken Cyclekit", 52.99, 2),
        (33, "Campagnolo", "Veloce", "CPB536", 10, "13-26", "Chicken Cyclekit", 52.99, 2),
        (34, "Campagnolo", "Veloce", "CPB537", 10, "13-29", "Chicken Cyclekit", 52.99, 2),
        (35, "Miche", "Primato", "MCX23", 10, "12-23", "Chicken Cyclekit", 48.99, 2),
        (36, "Miche", "Primato", "MCX20", 10, "12-25", "Chicken Cyclekit", 48.99, 2),
        (37, "Miche", "Primate", "MCX21", 10, "12-27", "Chicken Cyclekit", 48.99, 2),
        (38, "Miche", "Primato", "MCX22", 10, "12-29", "Chicken Cyclekit", 48.99, 2),
        (39, "Miche", "Primato", "MCX19", 10, "13-26", "Chicken Cyclekit", 48.99, 2),
        (40, "Miche", "Primato", "MCX24", 10, "13-30", "Chicken Cyclekit", 64.99, 2),
        (41, "Miche", "Primato", "MCX18", 10, "16-23", "Chicken Cyclekit", 48.99, 2),
        (42, "Miche", "Primato", "MCX25", 10, "12-25", "Chicken Cyclekit", 48.99, 2),
        (43, "Miche", "Primato", "MCX250", 10, "11-30", "Chicken Cyclekit", 54.99, 2),
        (44, "Miche", "Primato", "MCX251", 10, "12-30", "Chicken Cyclekit", 51.99, 2),
        (45, "Miche", "Primato", "MCX252", 10, "13-30", "Chicken Cyclekit", 64.99, 2),
        (46, "Miche", "Primato", "MCX253", 10, "11-27", "Chicken Cyclekit", 48.99, 2),
        (47, "Miche", "Primato", "MCX254", 10, "14-28", "Chicken Cyclekit", 48.99, 2),
        (48, "Miche", "Primato", "MCX26", 10, "12-27", "Chicken Cyclekit", 48.99, 2),
        (49, "Miche", "Primato", "MCX27", 10, "12-29", "Chicken Cyclekit", 48.99, 2),
        (50, "Miche", "Primato", "MCX956A", 10, "16-27", "Chicken Cyclekit", 48.99, 2),
        (51, "KMC", "REACT", "KX40", 10, "11-36", "Chicken Cyclekit", 45.99, 2),
        (52, "KMC", "REACT", "KX41", 10, "11-42", "Chicken Cyclekit", 49.99, 2),
        (53, "Tifosi", "10x", "TIF710A", 10, "11-34", "Chicken Cyclekit", 31.99, 2),
        (54, "Tifosi", "10x", "TIF710B", 10, "11-36", "Chicken Cyclekit", 32.99, 2),
        (55, "Clarks", "", "C-10SC-UKS", 10, "11-36", "Greyville", 31.96, 3),
        (56, "Sunrace", "MS1", "CSMS1TAWM", 10, "11-36", "Greyville", 29.95, 3),
        (57, "Sunrace", "MS3", "CSMS3M", 10, "11-42", "Greyville", 59.95, 3),
        (58, "Sunrace", "MX3", "CSMX3", 10, "11-42", "Greyville", 69.95, 3),
        (59, "GTB", "", "ESP1036N", 10, "11-36", "Greyville", 69.95, 3),
        (60, "Geardrive", "", "GD1025", 10, "11-25", "Greyville", 32.95, 3),
        (61, "Geardrive", "", "GD1028", 10, "11-28", "Greyville", 32.95, 3),
        (62, "Geardrive", "", "GD1032", 10, "11-32", "Greyville", 32.95, 3),
        (63, "Geardrive", "", "GD1036", 10, "11-36", "Greyville", 34.96, 3),
        (64, "Geardrive", "", "GD1040", 10, "11-40", "Greyville", 35.95, 3),
        (65, "Geardrive", "", "GD1042", 10, "11-42", "Greyville", 47.95, 3),
        (66, "Driven", "RZ", "CSDV1123", 10, "11-23", "Ison Distribution", 249.99, 4),
        (67, "Microshift", "Sword", "CSMSH10138", 10, "11-38", "Ison Distribution", 54.99, 4),
        (68, "Microshift", "Advent", "CSMSH10148", 10, "11-48", "Ison Distribution", 54.99, 4),
        (69, "N/A", "N/A", "CSESP1036", 10, "11-36", "Mackadams", 31.99, 5),
        (70, "S-Ride", "M400", "590848", 10, "11-36", "Mackadams", 59.99, 5),
        (71, "SRAM", "PG1030", "FWS131126", 10, "11-26", "Mackadams", 61.99, 5),
        (72, "SRAM", "PG1030", "FWS131128", 10, "11-28", "Mackadams", 61.99, 5),
        (73, "SRAM", "PG1030", "FWS131132", 10, "11-32", "Mackadams", 61.99, 5),
        (74, "SRAM", "PG1030", "FWS131136", 10, "11-36", "Mackadams", 61.99, 5),
        (75, "SRAM", "PG1050", "FWS151123", 10, "11-23", "Mackadams", 75.99, 5),
        (76, "SRAM", "PG1050", "FWS151126", 10, "11-26", "Mackadams", 75.99, 5),
        (77, "SRAM", "PG1050", "FWS151128", 10, "11-28", "Mackadams", 75.99, 5),
        (78, "SRAM", "PG1050", "FWS151132", 10, "11-32", "Mackadams", 75.99, 5),
        (79, "SRAM", "PG1050", "FWS151136", 10, "11-36", "Mackadams", 75.99, 5),
        (80, "Sunrace", "MS1", "CSMS1TAWM", 10, "11-36", "Mackadams", 46.99, 5),
        (81, "Sunrace", "MS1", "CSMS1TAWB", 10, "11-36", "Mackadams", 46.99, 5),
        (82, "Sunrace", "MS3", "CSMS3TAXM", 10, "11-40", "Mackadams", 64.99, 5),
        (83, "Sunrace", "MS3", "CSMS3TAYM", 10, "11-42", "Mackadams", 64.99, 5),
        (84, "Sunrace", "MS3", "CSMS3TAXB", 10, "11-40", "Mackadams", 64.99, 5),
        (85, "Sunrace", "MS3", "CSMS3TAYB", 10, "11-42", "Mackadams", 64.99, 5),
        (86, "Sunrace", "MX0", "CSMX0TAWM", 10, "11-36", "Mackadams", 68.99, 5),
        (87, "Sunrace", "MX0", "CSMX0TAWB", 10, "11-36", "Mackadams", 68.99, 5),
        (88, "Sunrace", "MX3", "CSMX3TAXM", 10, "11-40", "Mackadams", 69.99, 5),
        (89, "Sunrace", "MX3", "CSMX3TAYM", 10, "11-42", "Mackadams", 69.99, 5),
        (90, "Sunrace", "MX3", "CSMX3TAZM", 10, "11-46", "Mackadams", 69.99, 5),
        (91, "Sunrace", "MX3", "CSMX3TAXB", 10, "11-40", "Mackadams", 69.99, 5),
        (92, "Sunrace", "MX3", "CSMX3TAYB", 10, "11-42", "Mackadams", 69.99, 5),
        (93, "Sunrace", "MX3", "CSMX3TAZB", 10, "11-46", "Mackadams", 69.99, 5),
        (94, "Sunrace", "RS1", "CSRS1TAS", 10, "11-28", "Mackadams", 35.99, 5),
        (95, "Sunrace", "RS1", "CSRS1TAU", 10, "11-32", "Mackadams", 35.99, 5),
        (96, "Sunrace", "RS0", "CSRS0TAQ", 10, "11-25", "Mackadams", 54.99, 5),
        (97, "Sunrace", "RS0", "CSRS0TAS", 10, "11-28", "Mackadams", 54.99, 5),
        (98, "Sunrace", "RS0", "CSRS0TAU", 10, "11-32", "Mackadams", 54.99, 5),
        (99, "Sunrace", "RX0", "CSRX0TAQM", 10, "11-25", "Mackadams", 63.99, 5),
        (100, "Sunrace", "RX0", "CSRX0TASM", 10, "11-28", "Mackadams", 63.99, 5),
        (101, "Sunrace", "RX0", "CSRX0TAUM", 10, "11-32", "Mackadams", 63.99, 5),
        (102, "Sunrace", "RX0", "CSRX0TAQB", 10, "11-25", "Mackadams", 73.99, 5),
        (103, "Sunrace", "RX0", "CSRX0TASB", 10, "11-28", "Mackadams", 73.99, 5),
        (104, "Sunrace", "RX0", "CSRX0TAUB", 10, "11-32", "Mackadams", 73.99, 5),
        (105, "Shimano", "6700", "CS670010128", 10, "11-28", "Madison", 74.99, 6),
        (106, "Shimano", "6700", "CS670010225", 10, "12-25", "Madison", 74.99, 6),
        (107, "Shimano", "6700", "CS670010230", 10, "12-30", "Madison", 74.99, 6),
        (108, "Shimano", "M771", "CSM771132", 10, "11-32", "Madison", 74.99, 6),
        (109, "Shimano", "M771", "CSM771134", 10, "11-34", "Madison", 74.99, 6),
        (110, "Shimano", "M771", "CSM771136", 10, "11-36", "Madison", 74.99, 6),
        (111, "Shimano", "LG400", "CSLG40010139", 10, "11-39", "Madison", 49.99, 6),
        (112, "Shimano", "LG400", "CSLG40010143", 10, "11-43", "Madison", 59.99, 6),
        (113, "Shimano", "LG400", "CSLG40010148", 10, "11-48", "Madison", 59.99, 6),
        (114, "Shimano", "M4100", "CSM4100142", 10, "11-42", "Madison", 49.99, 6),
        (115, "Shimano", "M4100", "CSM4100146", 10, "11-46", "Madison", 59.99, 6),
        (116, "Shimano", "HG50", "CSHG5010136", 10, "11-36", "Madison", 44.99, 6),
        (117, "Shimano", "LG300", "CSLG30010139", 10, "11-39", "Madison", 44.99, 6),
        (118, "Shimano", "LG300", "CSLG30010148", 10, "11-48", "Madison", 54.99, 6),
        (119, "Shimano", "HG500", "CSHG50010125", 10, "11-25", "Madison", 34.99, 6),
        (120, "Shimano", "HG500", "CSHG50010132", 10, "11-32", "Madison", 39.99, 6),
        (121, "Shimano", "HG500", "CSHG50010134", 10, "11-34", "Madison", 39.99, 6),
        (122, "Shimano", "HG500", "CSHG50010228", 10, "12-28", "Madison", 34.99, 6),
        (123, "SRAM", "PG1030", "FWS131128", 10, "11-28", "ZyroFisher", 62.00, 7),
        (124, "SRAM", "PG1030", "FWS131132", 10, "11-32", "ZyroFisher", 62.00, 7),
        (125, "SRAM", "PG1030", "FWS131136", 10, "11-36", "ZyroFisher", 62.00, 7),
        (126, "SRAM", "PG1050", "FWS151128", 10, "11-28", "ZyroFisher", 76.00, 7),
        (127, "SRAM", "PG1050", "FWS151132", 10, "11-32", "ZyroFisher", 76.00, 7),
        (128, "SRAM", "PG1050", "FWS151136", 10, "11-36", "ZyroFisher", 76.00, 7),
        (129, "SRAM", "PG1050", "FWS151232", 10, "12-32", "ZyroFisher", 76.00, 7),
        (130, "SRAM", "PG1050", "FWS151236", 10, "12-36", "ZyroFisher", 76.00, 7),
        (132, "SRAM", "PG1070", "FWS171125", 10, "11-25", "ZyroFisher", 91.00, 7),
        (133, "SRAM", "PG1070", "FWS171126", 10, "11-26", "ZyroFisher", 91.00, 7),
        (134, "SRAM", "PG1070", "FWS171128", 10, "11-28", "ZyroFisher", 91.00, 7),
        (135, "SRAM", "PG1070", "FWS171136", 10, "11-36", "ZyroFisher", 91.00, 7),
        (136, "SRAM", "PG1070", "FWS171225", 10, "12-25", "ZyroFisher", 91.00, 7),
        (137, "SRAM", "PG1070", "FWS171232", 10, "12-32", "ZyroFisher", 91.00, 7),
        (138, "SRAM", "PG1070", "FWS171236", 10, "12-36", "ZyroFisher", 91.00, 7),
        (139, "Clarks", "", "C-10SC", 10, "11-36", "ZyroFisher", 39.99, 7),
        (140, "Microshift", "Advent", "CSMSG10148", 10, "11-48", "Ison Distribution", 74.99, 4),
        (141, "Microshift", "Sword", "CSMSG10138", 10, "11-38", "Ison Distribution", 79.99, 4)]
    
    cursor.executemany("REPLACE INTO cassettes_10spd VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)", data)

    connect.commit()
    connect.close()

def get_distributor_10spd_all(distributor: str):
    connect = connect_database()
    cursor = connect.cursor()
    print(distributor)
    result = cursor.execute(
        "SELECT brand, model, partNumber, speed, ratio, distributor, rrp FROM cassettes_10spd")

    rows = result.fetchall()
    connect.close()
    return response(rows)

def get_distributor_10spd(distributor: str):
    connect = connect_database()
    cursor = connect.cursor()
    print(distributor)
    result = cursor.execute(
        "SELECT brand, model, partNumber, speed, ratio, distributor, rrp FROM cassettes_10spd WHERE distributor=?", [distributor])

    rows = result.fetchall()
    connect.close()
    return response(rows)

def get_brand_10spd_all(brand: str):
    connect = connect_database()
    cursor = connect.cursor()
    print(brand)
    cursor = connect.cursor()
    result = cursor.execute(
        "SELECT brand, model, partNumber, speed, ratio, distributor, rrp FROM cassettes_10spd")

    rows = result.fetchall()
    connect.close()
    return response(rows)

def get_brand_10spd(brand: str):
    connect = connect_database()
    cursor = connect.cursor()
    print(brand)
    cursor = connect.cursor()
    result = cursor.execute(
        "SELECT brand, model, partNumber, speed, ratio, distributor, rrp FROM cassettes_10spd WHERE brand=?", [brand])

    rows = result.fetchall()
    connect.close()
    return response(rows)

def get_speed_10spd_all():
    connect = connect_database()
    cursor = connect.cursor()
    result = cursor.execute(
        "SELECT brand, model, partNumber, speed, ratio, distributor, rrp FROM cassettes_10spd")

    rows = result.fetchall()
    connect.close()
    return response(rows)

def get_speed_10spd(speed: int):
    connect = connect_database()
    cursor = connect.cursor()
    print(speed)
    cursor = connect.cursor()
    result = cursor.execute(
        "SELECT brand, model, partNumber, speed, ratio, distributor, rrp FROM cassettes_10spd WHERE speed=?", [speed])

    rows = result.fetchall()
    connect.close()
    return response(rows)

def get_ratio_10spd_all(ratio: str):
    connect = connect_database()
    cursor = connect.cursor()
    print(ratio)
    cursor = connect.cursor()
    result = cursor.execute(
        "SELECT brand, model, partNumber, speed, ratio, distributor, rrp FROM cassettes_10spd")

    rows = result.fetchall()
    connect.close()
    return response(rows)

def get_ratio_10spd(ratio: str):
    connect = connect_database()
    cursor = connect.cursor()
    print(ratio)
    cursor = connect.cursor()
    result = cursor.execute(
        "SELECT brand, model, partNumber, speed, ratio, distributor, rrp FROM cassettes_10spd WHERE ratio=?", [ratio])

    rows = result.fetchall()
    connect.close()
    return response(rows)

def get_speed_ratio_10spd(ratio: str):
    connect = connect_database()
    cursor = connect.cursor()
    print(ratio)
    cursor = connect.cursor()
    result = cursor.execute(
        "SELECT brand, model, partNumber, speed, ratio, distributor, rrp FROM cassettes_10spd WHERE speed=10 AND ratio=?", [ratio])

    rows = result.fetchall()
    connect.close()
    return response(rows)

