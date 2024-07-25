#번호  = 전체 건수 - 시작인덱스 - 현재인덱스 + 1
#빼기 기능을 위한 필터 작성
from django import template
register = template.Library()

@register.filter
def sub(value, arg):
    return value - arg
