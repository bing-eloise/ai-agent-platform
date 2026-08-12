"""把文本转换成向量"""
from sentence_transformers import SentenceTransformer

class EmbeddingModel:
    """文本向量化模型"""
    def __init__(self, model_name: str = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"):
        self.model = SentenceTransformer(model_name)

    def embed_text(self, text: str) -> list[float]:
        """将单个文本转换为向量"""
        if not text:
            raise ValueError("text cannot be empty")
        embedding = self.model.encode(text)
        return embedding.tolist()

    def embed_documents(self, documents: list[str]) -> list[list[float]]:
        """将多个文本转换为向量"""
        if not documents:
            return []
        embeddings = self.model.encode(documents)
        return embeddings.tolist()