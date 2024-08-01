## Django Study during 🌷🏖️

여름 방학동안 진행한 , Django 스터디

###  file structure
```tsx
mysite //Repository_Root
├── common 
│   ├── migrations //DataBase Migration
│   ├── admin.py // Django Admin 
│   ├── apps.py //Django App Setting
│   ├── forms.py //Define of Django form 
│   ├── modles.py //DataBase Model
│   ├── tests.py //Application Test
│   ├── urls.py //URL Routing
│   ├── views.py //View
├── config //Setting
│   ├── settings 
│   │   ├── base.py //기본설정
│   │   ├── local.py //로컬개발환경을 위한 설정
│   │   ├── prod.py//프로덕션 환경
│   ├── asgi.py //ASGI 설정파일
│   ├── urls.py //프로젝트 전역의 URL 라우팅 정의
│   ├── wsgi.py //웹 서버와의 인터페이스 정의
├── pybo
│   ├── migrations //Pybo DataBase Migration
│   ├── templatetags //Pybo Templates
│   │   ├── pybo_filter.py
│   ├── views
├── static
├── templates 
├── manage.py 
└── db.sqlite3

```