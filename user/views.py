from django.shortcuts import render, redirect

# 화면에서 데이터를 받아와서 서버로 전달해줘야하니까 데이터베이스와 관련된 모델을 추가해줘야함
# .(나의위치와 동일한)model을 갖고올건데 UserModel을 임포트한다. (사용자정보를 저장하는 모델이니까)
import user.views
from .models import UserModel
from django.http import HttpResponse #화면에 글자를 띄우는 친구
#장고에 기본적인 친구를 가져올때는 auth까지 동일한듯.
from django.contrib.auth import get_user_model #사용자가 데이터베이스 안에 있는지 검사하는 함수
from django.contrib import auth #여기서는 auth를 임포트!
from django.contrib.auth.decorators import login_required #로그인한 사용자만 로그아웃할수 있게 추가

# ID oli PW 1235
# Create your views here.
def sign_up_view(request): #sign_up_view에 요청이 들어오는 url을 실행할때
    #장고서버가 url의 요청방식을 확인하고
    if request.method == 'GET': #GET요청으로 왔으면 화면출력
        user = request.user.is_authenticated # 로그인되어있는데 회원가입페이지나오는것 수정하기위해
        # 로그인여부 확인후 user있으면, user변수에 저장
        if user:
            return redirect('/')
        else:
            return render(request, 'user/sign_up.html')
    elif request.method == 'POST': #POST요청으로 왔으면 elif문실행
        # POST로 받은 요청을 .get(받아온다)'username'이라는 이름이라는 데이터를 가져오겠다. 만일 없다면 None으로 처리하겠다.
        username = request.POST.get('username','') #('username',None)으로하면 없을시 None값으로 들어감
        password = request.POST.get('password','')
        password2 = request.POST.get('password2', '')
        bio = request.POST.get('bio', '')

        # 패스워드가 같을때 회원가입이 되도록 하는 코드 추가
        if password != password2: #패스워드가 다르다면     #패스워드가 같지 않다고 알람
            return render(request, 'user/sign_up.html',{'error':'패스워드를 확인해 주세요'}) #페이지를 다시띄워줌
        else: #유저네임, 패스워드가 없을수도 있잖아? 잘적었다면 이부분은 지나가겠지
            if username == '' or password == '':
                return render(request, 'user/sign_up.html', {'error': '사용자 이름과 비밀번호는 필수 값 입니다.'})

            #get_user_model()을 사용해서 데이터베이스에 username을 가진사람이 있는지 확인
            exist_user = get_user_model().objects.filter(username=username)
            #---------여기는 우리가 만든 USerModel사용시 썼던 코드----------
            #여기에 사용자 이름이 존재한다면 걸러주는 코드 추가
            #UserModel에서 object갖고오는데 filter(검색)해서 가져오겠다.
            #filter는 검색해서 있으면 있다. 없으면 없음으로 출력해줌
            # exist_user = UserModel.objects.filter(username=username)
            #______________________________________여기까지 ___________

            if exist_user:#이게 그냥 이자체로 있다면 exist_user가 있다면
                return render(request, 'user/sign_up.html',{'error':'사용자가 존재합니다'}) #회원가입페이지 다시띄워
            else: #사용자가 없을경우
                #장고에 있는 모델사용시 이렇게 간편해짐. 그리고 비밀번호도 암호화해서 저장됨
                UserModel.objects.create_user(username=username, password=password, bio=bio)
                return redirect('/sign-in/')


            #-----------여기도 우리가 만든 UserModel()사용할떄 쓴코드--------
                # new_user = UserModel() #model.py에서 class UserModel()을 드디어 사용!
                # # UserModel()의 객체로 new_user가 생성되었고
                # new_user.username = username #new_user의 username = 우리가 받아온 username
                # new_user.password = password#new_user의 password = 우리가 받아온 username
                # new_user.bio = bio  # new_user의 bio = 우리가 받아온 username
                # new_user.save()  # 이 정보들을 저장하겠다. 어디에? 데이터베이스에
                # return redirect('/sign-in/')  # 로그인화면을 켜주자. 일단 redirect임포트하고~ 적자
            # __________________여기까지_________________________________

#로그인은 어떻게 하는거다? 세션에 사용자 정보를 저장하는 것이다.
def sign_in_view(request):
    if request.method == 'POST': #post요청으로 들어오면 '로그인성공!'을 보여줌
        # request.POST에는 요청한 POST 데이터가 다 담겨있음
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        #모듈을 먼저불러오는게 아닌 authenticate함수를 먼저불러온다.
        #얘는 암호화된 비밀번호랑 입력된 비밀번호가 일치하는지, 이 비밀번호가 사용자가 맞는지 한번에 확인해줌
        me = auth.authenticate(request, username=username, password=password)
        # ★사용자가 있는지 없는지만 구분해주면됨(위에서 autenticate가 다 비교해주니까 )
        if me is not None: #내정보가 있다면 (비어있지 않다면)
            #장고가 알아서 관리함. 세션설정안해줘도..
            auth.login(request, me) #내정보만 넣어주면 됨. (me)
            #여기서 logout으로 바꾸면 로그아웃이된대...개신기
            return redirect('/')
        else: #만약 패스워드가 다르다면
            return render(request, 'user/sign_in.html', {'error':'유저이름 혹은 패스워드를 확인해주세요.'}) #로그인페이지로 돌아가랏


      #-------------여기는 기존 우리가 작성한 UserModel로 사용시--------------
        #다 잘 받아왔다면 데이터베이스와 비교해야징? UserModel은 사용자 모델 데이터베이스
        #클래스 UserModel의 객체에서 username 과 POST에서 받아온 username과 같은친구를 불러와서 me에 넣겠다.
        #get함수는 데이터가 무조건 있어야함. 데이터가없으면 에러가남. 있든없든 오류가나지않는 filter와의 차이점!
        # me = UserModel.objects.get(username=username)

        # model에서 불러온 username과 같은사람의 패스워드가 POST에서 받아온 password와 같다면
        # if me.password == password: #★장고에 있는 기존 모델을 사용한 순간 이부분이 맞지않게됨.
                                    #왜? 패스워드가 데이터베이스에 암호화되서 저장이 되어있으니까
                                    #하지만 장고는 또 암호화된걸 복호화하는 기능도있지
            # session은 사용자 정보를 저장할 수 있는 공간!
            # session에 ['user']라는 걸 넣는데 그 내용을 모델의 username으로
            # request.session['user'] = me.username
        #     return HttpResponse(me.username)
        # else:  # 만약 패스워드가 다르다면
        #     return redirect('/sign-in')  # 로그인페이지로 돌아가랏
        # ----------------여기까지 ------------------------------------------


    elif request.method == 'GET': #get 요청으로 들어오면 화면을 보여주고
        #로그인되어있는데 로그인페이지 나오면안되잖아?
        user = request.user.is_authenticated
        if user:
            return redirect('/')
        else:
            return render(request, 'user/sign_in.html')

@login_required #사용자가 꼭 로그인이 되어있어야만 접근이 가능한 함수라고 말해주는것.
def logout(request):#로그인, 로그아웃은 user와 관련된 기능이기때문에 user앱에 작성
    #만약 우리가 장고의 기능을 사용하지 않았다면,
    #request에 session확인해서 user가 있는지 없는지 확인하고
    #있다면/없다면 의 작업들을 다 적어줘야함
    auth.logout(request)
    return redirect('/')
#views에서 함수만들었으니 이 logout함수를 사용할 수 있게해주는 url연결해야지? user앱의 urls.py로 가쟈

# user/views.py

@login_required
def user_view(request):
    if request.method == 'GET': #메소드가 get
        #exclude는 제외하겠다. 내가 나를 보거나 팔로우할 이유가 없으니 나를 제외하겠다.
        # 사용자를 불러오기, exclude와 request.user.username 를 사용해서 '로그인 한 사용자'를 제외하기
        user_list = UserModel.objects.all().exclude(username=request.user.username)
        return render(request, 'user/user_list.html', {'user_list': user_list}) #html과 함께 user_list도 보여줄거야~


@login_required
def user_follow(request, id):
    me = request.user #로그인한 사용자는 me
    click_user = UserModel.objects.get(id=id) #팔로우/팔로우취소하려고 누른 사용자가 click_user
    if me in click_user.followee.all(): #click_user를 팔로우하는 모든 사용자중에서 내가 있으면, 내가팔로우 중인거지?
        click_user.followee.remove(request.user) #그럼 내가 그사용자를 다시클릭한건 팔로우취소이므로, 나를 제거해준다.
    else: # click_user의 followee에 내가 없다면
        click_user.followee.add(request.user) #나를 추가해준다. 팔로우한다.
    return redirect('/user')
