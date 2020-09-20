from .. import db
from sqlalchemy import Column, String, Integer


class User(db.Model):
    __tablename__ = 'user'

    user_id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, default=0)
    age = Column(Integer, nullable=True)
    gender = Column(String(50), nullable=True)
    pscore = Column(Integer, nullable=False)
    walking = Column(Integer, nullable=False, default=0)
    biking = Column(Integer, nullable=False, default=0)
    swimming = Column(Integer, nullable=False, default=0)
    elliptical = Column(Integer, nullable=False, default=0)
    resistance_bands = Column(Integer, nullable=False, default=0)
    bench_press = Column(Integer, nullable=False, default=0)
    running = Column(Integer, nullable=False, default=0)
    stair_climbing = Column(Integer, nullable=False, default=0)
    pushups = Column(Integer, nullable=False, default=0)
    lunges = Column(Integer, nullable=False, default=0)
    sit_ups = Column(Integer, nullable=False, default=0)
    dips = Column(Integer, nullable=False, default=0)
    weight_machines = Column(Integer, nullable=False, default=0)
    knee_extensions = Column(Integer, nullable=False, default=0)
    squats = Column(Integer, nullable=False, default=0)
    yoga = Column(Integer, nullable=False, default=0)
    tai_chi = Column(Integer, nullable=False, default=0)
    gardening = Column(Integer, nullable=False, default=0)
    calf_raises = Column(Integer, nullable=False, default=0)
    leg_raises = Column(Integer, nullable=False, default=0)
    arm_stretch = Column(Integer, nullable=False, default=0)
    hip_stretch = Column(Integer, nullable=False, default=0)
    arm_stretch = Column(Integer, nullable=False, default=0)
    leg_stretch = Column(Integer, nullable=False, default=0)
    hip_stretch = Column(Integer, nullable=False, default=0)
    glute_bridges = Column(Integer, nullable=False, default=0)
    disability = Column(String(100), nullable=False, default=0)