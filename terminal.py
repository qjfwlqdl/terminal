import webbrowser as w
import time
import random

l = 0
lock = 0
print("터미널 by 벌집이 v0.03")

while True:
    on = 1
    a = input("원하시는 작업을 입력해주세요: ")
    if a == "네이버":
        if lock == 1:
            print("잠금이 되어있어 작업을 실행할수 없습니다.")
        else:
            w.open("https://www.naver.com")
    elif a == "다음":
        if lock == 1:
            print("잠금이 되어있어 작업을 실행할수 없습니다.")
        else:
            w.open("https://www.daum.net")
    elif a == "구글":
        if lock == 1:
            print("잠금이 되어있어 작업을 실행할수 없습니다.")
        else:
            w.open("https://www.google.com")
    elif a == "유튜브":
        if lock == 1:
            print("잠금이 되어있어 작업을 실행할수 없습니다.")
        else:
            w.open("https://www.youtube.com")
    elif a == "멜론차트":
        if lock == 1:
            print("잠금이 되어있어 작업을 실행할수 없습니다.")
        else:
            w.open("https://www.youtube.com/results?search_query=%EB%A9%9C%EB%A1%A0%EC%B0%A8%ED%8A%B8")    
    elif a == "무작위수":
        if lock == 1:
            print("잠금이 되어있어 작업을 실행할수 없습니다.")
        else:
            try:
                b, c = input("두개의 정수(시작,끝)를 공백을 포함해 입력해주세요:").split()
                print(random.randint(int(b),int(c)))
            except ValueError:
                print("오류가 발생했습니다.공백을 포함해 입력하거나 정수형으로 입력해야합니다.")    
    elif a == "메모":
        if lock == 1:
            print("잠금이 되어있어 작업을 실행할수 없습니다.")
        else:
            option = input("옵션을 선택해주세요: ")    
            if option == "초기화":
                f = open("memo.txt", "w")
                f.close()
                print("메모장이 성공적으로 초기화되었습니다.")
            elif option == "쓰기":
                while on:
                    memo = input("원하시는 메모 내용을 입력해주세요: ")
                    f = open("memo.txt", "a")
                    f.write(memo)
                    f.write('\n')
                    if not memo:
                        f.close()
                        on = 0
            elif option == "읽기":
                f = open("memo.txt")
                memo = f.read()
                if not memo:
                    print("-"*20)
                    print("읽을 내용이 없습니다.")
                    f.close()
                else:
                    print("-"*20)
                    print(memo)
                    f.close()
            else:
                print("옵션을 실행할수 없습니다.오타가 나진 않았는지 다시 확인해보세요.")
    elif a == "버전":
        if lock == 1:
            print("잠금이 되어있어 작업을 실행할수 없습니다.")
        else:
            print("v0.02(2023/06/14)")
            print("this program is made by 벌집이")
    elif a == "패치내역":
        if lock == 1:
            print("잠금이 되어있어 작업을 실행할수 없습니다.")
        else:
            print("""
                 작업 '잠금'실행시 비밀번호 유출 방지
              """)
    elif a == "작업목록":
        if lock == 1:
            print("잠금이 되어있어 작업을 실행할수 없습니다.")
        else:
            print("""
                  네이버
                  다음
                  구글
                  유튜브
                  멜론차트
                  무작위수
                  메모
                      초기화
                      쓰기
                      읽기
                  버전
                  패치내역
                  작업목록
                  잠금
                  잠금해제
                  종료
                  """)
    elif a == "잠금":
        if not l:
            try:
                l = int(input("비밀번호가 설정되지 않았습니다.비밀번호를 설정해주세요 : "))
                lock = 1
                print("------------------------\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n잠금되었습니다.")
            except ValueError:
                print("오류가 발생했습니다.공백이거나 문자열일수 없습니다.")
        else:
            lock = 1
            print("------------------------\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n잠금되었습니다.")
    elif a == "잠금해제":
        if lock:
            try:
                unlock = int(input("비밀번호를 입력해주세요 : "))
                if unlock == l:
                    lock = 0
                    print("잠금해제되었습니다.")
                else:
                    print("비밀번호가 일치하지 않습니다.")
            except ValueError:
                print("오류가 발생했습니다.공백이거나 문자열일수 없습니다.")
        else:
            print("이미 잠금해제되어있습니다.")
    elif a == "종료":
        if lock == 1:
            print("잠금이 되어있어 작업을 실행할수 없습니다.")
        else:
            print("프로그램을 종료합니다.")
            break
    else:
        if lock == 1:
            print("잠금이 되어있어 작업을 실행할수 없습니다.")
        else:
            print("작업을 실행할수 없습니다.오타가 나진 않았는지 다시 확인해보세요.")