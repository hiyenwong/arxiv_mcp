from typing import List, Optional


class PluginMetadata:
    """Metadata class for MCP plugins"""

    def __init__(
        self,
        name: str,
        description: str,
        version: str,
        author: str,
        capabilities: Optional[List[str]] = None,
    ):
        self.name = name
        self.description = description
        self.version = version
        self.author = author
        self.capabilities = capabilities or []
