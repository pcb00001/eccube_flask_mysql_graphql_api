# The file has been generated by tool- nguyennt2@rikkeisoft.com
from config.database import Base
from sqlalchemy import Column, DECIMAL, DateTime, ForeignKey, Index, String, text
from sqlalchemy.dialects.mysql import DECIMAL, INTEGER, SMALLINT, TINYINT, LONGTEXT, TEXT
from sqlalchemy.orm import relationship

from models.model_dtb_product_class import ModelDtbProductClass
from models.model_dtb_member import ModelDtbMember
from models.model_mtb_country import ModelMtbCountry
from models.model_mtb_pref import ModelMtbPref
from models.model_dtb_product import ModelDtbProduct
from models.model_mtb_rounding_type import ModelMtbRoundingType


class ModelDtbTaxRule(Base):
        __tablename__ = 'dtb_tax_rule'
 
        id = Column(INTEGER(10), primary_key=True, nullable=False) 
        product_class_id = Column(INTEGER(10), ForeignKey('dtb_product_class.id'), nullable=True)
        dtb_product_class = relationship('ModelDtbProductClass', primaryjoin='ModelDtbTaxRule.product_class_id == ModelDtbProductClass.id', backref='dtb_tax_rule_list')
 
        creator_id = Column(INTEGER(10), ForeignKey('dtb_member.id'), nullable=True)
        dtb_member = relationship('ModelDtbMember', primaryjoin='ModelDtbTaxRule.creator_id == ModelDtbMember.id', backref='dtb_tax_rule_list')
 
        country_id = Column(SMALLINT(5), ForeignKey('mtb_country.id'), nullable=True)
        mtb_country = relationship('ModelMtbCountry', primaryjoin='ModelDtbTaxRule.country_id == ModelMtbCountry.id', backref='dtb_tax_rule_list')
 
        pref_id = Column(SMALLINT(5), ForeignKey('mtb_pref.id'), nullable=True)
        mtb_pref = relationship('ModelMtbPref', primaryjoin='ModelDtbTaxRule.pref_id == ModelMtbPref.id', backref='dtb_tax_rule_list')
 
        product_id = Column(INTEGER(10), ForeignKey('dtb_product.id'), nullable=True)
        dtb_product = relationship('ModelDtbProduct', primaryjoin='ModelDtbTaxRule.product_id == ModelDtbProduct.id', backref='dtb_tax_rule_list')
 
        rounding_type_id = Column(SMALLINT(5), ForeignKey('mtb_rounding_type.id'), nullable=True)
        mtb_rounding_type = relationship('ModelMtbRoundingType', primaryjoin='ModelDtbTaxRule.rounding_type_id == ModelMtbRoundingType.id', backref='dtb_tax_rule_list')
 
        tax_rate = Column(DECIMAL(10, 0), nullable=False, server_default=text("'8'")) 
        tax_adjust = Column(DECIMAL(10, 0), nullable=False, server_default=text("'0'")) 
        apply_date = Column(DateTime, nullable=False, comment='(DC2Type:datetimetz)') 
        create_date = Column(DateTime, nullable=False, comment='(DC2Type:datetimetz)') 
        update_date = Column(DateTime, nullable=False, comment='(DC2Type:datetimetz)') 
        discriminator_type = Column(String(255), nullable=False)