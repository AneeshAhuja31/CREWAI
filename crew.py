from crewai import Crew,Process
from agents import blog_researcher,blog_writer
from tools import yt_tool
from tasks import researcher_task,write_task

#tech-focued crew with enhanced configs
crew = Crew(
    agents=[blog_researcher,blog_writer],
    tasks=[researcher_task,write_task],
    process=Process.sequential,
    memory=True,
    cache=True,
    max_rpm=100,
    share_crew=True
)

result = crew.kickoff(inputs={"topic":"top videogames"})
print(result)
