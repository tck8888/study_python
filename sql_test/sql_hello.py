import pymysql as sql

# 数据库的查询操作
try:
    conn = sql.connect(host='localhost', user='root', passwd='root', db='test', port=3306, charset='utf8')
    cur = conn.cursor()
    cur.execute('select * from user_info')
    data = cur.fetchall()
    for row in data:
        user_name = row[0]
        user_password = row[1]
        mobile = row[3]
        print("user_name=%s,user_password=%s,mobile=%s" % (user_name, user_password, mobile))
    cur.close()
    conn.close()

except Exception:
    print("查询失败")
