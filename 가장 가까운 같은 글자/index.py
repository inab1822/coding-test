def solution(s):
    answer = [-1]
    # s의 맨처음은 항상 처음 나오는 문자이기 때문에 answer의 첫 부분은 항상
    # -1일 것이다.
    for i in range(1,len(s)):
    # s의 맨 앞부분은 제외해야 하므로, 1 부터 s의 길이까지 반복문을 돌린다.
        a = True
        # a = True 라는 변수를 하나 만들어 준다.
        for j in range(i-1,-1,-1):
        # s의 인덱스 위치중 해당 인덱스의 전 부분부터 맨 앞까지 거꾸로 돌리기위해
        # range(i-1,-1,-1)로 범위를 정해 반복문을 돌린다.
            if s[i]==s[j]:
            # s의 i 부분과 i부분의 앞의 모든 부분을 비교하여 같으면
                answer.append(i-j)
                # answer에 마지막에 i-j값을 넣어준다.
                a = False
                # 그리고 a에 Fasle값을 넣어준다.
                break;
        if a == True:
        # 만약 if문에 걸리지않아 a가 True가 됬다면
        # 그뜻은 s의 i 인덱스와 같은 글자가 i 인덱스 앞에 하나도 없음을 의미
            answer.append(-1)
            # answer에 -1을 append 해준다. 
    print(answer)
    # answer을 출력하자.       
    return answer

# README.md에 있는 예제들로 실험해 보자.

solution("banana") # [-1,-1,-1,2,2,2]
solution("foobar") # [-1,-1,1,-1,-1,-1]

# 둘다 모두 제대로 출력된다.