from functools import wraps
import time

def robust(f):
    '''
    에러 없이 통과할 때 까지 함수를 반복 호출 하는 데코레이터
    함수에게 불굴의 의지를 부여합니다.
    아무 함수에게나 쓰지 마세요. 시간이 지나면 꼭 성공하리라 보장 된 함수에만 사용해야 합니다.
    '''
    @wraps(f)
    def robust_func(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except Exception as e:
            print(e)
            time.sleep(1)
            robust_func(*args, **kwargs)

    return robust_func


