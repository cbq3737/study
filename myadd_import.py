# import mymod #이렇게 서로쌍을 이룬다.
# print(mymod.myadd(2,3))

# import mymod as mm
# print(mm.myadd(2,3))
#
# from mymod import myadd
# print(myadd(2,3))

# from mymod import myadd as mm #이렇게 4가지 방법이있다.
# print(mm(2,3))

#만일 mymod이라는 파일이 work디렉토리 밑에있다면 여기서 사용해주고 싶다면?
from Work.B import Addb
print(Addb(2,3))
