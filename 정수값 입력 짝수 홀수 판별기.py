print('정수 값을 입력하시오.')
a=int(input())
if a%2==0 :
    print('입력한 값 {}은 짝수 입니다.'.format(a))
else :
    print('입력한 값 {}은 홀수 입니다.'.format(a))

print('{:->70}'.format('-'))
print('종료하시려면 엔터키를  눌러주세요')
input()
