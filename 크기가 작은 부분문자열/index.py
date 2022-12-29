def solution(t,p):
    answer = 0
    for i in range(len(t)):
    # 입력받은 t문자열의 길이만큼 반복한다.
        if len(t[i:len(p)+i])==len(p) and t[i:len(p)+i]<=p:
        # t의 i 인덱스붙터 p문자열의 길이+i 인덱스까지의 길이가 p문자열의 길이와 같고,
        # t의 i 인덱스붙터 p문자열의 길이+i 인덱스까지의 길이의 값이 p 보다 같거나 작으면,
            answer += 1
            # answer에 1을 더해준다.
    print(answer)
    # answer값을 출력해보자.
    return answer


# README.md에 있는 예제들로 실험해 보자.

solution("3141592","271") # 2
solution("500220839878","7") # 8
solution("10203","15") # 3

# 셋다 모두 값이 출력된다.