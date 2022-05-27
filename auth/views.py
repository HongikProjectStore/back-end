from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.db import connection

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

 
def login(request):
    # Using POST, get id & pw 
    if request.method =='POST':
        user_id = request.POST['userID']
        user_password = request.POST['userPassword']

    response_data = {
        "userID": user_id,
        "userPassword": user_password,
        "success": False
    }

    # Using select query, get id & pw that is matching input id & pw values.
    try:
        cursor = connection.cursor()
        query = "select user_id, user_password from user_table where user_id='{0}' and user_password='{1}'".format(user_id, user_password)
        cursor.execute(query)
        stocks = cursor.fetchone()

        connection.commit()
        connection.close()
    except:
        connection.rollback()
        return JsonResponse(response_data)

    # Check query result is empty
    if(stocks is None):
        return JsonResponse(response_data)

    # Result is not empty, one more check id & pw is matching
    if(str(stocks[0]) == user_id and str(stocks[1] == user_password)):
        response_data = {
            "userID" : user_id,
            "userPassword" : user_password,
            "success" : True
        }
        # When login success, send "True" flag
        return JsonResponse(response_data)
    else:
        # When login fail, send "False" flag
        return JsonResponse(response_data)


def register(request):
    # Using POST, get User's information for register
    if request.method =='POST':
        user_id = request.POST['userID']
        user_password = request.POST['userPassword']
        user_name = request.POST['userName']
        user_age = request.POST['userAge']
        # Hardcoding part
        user_email = request.POST['userEmail']
        user_gender = request.POST['userGender']
        user_image = 3
        num_go_to_store = 3
        time_to_go_to_store = 3

    response_data = {
        "success" : False
    }

    # Using insert query, insert user into table 
    try:
        cursor = connection.cursor()
        query = "insert into user_table values('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', {6}, {7}, {8})".format(
            user_id, user_password, user_name, user_email, user_gender, user_age, user_image, num_go_to_store, time_to_go_to_store
        )
        cursor.execute(query)

        connection.commit()
        connection.close()
    except:
        connection.rollback()
         # When insert fail, Send "False" flag
        return JsonResponse(response_data)
    
    response_data = {
        "success" : True
    }
    # When insert success, Send "True" flag
    return JsonResponse(response_data)


def deleteUser(request):
    # Using POST, get id & pw
    if request.method =='POST':
        user_id = request.POST['userID']
        user_password = request.POST['userPassword']

    response_data = {
        "success" : False
    }
    # Using select, get pw for id
    try:
        cursor = connection.cursor()
        pw_check_query = "select user_password from user_table where user_id='{0}'".format(user_id)
        cursor.execute(pw_check_query)
        check_pw = cursor.fetchone()
        
        # Before delete account, Check ID and PW
        if(str(check_pw[0]) != user_password):
            return JsonResponse(response_data)
        # When check password success, Start delete query
        query = "delete from user_table where user_id='{0}' and user_password='{1}'".format(user_id, user_password)
        cursor.execute(query)

        connection.commit()
        connection.close()
    except:
        connection.rollback()
        return JsonResponse(response_data)

    # When success delete, send "success" True
    response_data = {
        "success" : True
    }
    return JsonResponse(response_data)
