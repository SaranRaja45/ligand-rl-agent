---
title: HM-Dock
emoji: 🧬
colorFrom: blue
colorTo: purple
sdk: docker
app_file: app.py
pinned: false
---
# Reinforcement Learning for Ligand Prioritization in Drug Discovery
A lightweight RL system that simulates ligand selection and ranking, designed for OpenEnv-compatible evaluation and rapid deployment.
---
## Overview
Ligand selection is a critical step in drug discovery, where molecules are evaluated based on their binding affinity to a target protein.
This project models that process as a sequential decision-making problem, where an RL agent learns to:    - Explore available ligands
- Identify high-affinity candidates
- Prioritize the best molecules over time
This abstraction demonstrates how reinforcement learning can assist in prioritizing promising drug candidates efficiently.
---
## Core Idea
Binding affinity is treated as the reward signal:
- Lower affinity (more negative) -> Better binding
- Reward = negative of affinity -> Higher reward is better
The agent interacts with a custom environment and learns to maximize total reward by selecting optimal ligands.
---
## Tasks & Evaluation
The system evaluates performance across three progressively difficult tasks:
### Task 1: Best Ligand Selection
- Checks if the agent selects the single best ligand
- Focus: Final decision quality
### Task 2: Top-2 ligands identification 
- Evaluates whether the agent identifies top candidates within its last selections
- The ligands need to be in an order
- Focus: Short-term consistency
### Task 3: Top-3 ligand Ranking
- Measures the agent's ability to prioritize and rank the best ligands
- The ligands must be in the correct order
- Focus: Structured decision-making
---
## Example Results
Typical performance of the baseline agent:
- Task 1 Score: ~0.89
- Task 2 Score: ~0.35
- Task 3 Score: ~0.31
---
## Project Structure
.
├── RL_env.py           # Custom RL environment
├── run_baseline.py     # Baseline agent script
├── openenv.yaml        # Environment configuration
├── requirements.txt    # Dependencies (minimal)
├── openenv.yaml        # OpenEnv file
├── app.py              # app file
├── inference.py        # inference Script
└── README.md           # Project Documentation
---
## API Interface (OpenEnv Compatible)
This project exposes a minimal API for automated evaluation.
### Endpoint
POST /reset
### Description
- Runs the RL agent across all tasks
- Returns task scores as JSON
- Used by OpenEnv validator for submission testing
### Example Response
{
    "Task1": 0.89, 
    "Task2": 0.35,
    "Task3": 0.31
}
---
## Inference Script
The inference.py file is included to comply with the hackathon evaluation requirements.
It serves as a standardized execution interface that:
- Uses environment variables for configuration (API_BASE_URL, MODEL_NAME, HF_TOKEN)
- Initializes an OpenAI-compatible client (as required by the evaluation protocol)
- Executes the RL pipeline via run_all_tasks()
- Outputs structured logs im the format: START -> STEP -> END
Note: The core reinforcement learning logic is independent of this script. The inference file acts only as a wrapper for evaluation compatibility.
---
## How to Run
### Locally
python run_baseline.py
### Using Docker
docker build -t ligand-rl .
docker run ligand-rl
---
## Design Philosophy
This project is intentionally designed to be:
- Minimal yet functional
- Easy to understand and extend
- Focused on core RL concepts rather than heavy frameworks
---
## Real-World Connection
The task structure mirrors real drug discovery stages:
1. Initial screening = Task 1
2. Candidate narrowing = Task 2
3. Lead prioritization = Task 3
---
## Future Improvements
- Memory-based agents for better ranking
- Q-learning/policy optimization
- Integration with real molecular datasets
- Advanced scoring functions
---
## Conclusion
This project demonstrates how reinforcement learning can be applied to scientific decision-making problems, even with a simple and interpretable setup.
---
## Author
Built as a part of an exploration into RL-driven ligand prioritization systems.
---