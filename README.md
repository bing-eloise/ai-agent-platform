# Project01 AI Chat

一个用于学习 AI 应用开发的聊天助手项目。

## 当前进度

- [x] Day0：环境搭建
- [x] Day1：企业级项目结构
- [x] Day2: 接入 DeepSeek API
- [x] Day3: Chat Memory上下文记忆
- [x] Day4: Streaming输出 + Logging日志系统
- [x] Day5: Memory System(SQLite持久化 + 历史恢复)
- [x] Day6: Prompt管理 + 多角色助手

## 项目结构

```text
project01_ai_chat/
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── memory.py
│   ├── database.py
│   ├── llm.py
│   └── logger.py
├── config/
│   └── settings.py
├── tests/
│   └── .gitkeep
├── logs/
    └── .gitkeep
```

### Architecture

- `src/memory.py` — 短期记忆管理（ChatMemory），包含支持历史消息剪裁和上下文窗口控制
- `src/database.py` — 对话历史持久化（DatabaseManager），基于 SQLite
- `src/llm.py` — DeepSeek API 流式调用封装
- `src/logger.py` — 日志系统配置
- `src/main.py` — 程序入口与对话主循环
- `config/settings.py` — 环境变量与配置管理
- `src/prompt.py` - System Prompt管理和角色多模式定义

## 技术栈

- Python 3.12
- Git
- GitHub

## 作者

bing-eloise
