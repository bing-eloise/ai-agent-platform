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
- [x] Day7: Token统计 + 上下文窗口控制
- [x] Day8: AI Memory系统优化（自动摘要 + Summary持久化）
- [x] Day9: 异常处理与稳定性增强（Exception + Retry + Logging优化 + 自动化测试）

## 项目结构

```text
project01_ai_chat/
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── memory.py
│   ├── database.py
│   ├── summary.py
│   ├── prompt.py
│   ├── llm.py
│   ├── logger.py
│   ├── exceptions.py
│   └── utils/
│       └── retry.py
├── config/
│   └── settings.py
├── tests/
│   ├── test_retry.py
│   └── test_exception.py
├── logs/
    └── .gitkeep
```

### Architecture

- `src/memory.py` — 短期记忆管理（ChatMemory），包含支持历史消息剪裁和上下文窗口控制，token数量检测，自动触发历史压缩
- `src/database.py` — 对话历史持久化（DatabaseManager），基于 SQLite，保存聊天消息、摘要信息且支持历史恢复
- `src/summary.py` — 基于LLM生成对话摘要，支持增量摘要更新
- `src/llm.py` — DeepSeek API 流式调用封装
- `src/logger.py` — 日志系统配置
- `src/exceptions.py` — 项目统一异常体系，用于规范化处理 LLM、数据库、配置等异常
- `src/utils/retry.py` — Retry工具模块，实现失败重试和指数退避机制，提高API调用稳定性
- `src/main.py` — 程序入口与对话主循环
- `config/settings.py` — 环境变量与配置管理
- `src/prompt.py` - System Prompt管理和角色多模式定义

## Core Features
- DeepSeek API Chat
- Streaming Response
- Conversation Memory
- SQLite Persistent Storage
- Token-aware Context Management
- Automatic Conversation Summarization
- Summary Memory Recovery
- Exception Handling
- API Retry Mechanism
- Exponential Backoff
- Logging-based Error Tracking
- Automated Testing

## 技术栈

- Python 3.12
- Git
- GitHub
- SQLite
- DeepSeek API
- Pytest

## 作者

bing-eloise
