import sqlite3
from .database import connect_database, response

def createElevenSpeedTable():
    connect = connect_database()
    cursor = connect.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS cassettes_11spd 
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

def insertElevenSpeedData():
    connect = connect_database()
    cursor = connect.cursor()
    data = [
        (1, "Shimano", "R7000", "25200", 11, "11-28", "Bob-Elliot", 54.99, 1),
        (2, "Shimano", "R7000", "25201", 11, "11-30", "Bob-Elliot", 54.99, 1),
        (3, "Shimano", "R7000", "25202", 11, "11-32", "Bob-Elliot", 59.99, 1),
        (4, "Shimano", "R7000", "25203", 11, "12-25", "Bob-Elliot", 59.99, 1),
        (5, "Shimano", "M5100", "25268", 11, "11-51", "Bob-Elliot", 79.99, 1),
        (6, "Shimano", "R8000", "25255", 11, "11-25", "Bob-Elliot", 84.99, 1),
        (7, "Shimano", "R8000", "25256", 11, "11-28", "Bob-Elliot", 84.99, 1),
        (8, "Shimano", "R8000", "25257", 11, "11-30", "Bob-Elliot", 89.99, 1),
        (9, "Shimano", "R8000", "25258", 11, "11-32", "Bob-Elliot", 89.99, 1),
        (10, "Shimano", "R8000", "25259", 11, "12-25", "Bob-Elliot", 89.99, 1),
        (11, "Shimano", "R8000", "25260", 11, "14-28", "Bob-Elliot", 84.99, 1),
        (12, "Shimano", "HG700", "25205", 11, "11-34", "Bob-Elliot", 59.99, 1),
        (13, "Sunrace", "MS8", "50241", 11, "11-36", "Bob-Elliot", 80.99, 1),
        (14, "Sunrace", "MS8", "50242", 11, "11-36", "Bob-Elliot", 80.99, 1),
        (15, "Sunrace", "MS8", "50243", 11, "11-40", "Bob-Elliot", 80.99, 1),
        (16, "Sunrace", "MS8", "50244", 11, "11-40", "Bob-Elliot", 80.99, 1),
        (17, "Sunrace", "MS8", "50245", 11, "11-42", "Bob-Elliot", 80.99, 1),
        (18, "Sunrace", "MS8", "50246", 11, "11-42", "Bob-Elliot", 80.99, 1),
        (19, "Sunrace", "MS8", "50247", 11, "11-46", "Bob-Elliot", 88.99, 1),
        (20, "Sunrace", "MS8", "50248", 11, "11-46", "Bob-Elliot", 88.99, 1),
        (21, "Sunrace", "MX8", "50259", 11, "11-42", "Bob-Elliot", 105.99, 1),
        (22, "Sunrace", "MX8", "50260", 11, "11-42", "Bob-Elliot", 93.99, 1),
        (23, "Sunrace", "MX8", "50261", 11, "11-46", "Bob-Elliot", 113.99, 1),
        (24, "Sunrace", "MX8", "50262", 11, "11-46", "Bob-Elliot", 101.99, 1),
        (25, "Sunrace", "MX80", "50363", 11, "11-51", "Bob-Elliot", 139.99, 1),
        (26, "Sunrace", "MX80", "50364", 11, "11-51", "Bob-Elliot", 126.99, 1),
        (27, "Sunrace", "MX9X", "50304", 11, "11-42", "Bob-Elliot", 156.99, 1),
        (28, "Sunrace", "MX9X", "50305", 11, "11-46", "Bob-Elliot", 164.99, 1),
        (29, "Sunrace", "RS3", "50307", 11, "11-28", "Bob-Elliot", 54.99, 1),
        (30, "Sunrace", "RS3", "50308", 11, "11-28", "Bob-Elliot", 54.99, 1),
        (31, "Sunrace", "RS3", "50309", 11, "11-32", "Bob-Elliot", 54.99, 1),
        (32, "Sunrace", "RS3", "50310", 11, "11-32", "Bob-Elliot", 54.99, 1),
        (33, "Sunrace", "RX1", "50273", 11, "11-28", "Bob-Elliot", 67.99, 1),
        (34, "Sunrace", "RX1", "50274", 11, "11-32", "Bob-Elliot", 67.99, 1),
        (35, "Sunrace", "RX1", "50350", 11, "11-32", "Bob-Elliot", 79.99, 1),
        (36, "Sunrace", "RX1", "50351", 11, "11-36", "Bob-Elliot", 93.99, 1),
        (37, "Sunrace", "RX1", "50352", 11, "11-36", "Bob-Elliot", 79.99, 1),
        (38, "Sunrace", "RX1", "50349", 11, "11-28", "Bob-Elliot", 79.99, 1),
        (39, "Sunrace", "RX11", "50368", 11, "11-34", "Bob-Elliot", 79.99, 1),
        (40, "Sunrace", "RX11", "50369", 11, "11-34", "Bob-Elliot", 64.99, 1),
        (41, "Miche", "Supertype 11x", "MCX102", 11, "11-27", "Chicken Cyclekit", 244.99, 2),
        (42, "Miche", "Supertype 11x", "MCX103", 11, "12-29", "Chicken Cyclekit", 244.99, 2),
        (43, "Miche", "Supertype 11x", "MCX105", 11, "11-30", "Chicken Cyclekit", 244.99, 2),
        (44, "Miche", "Supertype 11x", "MCX212", 11, "12-27", "Chicken Cyclekit", 244.99, 2),
        (45, "Miche", "Supertype 11x", "MCX213", 11, "12-29", "Chicken Cyclekit", 244.99, 2),
        (46, "Miche", "Supertype 11x", "MCX209", 11, "16-29", "Chicken Cyclekit", 244.99, 2),
        (47, "Campagnolo", "", "CPB573", 11, "11-27", "Chicken Cyclekit", 149.99, 2),
        (48, "Campagnolo", "", "CPB574", 11, "11-29", "Chicken Cyclekit", 149.99, 2),
        (49, "Campagnolo", "", "CPB571", 11, "11-32", "Chicken Cyclekit", 163.99, 2),
        (50, "Campagnolo", "Chorus", "CPB510", 11, "11-23", "Chicken Cyclekit", 159.99, 2),
        (51, "Campagnolo", "Chorus", "CPB515", 11, "11-25", "Chicken Cyclekit", 139.99, 2),
        (52, "Campagnolo", "Chorus", "CPB519", 11, "11-27", "Chicken Cyclekit", 178.99, 2),
        (53, "Campagnolo", "Chorus", "CPB517", 11, "11-29", "Chicken Cyclekit", 178.99, 2),
        (54, "Campagnolo", "Chorus", "CPB511", 11, "12-25", "Chicken Cyclekit", 139.99, 2),
        (55, "Campagnolo", "Chorus", "CPB514", 11, "12-27", "Chicken Cyclekit", 139.99, 2),
        (56, "Campagnolo", "Chorus", "CPB518", 11, "12-29", "Chicken Cyclekit", 139.99, 2),
        (57, "Miche", "XM", "MCX810", 11, "11-46", "Chicken Cyclekit", 99.99, 2),
        (58, "Miche", "Primato Light", "MCX215", 11, "11-25", "Chicken Cyclekit", 79.99, 2),
        (59, "Miche", "Primato Light", "MCX218", 11, "11-30", "Chicken Cyclekit", 79.99, 2),
        (60, "Miche", "Primato Light", "MCX2150A", 11, "11-32", "Chicken Cyclekit", 79.99, 2),
        (61, "Miche", "Primato Light", "MCX1140", 11, "11-34", "Chicken Cyclekit", 79.99, 2),
        (62, "Miche", "Primato Light", "MCX216", 11, "12-27", "Chicken Cyclekit", 79.99, 2),
        (63, "Miche", "Primato Light", "MCX217", 11, "12-29", "Chicken Cyclekit", 79.99, 2),
        (64, "Miche", "Primato Light", "MCX113", 11, "12-30", "Chicken Cyclekit", 79.99, 2),
        (65, "Miche", "Primato Light", "MCX115", 11, "12-34", "Chicken Cyclekit", 79.99, 2),
        (66, "Miche", "Primato Light", "MCX1150", 11, "12-34", "Chicken Cyclekit", 79.99, 2),
        (67, "Miche", "Primato Light", "MCX116", 11, "14-25", "Chicken Cyclekit", 79.99, 2),
        (68, "Miche", "Primato Light", "MCX117", 11, "16-27", "Chicken Cyclekit", 79.99, 2),
        (69, "Miche", "Primato Light", "MCX115", 11, "16-30", "Chicken Cyclekit", 79.99, 2),
        (70, "Miche", "Primato Light", "MCX219", 11, "11-25", "Chicken Cyclekit", 79.99, 2),
        (71, "Miche", "Primato Light", "MCX223", 11, "11-30", "Chicken Cyclekit", 79.99, 2),
        (72, "Miche", "Primato Light", "MCX224", 11, "11-32", "Chicken Cyclekit", 79.99, 2),
        (73, "Miche", "Primato Light", "MCX221", 11, "12-27", "Chicken Cyclekit", 79.99, 2),
        (74, "Miche", "Primato Light", "MCX222", 11, "12-29", "Chicken Cyclekit", 79.99, 2),
        (75, "Miche", "Primato Light", "MCX153", 11, "12-32", "Chicken Cyclekit", 79.99, 2),
        (76, "Miche", "Primato Light", "MCX150", 11, "16-30", "Chicken Cyclekit", 79.99, 2),
        (77, "Campagnolo", "Centaur", "CPB521E", 11, "11-29", "Chicken Cyclekit", 86.99, 2),
        (78, "Campagnolo", "Centaur", "CPB522E", 11, "11-32", "Chicken Cyclekit", 86.99, 2),
        (79, "Campagnolo", "Centaur", "CPB524E", 11, "12-32", "Chicken Cyclekit", 71.99, 2),
        (80, "Miche", "Primato", "MCX10", 11, "11-23", "Chicken Cyclekit", 69.99, 2),
        (81, "Miche", "Primato", "MCX1131", 11, "11-29", "Chicken Cyclekit", 69.99, 2),
        (82, "Miche", "Primato", "MCX11", 11, "12-25", "Chicken Cyclekit", 69.99, 2),
        (83, "Miche", "Primato", "MCX12", 11, "11-27", "Chicken Cyclekit", 69.99, 2),
        (84, "Miche", "Primato", "MCX13", 11, "12-29", "Chicken Cyclekit", 69.99, 2),
        (85, "KMC", "React", "KX50", 11, "11-42", "Chicken Cyclekit", 68.99, 2),
        (86, "KMC", "React", "KX51", 11, "11-50", "Chicken Cyclekit", 73.99, 2),
        (87, "Miche", "Primato", "MCX14", 11, "11-23", "Chicken Cyclekit", 63.99, 2),
        (88, "Miche", "Primato", "MCX142", 11, "11-27", "Chicken Cyclekit", 63.99, 2),
        (89, "Miche", "Primato", "MCX40", 11, "11-28", "Chicken Cyclekit", 63.99, 2),
        (90, "Miche", "Primato", "MCX1121", 11, "11-29", "Chicken Cyclekit", 63.99, 2),
        (91, "Miche", "Primato", "MCX110", 11, "12-25", "Chicken Cyclekit", 63.99, 2),
        (92, "Miche", "Primato", "MCX111", 11, "12-27", "Chicken Cyclekit", 63.99, 2),
        (93, "Miche", "Primato", "MCX112", 11, "12-29", "Chicken Cyclekit", 63.99, 2),
        (94, "Tifosi", "", "TIF711J", 11, "11-25", "Chicken Cyclekit", 49.99, 2),
        (95, "Tifosi", "", "TIF711H", 11, "11-28", "Chicken Cyclekit", 53.99, 2),
        (94, "Tifosi", "", "TIF711A", 11, "11-32", "Chicken Cyclekit", 48.99, 2),
        (94, "Tifosi", "", "TIF711B", 11, "11-34", "Chicken Cyclekit", 52.99, 2),
        (94, "Tifosi", "", "TIF711E", 11, "11-42", "Chicken Cyclekit", 54.99, 2),
        (94, "Tifosi", "", "TIF711G", 11, "11-46", "Chicken Cyclekit", 71.99, 2),
        (95, "Sunrace", "MX80", "CSMX80Z", 11, "11-50", "Greyville", 119.96, 3),
        (96, "Sunrace", "MX80", "CSMX80S", 11, "11-50", "Greyville", 94.96, 3),
        (97, "Sunrace", "MX8", "CSMX8", 11, "11-42", "Greyville", 74.95, 3),
        (98, "Geradrive", "", "GD1150", 11, "11-50", "Greyville", 74.95, 3),
        (99, "Geradrive", "", "GD1146", 11, "11-46", "Greyville", 64.96, 3),
        (100, "Clarks", "", "C-11SC-UKS", 11, "11-42", "Greyville", 49.96, 3),
        (101, "Geardrive", "", "GD1132", 11, "11-32", "Greyville", 49.96, 3),
        (102, "Geardrive", "", "GD1128", 11, "11-28", "Greyville", 49.96, 3),
        (103, "Geardrive", "", "GD1142", 11, "11-42", "Greyville", 48.95, 3),
        (104, "Geardrive", "", "GD1140", 11, "11-40", "Greyville", 47.95, 3),
        (105, "Microshift", "H-Series", "CSMSH11134", 11, "11-34", "Ison Distribution", 44.99, 4),
        (106, "Sunrace", "RS3", "CSSRS3132Z", 11, "11-32", "Ison Distribution", 59.99, 4),
        (107, "Sunrace", "MS8", "CSSRS8136D", 11, "11-36", "Ison Distribution", 74.99, 4),
        (108, "Sunrace", "MS8", "CSSRS8140D", 11, "11-40", "Ison Distribution", 74.99, 4),
        (109, "Sunrace", "MS8", "CSSRS8142Z", 11, "11-42", "Ison Distribution", 74.99, 4),
        (110, "Sunrace", "RX1", "CSSRX1128S", 11, "11-28", "Ison Distribution", 62.50, 4),
        (111, "Sunrace", "RX1", "CSSRX1132S", 11, "11-32", "Ison Distribution", 62.50, 4),
        (112, "Sunrace", "RX1", "CSSRX1136Z", 11, "11-36", "Ison Distribution", 84.99, 4),
        (113, "Sunrace", "MX8", "CSSRX8142Z", 11, "11-42", "Ison Distribution", 99.99, 4),
        (114, "Sunrace", "MX8", "CSSRX8146D", 11, "11-46", "Ison Distribution", 94.99, 4),
        (115, "Sunrace", "MX8", "CSSRX8146Z", 11, "11-46", "Ison Distribution", 104.99, 4),
        (116, "Sunrace", "MX80", "CSSRX8151D", 11, "11-51", "Ison Distribution", 119.99, 4),
        (117, "Sunrace", "MX80", "CSSRX8151Z", 11, "11-51", "Ison Distribution", 124.99, 4),
        (118, "SRAM", "PG1130", "FW1131126", 11, "11-26", "Mackadams", 96.00, 5),
        (119, "SRAM", "PG1130", "FW1131128", 11, "11-28", "Mackadams", 96.00, 5),
        (120, "SRAM", "PG1130", "FW1131132", 11, "11-32", "Mackadams", 96.00, 5),
        (121, "SRAM", "PG1130", "FW1131136", 11, "11-36", "Mackadams", 96.00, 5),
        (122, "SRAM", "XG1175", "FW8079000", 11, "11-42", "Mackadams", 208.00, 5),
        (123, "Sunrace", "MS8", "CSMS8EAWM", 11, "11-36", "Mackadams", 80.99, 5),
        (124, "Sunrace", "MS8", "CSMS8EAXM", 11, "11-40", "Mackadams", 80.99, 5),
        (125, "Sunrace", "MS8", "CSMS8EAYM", 11, "11-42", "Mackadams", 80.99, 5),
        (126, "Sunrace", "MS8", "CSMS8EAZM", 11, "11-46", "Mackadams", 88.99, 5),
        (127, "Sunrace", "MS8", "CSMS8EAWB", 11, "11-36", "Mackadams", 80.99, 5),
        (128, "Sunrace", "MS8", "CSMS8EAXB", 11, "11-40", "Mackadams", 80.99, 5),
        (129, "Sunrace", "MS8", "CSMS8EAYB", 11, "11-42", "Mackadams", 80.99, 5),
        (130, "Sunrace", "MS8", "CSMS8EAZB", 11, "11-46", "Mackadams", 88.99, 5),
        (131, "Sunrace", "MX8", "CSMX8EAXM", 11, "11-40", "Mackadams", 99.99, 5),
        (132, "Sunrace", "MX8", "CSMX8EAYM", 11, "11-42", "Mackadams", 99.99, 5),
        (133, "Sunrace", "MX8", "CSMX8EAZM", 11, "11-46", "Mackadams", 104.99, 5),
        (134, "Sunrace", "MX8", "CSMX8140B", 11, "11-40", "Mackadams", 99.99, 5),
        (135, "Sunrace", "MX8", "CSMX8EAYB", 11, "11-42", "Mackadams", 104.99, 5),
        (136, "Sunrace", "MX8", "CSMX8EAZB", 11, "11-46", "Mackadams", 119.99, 5),
        (137, "Sunrace", "MX80", "CSMX80EA5M", 11, "11-50", "Mackadams", 119.99, 5),
        (138, "Sunrace", "MX80", "CSMX80EASB", 11, "11-50", "Mackadams", 129.99, 5),
        (139, "Sunrace", "MX80", "CSMX9XETYB", 11, "10-42", "Mackadams", 149.99, 5),
        (140, "Sunrace", "MX80", "CSMX9XETZB", 11, "10-46", "Mackadams", 149.99, 5),
        (141, "Sunrace", "RS3", "CSRS3EASM", 11, "11-28", "Mackadams", 54.99, 5),
        (142, "Sunrace", "RS3", "CSRS3EAUM", 11, "11-32", "Mackadams", 54.99, 5),
        (143, "Sunrace", "RS3", "CSRS3EASB", 11, "11-28", "Mackadams", 59.99, 5),
        (144, "Sunrace", "RS3", "CSRS3EAUB", 11, "11-32", "Mackadams", 59.99, 5),
        (145, "Sunrace", "RX1", "CSRX1EAQB", 11, "11-25", "Mackadams", 67.99, 5),
        (145, "Sunrace", "RX1", "CSRX1EASB", 11, "11-28", "Mackadams", 67.99, 5),
        (145, "Sunrace", "RX1", "CSRX1EAUB", 11, "11-32", "Mackadams", 67.99, 5),
        (145, "Sunrace", "RX1", "CSRX1EAWB", 11, "11-36", "Mackadams", 79.99, 5),
        (146, "Shimano", "HG700", "CSHG700134", 11, "11-34", "Madison", 59.99, 6),
        (147, "Shimano", "HG800", "CSHG800134", 11, "11-34", "Madison", 94.99, 6),
        (148, "Shimano", "M9001", "CSM9001140", 11, "11-40", "Madison", 289.99, 6),
        (149, "Shimano", "LG400", "CSLG40011145", 11, "11-45", "Madison", 79.99, 6),
        (150, "Shimano", "LG400", "CSLG40011150", 11, "11-50", "Madison", 94.99, 6),
        (151, "Shimano", "LG700", "CSLG70011145", 11, "11-45", "Madison", 129.99, 6),
        (152, "Shimano", "LG700", "CSLG70011150", 11, "11-50", "Madison", 129.99, 6),
        (153, "Shimano", "M5100", "CSM5100142", 11, "11-42", "Madison", 64.99, 6),
        (154, "Shimano", "M5100", "CSM5100151", 11, "11-51", "Madison", 79.99, 6),
        (155, "Shimano", "M7000", "CSM7000140", 11, "11-40", "Madison", 79.99, 6),
        (156, "Shimano", "M7000", "CSM7000142", 11, "11-42", "Madison", 79.99, 6),
        (157, "Shimano", "M7000", "CSM7000146", 11, "11-46", "Madison", 84.99, 6),
        (158, "Shimano", "M8000", "CSM8000140", 11, "11-40", "Madison", 104.99, 6),
        (159, "Shimano", "M8000", "CSM8000142", 11, "11-42", "Madison", 104.99, 6),
        (160, "Shimano", "M8000", "CSM8000146", 11, "11-46", "Madison", 114.99, 6),
        (161, "Shimano", "M9100", "CSM9100045", 11, "10-45", "Madison", 329.99, 6),
        (162, "Shimano", "M9100", "CSM9100051", 11, "10-51", "Madison", 329.99, 6),
        (163, "Shimano", "R7000", "CSR7000128", 11, "11-28", "Madison", 54.99, 6),
        (164, "Shimano", "R7000", "CSR7000130", 11, "11-30", "Madison", 54.99, 6),
        (165, "Shimano", "R7000", "CSR7000132", 11, "11-32", "Madison", 59.99, 6),
        (166, "Shimano", "R7000", "CSR7000225", 11, "12-25", "Madison", 54.99, 6),
        (167, "Shimano", "R8000", "CSR8000125", 11, "11-25", "Madison", 84.99, 6),
        (168, "Shimano", "R8000", "CSR8000128", 11, "11-28", "Madison", 84.99, 6),
        (169, "Shimano", "R8000", "CSR8000130", 11, "11-30", "Madison", 89.99, 6),
        (170, "Shimano", "R8000", "CSR8000132", 11, "11-32", "Madison", 89.99, 6),
        (171, "Shimano", "R8000", "CSR8000225", 11, "12-25", "Madison", 84.99, 6),
        (172, "Shimano", "R9100", "CSR9100125", 11, "11-25", "Madison", 229.99, 6),
        (173, "Shimano", "R9100", "CSR9100128", 11, "11-28", "Madison", 239.99, 6),
        (174, "Shimano", "R9100", "CSR9100130", 11, "11-30", "Madison", 249.99, 6),
        (175, "Shimano", "R9100", "CSR9100225", 11, "12-25", "Madison", 229.99, 6),
        (176, "Shimano", "R9100", "CSR9100228", 11, "12-28", "Madison", 239.99, 6),
        (177, "Clarks", "", "C-11SC", 11, "11-42", "ZyroFisher", 69.99, 8),
        (178, "SRAM", "XG1175", "FW8079000", 11, "10-42", "ZyroFisher", 208.00, 8),
        (179, "SRAM", "PG1130", "FW1111142", 11, "11-42", "ZyroFisher", 96.00, 8),
        (180, "SRAM", "PG1130", "FW1131126", 11, "11-26", "ZyroFisher", 69.00, 8),
        (181, "SRAM", "PG1130", "FW1131128", 11, "11-28", "ZyroFisher", 69.00, 8),
        (182, "SRAM", "PG1130", "FW1131132", 11, "11-32", "ZyroFisher", 75.00, 8),
        (183, "SRAM", "PG1130", "FW1131136", 11, "11-36", "ZyroFisher", 92.00, 8),
        (184, "SRAM", "PG1170", "FW1171125", 11, "11-25", "ZyroFisher", 96.00, 8),
        (185, "SRAM", "PG1170", "FW1171126", 11, "11-26", "ZyroFisher", 96.00, 8),            
        (186, "SRAM", "PG1170", "FW1171128", 11, "11-28", "ZyroFisher", 96.00, 8),
        (187, "SRAM", "PG1170", "FW1171132", 11, "11-32", "ZyroFisher", 107.00, 8),
        (188, "SRAM", "PG1170", "FW1171136", 11, "11-36", "ZyroFisher", 107.00, 8),
        (189, "SRAM", "X01 XG1195", "FWX011042", 11, "10-42", "ZyroFisher", 371.00, 8),
        (190, "SRAM", "XG1190", "FW18067004", 11, "11-32", "ZyroFisher", 352.00, 8),
        (191, "SRAM", "XG1150", "FW1151042", 11, "10-42", "ZyroFisher", 151.00, 8),
        (192, "SRAM", "XX1 XG1199", "FWXX1042", 11, "10-42", "ZyroFisher", 392.00, 8)]

    cursor.executemany("REPLACE INTO cassettes_11spd VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)", data)

    connect.commit()
    connect.close()

def get_distributor_11spd_all(distributor: str):
    connect = connect_database()
    cursor = connect.cursor()
    print(distributor)
    cursor = connect.cursor()
    result = cursor.execute(
        "SELECT brand, model, partNumber, speed, ratio, distributor, rrp FROM cassettes_11spd")

    rows = result.fetchall()
    connect.close()
    return response(rows)

def get_distributor_11spd(distributor: str):
    connect = connect_database()
    cursor = connect.cursor()
    print(distributor)
    cursor = connect.cursor()
    result = cursor.execute(
        "SELECT brand, model, partNumber, speed, ratio, distributor, rrp FROM cassettes_11spd WHERE distributor=?", [distributor])

    rows = result.fetchall()
    connect.close()
    return response(rows)

def get_brand_11spd_all(brand: str):
    connect = connect_database()
    cursor = connect.cursor()
    print(brand)
    cursor = connect.cursor()
    result = cursor.execute(
        "SELECT brand, model, partNumber, speed, ratio, distributor, rrp FROM cassettes_11spd ")

    rows = result.fetchall()
    connect.close()
    return response(rows)

def get_brand_11spd(brand: str):
    connect = connect_database()
    cursor = connect.cursor()
    print(brand)
    cursor = connect.cursor()
    result = cursor.execute(
        "SELECT brand, model, partNumber, speed, ratio, distributor, rrp FROM cassettes_11spd WHERE brand=?", [brand])

    rows = result.fetchall()
    connect.close()
    return response(rows)

def get_speed_11spd_all():
    connect = connect_database()
    cursor = connect.cursor()
    result = cursor.execute(
        "SELECT brand, model, partNumber, speed, ratio, distributor, rrp FROM cassettes_11spd")

    rows = result.fetchall()
    connect.close()
    return response(rows)

def get_speed_11spd(speed: int):
    connect = connect_database()
    cursor = connect.cursor()
    print(speed)
    cursor = connect.cursor()
    result = cursor.execute(
        "SELECT brand, model, partNumber, speed, ratio, distributor, rrp FROM cassettes_11spd WHERE speed=?", [speed])

    rows = result.fetchall()
    connect.close()
    return response(rows)
    
def get_ratio_11spd_all(ratio: str):
    connect = connect_database()
    cursor = connect.cursor()
    print(ratio)
    cursor = connect.cursor()
    result = cursor.execute(
        "SELECT brand, model, partNumber, speed, ratio, distributor, rrp FROM cassettes_11spd")

    rows = result.fetchall()
    connect.close()
    return response(rows)

def get_ratio_11spd(ratio: str):
    connect = connect_database()
    cursor = connect.cursor()
    print(ratio)
    cursor = connect.cursor()
    result = cursor.execute(
        "SELECT brand, model, partNumber, speed, ratio, distributor, rrp FROM cassettes_11spd WHERE ratio=?", [ratio])

    rows = result.fetchall()
    connect.close()
    return response(rows)

def get_speed_ratio_11spd(ratio: str):
    connect = connect_database()
    cursor = connect.cursor()
    print(ratio)
    cursor = connect.cursor()
    result = cursor.execute(
        "SELECT brand, model, partNumber, speed, ratio, distributor, rrp FROM cassettes_11spd WHERE speed=11 AND ratio=?", [ratio])

    rows = result.fetchall()
    connect.close()
    return response(rows)
