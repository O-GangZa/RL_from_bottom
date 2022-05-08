class GridWorld():  # 그리드월드 클래스 생성
    def __init__(self):  # 초기 변수 x, y (그리드 월드 시작 state)
        self.x = 0
        self.y = 0

    def step(self, a):
        # 0번 액션: 왼쪽, 1번 액션: 위, 2번 액션: 오른쪽, 3번 액션 : 아래쪽
        if a == 0:
            self.move_left()  # 각 이동함수를 통해서 현재 state의 좌표를 변환한다.
        elif a == 1:
            self.move_up()
        elif a == 2:
            self.move_right()
        elif a == 3:
            self.move_down()

        reward = -1  # 보상은 1로 고정 (MDP를 모르므로 실제 관측하기 전까지는 모른다고 가정)
        done = self.is_done()  # done을 불리언으로 판정 terminal state 판단을 위해
        return (self.x, self.y), reward, done

    def move_left(self):
        if self.y == 0:  # 벽(테두리)지정
            pass
        elif self.y == 3 and self.x in [0, 1, 2]:  # 장애물도 마찬가지로 지정해준다.
            pass
        elif self.y == 5 and self.x in [2, 3, 4]:
            pass
        else:
            self.y -= 1

    def move_right(self):
        if self.y == 1 and self.x in [0, 1, 2]:
            pass
        elif self.y == 3 and self.x in [2, 3, 4]:
            pass
        elif self.y == 6:
            pass
        else:
            self.y += 1

    def move_up(self):
        if self.x == 0:
            pass
        elif self.x == 3 and self.y == 2:
            pass
        else:
            self.x -= 1

    def move_down(self):
        if self.x == 4:
            pass
        elif self.x == 1 and self.y == 4:
            pass
        else:
            self.x += 1

    def is_done(self):
        if self.x == 4 and self.y == 6:  # 목표 state인 (4, 6)에 도달하면 끝난다.
            return True
        else:
            return False

    def reset(self):  # 시작 state로 돌아가는 함수
        self.x = 0
        self.y = 0
        return (self.x, self.y)
