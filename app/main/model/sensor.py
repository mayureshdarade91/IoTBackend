from .. import db
from sqlalchemy.orm import relationship


class Sensor(db.Model):
    """ Sensor Model for storing sensor related details """
    __tablename__ = "sensor"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), unique=True, nullable=False)
    sensor_code = db.Column(db.String(255), unique=True, nullable=False)
    registered_on = db.Column(db.DateTime, nullable=False)
    last_active = db.Column(db.DateTime, nullable=True)
    device_id = db.Column(db.Integer, db.ForeignKey('device.id'))
    sensor_data = relationship("SensorData", backref='Sensor', lazy=True)

    
    def __repr__(self):
        return "<Sensor '{}'>".format(self.name)