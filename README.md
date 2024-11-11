# AI Agents for Product Design and Marketing

## Introduction:
This project is an example of an agentic workflow that can develop outlines for products, along with marketing strategies for these products, for any given marketing niche. 

This project uses the CrewAI framework for the AI agent team.

## Details & Explanation:
- **Running the Script**: Enter OpenAI API key in the .env file then execute ``python main.py`` and input the marketing niche to be used when prompted. The script will leverage the AI agents to analyse the niche and generate a detailed report on products along with unique marketing strategies for each product.
- **Key Components**:
  - `./main.py`: Main script file.
  - `./agnets.py`: File where the agent team class is created and llm model is defined.
  - `./.env`: Environment file
  - `./config/agents.yaml`: Main file with the agent prompts.
  - `./config/tasks.yaml`: Main file with the task prompts.


### Note on language models:
The project by default uses the OpenAI GPT-4o model, so access to this is required in order to run it.

The model used can be altered within the agents.py file.
