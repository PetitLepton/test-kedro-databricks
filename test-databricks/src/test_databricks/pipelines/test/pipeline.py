"""
This is a boilerplate pipeline 'test'
generated using Kedro 0.18.7
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import filter_label

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([node(filter_label, inputs="flavien_bs", outputs="flavien_bs_copy_with_kedro")])
