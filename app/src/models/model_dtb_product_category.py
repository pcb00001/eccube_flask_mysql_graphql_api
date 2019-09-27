# The file has been generated by tool- nguyennt2@rikkeisoft.com
from config.database import Base
from sqlalchemy import Column, DECIMAL, DateTime, ForeignKey, Index, String, text
from sqlalchemy.dialects.mysql import DECIMAL, INTEGER, SMALLINT, TINYINT, LONGTEXT, TEXT
from sqlalchemy.orm import relationship

from models.model_dtb_product import ModelDtbProduct
from models.model_dtb_category import ModelDtbCategory


class ModelDtbProductCategory(Base):
        __tablename__ = 'dtb_product_category'
 
        product_id = Column(INTEGER(10), ForeignKey('dtb_product.id'), primary_key=True, nullable=False)
        dtb_product = relationship('ModelDtbProduct', primaryjoin='ModelDtbProductCategory.product_id == ModelDtbProduct.id', backref='dtb_product_category_list')
 
        category_id = Column(INTEGER(10), ForeignKey('dtb_category.id'), primary_key=True, nullable=False)
        dtb_category = relationship('ModelDtbCategory', primaryjoin='ModelDtbProductCategory.category_id == ModelDtbCategory.id', backref='dtb_product_category_list')
 
        discriminator_type = Column(String(255), nullable=False)