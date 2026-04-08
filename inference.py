import os
from openai import OpenAI
from run_baseline import run_all_tasks

def main():
    print("START")

    base_url = os.environ.get("API_BASE_URL")
    model_name = os.environ.get("MODEL_NAME")
    hf_token = os.environ.get("HF_TOKEN")

    if not base_url or not model_name or not hf_token:
        raise ValueError("Missing required environment variables")
    
    client = OpenAI(
        base_url = base_url, api_key = hf_token
    )
    
    print("STEP")

    t1, t2, t3 = run_all_tasks()
    episodes = 30

    result = {
        "Task1": round(t1 / episodes, 2),
        "Task2": round(t2 / episodes, 2),
        "Task3": round(t3 / episodes, 2)
    }
    print(result)
    print("END")

if __name__ == "__main__":
    main()