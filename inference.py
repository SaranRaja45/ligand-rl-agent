import os
from openai import OpenAI
from run_baseline import run_all_tasks

def main():
    # START block
    print("[START] task=hm-dock", flush=True)

    try:
        base_url = os.environ.get("API_BASE_URL")
        api_key = os.environ.get("API_KEY")

        client = None

        #Initialize client ONLY if variables exist
        if base_url and api_key:
            client = OpenAI(base_url = base_url, api_key = api_key)

            client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": "ping"}],
                max_tokens=1
            )

        # RL execution
        t1,t2,t3 = run_all_tasks()
        episodes = 30

        
        task1 = round(t1 / episodes, 2)
        task2 = round(t2 / episodes, 2)
        task3 = round(t3 / episodes, 2)
        
        # STEP block
        print(f"[STEP] step=1 task1={task1} task2={task2} task3={task3}", flush=True)

        # END block
        print(f"[END] task=hm-dock score={(task1+task2+task3)/3:.2f} steps=1", flush=True)

    except Exception as e:
        # NEVER crash - print error instead
        print("[STEP] step=1 error=true", flush=True)
        print(f"[END] task=hm-dock score=0 steps=1 error={str(e)}", flush=True)

if __name__ == "__main__":
    main()