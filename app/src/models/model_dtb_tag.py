# The file has been generated by tool- nguyennt2@rikkeisoft.com
from config.database import Base
from sqlalchemy import Column, DECIMAL, DateTime, ForeignKey, Index, String, text
from sqlalchemy.dialects.mysql import DECIMAL, INTEGER, SMALLINT, TINYINT, LONGTEXT, TEXT
from sqlalchemy.orm import relationship



class ModelDtbTag(Base):
        __tablename__ = 'dtb_tag'
 
        id = Column(INTEGER(10), primary_key=True, nullable=False) 
        name = Column(String(255), nullable=False) 
        sort_no = Column(SMALLINT(5), nullable=False) 
        discriminator_type = Column(String(255), nullable=False)