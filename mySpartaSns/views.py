# 각url에서 어떤 역할/기능을 수행할건지 만들어주는 공간
from django.http import HttpResponse
from django.shortcuts import render #render는 html파일을 보여주는 역할


def base_response(request):#얘를 작동하게 하려면 url과 연결해야함
    return HttpResponse("안녕하세요! 장고의 시작입니다!")
        #HttpResponse는 괄호안에 있는내용을 전달.

def first_view(request):
    return render(request, 'my_test.html')

#(기능별 분류)사용자 관리, 글쓰기, 친구만들기
#(주제별 분류) 글쓰기, 사용자
