import os
from dotenv import load_dotenv

from agents import ProductDesignMarketingAgents

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


def run():

    inputs = {"niche": input("Niche to design and market products for: ")}

    return ProductDesignMarketingAgents().crew().kickoff(inputs=inputs)


if __name__ == "__main__":
    print("## Product Design and Marketing Agents")
    print('-------------------------------')
    result = run()
    print("\n\n########################")
    print("## Here is the Report")
    print("########################\n")
    print(result)
    print("\n########################\n")