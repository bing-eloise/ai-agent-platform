class AIChatError(Exception):
    """项目基础异常"""
    pass

class LLMError(AIChatError):
    """LLM调用异常"""
    pass

class DatabaseError(AIChatError):
    """数据库异常"""
    pass

class ConfigError(AIChatError):
    """配置异常"""
    pass