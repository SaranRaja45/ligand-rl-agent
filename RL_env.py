import random

# ENVIRONMENT
class HMDockEnv:
    def __init__(self):
        self.ligands = {
            "L1": -3.2, "L2": -10.12, "L3": -11.3, "L4": -15.2,
            "L5": -12.9, "L6": -9.4, "L7": -9.8, "L8": -9.45,
            "L9": -7.6, "L10": -10.7
        }
        self.ligand_list = list(self.ligands.keys())
        self.n_actions = len(self.ligand_list)
        self.step_count = 0
        self.best_score = float('inf')

    def reset(self):
        self.step_count = 0
        self.best_score = float('inf')
        return self.state()

    def step(self, action):
        self.step_count += 1

        ligand = self.ligand_list[action]
        score = self.ligands[ligand]

        # Reward Logic
        reward = -score

        # penalty for weak ligand
        if score > -6:
            reward -= 2

        # bonus for global best ligand
        if score == min(self.ligands.values()):
            reward += 5

        # track best seen
        if score < self.best_score:
            self.best_score = score

        observation = {
            "ligand": ligand,
            "score": score,
            "step": self.step_count
        }

        done = self.step_count >= 5

        return{
            "observation": observation, "reward": reward, "done": done, "info": {}
        }
    
    def state(self):
        return{
            "step": self.step_count,
            "ligands_available": self.ligand_list
        }

# AGENT (epsilon-greedy bandit)
class LigandAgent:
    def __init__(self, n_actions):
        self.n_actions = n_actions
        self.memory = [0.0] * n_actions
        self.counts = [1] * n_actions

    def choose_action(self, epsilon=0.2):
        if random.random() < epsilon:
            return random.randint(0, self.n_actions - 1)
        avg_rewards = [self.memory[i] / self.counts[i] for i in range(self.n_actions)]
        return avg_rewards.index(max(avg_rewards))

    def update(self, action, reward):
        self.memory[action] += reward
        self.counts[action] += 1

# TASK 1: Pick BEST ligand
def grade_task1(selected_ligand, ligands):
    sorted_ligands = sorted(ligands, key=ligands.get)
    rank = sorted_ligands.index(selected_ligand)
    return 1 - (rank / (len(ligands) - 1))

# TASK 2: Pick 2 strong ligands
def grade_task2(selected_ligands, ligands):
    sorted_ligands = sorted(ligands, key=ligands.get)
    strong2 = set(sorted_ligands[:2])
    correct = len(set(selected_ligands) & strong2)
    return correct / 2

# TASK 3: Rank TOP-3 ligands in correct order
def grade_task3(ranked_ligands, ligands):
    sorted_ligands = sorted(ligands, key=ligands.get)
    top3 = sorted_ligands[:3]

    score = 0
    for i, ligand in enumerate(ranked_ligands[:3]):
        if ligand == top3[i]:
            score += 1
    return score / 3

# # RUN EPISODE
# def run_episode(env, agent):
#     obs = env.reset()
#     done = False
#     selected = []

#     while not done:
#         action = agent.choose_action()
#         result = env.step(action)

#         obs = result["observation"]
#         reward = result["reward"]
#         done = result["done"]

#         agent.update(action, reward)
#         selected.append(obs["ligand"])

#     return selected

# # BASELINE RUN
# def main():
#     env = HMDockEnv()
#     agent = LigandAgent(n_actions=env.n_actions)

#     episodes = 30
#     t1 = t2 = t3 = 0

#     for _ in range(episodes):
#         selected = run_episode(env, agent)

#         final_pick = selected[-1]
#         t1 += grade_task1(final_pick, env.ligands)

#         t2 += grade_task2(selected[-2:], env.ligands)

#         t3 += grade_task3(selected[-3:], env.ligands)

#     print("Task 1 Score:", round(t1 / episodes, 2))
#     print("Task 2 Score:", round(t2 / episodes, 2))
#     print("Task 3 Score:", round(t3 / episodes, 2))

# if __name__ == "__main__":
#     main()
