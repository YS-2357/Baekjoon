# 백준 6064번: 카잉 달력
# 문제 설명:
# 카잉 달력은 M년과 N년을 주기로 반복되며, 특정 해(year)에서 (x, y) 좌표가 등장하는 시점을 찾는 문제.
# - (M, N)은 주어진 범위 내에서 반복되며, (x, y)가 몇 번째 해(year)인지 계산해야 한다.
# - 해(year)가 없으면 -1을 출력한다.

# 입력 형식:
# 첫째 줄에 테스트 케이스 개수 T가 주어진다. (1 ≤ T ≤ 10^5)
# 이후 T개의 줄에 정수 M, N, x, y가 주어진다. (1 ≤ M, N ≤ 40,000, 1 ≤ x ≤ M, 1 ≤ y ≤ N)

# 출력 형식:
# 각 테스트 케이스마다 (x, y)가 몇 번째 해인지 출력한다.
# 만약 찾을 수 없다면 -1을 출력한다.

# 예제 입력 1:
# 3
# 10 12 3 9
# 10 12 7 2
# 13 11 5 6

# 예제 출력 1:
# 33
# -1
# 83

import sys
import math

# ✅ 입력 처리
N = int(input())
array = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# ✅ 테스트 케이스 실행
for i in range(N):
    m, n, x, y = array[i]
    lcm = (m * n) // math.gcd(m, n)  # 최소공배수(LCM) 계산
    j = x  # x부터 시작하여 증가

    while j <= lcm:
        if (j - 1) % n + 1 == y:  # ✅ (j - 1) % n + 1 을 통해 y 검증
            print(j)
            break
        j += m  # m씩 증가하며 탐색
    else:
        print(-1)  # 해(year)를 찾을 수 없는 경우 -1 출력


# -----------------------------------------------------
# ❌ 내가 쓴 코드와 틀린 점
# 1. 범위를 잘못 설정하여 불필요한 연산이 발생함
#    - 기존: `for j in range(min(x, y), m * n // gcd(m, n) + 1):`
#    - ✅ 수정: `j = x`부터 시작해 `j += m`씩 증가하며 `LCM(M, N)`까지만 탐색

# 2. `gcd()` 함수 호출 오류 (`gcd()` 정의되지 않음)
#    - 기존: `gcd(m, n)`
#    - ✅ 수정: `math.gcd(m, n)`

# 3. `j % m == x and j % n == y` 로직 오류
#    - (x, y)는 `(1,1)`부터 시작하므로 `(j - 1) % n + 1 == y`로 변환 필요

# 4. 불필요한 `함수` 제거 후 간결화
#    - 기존 코드에서 `find_year()` 함수를 제거하고, 바로 `for` 루프에서 계산

# ✅ 위 수정 후 실행하면 백준에서 정답 판정!
