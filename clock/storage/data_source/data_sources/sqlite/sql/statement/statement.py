from typing import List


class SqlStatement:
    pass


class SingleSqlStatement(SqlStatement):
    def __init__(self, statement: str):
        self.statement = statement

    def get_sql(self):
        return self.statement


class CompoundSqlStatement(SqlStatement):
    def __init__(self, statements: List[str]):
        self.statements = statements

    def get_statements(self):
        return self.statements
