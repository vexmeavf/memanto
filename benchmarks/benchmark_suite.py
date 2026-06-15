 1 import time
    2 from memanto.client import Client
    3
    4 # Benchmark Suite para Memanto (Issue #639)
    5 # Evalúa precisión de recuperación y latencia de ingesta
    6 def run_memanto_benchmark():
    7     client = Client()
    8     test_data = ["Fact 1", "Fact 2", "Fact 3"]
    9
   10     start = time.time()
   11     for item in test_data:
   12         client.store(item)
   13     ingestion_time = time.time() - start
   14
   15     recall_results = [client.recall(item) is not None for item in test_data]
   16     accuracy = sum(recall_results) / len(recall_results)
   17
   18     return {"accuracy": accuracy, "latency": ingestion_time}
   19
   20 if __name__ == "__main__":
   21     print(run_memanto_benchmark())
