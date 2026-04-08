from fastapi import FastAPI
from run_baseline import run_all_tasks

app = FastAPI()

@app.post("/reset")
def reset():
    t1, t2, t3 = run_all_tasks()
    episodes = 30

    return{
        "Task1": round(t1 / episodes, 2),
        "Task2": round(t2 / episodes, 2),
        "Task3": round(t3 / episodes, 2)
    }

@app.get("/")
def root():
    return{"status": "HM-Dock API working"}

def main():
    uvicorn.run(app, host="0.0.0.0", port=7860)

# REQUIRED for validator
if __name__ == "__main__":
    main()
