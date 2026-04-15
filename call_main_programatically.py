# from run_from_config import main

# main(
#     config_path="./task_configs/nmap.toml",
#     elicitation_index=1,
#     print_comms=True
# )

# import subprocess

# cmd = [
#     "poetry", "run", "python3", "run_from_config.py",
#     "--config_path", "./task_configs/nmap.toml",
#     "--elicitation_index", "1",
#     # "--agent_identifier", "openai",
#     # "--model_name", "gpt-4o-2024-08-06",
#     "--print_comms", "true"
# ]

# subprocess.run(cmd)
import os
import subprocess
from itertools import product

config_paths = [
    "./task_configs/nmap.toml",
    "./task_configs/binpwn_gdb_repl.toml"
]

elicitation_indices = ["0"]
agents = ["anthropic"]
models = ["claude-sonnet-4-6"]
total_runs = str(len(elicitation_indices))
parallel_runs = str(total_runs)

# check whether the output.txt file exist
#  if yes, remove and create new file in main program
output_file = "output.csv"
if os.path.exists("output_file"):
    os.remove("output_file")

for config, idx, agent, model in product(
    config_paths, 
    elicitation_indices, 
    agents, 
    models):
    cmd = [
        "poetry", "run", "python3", "run_from_config.py",
        "--config_path", config,
        "--elicitation_index", idx,
        "--agent_identifier", agent,
        "--model_name", model,
        "--total_runs", total_runs,
        "--parallel_runs", parallel_runs,
        "--print_comms", "true"
    ]

    print(f"Running: {config}, idx={idx}, agent={agent}, model={model}")
    subprocess.run(cmd)