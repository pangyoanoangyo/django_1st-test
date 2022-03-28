from django.http import HttpResponse
from django.shortcuts import render, HttpResponse, redirect
import random
from django.views.decorators.csrf import csrf_exempt 
#csrf의 보안을 일단 사용안하기 위해

# from matplotlib.pyplot import title 

# 랜덤을 불러온다.


# Create your views here.


nextId = 4
mydata = [ # mydata라는 리스트를 만든다
        {'id':1, "title":'view',"body":'view에 대해서 설명을 해봅시다'},
        {'id':2, "title":'model',"body":'model에 대해서 설명을 해봅시다'},
        {'id':3, "title":'random',"body":'random한 숫자'}
]        #딕셔너리를 만들어서 데이터를 만들어줌


#자주 사용하는 HTML내용은 함수로 만들자
def HTMLtem(articleTag):
    global mydata #외부의 변수이기 때문에 전역변수 선언
    ol = ""
    for data in mydata:
        ol += f'<li><a href="/read/{data["id"]}">{data["title"]}</a></li>'
        #여기는 f는 따옴표를 적는게 귀찮아서 적음, 그사이에 {}를 넣으면 따옴표 안써도됨.
        # 구글에 f-string을 검색해보면 나온다.        
    return HttpResponse(f'''
    <html>
    <body>
        <h1> <a href = "/"> Django Homepage </a> </h1>
        <ul>
            {ol}
        </ul>
        {articleTag}
        <ul>
            <a href ="/create/"><button> 글쓰기 </button></a></li> 
        </ul>
    </body>
    </html>            
                        
''') 
# '''여러줄을 사용할수 있음


# url를 통해온 내용이 여기로 오고 인덱스를 통해 view로 간다.
def index(request):  #처음에는 리퀘스트는 사용한다
    article ='''
            <h2> Welcome to World </h2>
        여기는 장고입니다<br>
        <a href ="/test"> 테스트 페이지 </a>
        '''
    return HttpResponse(HTMLtem(article))
#자주 사용하는 HTML은 함수로 만들어주고 그 내용을 위에 넣는다.

def read(request,id):  #여기에 생성하고, url에 넣어주면 그대로 나온다
    global mydata
    article = ''
    for data in mydata:
        if data['id'] ==int(id):
            article = f'<h1>{data["title"]}</h1>{data["body"]}'
    return HttpResponse(HTMLtem(article))

@csrf_exempt
def create(request): #여기에 생성하고, url에 넣어주면 그대로 나온다
    global nextId
    global mydata
    if request.method =='GET':
        article ='''
            <form action="/create/" method ="post"> 
                <h1> 글쓰기 페이지</h1>
                <p><input type"text" name="subject" placeholder='title'></p>
                <p><textarea name="content" placeholder="write page"></textarea></p>
                <p><input type="submit"></p>
            </form>
        ''' 
        return HttpResponse(HTMLtem(article))
    elif request.method == 'POST':
        title = request.POST['title']
        body = request.POST['body']
        newData= {"id":nextId, 'title':title, "body":body}            
        mydata.append(newData)
        url = '/read/'+str(nextId)
        nextId = nextId + 1 #추가시마다 1을 증가하여 ID값을 증가한다.
        return redirect(url) # 글의 상세보기페이지로 리디렉트해라고 지시
    
    # method ="post"를 하지 않으면 내부 정보가 다 나간다고 보는게 맞다
    # placeholder는 컨텐츠안에 내용 삽입
    # form태그안에 action은 실행할 내용
    
def test(request):
    return HttpResponse(f'''
    <html>
    <body>
        <h1> <a href = "/"> 여기는 테스트 페이지입니다 </a> </h1>

    </body>
    </html>            
                        
    ''')
