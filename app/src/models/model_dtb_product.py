# The file has been generated by tool- nguyennt2@rikkeisoft.com
from config.database import Base
from sqlalchemy import Column, DECIMAL, DateTime, ForeignKey, Index, String, text
from sqlalchemy.dialects.mysql import DECIMAL, INTEGER, SMALLINT, TINYINT, LONGTEXT, TEXT
from sqlalchemy.orm import relationship

from models.model_dtb_member import ModelDtbMember
from models.model_mtb_product_status import ModelMtbProductStatus


class ModelDtbProduct(Base):
    __tablename__ = 'dtb_product'

    id = Column(INTEGER(10), primary_key=True, nullable=False)
    creator_id = Column(INTEGER(10), ForeignKey('dtb_member.id'), nullable=True)
    dtb_member = relationship('ModelDtbMember', primaryjoin='ModelDtbProduct.creator_id == ModelDtbMember.id',
                              backref='dtb_product_list')

    product_status_id = Column(SMALLINT(5), ForeignKey('mtb_product_status.id'), nullable=True)
    mtb_product_status = relationship('ModelMtbProductStatus',
                                      primaryjoin='ModelDtbProduct.product_status_id == ModelMtbProductStatus.id',
                                      backref='dtb_product_list')

    name = Column(String(255), nullable=False)
    note = Column(String(4000), nullable=True)
    description_list = Column(String(4000), nullable=True)
    description_detail = Column(String(4000), nullable=True)
    search_word = Column(String(4000), nullable=True)
    free_area = Column(LONGTEXT, nullable=True)
    create_date = Column(DateTime, nullable=False, comment='(DC2Type:datetimetz)')
    update_date = Column(DateTime, nullable=False, comment='(DC2Type:datetimetz)')
    discriminator_type = Column(String(255), nullable=False)
