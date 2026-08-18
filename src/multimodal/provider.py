from abc import ABC, abstractmethod

class VisionProvider(ABC):
    """Vision模型统一接口"""
    @abstractmethod
    def analyze(self, prompt: str, image_data_url: str) -> str:
        """分析图片并返回文本结果"""
        pass