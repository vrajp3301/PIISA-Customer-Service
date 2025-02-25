import json
import os

def save_to_json(conversations, file_path):
    
    output_dir = os.path.dirname(file_path)
    os.makedirs(output_dir, exist_ok=True)  
    
    with open(file_path, "w") as f:
        json.dump(conversations, f, indent=4)
