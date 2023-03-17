from typing import List
import sqlalchemy as sa
from gino import Gino

db = Gino()

class ScheduleGroupTypeOneEvent(db.Model):
    __tablename__ = 'graphs'
    speciality = db.Column(db.Text())
    course = db.Column(db.Integer())
    format = db.Column(db.Text(10))
    term = db.Column(db.Integer())
    summary = db.Column(db.Text(50))
    start = db.Column(db.Date())
    end = db.Column(db.Date())
    group_fullname = db.Column(db.Text())
    

    def __str__(self):
        model = self.__class__.__name__
        table: sa.Table = sa.inspect(self.__class__)
        primary_key_columns: List[sa.Column] = table.columns
        values = {
            column.name: getattr(self, self._column_name_map[column.name])
            for column in primary_key_columns
        }
        values_str = " ".join(f"{name}={value!r}" for name, value in values.items())
        return f"<{model} {values_str}>"