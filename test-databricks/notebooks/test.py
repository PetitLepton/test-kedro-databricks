# Databricks notebook source
# MAGIC %pip install kedro python-json-logger

# COMMAND ----------

# MAGIC %load_ext kedro.ipython

# COMMAND ----------

import logging
from pathlib import Path

# suppress excessive logging from py4j
logging.getLogger("py4j.java_gateway").setLevel(logging.ERROR)

# copy project data into DBFS
project_root = "/Workspace/Repos/flavien.lambert@sencrop.com/test-kedro-databricks/test-databricks/"

# COMMAND ----------

from kedro.framework.session import KedroSession
from kedro.framework.startup import bootstrap_project

# bootstrap_project(project_root)

with KedroSession.create(project_path=project_root, env="local") as session:
    session.run()

# COMMAND ----------


