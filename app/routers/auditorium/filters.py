from fastapi_filter import Filter
from app.database.models import Auditorium
class Auditoriumfilter(Filter):
    class Constants(Filter.Constants):
        model = Auditorium