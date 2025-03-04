# -----------------------------------------------------
# ✅ 문제 설명:
# - N×M 크기의 배열이 주어지고, 특정 연산을 수행해야 한다.
# - 6개의 연산 (상하반전, 좌우반전, 시계90도 회전, 반시계90도 회전, 
#   4분면 시계방향 이동, 4분면 반시계방향 이동)을 구현해야 한다.
# - R개의 연산이 주어졌을 때, 최종 배열 상태를 출력해야 한다.
#
# ✅ 입력 형식:
# - 첫 번째 줄: `N M R` (2 ≤ N, M ≤ 100, 1 ≤ R ≤ 1000)
# - 이후 N개의 줄: 배열 원소 (0 ≤ 원소 ≤ 100)
# - 마지막 줄: `R`개의 연산 (1 ≤ 연산 ≤ 6)
#
# ✅ 출력 형식:
# - 연산을 수행한 후 최종 배열을 출력
#
# ✅ 입출력 예제:
# 🔹 예제 입력 1:
#   3 3 1
#   1 2 3
#   4 5 6
#   7 8 9
#   3
# 🔹 예제 출력 1:
#   7 4 1
#   8 5 2
#   9 6 3
# -----------------------------------------------------

import sys

# ✅ 90도 회전 (시계 방향)
# - 기존 행렬을 시계 방향으로 회전시키는 함수
# - 새로운 행렬을 만들어 (j, i) 위치로 값을 이동
# - N과 M의 크기가 서로 바뀌므로, 회전 후 크기를 함께 반환
def rotate_right(matrix, n, m):
    temp = [[0] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            temp[i][j] = matrix[n - 1 - j][i]  # 반시계 방향으로 90도 회전
    return temp, m, n  # 회전 후 크기 변경

# ✅ 90도 회전 (반시계 방향)
# - 기존 행렬을 반시계 방향으로 회전
# - (j, i) 위치로 값을 이동
# - 마찬가지로 N과 M 크기가 변경됨
def rotate_left(matrix, n, m):
    temp = [[0] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            temp[i][j] = matrix[j][m - 1 - i]  # 반시계 방향 90도 회전
    return temp, m, n  # 회전 후 크기 변경

# ✅ 4분면 시계 방향 이동
# - 1번 -> 2번, 2번 -> 3번, 3번 -> 4번, 4번 -> 1번 이동
# - 새로운 행렬을 만들어 기존 값을 이동시킴
def move_clockwise(matrix, n, m):
    temp = [[0] * m for _ in range(n)]
    for i in range(n // 2):
        for j in range(m // 2):
            temp[i][j + m // 2] = matrix[i][j]  # 1 -> 2
    for i in range(n // 2):
        for j in range(m // 2, m):
            temp[i + n // 2][j] = matrix[i][j]  # 2 -> 3
    for i in range(n // 2, n):
        for j in range(m // 2, m):
            temp[i][j - m // 2] = matrix[i][j]  # 3 -> 4
    for i in range(n // 2, n):
        for j in range(m // 2):
            temp[i - n // 2][j] = matrix[i][j]  # 4 -> 1
    return temp

# ✅ 4분면 반시계 방향 이동
# - 1번 -> 4번, 4번 -> 3번, 3번 -> 2번, 2번 -> 1번 이동
# - 새로운 행렬을 만들어 기존 값을 이동시킴
def move_counter_clockwise(matrix, n, m):
    temp = [[0] * m for _ in range(n)]
    for i in range(n // 2):
        for j in range(m // 2):
            temp[i + n // 2][j] = matrix[i][j]  # 1 -> 4
    for i in range(n // 2, n):
        for j in range(m // 2):
            temp[i][j + m // 2] = matrix[i][j]  # 4 -> 3
    for i in range(n // 2, n):
        for j in range(m // 2, m):
            temp[i - n // 2][j] = matrix[i][j]  # 3 -> 2
    for i in range(n // 2):
        for j in range(m // 2, m):
            temp[i][j - m // 2] = matrix[i][j]  # 2 -> 1
    return temp

# ✅ 입력 처리
n, m, r = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
operations = list(map(int, sys.stdin.readline().split()))

# ✅ 연산 수행
for op in operations:
    if op == 1:
        board.reverse()  # 상하반전
    elif op == 2:
        board = [row[::-1] for row in board]  # 좌우반전
    elif op == 3:
        board, n, m = rotate_right(board, n, m)  # 시계방향 회전
    elif op == 4:
        board, n, m = rotate_left(board, n, m)  # 반시계방향 회전
    elif op == 5:
        board = move_clockwise(board, n, m)  # 4분면 시계방향 이동
    elif op == 6:
        board = move_counter_clockwise(board, n, m)  # 4분면 반시계방향 이동

# ✅ 최종 결과 출력
for row in board:
    print(*row)

# ----------------------------------------------------------
# ✅ 2단계에서 발생한 오류 정리 및 수정:
# 1️⃣ **배열 반전 시 인덱스 오류**
# 기존 코드: `matrix.reverse()`가 상하반전만 수행하고 좌우반전은 따로 처리하지 않음.
# ✅ 해결: `board.reverse()`와 `board = [row[::-1] for row in board]`을 분리하여 구현.

# 2️⃣ **시계 및 반시계 회전 시 N, M 값 유지 오류**
# 기존 코드: `rotate_right()`와 `rotate_left()`에서 N, M 값이 변경되지 않음.
# ✅ 해결: `return temp, m, n`을 추가하여 회전 후 크기 변경.

# 3️⃣ **4분면 이동 연산에서 잘못된 위치 지정**
# 기존 코드에서 4분면 이동이 잘못 설정됨.
# ✅ 해결: `move_clockwise()`와 `move_counter_clockwise()`를 수정하여 올바른 방향 이동.

# ✅ 최종 정리:
# - `sys.stdin.readline()`을 사용하여 빠른 입력 처리.
# - 6가지 연산을 개별 함수로 정의하여 코드 모듈화.
# - N, M이 변경되는 회전 연산을 처리한 후 크기 조정.
# ----------------------------------------------------------
