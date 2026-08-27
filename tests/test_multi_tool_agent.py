from src.agent.agent import Agent

def test_agent_calculator():
    agent = Agent()
    answer = agent.run("请计算128乘以37")

    print("\nCalculator Answer:")
    print(answer)

    assert "4736" in answer

def test_agent_rag():
    agent = Agent()
    answer = agent.run("Chunk Overlap有什么作用？请查询项目知识库。")

    print("\nRAG Answer:")
    print(answer)

    assert ("上下文" in answer or "切分边界" in answer)

def test_agent_no_tool():
    agent = Agent()
    answer = agent.run("你好，请简单介绍一下你自己。")

    print("\nChat Answer:")
    print(answer)

    assert isinstance(answer, str)
    assert len(answer) > 0