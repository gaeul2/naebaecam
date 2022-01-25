from django.views.generic import ListView, TemplateView
from django.shortcuts import render,redirect
from .models import TweetModel,TweetComment #트윗모델을 임포트한다 POST요청을 저장할 곳
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    # 이를 통해 user가 로그인되어있는지, 인증이 되어있는지 확인가능
    user = request.user.is_authenticated
    if user:#인증되었다면 user변수에 할당될것이니까.
        return redirect('/tweet') #홈페이지 주소가 128.0.0.8000/tweet으로 바뀜 그러면서 자연스레 tweet함수실행
    else:
        return redirect('/sign-in')

def tweet(request):
    if request.method == 'GET': #페이지를 보여줘야 하니까 GET
        user = request.user.is_authenticated #로그인여부를 확인해서 있으면 user변수에 저장
        if user: #user가 있으면 home.html보여줌
            #게시글들 불러와서 보여줘야지!
            #TweetModel에 저장한 모든 객체들을 불러오겠다. 그런데 생성일자를 역순으로('-') 정렬해서 가져와~
            all_tweet = TweetModel.objects.all().order_by('-created_at')
            return render(request, 'tweet/home.html',{'tweet':all_tweet})
        else: #로그인하지 않고 이 링크로오면 로그인페이지로 보내기
            return redirect(('/sign-in'))
    elif request.method == 'POST': #이 POST요청에서 이루어진 작업들은 tweet모델에 들어갈것
        #우리가 어떤걸 모델로 보내줄지 home.html의 form에서 보고오자. #name: my-content
        #TweetModel에는 글과 작성자도 함께저장. 생성/업데이트 시각은 장고가 알아서함.
        user = request.user #지금 로그인 되어있는 사용자 전체의 정보를 들고옴.
        content = request.POST.get('my-content','')
        tags = request.POST.get('tag','').split(',')#html에서 받아오는 tag
        if content == '': #아무 내용없이 작성했다면, 에러메세지를 표시하기위해 render로 변환
            #에러메세지만 보내주면 허전하니까 POST로 보내줄때 all_tweet도 같이보내줌
            all_tweet = TweetModel.objects.all().order_by('-created_at')
            return render(request, 'tweet/home.html', {'error':'글은 공백일 수 없습니다.','tweet':all_tweet})
        else: #내용이 있게 잘 작성했다면,  #한번에 작성자와 content를 저장
            my_tweet = TweetModel.objects.create(author=user, content=content)
            for tag in tags: #해당하는 태그목록들을 분리하는것
                tag = tag.strip()
                if tag != '':#내용이 있다면
                    my_tweet.tags.add(tag) #tweet모델에 태그들을 넣어준다.
            my_tweet.save()
            return redirect('/tweet')
     #------------------------이게 원래 썼던 내용-------------------
        # my_tweet = TweetModel() #my_tweet이라는 변수를만들고
        # my_tweet.author = user #my_tweet의 작성자 속성에 user를 넣어주고
        # my_tweet.content = request.POST.get('my-content','') #my_tweet의 내용물속성에 우리가 form에서 받아온 정보를 넣어줌
        # my_tweet.save()
        # return redirect('/tweet')
     # ---------------------------------------------------------
@login_required() #일단 로그인한 사용자만 삭제가 가능하도록.
def delete_tweet(request, id): #id를 인자로 받아서 써먹자
    my_tweet = TweetModel.objects.get(id=id)#해당하는 id값만 불러오기위해 함수의 인자로받은 id를 여기서 써먹음
    my_tweet.delete() #개편해...이렇게만 적으면 된다니.
    return redirect('/tweet')

@login_required()
def detail_tweet(request, id): #보기버튼 눌렀을때 트윗 상세페이지 보여주기 #id는 글을 특정해주는 id
    # 내가 누른 글의 정보가 상세페이지에 보여야함 일단 그게 나라고 생각하자
    my_tweet = TweetModel.objects.get(id=id) #filter로하니까 안나오고 get으로 바꾸니 나옴. 개신기
    tweet_comment = TweetComment.objects.filter(tweet_id=id).order_by('-created_at')#이부분도..설명필요
    return render(request, 'tweet/tweet_detail.html',{'tweet':my_tweet,'comment': tweet_comment})

@login_required()
def write_comment(request, id):#댓글생성. 해당id트윗에 댓글을 작성한다.
    #form에서 제출버튼 클릭시 post요청으로 comment가 보내진다.
    if request.method == 'POST':
        comment = request.POST.get('comment','') #form에서 받아온 comment를 comment변수에 저장
        current_tweet = TweetModel.objects.get(id=id) #몇번째 글의 내용인지 TweetModel에서 찾아서 current_tweet에 저장
        #우리가 만든 TweetComment에 comment를 넣어준다.
        TC = TweetComment()
        TC.tweet = current_tweet #어떤글의 댓글인지 알려면 현재 글을 넣어야지
        TC.author = request.user #지금 접속해있는 사용자를 작성자로 저장
        TC.comment = comment #form에서 보내준 내용을 댓글내용으로 저장
        TC.save()

        return redirect('/tweet/'+str(id)) #문자형과 숫자형은 더하기가 안되므로 형태를 맞춰주기위해 str

@login_required() #여기서 id는 tweed의 id가 아닌 comment의 id
def delete_comment(request, id):#댓글 삭제. 해당 글의 댓글을 삭제한다
    #해당 글번호, 해당글의 댓글번호
    comment = TweetComment.objects.get(id=id)
    #여기 위치한 이유는 지우고나서 하면 지워졌기때문에 못찾음
    current_tweet = comment.tweet.id #comment에 저장된 tweet모델 전부가불러와짐 그 트윗의 Id.
    comment.delete()
    return redirect('/tweet/'+str(current_tweet))

class TagCloudTV(TemplateView): #tag_cloud_view.html을 보여주겠다.
    template_name = 'taggit/tag_cloud_view.html'


class TaggedObjectLV(ListView): #태그가 있으면 태그를 보여주겠다.
    template_name = 'taggit/tag_with_post.html'
    model = TweetModel

    def get_queryset(self):
        return TweetModel.objects.filter(tags__name=self.kwargs.get('tag'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tagname'] = self.kwargs['tag']
        return context