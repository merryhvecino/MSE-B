data = [
    {"name": "Alice", "age": 28},
    {"name": "Bob", "age": 24},
    {"name": "Charlie", "age": 30}
]
extracted_info = [i for i in data if i['age'] > 25]
print(extracted_info)