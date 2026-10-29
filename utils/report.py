import os
import pandas as pd

def generate_report(prompt: str, responses: dict) -> str:
    rows = [
        [model, response] for model, response in responses.items()
    ]
    
    df = pd.DataFrame(rows, columns=['Model', 'Response'])
    
    report_path = "reports/llm_comparison_report.csv"
    
    os.makedirs(os.path.dirname(report_path), exist_ok=True)
    
    df.to_csv(report_path, index=False)
    
    return report_path