from RL_env import HMDockEnv, LigandAgent, grade_task1, grade_task2, grade_task3

#Run Episode
def run_episode(env, agent):
    obs = env.reset()
    done = False
    selected = []

    while not done:
        action = agent.choose_action()
        result = env.step(action)

        obs = result["observation"]
        reward = result["reward"]
        done = result["done"]

        agent.update(action, reward)
        selected.append(obs["ligand"])

    return selected

#Main function
def run_all_tasks():
    env = HMDockEnv()
    agent = LigandAgent(n_actions=env.n_actions)

    episodes = 30
    t1= t2 = t3 = 0

    for _ in range(episodes):
        selected = run_episode(env, agent)

        final_pick = selected[-1]
        t1 += grade_task1(final_pick, env.ligands)

        t2 += grade_task2(selected[-2:], env.ligands)

        t3 += grade_task3(selected[-3:], env.ligands)

    return t1, t2, t3

if __name__ == "__main__":
    t1, t2, t3 = run_all_tasks()
    print(f"Task 1 Score: {t1}")
    print(f"Task 2 Score: {t2}")
    print(f"Task 3 Score: {t3}")