from django.shortcuts import render
import random
import requests
from faker import Faker

# Create your views here.
def index(request):
    return render(request, 'index.html')

def hello(request):

    username = '홍길동'

    result = {
        'username' : username,

    }

    return render(request, 'hello.html', result)

def lunch(request):
    menus = ['라면', '김밥', '떡볶이']

    pick = random.choice(menus)

    result = {
        'pick' : pick,
    }
    
    return render(request, 'lunch.html', result)

def lotto(request):
    # lotto_num = [i for i in range(1,30)]
    # lotto = []
    # for _ in range(6):
    #     lotto.append(random.choice(lotto_num))
    # lotto.sort()
    numbers = range(1,46)
    lucky_lotto = sorted(random.sample(numbers,6))

    url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=1081'

    # 크롤링
    res = requests.get(url)
    data = res.json()

    no1 = data['drwtNo1']
    no2 = data['drwtNo2']
    no3 = data['drwtNo3']
    no4 = data['drwtNo4']
    no5 = data['drwtNo5']
    no6 = data['drwtNo6']

    lotto_numbers = [no1, no2, no3, no4, no5, no6]

    num = set(lucky_lotto) & set(lotto_numbers)
    result = {
        'lucky_lotto' : lucky_lotto,
        'lotto_numbers' : lotto_numbers,
        'num' : num,
    }
    
    return render(request, 'lotto.html', result)

def greeting(request, name):
    result = {
        'name':name,
    }
    return render(request, 'greeting.html', result)

def cube(request, num):
    result = {
        'num' : num,
        'cube' : num ** 3,
    }
    return render(request,'cube.html',result)

def posts(request):
    fake = Faker()

    fake_posts = []

    for i in range(100):
        fake_posts.append(fake.text())

    result = {
        'posts' : fake_posts,
    }
    return render(request, 'posts.html', result)