# server.py
from mcp.server.fastmcp import FastMCP
from mcp.server.fastmcp.prompts import base
from paper_interpreter import PaperInterpreter
from typing import List, Dict, Any

# Create an MCP server
mcp = FastMCP("Demo")


# Add an addition tool
@mcp.tool()
async def arxiv_search(query: str) -> List[Dict[str, Any]]:
    """
    Search the Arxiv database using the provided query.
    """
    # Placeholder for actual search logic
    # In a real implementation, this would interact with the Arxiv API or database
    pi = PaperInterpreter()
    return await pi.search_papers(query, max_results=5)


@mcp.tool()
async def read_arxiv_html(arxiv_html_link: str) -> str:
    pass


@mcp.prompt()
def query_prompt(message: str) -> list[base.Message]:
    """
    Query the Arxiv MCP with a message.
    """
    return [
        base.UserMessage("# Query the ArXiv database"),
        base.UserMessage(
            "Please search the ArXiv academic repository using the following query:"
        ),
        base.UserMessage(message),
        base.AssistantMessage(
            "The system will process your query and return relevant academic papers matching your search criteria from the arXiv database of scientific papers and preprints."
        ),
    ]


@mcp.prompt()
def read_arxiv_html_prompt(arxiv_html_link: str) -> list[base.Message]:
    """
    Read the Arxiv HTML with a message.
    """
    return [
        base.UserMessage("# Read the ArXiv HTML"),
        base.UserMessage("Please read the ArXiv HTML using the following link:"),
        base.UserMessage(arxiv_html_link),
        base.AssistantMessage(
            "The system will process your query and return relevant academic papers matching your search criteria from the arXiv database of scientific papers and preprints."
        ),
    ]
