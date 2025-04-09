# 学术论文搜索与解释服务

这是一个基于Python的学术论文搜索和解释服务，利用ArXiv API获取学术论文信息，并提供论文解释功能。

## 功能特点

- 💡 基于MCP (Model Context Protocol)服务器架构
- 🔍 支持ArXiv论文数据库搜索
- 📚 提供论文元数据获取（标题、作者、摘要等）
- 🤖 集成LLM支持，可提供论文解释（待实现）
- 🌐 提供RESTful API接口

## 技术架构

- **FastMCP**: 用于构建MCP服务器
- **ArXiv API**: 用于论文搜索和获取
- **异步处理**: 使用Python `asyncio`进行异步操作
- **模块化设计**: 插件化架构，便于扩展

## 主要组件

1. `server.py`: MCP服务器实现，提供API endpoints
2. `paper_interpreter.py`: 论文搜索和解释的核心实现
3. `plugin_utils.py`: 插件相关工具类
4. `hello.py`: 基础测试模块

## 安装要求

```bash
# 使用pyproject.toml管理依赖
pip install .
```

主要依赖：
- arxiv-python
- fastmcp
- asyncio

## 使用示例

```python
from paper_interpreter import PaperInterpreter

# 创建解释器实例
interpreter = PaperInterpreter()

# 搜索论文
results = await interpreter.search_papers("quantum computing", max_results=5)

# 解释特定论文
interpretation = await interpreter.interpret_paper(paper_id, llm_client)
```

## API 端点

### ArXiv搜索
```
GET /arxiv_search?query=<search_query>
```

### 个性化问候
```
GET /greeting/{name}
```

## 项目状态

- ✅ 基础框架搭建
- ✅ ArXiv搜索功能
- ⏳ LLM论文解释功能（开发中）
- ⏳ API文档（计划中）

## 作者

Hiyen Wong

## 版本

当前版本：0.1.0

## 许可证

[Apache License]
