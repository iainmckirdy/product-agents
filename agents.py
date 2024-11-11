from crewai import Agent, Task, Crew, Process
from crewai.project import CrewBase, agent, task, crew
from crewai_tools import WebsiteSearchTool, ScrapeWebsiteTool
from langchain_openai import ChatOpenAI


@CrewBase
class ProductDesignMarketingAgents():

    # load agent and task descriptions
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    # define the llm 
    def __init__(self) -> None:
        self.llm = ChatOpenAI(
        model="gpt-4o",
        temperature=0.2,
        max_tokens=None,
        timeout=None)

    # define the agents
    @agent
    def researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['researcher'], 
            verbose=False,
            allow_delegation=False, 
            llm=self.llm,
            tools=[ScrapeWebsiteTool(), WebsiteSearchTool()]
            )
    
    @agent
    def marketer(self) -> Agent:
        return Agent(
            config=self.agents_config['marketer'], 
            verbose=False,
            allow_delegation=False, 
            llm=self.llm
            )
    
    @agent
    def product_designer(self) -> Agent:
        return Agent(
            config=self.agents_config['product_designer'], 
            verbose=False,
            allow_delegation=False, 
            llm=self.llm
            )
    
    # define the tasks
    @task
    def research(self) -> Task:
        return Task(
            config = self.tasks_config['research'], 
            agent = self.researcher()
        )
    
    @task
    def product_design(self) -> Task:
        return Task(
            config = self.tasks_config['design'], 
            agent = self.product_designer()
        )
    
    @task
    def marketing(self) -> Task:
        return Task(
            config = self.tasks_config['marketing'], 
            agent = self.marketer()
        )    
    
    # instantiate the agent team
    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents, 
            tasks=self.tasks, 
            process=Process.sequential, 
            verbose=True
        )