# 백준 10844번: 쉬운 계단 수 (다이나믹 프로그래밍 - DP)
# 문제 설명:
# - 계단 수란 인접한 자리의 숫자가 1 차이 나는 숫자를 의미함
# - 길이가 N인 계단 수의 개수를 구해야 함
# - 0으로 시작하는 수는 계단 수가 아님
# - 결과를 1,000,000,000으로 나눈 나머지를 출력해야 함

import sys

# ✅ 상수 설정: 모듈러 연산을 위한 상수
MOD = 1000000000

# ✅ 입력 처리
N = int(sys.stdin.readline())  # 계단 수의 길이 입력

# ✅ DP 테이블 초기화 (dp[i][j]: 길이가 i이고 마지막 숫자가 j인 계단 수의 개수)
dp = [[0] * 10 for _ in range(N + 1)]

# ✅ 기본값 설정 (1자리 계단 수는 1~9까지 각각 1개씩 존재)
for i in range(1, 10):
    dp[1][i] = 1  # 길이가 1인 경우: 1~9는 가능하지만 0은 불가능

# ✅ DP 테이블 채우기 (Bottom-Up 방식)
for i in range(2, N + 1):
    dp[i][0] = dp[i - 1][1]  # 0으로 끝나는 경우는 이전 숫자가 1인 경우만 가능
    dp[i][9] = dp[i - 1][8]  # 9로 끝나는 경우는 이전 숫자가 8인 경우만 가능
    for j in range(1, 9):  # 1~8 사이 숫자는 j-1과 j+1에서 오는 경우의 합
        dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j + 1]) % MOD

# ✅ 결과 출력 (길이가 N인 계단 수의 총 개수)
print(sum(dp[N]) % MOD)

# -----------------------------------------------------
# ✅ 2단계에서 발생했던 오류 정리 및 수정:
# 1. ✅ `total` 계산 시 `MOD` 적용 문제 해결:
#    - 기존 코드에서는 `total += dp[N][j]`에서 MOD 연산이 없었음
#    - 해결: `sum(dp[N]) % MOD`로 변경하여 모듈러 연산을 적용
#
# 2. ✅ `sum()`을 사용하여 코드 간결화:
#    - 기존: `for j in range(10): total += dp[N][j]`
#    - 개선: `sum(dp[N]) % MOD` 사용하여 불필요한 반복문 제거
#
# ✅ 3단계 최종 정답 코드 제공 완료 🚀
