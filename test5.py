######중요####
import sys
print("%s" % sys)  #터미널에서 인자수에 맞게 적여줘야 한다.
#
print("**********")

print("0번째 %s" % sys.argv[0])
print("1번째 %s" % sys.argv[1])
print("2번째 %s" % sys.argv[2])

print("3번째 %s" % sys.argv[3])

# 터미널에서 python tes5.py x x x로 인수넘겨주면 리스트형태로 각각 인덱스를 확인할 수 잇음,
#           파이썬 현재 위치 인자


