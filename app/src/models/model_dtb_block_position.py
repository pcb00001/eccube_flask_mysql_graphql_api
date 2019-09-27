# The file has been generated by tool- nguyennt2@rikkeisoft.com
from config.database import Base
from sqlalchemy import Column, DECIMAL, DateTime, ForeignKey, Index, String, text
from sqlalchemy.dialects.mysql import DECIMAL, INTEGER, SMALLINT, TINYINT, LONGTEXT, TEXT
from sqlalchemy.orm import relationship

from models.model_dtb_block import ModelDtbBlock
from models.model_dtb_layout import ModelDtbLayout


class ModelDtbBlockPosition(Base):
        __tablename__ = 'dtb_block_position'
 
        section = Column(INTEGER(10), primary_key=True, nullable=False) 
        block_id = Column(INTEGER(10), ForeignKey('dtb_block.id'), primary_key=True, nullable=False)
        dtb_block = relationship('ModelDtbBlock', primaryjoin='ModelDtbBlockPosition.block_id == ModelDtbBlock.id', backref='dtb_block_position_list')
 
        layout_id = Column(INTEGER(10), ForeignKey('dtb_layout.id'), primary_key=True, nullable=False)
        dtb_layout = relationship('ModelDtbLayout', primaryjoin='ModelDtbBlockPosition.layout_id == ModelDtbLayout.id', backref='dtb_block_position_list')
 
        block_row = Column(INTEGER(10), nullable=True) 
        discriminator_type = Column(String(255), nullable=False)