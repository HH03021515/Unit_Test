import pymysql


db = pymysql.connect(
    host='tidb.uat.etcp.net', port=5000, user='parking_dev', password='fTg1DIUKb81#tP3#', db='parking')
cursor = db.cursor()
sql = "SELECT id, plate_number, entrance_time, exit_time, receivable_fee, remarks FROM parking_record WHERE plate_number = '渝B52V96';"
cursor.execute(sql)
data = cursor.fetchall()
print(data)
db.close()