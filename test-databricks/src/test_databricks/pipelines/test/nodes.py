"""
This is a boilerplate pipeline 'test'
generated using Kedro 0.18.7
"""

def filter_label(data):
    return data.select("label")