# coding: utf-8
from sqlalchemy import Column, DECIMAL, DateTime, ForeignKey, Index, String, text
from sqlalchemy.dialects.mysql import DECIMAL, INTEGER, LONGTEXT, SMALLINT, TINYINT
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class DtbDeliveryDuration(Base):
    __tablename__ = 'dtb_delivery_duration'

    id = Column(INTEGER(10), primary_key=True)
    name = Column(String(255))
    duration = Column(SMALLINT(5), nullable=False, server_default=text("'0'"))
    sort_no = Column(INTEGER(10), nullable=False)
    discriminator_type = Column(String(255), nullable=False)


class DtbOrderPdf(Base):
    __tablename__ = 'dtb_order_pdf'

    member_id = Column(INTEGER(10), primary_key=True)
    title = Column(String(255))
    message1 = Column(String(255))
    message2 = Column(String(255))
    message3 = Column(String(255))
    note1 = Column(String(255))
    note2 = Column(String(255))
    note3 = Column(String(255))
    create_date = Column(DateTime, nullable=False, comment='(DC2Type:datetimetz)')
    update_date = Column(DateTime, nullable=False, comment='(DC2Type:datetimetz)')
    visible = Column(TINYINT(1), nullable=False, server_default=text("'1'"))
    discriminator_type = Column(String(255), nullable=False)


class DtbPage(Base):
    __tablename__ = 'dtb_page'

    id = Column(INTEGER(10), primary_key=True)
    master_page_id = Column(ForeignKey('dtb_page.id'), index=True)
    page_name = Column(String(255))
    url = Column(String(255), nullable=False, index=True)
    file_name = Column(String(255))
    edit_type = Column(SMALLINT(5), nullable=False, server_default=text("'1'"))
    author = Column(String(255))
    description = Column(String(255))
    keyword = Column(String(255))
    create_date = Column(DateTime, nullable=False, comment='(DC2Type:datetimetz)')
    update_date = Column(DateTime, nullable=False, comment='(DC2Type:datetimetz)')
    meta_robots = Column(String(255))
    meta_tags = Column(String(4000))
    discriminator_type = Column(String(255), nullable=False)

    master_page = relationship('DtbPage', remote_side=[id])


class DtbPlugin(Base):
    __tablename__ = 'dtb_plugin'

    id = Column(INTEGER(10), primary_key=True)
    name = Column(String(255), nullable=False)
    code = Column(String(255), nullable=False)
    enabled = Column(TINYINT(1), nullable=False, server_default=text("'0'"))
    version = Column(String(255), nullable=False)
    source = Column(String(255), nullable=False)
    initialized = Column(TINYINT(1), nullable=False, server_default=text("'0'"))
    create_date = Column(DateTime, nullable=False, comment='(DC2Type:datetimetz)')
    update_date = Column(DateTime, nullable=False, comment='(DC2Type:datetimetz)')
    discriminator_type = Column(String(255), nullable=False)


class DtbTag(Base):
    __tablename__ = 'dtb_tag'

    id = Column(INTEGER(10), primary_key=True)
    name = Column(String(255), nullable=False)
    sort_no = Column(SMALLINT(5), nullable=False)
    discriminator_type = Column(String(255), nullable=False)


class MtbAuthority(Base):
    __tablename__ = 'mtb_authority'

    id = Column(SMALLINT(5), primary_key=True)
    name = Column(String(255), nullable=False)
    sort_no = Column(SMALLINT(5), nullable=False)
    discriminator_type = Column(String(255), nullable=False)


class MtbCountry(Base):
    __tablename__ = 'mtb_country'

    id = Column(SMALLINT(5), primary_key=True)
    name = Column(String(255), nullable=False)
    sort_no = Column(SMALLINT(5), nullable=False)
    discriminator_type = Column(String(255), nullable=False)


class MtbCsvType(Base):
    __tablename__ = 'mtb_csv_type'

    id = Column(SMALLINT(5), primary_key=True)
    name = Column(String(255), nullable=False)
    sort_no = Column(SMALLINT(5), nullable=False)
    discriminator_type = Column(String(255), nullable=False)


class MtbCustomerOrderStatu(Base):
    __tablename__ = 'mtb_customer_order_status'

    id = Column(SMALLINT(5), primary_key=True)
    name = Column(String(255), nullable=False)
    sort_no = Column(SMALLINT(5), nullable=False)
    discriminator_type = Column(String(255), nullable=False)


class MtbCustomerStatu(Base):
    __tablename__ = 'mtb_customer_status'

    id = Column(SMALLINT(5), primary_key=True)
    name = Column(String(255), nullable=False)
    sort_no = Column(SMALLINT(5), nullable=False)
    discriminator_type = Column(String(255), nullable=False)


class MtbDeviceType(Base):
    __tablename__ = 'mtb_device_type'

    id = Column(SMALLINT(5), primary_key=True)
    name = Column(String(255), nullable=False)
    sort_no = Column(SMALLINT(5), nullable=False)
    discriminator_type = Column(String(255), nullable=False)


class MtbJob(Base):
    __tablename__ = 'mtb_job'

    id = Column(SMALLINT(5), primary_key=True)
    name = Column(String(255), nullable=False)
    sort_no = Column(SMALLINT(5), nullable=False)
    discriminator_type = Column(String(255), nullable=False)


class MtbOrderItemType(Base):
    __tablename__ = 'mtb_order_item_type'

    id = Column(SMALLINT(5), primary_key=True)
    name = Column(String(255), nullable=False)
    sort_no = Column(SMALLINT(5), nullable=False)
    discriminator_type = Column(String(255), nullable=False)


class MtbOrderStatu(Base):
    __tablename__ = 'mtb_order_status'

    id = Column(SMALLINT(5), primary_key=True)
    display_order_count = Column(TINYINT(1), nullable=False, server_default=text("'0'"))
    name = Column(String(255), nullable=False)
    sort_no = Column(SMALLINT(5), nullable=False)
    discriminator_type = Column(String(255), nullable=False)


class MtbOrderStatusColor(Base):
    __tablename__ = 'mtb_order_status_color'

    id = Column(SMALLINT(5), primary_key=True)
    name = Column(String(255), nullable=False)
    sort_no = Column(SMALLINT(5), nullable=False)
    discriminator_type = Column(String(255), nullable=False)


class MtbPageMax(Base):
    __tablename__ = 'mtb_page_max'

    id = Column(SMALLINT(5), primary_key=True)
    name = Column(String(255), nullable=False)
    sort_no = Column(SMALLINT(5), nullable=False)
    discriminator_type = Column(String(255), nullable=False)


class MtbPref(Base):
    __tablename__ = 'mtb_pref'

    id = Column(SMALLINT(5), primary_key=True)
    name = Column(String(255), nullable=False)
    sort_no = Column(SMALLINT(5), nullable=False)
    discriminator_type = Column(String(255), nullable=False)


class MtbProductListMax(Base):
    __tablename__ = 'mtb_product_list_max'

    id = Column(SMALLINT(5), primary_key=True)
    name = Column(String(255), nullable=False)
    sort_no = Column(SMALLINT(5), nullable=False)
    discriminator_type = Column(String(255), nullable=False)


class MtbProductListOrderBy(Base):
    __tablename__ = 'mtb_product_list_order_by'

    id = Column(SMALLINT(5), primary_key=True)
    name = Column(String(255), nullable=False)
    sort_no = Column(SMALLINT(5), nullable=False)
    discriminator_type = Column(String(255), nullable=False)


class MtbProductStatu(Base):
    __tablename__ = 'mtb_product_status'

    id = Column(SMALLINT(5), primary_key=True)
    name = Column(String(255), nullable=False)
    sort_no = Column(SMALLINT(5), nullable=False)
    discriminator_type = Column(String(255), nullable=False)


class MtbRoundingType(Base):
    __tablename__ = 'mtb_rounding_type'

    id = Column(SMALLINT(5), primary_key=True)
    name = Column(String(255), nullable=False)
    sort_no = Column(SMALLINT(5), nullable=False)
    discriminator_type = Column(String(255), nullable=False)


class MtbSaleType(Base):
    __tablename__ = 'mtb_sale_type'

    id = Column(SMALLINT(5), primary_key=True)
    name = Column(String(255), nullable=False)
    sort_no = Column(SMALLINT(5), nullable=False)
    discriminator_type = Column(String(255), nullable=False)


class MtbSex(Base):
    __tablename__ = 'mtb_sex'

    id = Column(SMALLINT(5), primary_key=True)
    name = Column(String(255), nullable=False)
    sort_no = Column(SMALLINT(5), nullable=False)
    discriminator_type = Column(String(255), nullable=False)


class MtbTaxDisplayType(Base):
    __tablename__ = 'mtb_tax_display_type'

    id = Column(SMALLINT(5), primary_key=True)
    name = Column(String(255), nullable=False)
    sort_no = Column(SMALLINT(5), nullable=False)
    discriminator_type = Column(String(255), nullable=False)


class MtbTaxType(Base):
    __tablename__ = 'mtb_tax_type'

    id = Column(SMALLINT(5), primary_key=True)
    name = Column(String(255), nullable=False)
    sort_no = Column(SMALLINT(5), nullable=False)
    discriminator_type = Column(String(255), nullable=False)


class MtbWork(Base):
    __tablename__ = 'mtb_work'

    id = Column(SMALLINT(5), primary_key=True)
    name = Column(String(255), nullable=False)
    sort_no = Column(SMALLINT(5), nullable=False)
    discriminator_type = Column(String(255), nullable=False)


class DtbBaseInfo(Base):
    __tablename__ = 'dtb_base_info'

    id = Column(INTEGER(10), primary_key=True)
    country_id = Column(ForeignKey('mtb_country.id'), index=True)
    pref_id = Column(ForeignKey('mtb_pref.id'), index=True)
    company_name = Column(String(255))
    company_kana = Column(String(255))
    postal_code = Column(String(8))
    addr01 = Column(String(255))
    addr02 = Column(String(255))
    phone_number = Column(String(14))
    business_hour = Column(String(255))
    email01 = Column(String(255))
    email02 = Column(String(255))
    email03 = Column(String(255))
    email04 = Column(String(255))
    shop_name = Column(String(255))
    shop_kana = Column(String(255))
    shop_name_eng = Column(String(255))
    update_date = Column(DateTime, nullable=False, comment='(DC2Type:datetimetz)')
    good_traded = Column(String(4000))
    message = Column(String(4000))
    delivery_free_amount = Column(DECIMAL(12, 2))
    delivery_free_quantity = Column(INTEGER(10))
    option_mypage_order_status_display = Column(TINYINT(1), nullable=False, server_default=text("'1'"))
    option_nostock_hidden = Column(TINYINT(1), nullable=False, server_default=text("'0'"))
    option_favorite_product = Column(TINYINT(1), nullable=False, server_default=text("'1'"))
    option_product_delivery_fee = Column(TINYINT(1), nullable=False, server_default=text("'0'"))
    option_product_tax_rule = Column(TINYINT(1), nullable=False, server_default=text("'0'"))
    option_customer_activate = Column(TINYINT(1), nullable=False, server_default=text("'1'"))
    option_remember_me = Column(TINYINT(1), nullable=False, server_default=text("'1'"))
    authentication_key = Column(String(255))
    php_path = Column(String(255))
    option_point = Column(TINYINT(1), nullable=False, server_default=text("'1'"))
    basic_point_rate = Column(DECIMAL(10, 0), server_default=text("'1'"))
    point_conversion_rate = Column(DECIMAL(10, 0), server_default=text("'1'"))
    discriminator_type = Column(String(255), nullable=False)

    country = relationship('MtbCountry')
    pref = relationship('MtbPref')


class DtbBlock(Base):
    __tablename__ = 'dtb_block'
    __table_args__ = (
        Index('device_type_id', 'device_type_id', 'file_name', unique=True),
    )

    id = Column(INTEGER(10), primary_key=True)
    device_type_id = Column(ForeignKey('mtb_device_type.id'), index=True)
    block_name = Column(String(255))
    file_name = Column(String(255), nullable=False)
    use_controller = Column(TINYINT(1), nullable=False, server_default=text("'0'"))
    deletable = Column(TINYINT(1), nullable=False, server_default=text("'1'"))
    create_date = Column(DateTime, nullable=False, comment='(DC2Type:datetimetz)')
    update_date = Column(DateTime, nullable=False, comment='(DC2Type:datetimetz)')
    discriminator_type = Column(String(255), nullable=False)

    device_type = relationship('MtbDeviceType')


class DtbCustomer(Base):
    __tablename__ = 'dtb_customer'

    id = Column(INTEGER(10), primary_key=True)
    customer_status_id = Column(ForeignKey('mtb_customer_status.id'), index=True)
    sex_id = Column(ForeignKey('mtb_sex.id'), index=True)
    job_id = Column(ForeignKey('mtb_job.id'), index=True)
    country_id = Column(ForeignKey('mtb_country.id'), index=True)
    pref_id = Column(ForeignKey('mtb_pref.id'), index=True)
    name01 = Column(String(255), nullable=False)
    name02 = Column(String(255), nullable=False)
    kana01 = Column(String(255))
    kana02 = Column(String(255))
    company_name = Column(String(255))
    postal_code = Column(String(8))
    addr01 = Column(String(255))
    addr02 = Column(String(255))
    email = Column(String(255), nullable=False, index=True)
    phone_number = Column(String(14))
    birth = Column(DateTime, comment='(DC2Type:datetimetz)')
    password = Column(String(255), nullable=False)
    salt = Column(String(255))
    secret_key = Column(String(255), nullable=False, unique=True)
    first_buy_date = Column(DateTime, comment='(DC2Type:datetimetz)')
    last_buy_date = Column(DateTime, index=True, comment='(DC2Type:datetimetz)')
    buy_times = Column(DECIMAL(10, 0), index=True, server_default=text("'0'"))
    buy_total = Column(DECIMAL(12, 2), index=True, server_default=text("'0.00'"))
    note = Column(String(4000))
    reset_key = Column(String(255))
    reset_expire = Column(DateTime, comment='(DC2Type:datetimetz)')
    point = Column(DECIMAL(12, 0), nullable=False, server_default=text("'0'"))
    create_date = Column(DateTime, nullable=False, index=True, comment='(DC2Type:datetimetz)')
    update_date = Column(DateTime, nullable=False, index=True, comment='(DC2Type:datetimetz)')
    discriminator_type = Column(String(255), nullable=False)

    country = relationship('MtbCountry')
    customer_status = relationship('MtbCustomerStatu')
    job = relationship('MtbJob')
    pref = relationship('MtbPref')
    sex = relationship('MtbSex')


class DtbLayout(Base):
    __tablename__ = 'dtb_layout'

    id = Column(INTEGER(10), primary_key=True)
    device_type_id = Column(ForeignKey('mtb_device_type.id'), index=True)
    layout_name = Column(String(255))
    create_date = Column(DateTime, nullable=False, comment='(DC2Type:datetimetz)')
    update_date = Column(DateTime, nullable=False, comment='(DC2Type:datetimetz)')
    discriminator_type = Column(String(255), nullable=False)

    device_type = relationship('MtbDeviceType')


class DtbMember(Base):
    __tablename__ = 'dtb_member'

    id = Column(INTEGER(10), primary_key=True)
    work_id = Column(ForeignKey('mtb_work.id'), index=True)
    authority_id = Column(ForeignKey('mtb_authority.id'), index=True)
    creator_id = Column(ForeignKey('dtb_member.id'), index=True)
    name = Column(String(255))
    department = Column(String(255))
    login_id = Column(String(255), nullable=False)
    password = Column(String(255), nullable=False)
    salt = Column(String(255))
    sort_no = Column(SMALLINT(5), nullable=False)
    create_date = Column(DateTime, nullable=False, comment='(DC2Type:datetimetz)')
    update_date = Column(DateTime, nullable=False, comment='(DC2Type:datetimetz)')
    login_date = Column(DateTime, comment='(DC2Type:datetimetz)')
    discriminator_type = Column(String(255), nullable=False)

    authority = relationship('MtbAuthority')
    creator = relationship('DtbMember', remote_side=[id])
    work = relationship('MtbWork')


class DtbTemplate(Base):
    __tablename__ = 'dtb_template'

    id = Column(INTEGER(10), primary_key=True)
    device_type_id = Column(ForeignKey('mtb_device_type.id'), index=True)
    template_code = Column(String(255), nullable=False)
    template_name = Column(String(255), nullable=False)
    create_date = Column(DateTime, nullable=False, comment='(DC2Type:datetimetz)')
    update_date = Column(DateTime, nullable=False, comment='(DC2Type:datetimetz)')
    discriminator_type = Column(String(255), nullable=False)

    device_type = relationship('MtbDeviceType')


class DtbAuthorityRole(Base):
    __tablename__ = 'dtb_authority_role'

    id = Column(INTEGER(10), primary_key=True)
    authority_id = Column(ForeignKey('mtb_authority.id'), index=True)
    creator_id = Column(ForeignKey('dtb_member.id'), index=True)
    deny_url = Column(String(4000), nullable=False)
    create_date = Column(DateTime, nullable=False, comment='(DC2Type:datetimetz)')
    update_date = Column(DateTime, nullable=False, comment='(DC2Type:datetimetz)')
    discriminator_type = Column(String(255), nullable=False)

    authority = relationship('MtbAuthority')
    creator = relationship('DtbMember')


class DtbBlockPosition(Base):
    __tablename__ = 'dtb_block_position'

    section = Column(INTEGER(10), primary_key=True, nullable=False)
    block_id = Column(ForeignKey('dtb_block.id'), primary_key=True, nullable=False, index=True)
    layout_id = Column(ForeignKey('dtb_layout.id'), primary_key=True, nullable=False, index=True)
    block_row = Column(INTEGER(10))
    discriminator_type = Column(String(255), nullable=False)

    block = relationship('DtbBlock')
    layout = relationship('DtbLayout')


class DtbCart(Base):
    __tablename__ = 'dtb_cart'

    id = Column(INTEGER(10), primary_key=True)
    customer_id = Column(ForeignKey('dtb_customer.id'), index=True)
    cart_key = Column(String(255))
    pre_order_id = Column(String(255), unique=True)
    total_price = Column(DECIMAL(12, 2), nullable=False, server_default=text("'0.00'"))
    delivery_fee_total = Column(DECIMAL(12, 2), nullable=False, server_default=text("'0.00'"))
    sort_no = Column(SMALLINT(5))
    create_date = Column(DateTime, nullable=False, comment='(DC2Type:datetimetz)')
    update_date = Column(DateTime, nullable=False, index=True, comment='(DC2Type:datetimetz)')
    add_point = Column(DECIMAL(12, 0), nullable=False, server_default=text("'0'"))
    use_point = Column(DECIMAL(12, 0), nullable=False, server_default=text("'0'"))
    discriminator_type = Column(String(255), nullable=False)

    customer = relationship('DtbCustomer')


class DtbCategory(Base):
    __tablename__ = 'dtb_category'

    id = Column(INTEGER(10), primary_key=True)
    parent_category_id = Column(ForeignKey('dtb_category.id'), index=True)
    creator_id = Column(ForeignKey('dtb_member.id'), index=True)
    category_name = Column(String(255), nullable=False)
    hierarchy = Column(INTEGER(10), nullable=False)
    sort_no = Column(INTEGER(11), nullable=False)
    create_date = Column(DateTime, nullable=False, comment='(DC2Type:datetimetz)')
    update_date = Column(DateTime, nullable=False, comment='(DC2Type:datetimetz)')
    discriminator_type = Column(String(255), nullable=False)

    creator = relationship('DtbMember')
    parent_category = relationship('DtbCategory', remote_side=[id])


class DtbClassName(Base):
    __tablename__ = 'dtb_class_name'

    id = Column(INTEGER(10), primary_key=True)
    creator_id = Column(ForeignKey('dtb_member.id'), index=True)
    backend_name = Column(String(255))
    name = Column(String(255), nullable=False)
    sort_no = Column(INTEGER(10), nullable=False)
    create_date = Column(DateTime, nullable=False, comment='(DC2Type:datetimetz)')
    update_date = Column(DateTime, nullable=False, comment='(DC2Type:datetimetz)')
    discriminator_type = Column(String(255), nullable=False)

    creator = relationship('DtbMember')


class DtbCsv(Base):
    __tablename__ = 'dtb_csv'

    id = Column(INTEGER(10), primary_key=True)
    csv_type_id = Column(ForeignKey('mtb_csv_type.id'), index=True)
    creator_id = Column(ForeignKey('dtb_member.id'), index=True)
    entity_name = Column(String(255), nullable=False)
    field_name = Column(String(255), nullable=False)
    reference_field_name = Column(String(255))
    disp_name = Column(String(255), nullable=False)
    sort_no = Column(SMALLINT(5), nullable=False)
    enabled = Column(TINYINT(1), nullable=False, server_default=text("'1'"))
    create_date = Column(DateTime, nullable=False, comment='(DC2Type:datetimetz)')
    update_date = Column(DateTime, nullable=False, comment='(DC2Type:datetimetz)')
    discriminator_type = Column(String(255), nullable=False)

    creator = relationship('DtbMember')
    csv_type = relationship('MtbCsvType')


class DtbCustomerAddres(Base):
    __tablename__ = 'dtb_customer_address'

    id = Column(INTEGER(10), primary_key=True)
    customer_id = Column(ForeignKey('dtb_customer.id'), index=True)
    country_id = Column(ForeignKey('mtb_country.id'), index=True)
    pref_id = Column(ForeignKey('mtb_pref.id'), index=True)
    name01 = Column(String(255), nullable=False)
    name02 = Column(String(255), nullable=False)
    kana01 = Column(String(255))
    kana02 = Column(String(255))
    company_name = Column(String(255))
    postal_code = Column(String(8))
    addr01 = Column(String(255))
    addr02 = Column(String(255))
    phone_number = Column(String(14))
    create_date = Column(DateTime, nullable=False, comment='(DC2Type:datetimetz)')
    update_date = Column(DateTime, nullable=False, comment='(DC2Type:datetimetz)')
    discriminator_type = Column(String(255), nullable=False)

    country = relationship('MtbCountry')
    customer = relationship('DtbCustomer')
    pref = relationship('MtbPref')


class DtbDelivery(Base):
    __tablename__ = 'dtb_delivery'

    id = Column(INTEGER(10), primary_key=True)
    creator_id = Column(ForeignKey('dtb_member.id'), index=True)
    sale_type_id = Column(ForeignKey('mtb_sale_type.id'), index=True)
    name = Column(String(255))
    service_name = Column(String(255))
    description = Column(String(4000))
    confirm_url = Column(String(4000))
    sort_no = Column(INTEGER(10))
    visible = Column(TINYINT(1), nullable=False, server_default=text("'1'"))
    create_date = Column(DateTime, nullable=False, comment='(DC2Type:datetimetz)')
    update_date = Column(DateTime, nullable=False, comment='(DC2Type:datetimetz)')
    discriminator_type = Column(String(255), nullable=False)

    creator = relationship('DtbMember')
    sale_type = relationship('MtbSaleType')


class DtbMailTemplate(Base):
    __tablename__ = 'dtb_mail_template'

    id = Column(INTEGER(10), primary_key=True)
    creator_id = Column(ForeignKey('dtb_member.id'), index=True)
    name = Column(String(255))
    file_name = Column(String(255))
    mail_subject = Column(String(255))
    create_date = Column(DateTime, nullable=False, comment='(DC2Type:datetimetz)')
    update_date = Column(DateTime, nullable=False, comment='(DC2Type:datetimetz)')
    discriminator_type = Column(String(255), nullable=False)

    creator = relationship('DtbMember')


class DtbNew(Base):
    __tablename__ = 'dtb_news'

    id = Column(INTEGER(10), primary_key=True)
    creator_id = Column(ForeignKey('dtb_member.id'), index=True)
    publish_date = Column(DateTime, comment='(DC2Type:datetimetz)')
    title = Column(String(255), nullable=False)
    description = Column(LONGTEXT)
    url = Column(String(4000))
    link_method = Column(TINYINT(1), nullable=False, server_default=text("'0'"))
    create_date = Column(DateTime, nullable=False, comment='(DC2Type:datetimetz)')
    update_date = Column(DateTime, nullable=False, comment='(DC2Type:datetimetz)')
    visible = Column(TINYINT(1), nullable=False, server_default=text("'1'"))
    discriminator_type = Column(String(255), nullable=False)

    creator = relationship('DtbMember')


class DtbPageLayout(Base):
    __tablename__ = 'dtb_page_layout'

    page_id = Column(ForeignKey('dtb_page.id'), primary_key=True, nullable=False, index=True)
    layout_id = Column(ForeignKey('dtb_layout.id'), primary_key=True, nullable=False, index=True)
    sort_no = Column(SMALLINT(5), nullable=False)
    discriminator_type = Column(String(255), nullable=False)

    layout = relationship('DtbLayout')
    page = relationship('DtbPage')


class DtbPayment(Base):
    __tablename__ = 'dtb_payment'

    id = Column(INTEGER(10), primary_key=True)
    creator_id = Column(ForeignKey('dtb_member.id'), index=True)
    payment_method = Column(String(255))
    charge = Column(DECIMAL(12, 2), server_default=text("'0.00'"))
    rule_max = Column(DECIMAL(12, 2))
    sort_no = Column(SMALLINT(5))
    fixed = Column(TINYINT(1), nullable=False, server_default=text("'1'"))
    payment_image = Column(String(255))
    rule_min = Column(DECIMAL(12, 2))
    method_class = Column(String(255))
    visible = Column(TINYINT(1), nullable=False, server_default=text("'1'"))
    create_date = Column(DateTime, nullable=False, comment='(DC2Type:datetimetz)')
    update_date = Column(DateTime, nullable=False, comment='(DC2Type:datetimetz)')
    discriminator_type = Column(String(255), nullable=False)

    creator = relationship('DtbMember')


class DtbProduct(Base):
    __tablename__ = 'dtb_product'

    id = Column(INTEGER(10), primary_key=True)
    creator_id = Column(ForeignKey('dtb_member.id'), index=True)
    product_status_id = Column(ForeignKey('mtb_product_status.id'), index=True)
    name = Column(String(255), nullable=False)
    note = Column(String(4000))
    description_list = Column(String(4000))
    description_detail = Column(String(4000))
    search_word = Column(String(4000))
    free_area = Column(LONGTEXT)
    create_date = Column(DateTime, nullable=False, comment='(DC2Type:datetimetz)')
    update_date = Column(DateTime, nullable=False, comment='(DC2Type:datetimetz)')
    discriminator_type = Column(String(255), nullable=False)

    creator = relationship('DtbMember')
    product_status = relationship('MtbProductStatu')


class DtbClassCategory(Base):
    __tablename__ = 'dtb_class_category'

    id = Column(INTEGER(10), primary_key=True)
    class_name_id = Column(ForeignKey('dtb_class_name.id'), index=True)
    creator_id = Column(ForeignKey('dtb_member.id'), index=True)
    backend_name = Column(String(255))
    name = Column(String(255), nullable=False)
    sort_no = Column(INTEGER(10), nullable=False)
    visible = Column(TINYINT(1), nullable=False, server_default=text("'1'"))
    create_date = Column(DateTime, nullable=False, comment='(DC2Type:datetimetz)')
    update_date = Column(DateTime, nullable=False, comment='(DC2Type:datetimetz)')
    discriminator_type = Column(String(255), nullable=False)

    class_name = relationship('DtbClassName')
    creator = relationship('DtbMember')


class DtbCustomerFavoriteProduct(Base):
    __tablename__ = 'dtb_customer_favorite_product'

    id = Column(INTEGER(10), primary_key=True)
    customer_id = Column(ForeignKey('dtb_customer.id'), index=True)
    product_id = Column(ForeignKey('dtb_product.id'), index=True)
    create_date = Column(DateTime, nullable=False, comment='(DC2Type:datetimetz)')
    update_date = Column(DateTime, nullable=False, comment='(DC2Type:datetimetz)')
    discriminator_type = Column(String(255), nullable=False)

    customer = relationship('DtbCustomer')
    product = relationship('DtbProduct')


class DtbDeliveryFee(Base):
    __tablename__ = 'dtb_delivery_fee'

    id = Column(INTEGER(10), primary_key=True)
    delivery_id = Column(ForeignKey('dtb_delivery.id'), index=True)
    pref_id = Column(ForeignKey('mtb_pref.id'), index=True)
    fee = Column(DECIMAL(12, 2), nullable=False)
    discriminator_type = Column(String(255), nullable=False)

    delivery = relationship('DtbDelivery')
    pref = relationship('MtbPref')


class DtbDeliveryTime(Base):
    __tablename__ = 'dtb_delivery_time'

    id = Column(INTEGER(10), primary_key=True)
    delivery_id = Column(ForeignKey('dtb_delivery.id'), index=True)
    delivery_time = Column(String(255), nullable=False)
    sort_no = Column(SMALLINT(5), nullable=False)
    visible = Column(TINYINT(1), nullable=False, server_default=text("'1'"))
    create_date = Column(DateTime, nullable=False, comment='(DC2Type:datetimetz)')
    update_date = Column(DateTime, nullable=False, comment='(DC2Type:datetimetz)')
    discriminator_type = Column(String(255), nullable=False)

    delivery = relationship('DtbDelivery')


class DtbOrder(Base):
    __tablename__ = 'dtb_order'

    id = Column(INTEGER(10), primary_key=True)
    customer_id = Column(ForeignKey('dtb_customer.id'), index=True)
    country_id = Column(ForeignKey('mtb_country.id'), index=True)
    pref_id = Column(ForeignKey('mtb_pref.id'), index=True)
    sex_id = Column(ForeignKey('mtb_sex.id'), index=True)
    job_id = Column(ForeignKey('mtb_job.id'), index=True)
    payment_id = Column(ForeignKey('dtb_payment.id'), index=True)
    device_type_id = Column(ForeignKey('mtb_device_type.id'), index=True)
    pre_order_id = Column(String(255), unique=True)
    order_no = Column(String(255), index=True)
    message = Column(String(4000))
    name01 = Column(String(255), nullable=False)
    name02 = Column(String(255), nullable=False)
    kana01 = Column(String(255))
    kana02 = Column(String(255))
    company_name = Column(String(255))
    email = Column(String(255), index=True)
    phone_number = Column(String(14))
    postal_code = Column(String(8))
    addr01 = Column(String(255))
    addr02 = Column(String(255))
    birth = Column(DateTime, comment='(DC2Type:datetimetz)')
    subtotal = Column(DECIMAL(12, 2), nullable=False, server_default=text("'0.00'"))
    discount = Column(DECIMAL(12, 2), nullable=False, server_default=text("'0.00'"))
    delivery_fee_total = Column(DECIMAL(12, 2), nullable=False, server_default=text("'0.00'"))
    charge = Column(DECIMAL(12, 2), nullable=False, server_default=text("'0.00'"))
    tax = Column(DECIMAL(12, 2), nullable=False, server_default=text("'0.00'"))
    total = Column(DECIMAL(12, 2), nullable=False, server_default=text("'0.00'"))
    payment_total = Column(DECIMAL(12, 2), nullable=False, server_default=text("'0.00'"))
    payment_method = Column(String(255))
    note = Column(String(4000))
    create_date = Column(DateTime, nullable=False, comment='(DC2Type:datetimetz)')
    update_date = Column(DateTime, nullable=False, index=True, comment='(DC2Type:datetimetz)')
    order_date = Column(DateTime, index=True, comment='(DC2Type:datetimetz)')
    payment_date = Column(DateTime, index=True, comment='(DC2Type:datetimetz)')
    currency_code = Column(String(255))
    complete_message = Column(LONGTEXT)
    complete_mail_message = Column(LONGTEXT)
    add_point = Column(DECIMAL(12, 0), nullable=False, server_default=text("'0'"))
    use_point = Column(DECIMAL(12, 0), nullable=False, server_default=text("'0'"))
    order_status_id = Column(SMALLINT(5), index=True)
    discriminator_type = Column(String(255), nullable=False)

    country = relationship('MtbCountry')
    customer = relationship('DtbCustomer')
    device_type = relationship('MtbDeviceType')
    job = relationship('MtbJob')
    payment = relationship('DtbPayment')
    pref = relationship('MtbPref')
    sex = relationship('MtbSex')


class DtbPaymentOption(Base):
    __tablename__ = 'dtb_payment_option'

    delivery_id = Column(ForeignKey('dtb_delivery.id'), primary_key=True, nullable=False, index=True)
    payment_id = Column(ForeignKey('dtb_payment.id'), primary_key=True, nullable=False, index=True)
    discriminator_type = Column(String(255), nullable=False)

    delivery = relationship('DtbDelivery')
    payment = relationship('DtbPayment')


class DtbProductCategory(Base):
    __tablename__ = 'dtb_product_category'

    product_id = Column(ForeignKey('dtb_product.id'), primary_key=True, nullable=False, index=True)
    category_id = Column(ForeignKey('dtb_category.id'), primary_key=True, nullable=False, index=True)
    discriminator_type = Column(String(255), nullable=False)

    category = relationship('DtbCategory')
    product = relationship('DtbProduct')


class DtbProductImage(Base):
    __tablename__ = 'dtb_product_image'

    id = Column(INTEGER(10), primary_key=True)
    product_id = Column(ForeignKey('dtb_product.id'), index=True)
    creator_id = Column(ForeignKey('dtb_member.id'), index=True)
    file_name = Column(String(255), nullable=False)
    sort_no = Column(SMALLINT(5), nullable=False)
    create_date = Column(DateTime, nullable=False, comment='(DC2Type:datetimetz)')
    discriminator_type = Column(String(255), nullable=False)

    creator = relationship('DtbMember')
    product = relationship('DtbProduct')


class DtbProductTag(Base):
    __tablename__ = 'dtb_product_tag'

    id = Column(INTEGER(10), primary_key=True)
    product_id = Column(ForeignKey('dtb_product.id'), index=True)
    tag_id = Column(ForeignKey('dtb_tag.id'), index=True)
    creator_id = Column(ForeignKey('dtb_member.id'), index=True)
    create_date = Column(DateTime, nullable=False, comment='(DC2Type:datetimetz)')
    discriminator_type = Column(String(255), nullable=False)

    creator = relationship('DtbMember')
    product = relationship('DtbProduct')
    tag = relationship('DtbTag')


class DtbMailHistory(Base):
    __tablename__ = 'dtb_mail_history'

    id = Column(INTEGER(10), primary_key=True)
    order_id = Column(ForeignKey('dtb_order.id'), index=True)
    creator_id = Column(ForeignKey('dtb_member.id'), index=True)
    send_date = Column(DateTime, comment='(DC2Type:datetimetz)')
    mail_subject = Column(String(255))
    mail_body = Column(LONGTEXT)
    mail_html_body = Column(LONGTEXT)
    discriminator_type = Column(String(255), nullable=False)

    creator = relationship('DtbMember')
    order = relationship('DtbOrder')


class DtbProductClas(Base):
    __tablename__ = 'dtb_product_class'
    __table_args__ = (
        Index('dtb_product_class_stock_stock_unlimited_idx', 'stock', 'stock_unlimited'),
    )

    id = Column(INTEGER(10), primary_key=True)
    product_id = Column(ForeignKey('dtb_product.id'), index=True)
    sale_type_id = Column(ForeignKey('mtb_sale_type.id'), index=True)
    class_category_id1 = Column(ForeignKey('dtb_class_category.id'), index=True)
    class_category_id2 = Column(ForeignKey('dtb_class_category.id'), index=True)
    delivery_duration_id = Column(ForeignKey('dtb_delivery_duration.id'), index=True)
    creator_id = Column(ForeignKey('dtb_member.id'), index=True)
    product_code = Column(String(255))
    stock = Column(DECIMAL(10, 0))
    stock_unlimited = Column(TINYINT(1), nullable=False, server_default=text("'0'"))
    sale_limit = Column(DECIMAL(10, 0))
    price01 = Column(DECIMAL(12, 2))
    price02 = Column(DECIMAL(12, 2), nullable=False, index=True)
    delivery_fee = Column(DECIMAL(12, 2))
    visible = Column(TINYINT(1), nullable=False, server_default=text("'1'"))
    create_date = Column(DateTime, nullable=False, comment='(DC2Type:datetimetz)')
    update_date = Column(DateTime, nullable=False, comment='(DC2Type:datetimetz)')
    currency_code = Column(String(255))
    point_rate = Column(DECIMAL(10, 0))
    discriminator_type = Column(String(255), nullable=False)

    dtb_class_category = relationship('DtbClassCategory', primaryjoin='DtbProductClas.class_category_id1 == DtbClassCategory.id')
    dtb_class_category1 = relationship('DtbClassCategory', primaryjoin='DtbProductClas.class_category_id2 == DtbClassCategory.id')
    creator = relationship('DtbMember')
    delivery_duration = relationship('DtbDeliveryDuration')
    product = relationship('DtbProduct')
    sale_type = relationship('MtbSaleType')


class DtbShipping(Base):
    __tablename__ = 'dtb_shipping'

    id = Column(INTEGER(10), primary_key=True)
    order_id = Column(ForeignKey('dtb_order.id'), index=True)
    country_id = Column(ForeignKey('mtb_country.id'), index=True)
    pref_id = Column(ForeignKey('mtb_pref.id'), index=True)
    delivery_id = Column(ForeignKey('dtb_delivery.id'), index=True)
    creator_id = Column(ForeignKey('dtb_member.id'), index=True)
    name01 = Column(String(255), nullable=False)
    name02 = Column(String(255), nullable=False)
    kana01 = Column(String(255))
    kana02 = Column(String(255))
    company_name = Column(String(255))
    phone_number = Column(String(14))
    postal_code = Column(String(8))
    addr01 = Column(String(255))
    addr02 = Column(String(255))
    delivery_name = Column(String(255))
    time_id = Column(INTEGER(10))
    delivery_time = Column(String(255))
    delivery_date = Column(DateTime, comment='(DC2Type:datetimetz)')
    shipping_date = Column(DateTime, comment='(DC2Type:datetimetz)')
    tracking_number = Column(String(255))
    note = Column(String(4000))
    sort_no = Column(SMALLINT(5))
    create_date = Column(DateTime, nullable=False, comment='(DC2Type:datetimetz)')
    update_date = Column(DateTime, nullable=False, comment='(DC2Type:datetimetz)')
    mail_send_date = Column(DateTime, comment='(DC2Type:datetimetz)')
    discriminator_type = Column(String(255), nullable=False)

    country = relationship('MtbCountry')
    creator = relationship('DtbMember')
    delivery = relationship('DtbDelivery')
    order = relationship('DtbOrder')
    pref = relationship('MtbPref')


class DtbCartItem(Base):
    __tablename__ = 'dtb_cart_item'

    id = Column(INTEGER(10), primary_key=True)
    product_class_id = Column(ForeignKey('dtb_product_class.id'), index=True)
    cart_id = Column(ForeignKey('dtb_cart.id', ondelete='CASCADE'), index=True)
    price = Column(DECIMAL(12, 2), nullable=False, server_default=text("'0.00'"))
    quantity = Column(DECIMAL(10, 0), nullable=False, server_default=text("'0'"))
    point_rate = Column(DECIMAL(10, 0))
    discriminator_type = Column(String(255), nullable=False)

    cart = relationship('DtbCart')
    product_class = relationship('DtbProductClas')


class DtbOrderItem(Base):
    __tablename__ = 'dtb_order_item'

    id = Column(INTEGER(10), primary_key=True)
    order_id = Column(ForeignKey('dtb_order.id'), index=True)
    product_id = Column(ForeignKey('dtb_product.id'), index=True)
    product_class_id = Column(ForeignKey('dtb_product_class.id'), index=True)
    shipping_id = Column(ForeignKey('dtb_shipping.id'), index=True)
    rounding_type_id = Column(ForeignKey('mtb_rounding_type.id'), index=True)
    tax_type_id = Column(ForeignKey('mtb_tax_type.id'), index=True)
    tax_display_type_id = Column(ForeignKey('mtb_tax_display_type.id'), index=True)
    order_item_type_id = Column(ForeignKey('mtb_order_item_type.id'), index=True)
    product_name = Column(String(255), nullable=False)
    product_code = Column(String(255))
    class_name1 = Column(String(255))
    class_name2 = Column(String(255))
    class_category_name1 = Column(String(255))
    class_category_name2 = Column(String(255))
    price = Column(DECIMAL(12, 2), nullable=False, server_default=text("'0.00'"))
    quantity = Column(DECIMAL(10, 0), nullable=False, server_default=text("'0'"))
    tax = Column(DECIMAL(10, 0), nullable=False, server_default=text("'0'"))
    tax_rate = Column(DECIMAL(10, 0), nullable=False, server_default=text("'0'"))
    tax_rule_id = Column(SMALLINT(5))
    currency_code = Column(String(255))
    processor_name = Column(String(255))
    point_rate = Column(DECIMAL(10, 0))
    discriminator_type = Column(String(255), nullable=False)

    order = relationship('DtbOrder')
    order_item_type = relationship('MtbOrderItemType')
    product_class = relationship('DtbProductClas')
    product = relationship('DtbProduct')
    rounding_type = relationship('MtbRoundingType')
    shipping = relationship('DtbShipping')
    tax_display_type = relationship('MtbTaxDisplayType')
    tax_type = relationship('MtbTaxType')


class DtbProductStock(Base):
    __tablename__ = 'dtb_product_stock'

    id = Column(INTEGER(10), primary_key=True)
    product_class_id = Column(ForeignKey('dtb_product_class.id'), index=True)
    creator_id = Column(ForeignKey('dtb_member.id'), index=True)
    stock = Column(DECIMAL(10, 0))
    create_date = Column(DateTime, nullable=False, comment='(DC2Type:datetimetz)')
    update_date = Column(DateTime, nullable=False, comment='(DC2Type:datetimetz)')
    discriminator_type = Column(String(255), nullable=False)

    creator = relationship('DtbMember')
    product_class = relationship('DtbProductClas')


class DtbTaxRule(Base):
    __tablename__ = 'dtb_tax_rule'

    id = Column(INTEGER(10), primary_key=True)
    product_class_id = Column(ForeignKey('dtb_product_class.id'), index=True)
    creator_id = Column(ForeignKey('dtb_member.id'), index=True)
    country_id = Column(ForeignKey('mtb_country.id'), index=True)
    pref_id = Column(ForeignKey('mtb_pref.id'), index=True)
    product_id = Column(ForeignKey('dtb_product.id'), index=True)
    rounding_type_id = Column(ForeignKey('mtb_rounding_type.id'), index=True)
    tax_rate = Column(DECIMAL(10, 0), nullable=False, server_default=text("'8'"))
    tax_adjust = Column(DECIMAL(10, 0), nullable=False, server_default=text("'0'"))
    apply_date = Column(DateTime, nullable=False, comment='(DC2Type:datetimetz)')
    create_date = Column(DateTime, nullable=False, comment='(DC2Type:datetimetz)')
    update_date = Column(DateTime, nullable=False, comment='(DC2Type:datetimetz)')
    discriminator_type = Column(String(255), nullable=False)

    country = relationship('MtbCountry')
    creator = relationship('DtbMember')
    pref = relationship('MtbPref')
    product_class = relationship('DtbProductClas')
    product = relationship('DtbProduct')
    rounding_type = relationship('MtbRoundingType')
