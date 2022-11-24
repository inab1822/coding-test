# 반환될 동전의 타입이다.

coin_type = [500, 100, 50, 10]



def change(N):
  count = 0
# coin_type안에있는 각 coin 들을 하나하나 대입한다.
  for coin in coin_type:
# N 값을 coin 으로 나눈 몫을 count에 더하여 저장.    
    count += N // coin 
# 처음 입력된 N에 N을 coin으로 나눈 몫에 해당 coin을 곱하여 빼준다. N %= coin
    N = N - (N // coin)*coin 
# coin_type에 있는 각 coin들을 모두 대입해서 count를 올리고 마지막으로 count를 출력한다.
  return print(count)

change(1560)