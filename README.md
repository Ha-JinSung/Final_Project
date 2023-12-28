# 목표 

Django 프레임워크를 사용하여 CRUD 블로그를 CBV 모놀리식 구현

---
# 기술스택

- Django
- Python


- Bootstrap
- Javascript
- Html5


- Visual Studio Code

---

# 프로젝트 구조
```sh
my_blog
│
│  db.sqlite3
│  manage.py
│  requirements.txt
│  
├─accounts
│    admin.py
│    apps.py
│    models.py
│    tests.py
│    urls.py
│    views.py
│          
├─blog
│    admin.py
│    apps.py
│    forms.py
│    models.py
│    tests.py
│    urls.py
│    views.py
│          
├─blogbase
│    asgi.py
│    settings.py
│    urls.py
│    wsgi.py
│          
├─locale
│  ├─en
│  │          
│  └─ko
│              
├─logs         
│   bloglog
│      
├─main
│    admin.py
│    apps.py
│    models.py
│    tests.py
│    urls.py
│    views.py
│          
├─media
│  └─blog
│      ├─files               
│      └─images
│                          
├─static
│  ├─assets
│  │      error.jpg
│  │      favicon.ico
│  │      home-bg.jpg
│  │      
│  ├─css
│  │      styles.css
│  │      
│  └─js
│         scripts.js
│          
└─templates
    │  400.html
    │  403.html
    │  404.html
    │  500.html
    │  base.html
    │  
    ├─accounts
    │      change_password.html
    │      form.html
    │      profile.html
    │      user_delete.html
    │      
    ├─blog
    │      form.html
    │      post_confirm_delete.html
    │      post_detail.html
    │      post_list.html
    │      
    └─main
           index.html
```

# ERD 구조
![281118895-b1d723e8-b82c-4b19-a69a-f018a44b24ee](https://github.com/Ha-JinSung/Final_Project/assets/142278871/b52c4fe2-774d-4191-b4d0-0c0e4cfbb9e1)


---

# Url 구조

|app: main |views 함수 이름|html 파일이름|
|:--------|:------------|:---------|
|''       |index         |index.html |

|app: accounts |views 함수 이름|html 파일이름   |
|:------------|:------------|:------------|
|'signup/'     |signup        |form.html|
|'login/'      |login         |form.html|
|'logout/'     |logout        |
|'profile/'    |profile       |profile.html  |
|'change_password/'|change_password|change_password.html|
|'delete/'|user_delete|user_delete.html|

|app: blog  |views 함수 이름  |html 파일이름   |
|:-------------|:--------------|:------------|
|''|post_list|post_list.html|
|'new/'|post_new|form.html|
|'<int: pk>/'|post_detail|post_detail.html|
|'<int: pk>/edit/'|postedit|form.html|
|'<int: pk>/delete/'|post_delete|post_confirm_delete.html|
|'<int: pk>/comment/new/'|comment_new|form.html|
|'<int: post_pk>/comment/<int: comment_pk>/edit/'|comment_edit|form.html|
|'<int: post_pk>/comment/<int: comment_pk>/delete/'|comment_delete|post_confirm_delete.html|
|'<int: post_pk>/comment/<int: comment_pk>/reply/'|comment_reply|form.html|
|'<int: post_pk>/comment/<int: comment_pk>/reply/<int: reply_pk>/edit/'|reply_edit|form.html|
|'<int: post_pk>/comment/<int: comment_pk>/reply/<int: reply_pk>/delete/'|reply_delete|post_confirm_delete.html|

---

# 요구 기능 구현

## 블로그
![블로그](https://github.com/Ha-JinSung/Final_Project/assets/142278871/5990888e-0887-4fe2-8e7b-c6d0ea951be9)


---

## 검색 (태그, 제목)
![검색 (태그, 제목)](https://github.com/Ha-JinSung/Final_Project/assets/142278871/3ee75c2e-83ee-46b3-8f4b-44de02d4e545)


---

## 영한 변환 (I18N)
![영한 변환 (I18N)](https://github.com/Ha-JinSung/Final_Project/assets/142278871/3675e20d-2188-4bc4-bc0b-1a719ffc5418)


setting.py
```
LANGUAGE_CODE = 'ko-kr'

# 번역할 언어 추가
LANGUAGES = [
    ('en', 'English'),
    ('ko', 'Korean'),
]

USE_I18N = True # <-  True 인지 확인


# 번역될 .po 파일 저장소
LOCALE_PATHS = [
    BASE_DIR / 'locale',
]

# 추가
'django.middleware.locale.LocaleMiddleware',

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware', # <--- 이곳에 추가함 (꼭 이곳에 추가)
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
```

MY_BLOG 폴더 안에서 locale 폴더 생성
```
mkdir locale
```


터미널에서
```
django-admin makemessages -l en
django-admin makemessages -l ko
```

입력하여 django.po 파일생성 후 

변역될 부분 
예시로 
```
#: .\templates\base.html:21 .\templates\base.html:39
msgid "블로그"
msgstr "블로그" <- 이곳에 번역 될 언어로 작성
```
입력 후 터미널에서
```
django-admin compilemessages
```
입력하여 django.mo파일이 생성되면 완료

---

## 비밀번호 수정 및 회원탈퇴
![비밀번호 수정 및 회원탈퇴](https://github.com/Ha-JinSung/Final_Project/assets/142278871/4114846c-cd60-4a16-9ed4-a6cbb2e0b281)


---

## 댓글과 대댓글 (생성, 수정, 삭제)
![댓글과 대댓글 (생성, 수정, 삭제)](https://github.com/Ha-JinSung/Final_Project/assets/142278871/2a4e3641-708a-472c-abcf-77ebb0f536b1)


---

## 게시물 수정 삭제
![게시물 수정 삭제](https://github.com/Ha-JinSung/Final_Project/assets/142278871/07b4a446-77c5-4049-94f0-d79b1b49f4cd)


---

## 삭제된 페이지 오류 페이지 
![삭제된 페이지 오류 페이지](https://github.com/Ha-JinSung/Final_Project/assets/142278871/fa7a63fb-179f-4d6c-a483-a37a36fc8fed)


---
# 로그 코드

```
# log 기록 남기는 코드 
DEBUG = True  # <- True와 False일때 밑의 LOGGING 코드에서 'filters': ['require_debug_true'],에서 True를 Fales 로 수정 해줘야 한다. (수정될 부분은 * 로 표기)

ALLOWED_HOSTS = ['*']

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'formatters': {
        'django.server': {
            '()': 'django.utils.log.ServerFormatter',
            'format': '[{server_time}] {message}',
            'style': '{',
        },
        'standard': {
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'filters': ['require_debug_false'], # *
            'class': 'logging.StreamHandler',
        },
        'django.server': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'django.server',
        },
        'mail_admins': {
            'level': 'INFO',
            'filters': ['require_debug_false'], # *
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'file': {
            'level': 'INFO',
            'encoding': 'utf-8',
            'filters': ['require_debug_false'], # *
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': BASE_DIR / 'logs/bloglog', # log파일 경로와 저장될 파일명
            'maxBytes': 1024*1024*1,  # 용량 1 MB
            'backupCount': 25, # 파일갯수 (25개 넘어가면 기존파일이 지워지고 새로 생성)
            'formatter': 'standard',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'mail_admins', 'file'],
            'level': 'INFO',
        },
        'django.server': {
            'handlers': ['django.server'],
            'level': 'INFO',
            'propagate': False,
        },
        'my': {
            'handlers': ['console', 'file'],
            'level': 'INFO',
        },
    }
}

# 'level' 은 DEBUG < INFO < WARNING < ERROR < CRITICAL 순 입니다.
```

MY_BLOG 폴더 
```
mkdir logs 
```
폴더 생성 하면 완료

---


# 개발 중 장애물 & 극복 방법


- fields.E304 에러 
migrate실행 시 fields.E304가 발생하였으며, 해결법으론 settings.py 에서 AUTH_USER_MODEL : ‘앱이름.클래스이름’ 을 넣으면 된다고 하여 시도를 했으나, 이것도 실패를 하였으며 나중에서 처음 앱생성 하고서 migrate을 하고서 models.py를 모델링을 해야 AUTH_USER_MODEL : ‘앱이름.클래스이름’ 이 가능 했었습니다.

- django.core.exceptions.ImproperlyConfigured 에러
'''
class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True, null=True, blank=True)
'''
Tag 모델 중에 null=True 와 데이터 입력을 안해서 (대개 NULL 값 입력 때문에 발생) 생기거나, Django 모델에서 필드를 수정한 후 migrate 안하면 나오는 오류 (migrate 안한다고 해서 꼭 에러가 나오는게 아니여서 원인 찾는데 시간이 걸렸습니다.) 
Tag 모델에 null=True를 넣은 후에 python manage.py migrate를 하여 해결 하였습니다.

---


# 프로젝트 소감

- DRF로 개발 실패
블로그 만들기를 DRF를 사용하여 만들려고 하였으나, 권한부여 및 Serialize, view, router와 Html의 API연결 등등의 기술적인 이해가 부족하여 이후에서 Serialize의 구성을 잡아야 할 갈피를 못잡고 개발에 난항을 겪어서 CBV 모놀리식으로 구현하는 방향으로 바꾸었습니다.

-느낀 점
처음으로 배운 Python과 Django를 사용하여 블로그를 만들면서 점점 구현되어 가는 모습에 좋기도 하였지만, 아직 이해도 제대로 안된 기술을 무리하게 적용 해보고 싶은 욕심에 너무 한가지에 붙잡혀 기획이 점점 틀어져 버려서 빠르게 구현이 가능한 방법으로 전환하여 개발하게 된 점이 아쉽게 느껴집니다.



