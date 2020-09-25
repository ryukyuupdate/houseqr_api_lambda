from datetime import datetime
import ast
import my_mysql



def distribution(request_url_path, request_body_data):
    if request_url_path == '/api/company/register':
        return api_company_register(request_body_data=request_body_data)

    elif request_url_path == '/api/company/phone_check':
        return api_company_phone_check(request_body_data=request_body_data)
        
    elif request_url_path == '/api/company/email_check':
        return api_company_email_check(request_body_data=request_body_data)
        
    elif request_url_path == '/api/company/email_check_db':
        return api_company_email_check_db(request_body_data=request_body_data)
        
    elif request_url_path == '/api/company/login':
        return api_company_login(request_body_data=request_body_data)
        
    elif request_url_path == '/api/company/info':
        return api_company_info(request_body_data=request_body_data)
        
    elif request_url_path == '/api/company/delete':
        return api_company_delete(request_body_data=request_body_data)
        
    elif request_url_path == '/api/company/change':
        return api_company_change(request_body_data=request_body_data)
        
    elif request_url_path == '/api/company/emailcheck':
        return api_company_emailcheck(request_body_data=request_body_data)
        
    elif request_url_path == '/api/property/register':
        return api_property_register(request_body_data=request_body_data)
        
    elif request_url_path == '/api/property/list':
        return api_property_list(request_body_data=request_body_data)
        
    elif request_url_path == '/api/property/info':
        return api_property_info(request_body_data=request_body_data)
        
    elif request_url_path == '/api/property/delete':
        return api_property_delete(request_body_data=request_body_data)
        
    elif request_url_path == '/api/property/change':
        return api_property_change(request_body_data=request_body_data)
        
    elif request_url_path == '/api/part/register':
        return api_part_register(request_body_data=request_body_data)
        
    elif request_url_path == '/api/part/propertyidlist':
        return api_part_propertyidlist(request_body_data=request_body_data)
        
    elif request_url_path == '/api/part/info':
        return api_part_info(request_body_data=request_body_data)
        
    elif request_url_path == '/api/part/delete':
        return api_part_delete(request_body_data=request_body_data)
        
    elif request_url_path == '/api/part/change':
        return api_part_change(request_body_data=request_body_data)
        
    elif request_url_path == '/api/part/notification':
        return api_part_notification(request_body_data=request_body_data)
        
    elif request_url_path == '/api/propertypart/list':
        return api_propertypart_list(request_body_data=request_body_data)
        
    elif request_url_path == '/api/propertypart/info':
        return api_propertypart_info(request_body_data=request_body_data)
        
    else:
        return 'error!!'


# ----------------------------------------------------------------------------------


# 新規で会社を登録する
# @app.route('/api/company/register', methods=["POST"])
def api_company_register(request_body_data):
    email = request_body_data['email']
    password = request_body_data['password']
    company_name = request_body_data['company_name']
    officer_name = request_body_data['officer_name']
    phone_number = request_body_data['phone_number']
    notification_email = request_body_data['notification_email']
    notification_phone = request_body_data['notification_phone']
    # idTokenはここで生成
    idToken = email + password
    data = my_mysql.db_company_register(
        email = email, 
        password = password, 
        company_name = company_name, 
        officer_name = officer_name, 
        phone_number = phone_number, 
        notification_email = notification_email, 
        notification_phone = notification_phone, 
        idToken = idToken
    )
    idToken = {'idToken': idToken}
    return idToken


# 電話番号を認証する
# @app.route('/api/company/phone_check', methods=["POST"])
def api_company_phone_check(request_body_data):
    company_id = request_body_data['company_id']
    check_status = request_body_data['check_status']
    data = my_mysql.db_company_phone_check(
        id = company_id,
        phone_check = check_status
    )
    return data


# メールを認証する
# @app.route('/api/company/email_check', methods=["POST"])
def api_company_email_check(request_body_data):
    company_id = request_body_data['company_id']
    data = my_mysql.db_company_phone_check(
        id = company_id,
        phone_check = 1
    )
    return data


# 電話番号認証のステータス変更
# @app.route('/api/company/email_check_db', methods=["POST"])
def api_company_email_check_db(request_body_data):
    company_id = request_body_data['company_id']
    check_status = request_body_data['check_status']
    data = my_mysql.db_company_email_check_db(
        id = company_id,
        email_check = check_status
    )
    return data


# トークを取得
# @app.route('/api/company/login', methods=["POST"])
def api_company_login(request_body_data):
    email = request_body_data['email']
    password = request_body_data['password']
    data =my_mysql.db_company_login(
        email=email, 
        password=password
    )
    if len(data) == 0:
        data = {"idToken": "loginError"}
    else:
        data = data[0]
    return data


# トークンで会社情報を取得
# @app.route('/api/company/info', methods=["POST"])
def api_company_info(request_body_data):
    idToken = request_body_data['idtoken']
    
    data = my_mysql.db_company_info(
        idToken = idToken
    )
    data = data[0]
    return data


# 指定したidの会社を削除
# @app.route('/api/company/delete', methods=["POST"])
def api_company_delete(request_body_data):
    idToken = request_body_data['idToken']
    data = my_mysql.db_company_delete(
        idToken = idToken
    )
    return data


# 会社情報を更新
# @app.route('/api/company/change', methods=["POST"])
def api_company_change(request_body_data):
    id = request_body_data['id']
    email = request_body_data['email']
    password = request_body_data['password']
    company_name = request_body_data['company_name']
    officer_name = request_body_data['officer_name']
    phone_number = request_body_data['phone_number']
    notification_email = request_body_data['notification_email']
    notification_phone = request_body_data['notification_phone']
    idToken = request_body_data['idToken']
    idToken = email + password
    data = my_mysql.db_company_change(
        id = id, 
        email = email, 
        password = password, 
        company_name = company_name, 
        officer_name = officer_name, 
        phone_number = phone_number, 
        notification_email = notification_email, 
        notification_phone = notification_phone, 
        idToken = idToken
    )
    # 変更後の会社情報を取得
    data = my_mysql.db_company_info(
        idToken = idToken
    )
    data = data[0]
    return data


# 現在登録されているメールアドレスを検索
# @app.route('/api/company/emailcheck', methods=["POST"])
def api_company_emailcheck(request_body_data):
    email = request_body_data['email']
    data = my_mysql.db_company_emailcheck(
        email = email,
    )
    return data


# ----------------------


# 新規で物件情報を登録する
# @app.route('/api/property/register', methods=["POST"])
def api_property_register(request_body_data):
    property_name = request_body_data['property_name']
    property_address = request_body_data['property_address']
    idToken = request_body_data['idtoken']
    company_id = my_mysql.db_company_id(idToken=idToken)
    data = my_mysql.db_property_register(
        company_id = company_id[0]['id'], 
        property_name = property_name, 
        property_address = property_address
    )
    return data
    


# トークンで会社情報を取得
# @app.route('/api/property/list', methods=["POST"])
def api_property_list(request_body_data):
    idToken = request_body_data['idtoken']
    company_id = my_mysql.db_company_id(idToken=idToken)
    data = my_mysql.db_property_list(
        company_id = company_id[0]['id']
    )
    return data


# 特定に物件情報を取得
# @app.route('/api/property/info', methods=["POST"])
def api_property_info(request_body_data):
    property_id = request_body_data['property_id']
    data = my_mysql.db_property_info2(
        id = property_id
    )
    data2 = data[0]
    return data2


# 指定したidの物件情報を削除
# @app.route('/api/property/delete', methods=["POST"])
def api_property_delete(request_body_data):
    id = request_body_data['id']
    idToken = request_body_data['idtoken']
    company_id = my_mysql.db_company_id(idToken=idToken)
    data = my_mysql.db_property_delete(
        company_id = company_id[0]['id'],
        id = id
    )
    return data


# 物件情報を更新
# @app.route('/api/property/change', methods=["POST"])
def api_property_change(request_body_data):
    id = request_body_data['id']
    property_name = request_body_data['property_name']
    property_address = request_body_data['property_address']
    idToken = request_body_data['idtoken']
    company_id = my_mysql.db_company_id(idToken=idToken)
    data = my_mysql.db_property_change(
        company_id = company_id[0]['id'],
        id = id, 
        property_name = property_name, 
        property_address = property_address
    )
    # 変更後の物件情報を取得
    data = my_mysql.db_property_info(
        company_id = company_id[0]['id'], 
        id = id
    )
    data = data[0]
    return data


# ----------------------



# 新規で通知場所情報を登録する
# @app.route('/api/part/register', methods=["POST"])
def api_part_register(request_body_data):
    property_id = request_body_data['property_id']
    part_name = request_body_data['part_name']
    part_status = request_body_data['part_status']
    data = my_mysql.db_part_register(
        property_id = property_id, 
        part_name = part_name, 
        part_status = part_status
    )
    return data


# property_idで全ての通知場所情報を取得する
# @app.route('/api/part/propertyidlist', methods=["POST"])
def api_part_propertyidlist(request_body_data):
    property_id = request_body_data['property_id']
    data = my_mysql.db_part_propertyid_list(
        property_id = property_id
    )
    return data


# 特定の監視場所情報を返す
# @app.route('/api/part/info', methods=["POST"])
def api_part_info(request_body_data):
    part_id = request_body_data['part_id']
    data = my_mysql.db_part_info(
        id = part_id
    )
    data2 = data[0]
    return data2


# 指定したidの通知場所情報を削除
# @app.route('/api/part/delete', methods=["POST"])
def api_part_delete(request_body_data):
    id = request_body_data['id']
    data = my_mysql.db_part_delete(
        id = id
    )
    return data


# 通知場所情報を更新
# @app.route('/api/part/change', methods=["POST"])
def api_part_change(request_body_data):
    id = request_body_data['id']
    part_name = request_body_data['part_name']
    part_status = request_body_data['part_status']
    if part_status == 'true':
        part_status = 1
    elif part_status == 'false':
        part_status = 0
    data = my_mysql.db_part_change(
        id = id, 
        part_name = part_name, 
        part_status = part_status
    )
    # 変更後の物件情報を取得
    data = my_mysql.db_part_info(
        id = id
    )
    data = data[0]
    return data


# 住居者が通知場所の交換依頼
# @app.route('/api/part/notification', methods=["POST"])
def api_part_notification(request_body_data):
    id = request_body_data['id']
    part_name = request_body_data['part_name']
    part_status = request_body_data['part_status']
    property_id = request_body_data['property_id']
    property_name = request_body_data['property_name']
    if part_status == 'true':
        part_status = 1
    elif part_status == 'false':
        part_status = 0
    else:
        pass
    # 通知ありの状態にする
    data = my_mysql.db_part_change(
        id = id, 
        part_name = part_name, 
        part_status = part_status
    )
    # property_idでcompany_idを取得
    data2 = my_mysql.db_property_info2(
        id=property_id
    )
    property_name = data2[0]['property_name']
    # company_idでphone_numberとemailを取得
    company_info_data = my_mysql.db_company_info2(
        id=data2[0]['company_id']
    )
    email_address = company_info_data[0]['email']
    phone_number = company_info_data[0]['phone_number']
    return company_info_data[0]


# property_idでメールアドレスを取得してメール送信
# def notification_sendemail(property_id, part_name, email_address, property_name):
#     subject = 'HouseWathcer からの通知です'
#     message01 = '「' + property_name + '」で「' + part_name + '」の交換依頼がありました。'
#     message02 = '下記リンクから確認してください。'
#     message03 = 'http://3.114.195.102:8080/mypage/changepart?property_id=' + property_id


# property_idで電話番号を取得してAmazon Connectで電話をかける
# def notification_connect(property_id, property_name, part_name, phone_number):
#     call.call_connect(
#         phone_number = phone_number,
#         property_name = property_name,
#         part_name = part_name
#     )


# --------------------------

# トークンで会社情報を取得
# @app.route('/api/propertypart/list', methods=["POST"])
def api_propertypart_list(request_body_data):
    idToken = request_body_data['idtoken']
    company_id = my_mysql.db_company_id(idToken=idToken)
    data = my_mysql.db_property_list(
        company_id = company_id[0]['id']
    )
    data3 = []
    for i in data:
        data2 = my_mysql.db_part_propertyid_list(
            property_id = i['id']
        )
        i['part_info'] = data2
        data3.append(i)
    return data3


# 特定の物件情報とその物件の監視場所を返す
# @app.route('/api/propertypart/info', methods=["POST"])
def api_propertypart_info(request_body_data):
    property_id = request_body_data['property_id']
    idToken = request_body_data['idtoken']
    company_id = my_mysql.db_company_id(idToken=idToken)
    data = my_mysql.db_property_info(
        company_id = company_id[0]['id'], 
        id = property_id
    )
    data2 = my_mysql.db_part_propertyid_list(
        property_id = property_id
    )
    data[0]['part_info'] = data2
    data = data[0]
    return data