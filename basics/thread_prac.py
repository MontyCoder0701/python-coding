import threading
import time

# def work():
#     print("[sub] start")
#     keyword = input("[sub] 검색어를 입력하세요 >>> ")
#     print(f"[sub] {keyword}로 검색을 시작합니다 ... ")
#     print("[sub] end")


# print("[main]")

# worker = threading.Thread(target=work)
# worker.daemon = True
# worker.start()

# print("[main] 메인 스레드는 자기 할일을 합니다")
# print("[main] end")

def buyer():
    for i in range(5):
        print("[매수] 데이터 요청 중 ...")
        time.sleep(1)
        print("[매수] 데이터 분석 중 ...")
        time.sleep(1)
        print("[매수] 데이터 요청 중 ...")
        time.sleep(1)
        print("[매수] 지금이 매수 타이밍 ...")
        time.sleep(1)
        print("[매수] 매수합니다 ...")
        time.sleep(1)


def seller():
    for i in range(5):
        print("[매도] 데이터 요청 중 ...")
        time.sleep(1)
        print("[매도] 데이터 분석 중 ...")
        time.sleep(1)
        print("[매도] 데이터 요청 중 ...")
        time.sleep(1)
        print("[매도] 지금이 매도 타이밍 ...")
        time.sleep(1)
        print("[매도] 매도합니다 ...")
        time.sleep(1)


print("[메인] start")
buyer = threading.Thread(target=buyer)
seller = threading.Thread(target=seller)
buyer.start()
seller.start()

buyer.join()
seller.join()
print("[메인] 장이 종료되었습니다.")
