# The file has been generated by tool- nguyennt2@rikkeisoft.com
from config.database import Base
from sqlalchemy import Column, DECIMAL, DateTime, ForeignKey, Index, String, text
from sqlalchemy.dialects.mysql import DECIMAL, INTEGER, SMALLINT, TINYINT, LONGTEXT, TEXT
from sqlalchemy.orm import relationship

from models.model_dtb_order import ModelDtbOrder
from models.model_mtb_country import ModelMtbCountry
from models.model_mtb_pref import ModelMtbPref
from models.model_dtb_delivery import ModelDtbDelivery
from models.model_dtb_member import ModelDtbMember


class ModelDtbShipping(Base):
        __tablename__ = 'dtb_shipping'
 
        id = Column(INTEGER(10), primary_key=True, nullable=False) 
        order_id = Column(INTEGER(10), ForeignKey('dtb_order.id'), nullable=True)
        dtb_order = relationship('ModelDtbOrder', primaryjoin='ModelDtbShipping.order_id == ModelDtbOrder.id', backref='dtb_shipping_list')
 
        country_id = Column(SMALLINT(5), ForeignKey('mtb_country.id'), nullable=True)
        mtb_country = relationship('ModelMtbCountry', primaryjoin='ModelDtbShipping.country_id == ModelMtbCountry.id', backref='dtb_shipping_list')
 
        pref_id = Column(SMALLINT(5), ForeignKey('mtb_pref.id'), nullable=True)
        mtb_pref = relationship('ModelMtbPref', primaryjoin='ModelDtbShipping.pref_id == ModelMtbPref.id', backref='dtb_shipping_list')
 
        delivery_id = Column(INTEGER(10), ForeignKey('dtb_delivery.id'), nullable=True)
        dtb_delivery = relationship('ModelDtbDelivery', primaryjoin='ModelDtbShipping.delivery_id == ModelDtbDelivery.id', backref='dtb_shipping_list')
 
        creator_id = Column(INTEGER(10), ForeignKey('dtb_member.id'), nullable=True)
        dtb_member = relationship('ModelDtbMember', primaryjoin='ModelDtbShipping.creator_id == ModelDtbMember.id', backref='dtb_shipping_list')
 
        name01 = Column(String(255), nullable=False) 
        name02 = Column(String(255), nullable=False) 
        kana01 = Column(String(255), nullable=True) 
        kana02 = Column(String(255), nullable=True) 
        company_name = Column(String(255), nullable=True) 
        phone_number = Column(String(14), nullable=True) 
        postal_code = Column(String(8), nullable=True) 
        addr01 = Column(String(255), nullable=True) 
        addr02 = Column(String(255), nullable=True) 
        delivery_name = Column(String(255), nullable=True) 
        time_id = Column(INTEGER(10), nullable=True) 
        delivery_time = Column(String(255), nullable=True) 
        delivery_date = Column(DateTime, nullable=True, comment='(DC2Type:datetimetz)') 
        shipping_date = Column(DateTime, nullable=True, comment='(DC2Type:datetimetz)') 
        tracking_number = Column(String(255), nullable=True) 
        note = Column(String(4000), nullable=True) 
        sort_no = Column(SMALLINT(5), nullable=True) 
        create_date = Column(DateTime, nullable=False, comment='(DC2Type:datetimetz)') 
        update_date = Column(DateTime, nullable=False, comment='(DC2Type:datetimetz)') 
        mail_send_date = Column(DateTime, nullable=True, comment='(DC2Type:datetimetz)') 
        discriminator_type = Column(String(255), nullable=False)