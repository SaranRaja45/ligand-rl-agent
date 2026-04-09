import os
from openai import OpenAI
from run_baseline import run_all_tasks

def main():
    # START block
    print("[START] task=hm-dock", flush=True)

    try:
        base_url = os.environ.get("API_BASE_URL")
        model_name = os.environ.get("MODEL_NAME")
        hf_token = os.environ.get("HF_TOKEN")

        #Initialize client ONLY if variables exist
        if base_url and model_name and hf_token:
            client = OpenAI(base_url = base_url, api_key = hf_token)

        t1,t2,t3 = run_all_tasks()
        episodes = 30

        
        Task1 = round(t1 / episodes, 2)
        Task2 = round(t2 / episodes, 2)
        Task3 = round(t3 / episodes, 2)
        
        # STEP block (at least one required)
        print(f"[STEP] step=1 Task1={Task1} Task2={Task2} Task3={Task3}", flush=True)

        # END block
        print(f"[END] task=hm-dock score={(Task1+Task2+Task3)/3:.2f} steps=1", flush=True)

    except Exception as e:
        # NEVER crash - print error instead
        print("[STEP] step=1 error=true", flush=True)
        print(f"[END] task=hm-dock score=0 steps=1 error={str(e)}", flush=True)
    
    print("END")

if __name__ == "__main__":
    main()