from crewai import Agent
from tools import yt_tool
from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv
load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

llm = ChatGoogleGenerativeAI(google_api_key=GEMINI_API_KEY,model="gemini-2.5-flash")

# Create a senior blog researcher
blog_researcher = Agent(
    role='Blog Researcher from Youtube Videos',
    goal='get relevant video content for the topic: {topic} from YT channel',
    verbose=True,
    memory=True,
    backstory=(
        "Expert in understanding videos in AI Data Science, ML and GenAI and giving suggestions"
    ),
    tools=[yt_tool],
    allow_delegation=True,
    llm=llm
)

# Create a senior blog writer agent with YT tool
blog_writer = Agent(
    role="Blog Writer",
    goal="Narate compelling tech stories about the video {topic} from YT channel",
    verbose=True,
    memory=True,
    backstory=(
        """
        With a flair for simplifying complex topics, you craft 
        engaging narratives that captivate and educate, bringing new
        discoveries to light in an accessible manner.
        """
    ),
    tools=[yt_tool],
    allow_delegation=False,
    llm=llm
)