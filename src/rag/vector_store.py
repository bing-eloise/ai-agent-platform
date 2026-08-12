"""保存向量，并根据问题进行相似度检索"""
import numpy as np

class VectorStore:
    """简单的内存向量存储与相似度检索"""

    def __init__(self):
        self.documents = []
        self.vectors = []

    def add(self, documents: list[str], vectors: list[list[float]]):
        print(">>> 正在进入 add 方法...")
        """添加文本及对应向量"""
        if len(documents) != len(vectors):
            raise ValueError("documents and vectors must have the same length")
        self.documents.extend(documents)
        self.vectors.extend(vectors)

    def search(self, query_vector: list[float], top_k: int = 3) -> list[dict]:
        print(">>> 正在进入 search 方法...")
        """根据余弦相似度检索最相关文本"""
        if not self.vectors:
            return []

        query = np.array(query_vector)
        results = []

        for document, vector in zip(self.documents, self.vectors):
            vector = np.array(vector)
            similarity = np.dot(query, vector) / (np.linalg.norm(query) * np.linalg.norm(vector))
            results.append({"text": document, "score": float(similarity)})

        results.sort(key=lambda item: item["score"], reverse=True)
        return results[:top_k]