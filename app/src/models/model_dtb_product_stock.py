# The file has been generated by tool- nguyennt2@rikkeisoft.com
from config.database import Base
from sqlalchemy import Column, DECIMAL, DateTime, ForeignKey, Index, String, text
from sqlalchemy.dialects.mysql import DECIMAL, INTEGER, SMALLINT, TINYINT, LONGTEXT, TEXT
from sqlalchemy.orm import relationship

from models.model_dtb_product_class import ModelDtbProductClass
from models.model_dtb_member import ModelDtbMember


class ModelDtbProductStock(Base):
        __tablename__ = 'dtb_product_stock'
 
        id = Column(INTEGER(10), primary_key=True, nullable=False) 
        product_class_id = Column(INTEGER(10), ForeignKey('dtb_product_class.id'), nullable=True)
        dtb_product_class = relationship('ModelDtbProductClass', primaryjoin='ModelDtbProductStock.product_class_id == ModelDtbProductClass.id', backref='dtb_product_stock_list')
 
        creator_id = Column(INTEGER(10), ForeignKey('dtb_member.id'), nullable=True)
        dtb_member = relationship('ModelDtbMember', primaryjoin='ModelDtbProductStock.creator_id == ModelDtbMember.id', backref='dtb_product_stock_list')
 
        stock = Column(DECIMAL(10, 0), nullable=True) 
        create_date = Column(DateTime, nullable=False, comment='(DC2Type:datetimetz)') 
        update_date = Column(DateTime, nullable=False, comment='(DC2Type:datetimetz)') 
        discriminator_type = Column(String(255), nullable=False)