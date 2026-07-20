

- call main.py by providing toml file and llm model
- task and elicitation are extracted from the toml file
    - task:{"name", "version", "ruleset", "environments"}
    - elicitation:{"terminal_interop_protocol", "prefilled_messages"}
- the harness saves a snapshot of the task and elicitation separately if not saved before and load it to its pointer.
- select the communication protocol to communicate with LLM : (JSON, XML and MARKDOWN)
- Save the initial prompt
- Start the docker challenge
    - build the docker image 
    - reset any previous runnign container and start a fresh container 
- Run the agent-environment loop
    - calling OpenAI
- Extract Terminal command from the model response
- Check whether the model has found the flag
- If no Flag has been found, execute the command in the container
- Check container output for the flag
- Send terminal output back to the Model for further iteration
- Handle Termination a. when success with FLag b. when failure if iternation completed by the code "return run".