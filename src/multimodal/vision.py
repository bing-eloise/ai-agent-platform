"""调用Vision模型"""
from src.multimodal.image_loader import image_to_data_url
from src.multimodal.provider import VisionProvider

class MockVisionProvider(VisionProvider):
    """Mock Vision Provider 用于在没有真实Vision API时验证多模态应用流程。"""
    def analyze(self, prompt: str, image_data_url: str) -> str:
        if not prompt:
            raise ValueError("prompt cannot be empty")
        if not image_data_url:
            raise ValueError("image_data_url cannot be empty")
        return ("Mock Vision Result:图片已成功接收并完成分析。")

class VisionService:
    """多模态图片理解服务"""
    def __init__(self, provider: VisionProvider):
        self.provider = provider

    def analyze_image(self, file_path: str, prompt: str) -> str:
        """图片分析统一入口"""
        image_data_url = image_to_data_url(file_path)
        return self.provider.analyze(prompt, image_data_url)