from typing import Any, Dict, List

import arxiv

from plugin_utils import PluginMetadata

metadata = PluginMetadata(
    name="paper_interpreter",
    description="Searches and interprets ArXiv papers using LLM",
    version="0.1.0",
    author="Hiyen Wong",
    capabilities=["paper_search", "paper_interpret"],
)


class PaperInterpreter:
    def __init__(self):
        pass

    async def search_papers(
        self, query: str, max_results: int = 5
    ) -> List[Dict[str, Any]]:
        """Search for papers on ArXiv"""
        search = arxiv.Search(
            query=query, max_results=max_results, sort_by=arxiv.SortCriterion.Relevance
        )

        results = []
        for paper in arxiv.Client().results(search):
            results.append(
                {
                    "title": paper.title,
                    "authors": [str(author.name) for author in paper.authors],
                    "summary": paper.summary,
                    "published": paper.published.strftime("%Y-%m-%d"),
                    "pdf_url": paper.pdf_url,
                    "entry_id": paper.entry_id,
                }
            )
        return results

    async def interpret_paper(self, paper_id: str, llm_client) -> Dict[str, Any]:
        """Interpret a paper using LLM"""
        # Get the paper
        search = arxiv.Search(id_list=[paper_id])
        results = list(arxiv.Client().results(search))
        if not results:
            raise ValueError(f"No paper found with ID: {paper_id}")
        paper = results[0]

        # Create a prompt for the LLM
        prompt = f"""
        Title: {paper.title}
        Authors: {", ".join([author.name for author in paper.authors])}
        Abstract: {paper.summary}
        
        Please provide:
        1. A simplified explanation of this research
        2. Key findings and implications
        3. How this relates to the current state of the field
        """

        # This is where you would call your LLM client
        # For example with OpenAI:
        # response = await llm_client.chat.completions.create(...)

        # For now, return a placeholder
        return {
            "paper_id": paper_id,
            "title": paper.title,
            "interpretation": "LLM interpretation would go here",
        }


def create_plugin():
    return {"metadata": metadata, "handler": PaperInterpreter()}
