import streamlit as st
import os
from crewai import Agent, Task, Crew, Process
from langchain.chat_models import AzureChatOpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Azure OpenAI Configuration
azure_openai_config = {
    'openai_4_version': os.getenv("openai_4_version"),
    'openai_4_key': os.getenv("openai_4_key"),
    'openai_4_deployment': os.getenv("openai_4_deployment"),
    'openai_4_endpoint': os.getenv("openai_4_endpoint"),
    'openai_4_model': os.getenv("openai_4_model")
}

def create_agent(role: str, goal: str, backstory: str, verbose: bool, allow_delegation: bool) -> Agent:
    llm = AzureChatOpenAI(
        openai_api_version=azure_openai_config['openai_4_version'],
        openai_api_key=azure_openai_config['openai_4_key'],
        deployment_name=azure_openai_config['openai_4_deployment'],
        azure_endpoint=azure_openai_config['openai_4_endpoint'],
        model_name=azure_openai_config['openai_4_model']
    )
    return Agent(
        role=role,
        goal=goal,
        backstory=backstory,
        verbose=verbose,
        allow_delegation=allow_delegation,
        llm=llm
    )

def create_task(description: str, expected_output: str, agent: Agent) -> Task:
    return Task(
        description=description,
        expected_output=expected_output,
        agent=agent
    )

st.title("CrewAI Configuration App with Azure OpenAI")

# # Display Azure OpenAI Configuration (optional, for verification)
# st.header("Azure OpenAI Configuration")
# st.write("Using the following configuration from environment variables:")
# st.write(f"API Version: {azure_openai_config['openai_4_version']}")
# st.write(f"Deployment: {azure_openai_config['openai_4_deployment']}")
# st.write(f"Endpoint: {azure_openai_config['openai_4_endpoint']}")
# st.write(f"Model: {azure_openai_config['openai_4_model']}")
# st.write("API Key: [Hidden for security]")

# Agent Configuration
st.header("Agent Configuration")
num_agents = st.number_input("Number of Agents", min_value=1, max_value=5, value=2)

agents = []
agent_names = []  # Store agent names separately
for i in range(num_agents):
    st.subheader(f"Agent {i+1}")
    name = st.text_input(f"Name for Agent {i+1}", value=f"Agent {i+1}")
    role = st.text_input(f"Role for Agent {i+1}", value=f"Role {i+1}")
    goal = st.text_area(f"Goal for Agent {i+1}", value=f"Goal for Agent {i+1}")
    backstory = st.text_area(f"Backstory for Agent {i+1}", value=f"Backstory for Agent {i+1}")
    verbose = st.checkbox(f"Verbose for Agent {i+1}", value=True)
    allow_delegation = st.checkbox(f"Allow Delegation for Agent {i+1}", value=True)
    
    agent = create_agent(role, goal, backstory, verbose, allow_delegation)
    agents.append(agent)
    agent_names.append(name)  # Store the name

# Task Configuration
st.header("Task Configuration")
num_tasks = st.number_input("Number of Tasks", min_value=1, max_value=5, value=2)

tasks = []
for i in range(num_tasks):
    st.subheader(f"Task {i+1}")
    description = st.text_area(f"Description for Task {i+1}", value=f"Description for Task {i+1}")
    expected_output = st.text_area(f"Expected Output for Task {i+1}", value=f"Expected output for Task {i+1}")
    agent_index = st.selectbox(f"Assign Agent for Task {i+1}", range(num_agents), format_func=lambda x: agent_names[x])
    
    task = create_task(description, expected_output, agents[agent_index])
    tasks.append(task)

# Crew Configuration
st.header("Crew Configuration")
crew_name = st.text_input("Crew Name", value="My Crew")
crew_description = st.text_area("Crew Description", value="A crew created using Streamlit")

# Create and Run Crew
if st.button("Create and Run Crew"):
    crew = Crew(
        agents=agents,
        tasks=tasks,
        verbose=2,  # You can make this configurable if needed
        process=Process.sequential  # You can make this configurable if needed
    )
    
    result = crew.kickoff()
    
    st.success("Crew has completed its tasks!")
    st.write("Result:")
    st.write(result)

st.info("Note: This is a basic implementation. You may need to add error handling, more configuration options, and integrate with your specific CrewAI setup and tools.")