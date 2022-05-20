from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.db import connection

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def login(request):
    #POST 로그인 정보 받기
    if request.method =='POST':
        user_id = request.POST['userID']
        user_password = request.POST['userPassword']

    #로그인 시 보내주는 데이터
    response_data = {
        "userID": user_id,
        "userPassword": user_password,
        "success": False
    }

    #select query를 사용하여 id, pw를 확인
    try:
        cursor = connection.cursor()
        query = "select user_id, user_password from user_table where user_id='{0}' and user_password='{1}'".format(user_id, user_password)
        #query = "select user_id, user_password from user_table"
        cursor.execute(query)
        stocks = cursor.fetchone()

        connection.commit()
        connection.close()
    except:
        connection.rollback()
        return JsonResponse(response_data)

    #로그인 실패 시 success False로 보냄
    if(stocks is None):
        return JsonResponse(response_data)

    #로그인 성공 시 맞는지 확인 후 success True로 보냄
    if(str(stocks[0]) == user_id and str(stocks[1] == user_password)):
        response_data = {
            "userID" : user_id,
            "userPassword" : user_password,
            "success" : True
        }
        return JsonResponse(response_data)
    else:
        return JsonResponse(response_data)


def register(request):
    #front에서 회원가입 정보 받아오기
    if request.method =='POST':
        user_id = request.POST['userID']
        user_password = request.POST['userPassword']
        user_name = request.POST['userName']
        user_age = request.POST['userAge']
        user_email = "new@new.com"
        user_gender = 'male'
        user_image = 3
        num_go_to_store = 3
        time_to_go_to_store = 3

    #front로 보내기 위한 데이터
    response_data = {
        "success" : False
    }

    #insert query 실행해서 회원정보를 입력, 성공 시 success를 true로 바꿔 보냄 
    try:
        cursor = connection.cursor()
        query = "insert into user_table values('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', {6}, {7}, {8})".format(
            user_id, user_password, user_name, user_email, user_gender, user_age, user_image, num_go_to_store, time_to_go_to_store
        )
        #query = "select user_id, user_password from user_table"
        cursor.execute(query)


        connection.commit()
        connection.close()
    except:
        connection.rollback()
        return HttpResponse(query)
        #return JsonResponse(response_data)
    response_data = {
        "success" : True
    }
    return JsonResponse(response_data)


# Create your views here.
