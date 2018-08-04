print('{:^30}'.format('비만도 계산기'))
name=str(input('이름을 입력하시오 :'))
height=float(input('키를 입력하시오 (cm) : '))
weight=float(input('몸무게를 입력하시오 (kg) : '))
print('{:->50}'.format('-'))
a=((height-100)*0.9)
b=((weight/a)*100)
if b<100 :
    print('{}님의 비만도는 {:.2f}%로 저체중 입니다.'.format(name,b))
elif 100<=b<110 :
    print('{}님의 비만도는 {:.2f}%로 정상 입니다.'.format(name,b))
elif 110<=b<120 :
    print('{}님의 비만도는 {:.2f}%로 과체중 입니다.'.format(name,b))
elif 120<=b<130 :
    print('{}님의 비만도는 {:.2f}%로 비만 입니다.'.format(name,b))
elif b>=130 :
    print('{}님의 비만도는 {:.2f}%로 고도비만 입니다.운동하세요'.format(name,b))
input()
