from clock.storage.data_source.data_sources.sqlite.component.component import SqliteStorageComponent


class QuerySqliteComponent(SqliteStorageComponent):
    version = 1

    def __init__(self):
        super().__init__("query", self.version)

    def create(self):
        self._sql("create table if not exists query ("
                  "timestamp text,"
                  "user_id integer not null,"
                  "time_point text not null,"
                  "query text,"
                  "offset text,"
                  "locale text,"
                  "results_found_len integer,"
                  "results_sent_len integer,"
                  "processing_seconds real"
                  ")")
        self._sql("create table if not exists chosen_result ("
                  "timestamp text,"
                  "user_id integer not null,"
                  "time_point text,"
                  "chosen_zone_name text,"
                  "query text,"
                  "choosing_seconds real"
                  ")")

    def save_query(self, user_id: int, timestamp: str, query: str, offset: str, locale: str, results_found_len: int,
                   results_sent_len: int, processing_seconds: float):
        self._sql("insert into query "
                  "(timestamp, user_id, time_point, query, offset, locale, results_found_len, results_sent_len, "
                  "processing_seconds) "
                  "values (strftime('%s', 'now'), ?, ?, ?, ?, ?, ?, ?, ?)",
                  (user_id, timestamp, query, offset, locale, results_found_len, results_sent_len, processing_seconds))

    def save_chosen_result(self, user_id: int, timestamp: str, chosen_zone_name: str, query: str,
                           choosing_seconds: float):
        self._sql("insert into chosen_result "
                  "(timestamp, user_id, time_point, chosen_zone_name, query, choosing_seconds) "
                  "values (strftime('%s', 'now'), ?, ?, ?, ?, ?)",
                  (user_id, timestamp, chosen_zone_name, query, choosing_seconds))