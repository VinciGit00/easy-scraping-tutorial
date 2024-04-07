# if you plan on using text_to_speech and GPT4-Vision models be sure to use the
# correct APIKEY
OPENAI_API_KEY = "YOUR_API_KEY"

from scrapegraphai.graphs import SmartScraperGraph

# Define the configuration for the graph
graph_config = {
    "llm": {
        "api_key": OPENAI_API_KEY,
        "model": "gpt-3.5-turbo",
    },
}

# Create the SmartScraperGraph instance
smart_scraper_graph = SmartScraperGraph(
    prompt="List me all the news with their description.",
    file_source="https://www.wired.com/",  # also accepts a string with the already downloaded HTML code in text format
    config=graph_config
)

result = smart_scraper_graph.run()
print(result)