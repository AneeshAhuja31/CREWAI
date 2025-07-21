from crewai_tools import YoutubeChannelSearchTool

# Create the tool with Hugging Face embeddings (free)
yt_tool = YoutubeChannelSearchTool(
    youtube_channel_handle='@TheLeaderboard',
    config={
        "embedder": {
            "provider": "huggingface",
            "config": {
                "model": "sentence-transformers/all-MiniLM-L6-v2"
            }
        }
    }
)