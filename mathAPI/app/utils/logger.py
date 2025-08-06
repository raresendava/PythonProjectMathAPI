def log_to_kafka(log_entry):
    print(f"[Kafka Log] User: {log_entry.username}, Operation: {log_entry.operation}, Result: {log_entry.result}")