import pandas as pd

def load_queries(file):
    """Loads customer queries from an uploaded Excel file."""
    df = pd.read_excel(file, sheet_name='Chat_Team_CaseStudy')
    return df['Text'].dropna().tolist()
