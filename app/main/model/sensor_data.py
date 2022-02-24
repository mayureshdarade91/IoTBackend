from .. import db

class SensorData(db.Model):
    """ SensorData Model for storing sensor data """
    __tablename__ = "sensor_data"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    sensor_id = db.Column(db.Integer, db.ForeignKey('sensor.id'))
    sensor_data = db.Column(db.Integer, nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False)
    
    def __repr__(self):
        return "<SensorData '{}'>".format(self.sensor_id)