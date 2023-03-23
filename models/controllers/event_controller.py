from models import Event, Class
from extensions.database_extension import db_session


class EventController:
    @staticmethod
    def get_all_events():
        return db_session.query(Event).all()

    @staticmethod
    def get_event(event_id=None, teacher_name=None):
        if event_id:
            return db_session.query(Event).filter_by(id=event_id).first()
        if teacher_name:
            return db_session.query(Event, Class).filter(Event.summaryId == Class.id,
                                                         Event.description.like(f"%{teacher_name}%")).all()
