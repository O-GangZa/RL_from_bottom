import gym
import torch
from torch.distributions import Categorical
from Policy import Policy

def main():
    env = gym.make('CartPole-v1') #카트폴 환경을 env로 설정
    pi = Policy()   # 정책 클래스를 호출해주면 __call__에 의해 forward가 자동 실행된다.
    score = 0.0     # 리턴이 곧 score
    print_interval = 20

    for n_epi in range(10000):
        s = env.reset()   # 초기 state로 리셋해주고 시작
        done = False

        while not done:
            print(torch.from_numpy(s).float())
            # prob = pi(torch.from_numpy(s).float())
            # # 아마도 확률을 관측값에 따라 변동시켜주는 것, 다시말해 정책 π_θ에 해당하는 것 같다.
            # m = Categorical(prob) # 행동의 경우의 수가 적은경우 categorical을 쓴다고함
            # # 샘플이 쌓일때마다 확률이 높은 액션은 자주, 낮은 액션은 덜 뽑히게 됨,
            # a = m.sample()
            # s_prime, r, done, info = env.step(a.item())
            # pi.put_data((r, prob[a]))
            # s = s_prime
            # score += r

        pi.train_net()

        if n_epi%print_interval==0 and n_epi!=0: #인터벌로 나눴을 때 0이고, 첫 에피소드가 아니면
            print("# of epidode :{}, avg score : {}".format(n_epi, score/print_interval))
            score = 0.0
    env.close()

if __name__ == "__main__":
    main()
