from employee_events.sql_execution import QueryMixin

class QueryBase(QueryMixin):

    name = ""

    def names(self):
        return []

    def event_counts(self, id):
        sql_query = f"""
            SELECT event_date,
                   CAST(SUM(positive_events) AS INTEGER) AS positive_events,
                   CAST(SUM(negative_events) AS INTEGER) AS negative_events
            FROM employee_events
            JOIN {self.name}
                USING({self.name}_id)
            WHERE {self.name}.{self.name}_id = {id}
            GROUP BY event_date
            ORDER BY event_date
        """
        return self.pandas_query(sql_query)

    def notes(self, id):
        sql_query = f"""
            SELECT note_date, note
            FROM notes
            WHERE {self.name}_id = {id}
            ORDER BY note_date
        """
        return self.pandas_query(sql_query)