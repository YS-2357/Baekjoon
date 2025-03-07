# 백준 10430번: 나머지
# 문제 설명:
# 세 개의 자연수 A, B, C가 주어졌을 때, 다음 연산의 결과를 출력하는 프로그램을 작성한다.
# 1. (A + B) % C
# 2. ((A % C) + (B % C)) % C
# 3. (A × B) % C
# 4. ((A % C) × (B % C)) % C
# 위 네 가지 연산의 결과를 순서대로 출력한다.

# 입력 형식:
# 첫 번째 줄에 A, B, C가 주어진다. (2 ≤ A, B, C ≤ 10000)

# 출력 형식:
# 문제에서 요구한 네 가지 연산의 결과를 한 줄에 하나씩 출력한다.

# 예제 입력 1:
# 5 8 4
# 예제 출력 1:
# 1
# 1
# 0
# 0

# ✅ 모범 답안: 정확한 연산 수행
# - 파이썬 내장 함수 사용: input(), print(), map()
# - 문제에서 요구한 네 가지 연산을 정확하게 계산
# - 시간 복잡도: O(1) (단순 연산)

# 입력 처리
a, b, c = map(int, input().split())  # 세 개의 정수 입력받기

# 나머지 연산 결과 출력
print((a + b) % c)          # (A + B) % C
print(((a % c) + (b % c)) % c)  # ((A % C) + (B % C)) % C
print((a * b) % c)          # (A × B) % C
print(((a % c) * (b % c)) % c)  # ((A % C) × (B % C)) % C
