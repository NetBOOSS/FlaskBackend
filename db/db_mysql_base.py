from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.pool import QueuePool
from config import config
# 创建数据库连接引擎
engine = create_engine(config.SQLALCHEMY_DATABASE_URI,  poolclass=QueuePool,pool_size=config.SQLALCHEMY_POOL_SIZE, max_overflow=config.SQLALCHEMY_MAX_OVERFLOW)

# 创建 Session 类
Session = sessionmaker(bind=engine)

# 创建 Base 类
Base = declarative_base()