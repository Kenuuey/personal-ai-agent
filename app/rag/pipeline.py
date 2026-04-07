class RAGPipeline:
    def __init__(self, retriever, llm):
        self.retriever = retriever
        self.llm = llm

    def query(self, question):
        docs = self.retriever.retrieve(question)

        context = "\n".join(docs)

        prompt = f"""
        Answer the question using context:

        {context}

        Question: {question}
        """

        return self.llm.chat({"role": "user", "content": prompt})