import sys

# ✅ 입력 처리 (빠른 입력을 위해 sys.stdin.readline 사용)
N, M, R = map(int, sys.stdin.readline().split())  # 행(N), 열(M), 회전 횟수(R)
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]  # 2차원 배열 입력

# ✅ 배열을 레이어(껍질) 단위로 회전하는 함수
def rotate_layers(board, N, M, R):
    num_layers = min(N, M) // 2  # 총 레이어 개수 (가장 바깥쪽부터 안쪽으로)

    for layer in range(num_layers):
        # ✅ 현재 레이어의 경계 좌표 설정
        sx, sy = layer, layer  # 좌상단 좌표
        ex, ey = N - layer - 1, M - layer - 1  # 우하단 좌표

        # ✅ 현재 레이어의 주기 계산 (한 바퀴 도는 길이)
        cycle_length = 2 * ((ex - sx + 1) + (ey - sy + 1) - 2)

        # ✅ 불필요한 회전을 줄이기 위해 R을 주기로 나눔
        rotate_count = R % cycle_length  

        # ✅ 회전할 필요가 없으면 스킵
        if rotate_count == 0:
            continue

        # ✅ 1. 레이어를 리스트로 변환
        elements = []
        
        # 🔹 → (왼쪽 → 오른쪽) (맨 윗줄)
        for j in range(sy, ey + 1):
            elements.append(board[sx][j])  # (sx, j)

        # 🔹 ↓ (위쪽 → 아래쪽) (맨 오른쪽 줄)
        for i in range(sx + 1, ex + 1):
            elements.append(board[i][ey])  # (i, ey)

        # 🔹 ← (오른쪽 → 왼쪽) (맨 아래줄)
        if sx != ex:  
            for j in range(ey - 1, sy - 1, -1):
                elements.append(board[ex][j])  # (ex, j)

        # 🔹 ↑ (아래쪽 → 위쪽) (맨 왼쪽 줄)
        if sy != ey:
            for i in range(ex - 1, sx, -1):
                elements.append(board[i][sy])  # (i, sy)

        # ✅ 2. 리스트를 R % 주기 칸 회전
        rotated = elements[rotate_count:] + elements[:rotate_count]

        # ✅ 3. 회전된 리스트를 다시 원래 배열에 채워넣기
        idx = 0  # rotated 리스트의 인덱스
        
        # 🔹 → (왼쪽 → 오른쪽) (맨 윗줄)
        for j in range(sy, ey + 1):
            board[sx][j] = rotated[idx]  # (sx, j)
            idx += 1

        # 🔹 ↓ (위쪽 → 아래쪽) (맨 오른쪽 줄)
        for i in range(sx + 1, ex + 1):
            board[i][ey] = rotated[idx]  # (i, ey)
            idx += 1

        # 🔹 ← (오른쪽 → 왼쪽) (맨 아래줄)
        if sx != ex:  
            for j in range(ey - 1, sy - 1, -1):
                board[ex][j] = rotated[idx]  # (ex, j)
                idx += 1

        # 🔹 ↑ (아래쪽 → 위쪽) (맨 왼쪽 줄)
        if sy != ey:
            for i in range(ex - 1, sx, -1):
                board[i][sy] = rotated[idx]  # (i, sy)
                idx += 1

# ✅ 배열 회전 수행
rotate_layers(board, N, M, R)

# ✅ 최종 결과 출력
for row in board:
    print(*row)
