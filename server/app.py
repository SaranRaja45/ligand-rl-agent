from fastapi import FastAPI
import uvicorn
from run_baseline import run_all_tasks

app = FastAPI()

def normalize(score):
    if score <= 0:
        return 0.01
    if score >= 1:
        return 0.99
    return round(score,2)

@app.post("/reset")
def reset():
    t1, t2, t3 = run_all_tasks()
    episodes = 30

    task1 = round(t1 / episodes, 2)
    task2 = round(t2 / episodes, 2)
    task3 = round(t3 / episodes, 2)

    return{"Task1": task1, "Task2": task2, "Task3": task3}

@app.get("/")
def root():
    return{"status": "HM-Dock API working"}

def main():
    uvicorn.run(app, host="0.0.0.0", port=7860)

if __name__ == "__main__":
    main()
