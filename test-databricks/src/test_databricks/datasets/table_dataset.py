from kedro.io.core import AbstractDataSet
from typing import NoReturn
from pyspark.sql import SparkSession
class TableDataSet(AbstractDataSet):
    def __init__(self, name: str) -> None:
        self.name = name

    @staticmethod
    def _get_spark():
        return SparkSession.builder.getOrCreate()

    def _load(self):
        return self._get_spark().read.table(self.name)

    def _save(self, data: None) -> NoReturn:
        data.write.mode("append").saveAsTable(name=self.name)

    def _exists(self) -> bool:
        return True

    def _describe(self):
        return None