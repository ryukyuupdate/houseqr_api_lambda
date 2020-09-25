import mysql.connector as mydb



def db_start():
    conn = mydb.connect(
        host='database-1.cvcdesc9d2ur.ap-northeast-1.rds.amazonaws.com',
        port='3306',
        user='admin',
        password='password',
        database='db01'
    )
    cur = conn.cursor(dictionary=True)
    return conn, cur


# ----------------------


# 新規で会社を登録する
def db_company_register(email, password, company_name, officer_name, phone_number, notification_email, notification_phone, idToken):
    conn, cur = db_start()
    cur.execute(
        "INSERT INTO companys(email, password, company_name, officer_name, phone_number, notification_email, notification_phone, idToken) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)", 
        (email, password, company_name, officer_name, phone_number, notification_email, notification_phone, idToken)
    )
    conn.commit()
    return 0


# トークを取得
def db_company_login(email, password):
    conn, cur = db_start()
    cur.execute('select idToken from companys where email="'+ email +'" and password="'+ password +'"')
    data = cur.fetchall()
    return data


# トークンで会社情報を取得
def db_company_info(idToken):
    conn, cur = db_start()
    cur.execute('select * from companys where idToken="'+ idToken +'"')
    data = cur.fetchall()
    for i in data:
        i.pop('created_at')
        i.pop('updated_at')
    return data


# idで会社情報を取得
def db_company_info2(id):
    conn, cur = db_start()
    cur.execute('select * from companys where id='+ str(id))
    data = cur.fetchall()
    for i in data:
        i.pop('created_at')
        i.pop('updated_at')
    return data


# 指定したidの会社を削除
def db_company_delete(idToken):
    conn, cur = db_start()
    cur.execute("DELETE FROM companys WHERE idToken='" + idToken + "'" )
    conn.commit()
    return 0


# 会社情報を更新
def db_company_change(id, email, password, company_name, officer_name, phone_number, notification_email, notification_phone, idToken):
    conn, cur = db_start()
    cur.execute(
        'UPDATE companys SET email=%s, password=%s, company_name=%s, officer_name=%s, phone_number=%s, notification_email=%s, notification_phone=%s, idToken=%s WHERE id=%s', 
        (email, password, company_name, officer_name, phone_number, notification_email, notification_phone, idToken, id)
    )
    conn.commit()
    return 0


# 現在登録されているメールアドレスを検索
def db_company_emailcheck(email):
    conn, cur = db_start()
    cur.execute('select email from companys where email="'+ email +'"')
    data = cur.fetchall()
    data = len(data)
    return data


# トークンで会社IDを取得
def db_company_id(idToken):
    conn, cur = db_start()
    cur.execute('select id from companys where idToken="'+ idToken +'"')
    data = cur.fetchall()
    return data


# 電話認証を更新にする
def db_company_phone_check(id, phone_check):
    conn, cur = db_start()
    cur.execute(
        'UPDATE companys SET phone_check=%s WHERE id=%s', 
        (phone_check, id)
    )
    conn.commit()
    return 0


# メール認証を更新にする
def db_company_email_check_db(id, email_check):
    conn, cur = db_start()
    cur.execute(
        'UPDATE companys SET email_check=%s WHERE id=%s', 
        (email_check, id)
    )
    conn.commit()
    return 0


# ----------------------my_mysql_propertys


# 新規で物件を登録する
def db_property_register(company_id, property_name, property_address):
    conn, cur = db_start()
    cur.execute(
        "INSERT INTO propertys(company_id, property_name, property_address) VALUES(%s, %s, %s)", 
        (company_id, property_name, property_address)
    )
    conn.commit()
    return cur.lastrowid


# 会社IDで全ての物件情報を取得
def db_property_list(company_id):
    conn, cur = db_start()
    cur.execute('select * from propertys where company_id="'+ str(company_id) +'"')
    data = cur.fetchall()
    for i in data:
        i.pop('created_at')
        i.pop('updated_at')
    return data


# 会社IDで全ての物件情報を取得
def db_property_id(company_id):
    conn, cur = db_start()
    cur.execute('select id from propertys where company_id="'+ str(company_id) +'"')
    data = cur.fetchall()
    return data


# 会社IDと物件IDで物件情報を取得
def db_property_info(company_id, id):
    conn, cur = db_start()
    cur.execute('select * from propertys where company_id="'+ str(company_id) +'"' + 'and id="' + str(id) +'"')
    data = cur.fetchall()
    for i in data:
        i.pop('created_at')
        i.pop('updated_at')
    return data

# 物件IDで物件情報を取得
def db_property_info2(id):
    conn, cur = db_start()
    cur.execute('select * from propertys where id="'+ str(id) +'"')
    data = cur.fetchall()
    for i in data:
        i.pop('created_at')
        i.pop('updated_at')
    return data


# 指定したidの物件情報を削除
def db_property_delete(company_id, id):
    conn, cur = db_start()
    cur.execute("DELETE FROM propertys WHERE id='" + str(id) + "AMD company_id=" + str(company_id) + "'")
    conn.commit()
    return 0


# 指定したIDの物件情報を更新
def db_property_change(company_id, id, property_name, property_address):
    conn, cur = db_start()
    cur.execute(
        'UPDATE propertys SET property_name=%s, property_address=%s WHERE id=%s AND company_id=%s', 
        (property_name, property_address, id, company_id)
    )
    conn.commit()
    return 0


# ----------------------my_mysql_parts


# 新規で通知部分を登録する
def db_part_register(property_id, part_name, part_status):
    conn, cur = db_start()
    cur.execute(
        "INSERT INTO parts(property_id, part_name, part_status) VALUES(%s, %s, %s)", 
        (property_id, part_name, part_status)
    )
    conn.commit()
    return 0


# 物件IDで全ての通知場所情報を取得
def db_part_propertyid_list(property_id):
    conn, cur = db_start()
    cur.execute('select * from parts where property_id="'+ str(property_id) +'"')
    data = cur.fetchall()
    for i in data:
        i.pop('created_at')
        i.pop('updated_at')
    return data


# 物件IDで全ての通知場所情報を取得
def db_part_info(id):
    conn, cur = db_start()
    cur.execute('select * from parts where id="'+ str(id) +'"')
    data = cur.fetchall()
    for i in data:
        i.pop('created_at')
        i.pop('updated_at')
    return data


# 指定したidの通知場所情報を削除
def db_part_delete(id):
    conn, cur = db_start()
    cur.execute("DELETE FROM parts WHERE id='" + str(id) + "'" )
    conn.commit()
    return 0


# 指定したIDの通知場所情報を更新
def db_part_change(id, part_name, part_status):
    conn, cur = db_start()
    cur.execute(
        'UPDATE parts SET part_name=%s, part_status=%s WHERE id=%s', 
        (part_name, part_status, id)
    )
    conn.commit()
    return 0