# The file has been generated by tool- nguyennt2@rikkeisoft.com
from config.database import Base
from sqlalchemy import Column, DECIMAL, DateTime, ForeignKey, Index, String, text
from sqlalchemy.dialects.mysql import DECIMAL, INTEGER, SMALLINT, TINYINT, LONGTEXT, TEXT
from sqlalchemy.orm import relationship

from models.model_dtb_product import ModelDtbProduct
from models.model_dtb_member import ModelDtbMember


class ModelDtbProductImage(Base):
        __tablename__ = 'dtb_product_image'
 
        id = Column(INTEGER(10), primary_key=True, nullable=False) 
        product_id = Column(INTEGER(10), ForeignKey('dtb_product.id'), nullable=True)
        dtb_product = relationship('ModelDtbProduct', primaryjoin='ModelDtbProductImage.product_id == ModelDtbProduct.id', backref='dtb_product_image_list')
 
        creator_id = Column(INTEGER(10), ForeignKey('dtb_member.id'), nullable=True)
        dtb_member = relationship('ModelDtbMember', primaryjoin='ModelDtbProductImage.creator_id == ModelDtbMember.id', backref='dtb_product_image_list')
 
        file_name = Column(String(255), nullable=False) 
        sort_no = Column(SMALLINT(5), nullable=False) 
        create_date = Column(DateTime, nullable=False, comment='(DC2Type:datetimetz)') 
        discriminator_type = Column(String(255), nullable=False)