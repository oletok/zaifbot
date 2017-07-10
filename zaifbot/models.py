from zaifbot.common.database import Base
from sqlalchemy import Column, Integer, Float, String, Boolean, Text


class Trades(Base):
    __tablename__ = 'trades'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    currency_pair = Column('currency_pair', String, nullable=False)
    amount = Column('amount', Float, nullable=False)
    action = Column('action', String, nullable=False)
    entry_price = Column('entry_price', Float, nullable=False)
    entry_datetime = Column('entry_time', Integer)
    exit_price = Column('exit_price', Float, nullable=True)
    exit_datetime = Column('exit_time', Integer)
    profit = Column('profit', Float, nullable=True)
    closed = Column('closed', Boolean, nullable=False)


class OrderLogs(Base):
    __tablename__ = 'order_logs'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    order_id = Column('order_id', Integer)
    time = Column('time', Integer)
    currency_pair = Column('currency_pair', String)
    action = Column('action', String, nullable=False)
    price = Column('price', Float, nullable=False)
    amount = Column('amount', Float, nullable=False)
    limit = Column('limit', Float)
    received = Column('received', Float)
    remains = Column('remains', Float)
    comment = Column('comment', Text)


class CandleSticks(Base):
    __tablename__ = 'candle_sticks'
    time = Column('time', Integer, primary_key=True)
    currency_pair = Column('currency_pair', String, primary_key=True)
    period = Column('period', String, primary_key=True)
    open = Column('open', Float, nullable=False)
    high = Column('high', Float, nullable=False)
    low = Column('low', Float, nullable=False)
    close = Column('close', Float, nullable=False)
    average = Column('average', Float, nullable=False)
    volume = Column('volume', Float, nullable=False)
    closed = Column('closed', Boolean, nullable=False)


def init_database():
    Base.metadata.create_all()