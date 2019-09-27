from graphene_sqlalchemy import SQLAlchemyConnectionField
import graphene

from schemas.schema_dtb_authority_role import DtbAuthorityRole
from schemas.schema_dtb_base_info import DtbBaseInfo
from schemas.schema_dtb_block import DtbBlock
from schemas.schema_dtb_block_position import DtbBlockPosition
from schemas.schema_dtb_cart import DtbCart
from schemas.schema_dtb_cart_item import DtbCartItem
from schemas.schema_dtb_category import DtbCategory
from schemas.schema_dtb_class_category import DtbClassCategory
from schemas.schema_dtb_class_name import DtbClassName
from schemas.schema_dtb_csv import DtbCsv
from schemas.schema_dtb_customer import DtbCustomer
from schemas.schema_dtb_customer_address import DtbCustomerAddress
from schemas.schema_dtb_customer_favorite_product import DtbCustomerFavoriteProduct
from schemas.schema_dtb_delivery import DtbDelivery
from schemas.schema_dtb_delivery_duration import DtbDeliveryDuration
from schemas.schema_dtb_delivery_fee import DtbDeliveryFee
from schemas.schema_dtb_delivery_time import DtbDeliveryTime
from schemas.schema_dtb_layout import DtbLayout
from schemas.schema_dtb_mail_history import DtbMailHistory
from schemas.schema_dtb_mail_template import DtbMailTemplate
from schemas.schema_dtb_member import DtbMember
from schemas.schema_dtb_news import DtbNews
from schemas.schema_dtb_order import DtbOrder
from schemas.schema_dtb_order_item import DtbOrderItem
from schemas.schema_dtb_order_pdf import DtbOrderPdf
from schemas.schema_dtb_page import DtbPage
from schemas.schema_dtb_page_layout import DtbPageLayout
from schemas.schema_dtb_payment import DtbPayment
from schemas.schema_dtb_payment_option import DtbPaymentOption
from schemas.schema_dtb_plugin import DtbPlugin
from schemas.schema_dtb_product import DtbProduct
from schemas.schema_dtb_product_category import DtbProductCategory
from schemas.schema_dtb_product_class import DtbProductClass
from schemas.schema_dtb_product_image import DtbProductImage
from schemas.schema_dtb_product_stock import DtbProductStock
from schemas.schema_dtb_product_tag import DtbProductTag
from schemas.schema_dtb_shipping import DtbShipping
from schemas.schema_dtb_tag import DtbTag
from schemas.schema_dtb_tax_rule import DtbTaxRule
from schemas.schema_dtb_template import DtbTemplate
from schemas.schema_mtb_authority import MtbAuthority
from schemas.schema_mtb_country import MtbCountry
from schemas.schema_mtb_csv_type import MtbCsvType
from schemas.schema_mtb_customer_order_status import MtbCustomerOrderStatus
from schemas.schema_mtb_customer_status import MtbCustomerStatus
from schemas.schema_mtb_device_type import MtbDeviceType
from schemas.schema_mtb_job import MtbJob
from schemas.schema_mtb_order_item_type import MtbOrderItemType
from schemas.schema_mtb_order_status import MtbOrderStatus
from schemas.schema_mtb_order_status_color import MtbOrderStatusColor
from schemas.schema_mtb_page_max import MtbPageMax
from schemas.schema_mtb_pref import MtbPref
from schemas.schema_mtb_product_list_max import MtbProductListMax
from schemas.schema_mtb_product_list_order_by import MtbProductListOrderBy
from schemas.schema_mtb_product_status import MtbProductStatus
from schemas.schema_mtb_rounding_type import MtbRoundingType
from schemas.schema_mtb_sale_type import MtbSaleType
from schemas.schema_mtb_sex import MtbSex
from schemas.schema_mtb_tax_display_type import MtbTaxDisplayType
from schemas.schema_mtb_tax_type import MtbTaxType
from schemas.schema_mtb_work import MtbWork


class DtbAuthorityRoleConnections(graphene.relay.Connection):
    class Meta:
        node = DtbAuthorityRole


class DtbBaseInfoConnections(graphene.relay.Connection):
    class Meta:
        node = DtbBaseInfo


class DtbBlockConnections(graphene.relay.Connection):
    class Meta:
        node = DtbBlock


class DtbBlockPositionConnections(graphene.relay.Connection):
    class Meta:
        node = DtbBlockPosition


class DtbCartConnections(graphene.relay.Connection):
    class Meta:
        node = DtbCart


class DtbCartItemConnections(graphene.relay.Connection):
    class Meta:
        node = DtbCartItem


class DtbCategoryConnections(graphene.relay.Connection):
    class Meta:
        node = DtbCategory


class DtbClassCategoryConnections(graphene.relay.Connection):
    class Meta:
        node = DtbClassCategory


class DtbClassNameConnections(graphene.relay.Connection):
    class Meta:
        node = DtbClassName


class DtbCsvConnections(graphene.relay.Connection):
    class Meta:
        node = DtbCsv


class DtbCustomerConnections(graphene.relay.Connection):
    class Meta:
        node = DtbCustomer


class DtbCustomerAddressConnections(graphene.relay.Connection):
    class Meta:
        node = DtbCustomerAddress


class DtbCustomerFavoriteProductConnections(graphene.relay.Connection):
    class Meta:
        node = DtbCustomerFavoriteProduct


class DtbDeliveryConnections(graphene.relay.Connection):
    class Meta:
        node = DtbDelivery


class DtbDeliveryDurationConnections(graphene.relay.Connection):
    class Meta:
        node = DtbDeliveryDuration


class DtbDeliveryFeeConnections(graphene.relay.Connection):
    class Meta:
        node = DtbDeliveryFee


class DtbDeliveryTimeConnections(graphene.relay.Connection):
    class Meta:
        node = DtbDeliveryTime


class DtbLayoutConnections(graphene.relay.Connection):
    class Meta:
        node = DtbLayout


class DtbMailHistoryConnections(graphene.relay.Connection):
    class Meta:
        node = DtbMailHistory


class DtbMailTemplateConnections(graphene.relay.Connection):
    class Meta:
        node = DtbMailTemplate


class DtbMemberConnections(graphene.relay.Connection):
    class Meta:
        node = DtbMember


class DtbNewsConnections(graphene.relay.Connection):
    class Meta:
        node = DtbNews


class DtbOrderConnections(graphene.relay.Connection):
    class Meta:
        node = DtbOrder


class DtbOrderItemConnections(graphene.relay.Connection):
    class Meta:
        node = DtbOrderItem


class DtbOrderPdfConnections(graphene.relay.Connection):
    class Meta:
        node = DtbOrderPdf


class DtbPageConnections(graphene.relay.Connection):
    class Meta:
        node = DtbPage


class DtbPageLayoutConnections(graphene.relay.Connection):
    class Meta:
        node = DtbPageLayout


class DtbPaymentConnections(graphene.relay.Connection):
    class Meta:
        node = DtbPayment


class DtbPaymentOptionConnections(graphene.relay.Connection):
    class Meta:
        node = DtbPaymentOption


class DtbPluginConnections(graphene.relay.Connection):
    class Meta:
        node = DtbPlugin


class DtbProductConnections(graphene.relay.Connection):
    class Meta:
        node = DtbProduct


class DtbProductCategoryConnections(graphene.relay.Connection):
    class Meta:
        node = DtbProductCategory


class DtbProductClassConnections(graphene.relay.Connection):
    class Meta:
        node = DtbProductClass


class DtbProductImageConnections(graphene.relay.Connection):
    class Meta:
        node = DtbProductImage


class DtbProductStockConnections(graphene.relay.Connection):
    class Meta:
        node = DtbProductStock


class DtbProductTagConnections(graphene.relay.Connection):
    class Meta:
        node = DtbProductTag


class DtbShippingConnections(graphene.relay.Connection):
    class Meta:
        node = DtbShipping


class DtbTagConnections(graphene.relay.Connection):
    class Meta:
        node = DtbTag


class DtbTaxRuleConnections(graphene.relay.Connection):
    class Meta:
        node = DtbTaxRule


class DtbTemplateConnections(graphene.relay.Connection):
    class Meta:
        node = DtbTemplate


class MtbAuthorityConnections(graphene.relay.Connection):
    class Meta:
        node = MtbAuthority


class MtbCountryConnections(graphene.relay.Connection):
    class Meta:
        node = MtbCountry


class MtbCsvTypeConnections(graphene.relay.Connection):
    class Meta:
        node = MtbCsvType


class MtbCustomerOrderStatusConnections(graphene.relay.Connection):
    class Meta:
        node = MtbCustomerOrderStatus


class MtbCustomerStatusConnections(graphene.relay.Connection):
    class Meta:
        node = MtbCustomerStatus


class MtbDeviceTypeConnections(graphene.relay.Connection):
    class Meta:
        node = MtbDeviceType


class MtbJobConnections(graphene.relay.Connection):
    class Meta:
        node = MtbJob


class MtbOrderItemTypeConnections(graphene.relay.Connection):
    class Meta:
        node = MtbOrderItemType


class MtbOrderStatusConnections(graphene.relay.Connection):
    class Meta:
        node = MtbOrderStatus


class MtbOrderStatusColorConnections(graphene.relay.Connection):
    class Meta:
        node = MtbOrderStatusColor


class MtbPageMaxConnections(graphene.relay.Connection):
    class Meta:
        node = MtbPageMax


class MtbPrefConnections(graphene.relay.Connection):
    class Meta:
        node = MtbPref


class MtbProductListMaxConnections(graphene.relay.Connection):
    class Meta:
        node = MtbProductListMax


class MtbProductListOrderByConnections(graphene.relay.Connection):
    class Meta:
        node = MtbProductListOrderBy


class MtbProductStatusConnections(graphene.relay.Connection):
    class Meta:
        node = MtbProductStatus


class MtbRoundingTypeConnections(graphene.relay.Connection):
    class Meta:
        node = MtbRoundingType


class MtbSaleTypeConnections(graphene.relay.Connection):
    class Meta:
        node = MtbSaleType


class MtbSexConnections(graphene.relay.Connection):
    class Meta:
        node = MtbSex


class MtbTaxDisplayTypeConnections(graphene.relay.Connection):
    class Meta:
        node = MtbTaxDisplayType


class MtbTaxTypeConnections(graphene.relay.Connection):
    class Meta:
        node = MtbTaxType


class MtbWorkConnections(graphene.relay.Connection):
    class Meta:
        node = MtbWork


class Query(graphene.ObjectType):
    # Get DtbAuthorityRole by id
    dtbAuthorityRole = graphene.relay.Node.Field(DtbAuthorityRole)
    # List all DtbAuthorityRole
    getAllDtbAuthorityRole = SQLAlchemyConnectionField(DtbAuthorityRoleConnections)

    # Get DtbBaseInfo by id
    dtbBaseInfo = graphene.relay.Node.Field(DtbBaseInfo)
    # List all DtbBaseInfo
    getAllDtbBaseInfo = SQLAlchemyConnectionField(DtbBaseInfoConnections)

    # Get DtbBlock by id
    dtbBlock = graphene.relay.Node.Field(DtbBlock)
    # List all DtbBlock
    getAllDtbBlock = SQLAlchemyConnectionField(DtbBlockConnections)

    # Get DtbBlockPosition by id
    dtbBlockPosition = graphene.relay.Node.Field(DtbBlockPosition)
    # List all DtbBlockPosition
    getAllDtbBlockPosition = SQLAlchemyConnectionField(DtbBlockPositionConnections)

    # Get DtbCart by id
    dtbCart = graphene.relay.Node.Field(DtbCart)
    # List all DtbCart
    getAllDtbCart = SQLAlchemyConnectionField(DtbCartConnections)

    # Get DtbCartItem by id
    dtbCartItem = graphene.relay.Node.Field(DtbCartItem)
    # List all DtbCartItem
    getAllDtbCartItem = SQLAlchemyConnectionField(DtbCartItemConnections)

    # Get DtbCategory by id
    dtbCategory = graphene.relay.Node.Field(DtbCategory)
    # List all DtbCategory
    getAllDtbCategory = SQLAlchemyConnectionField(DtbCategoryConnections)

    # Get DtbClassCategory by id
    dtbClassCategory = graphene.relay.Node.Field(DtbClassCategory)
    # List all DtbClassCategory
    getAllDtbClassCategory = SQLAlchemyConnectionField(DtbClassCategoryConnections)

    # Get DtbClassName by id
    dtbClassName = graphene.relay.Node.Field(DtbClassName)
    # List all DtbClassName
    getAllDtbClassName = SQLAlchemyConnectionField(DtbClassNameConnections)

    # Get DtbCsv by id
    dtbCsv = graphene.relay.Node.Field(DtbCsv)
    # List all DtbCsv
    getAllDtbCsv = SQLAlchemyConnectionField(DtbCsvConnections)

    # Get DtbCustomer by id
    dtbCustomer = graphene.relay.Node.Field(DtbCustomer)
    # List all DtbCustomer
    getAllDtbCustomer = SQLAlchemyConnectionField(DtbCustomerConnections)

    # Get DtbCustomerAddress by id
    dtbCustomerAddress = graphene.relay.Node.Field(DtbCustomerAddress)
    # List all DtbCustomerAddress
    getAllDtbCustomerAddress = SQLAlchemyConnectionField(DtbCustomerAddressConnections)

    # Get DtbCustomerFavoriteProduct by id
    dtbCustomerFavoriteProduct = graphene.relay.Node.Field(DtbCustomerFavoriteProduct)
    # List all DtbCustomerFavoriteProduct
    getAllDtbCustomerFavoriteProduct = SQLAlchemyConnectionField(DtbCustomerFavoriteProductConnections)

    # Get DtbDelivery by id
    dtbDelivery = graphene.relay.Node.Field(DtbDelivery)
    # List all DtbDelivery
    getAllDtbDelivery = SQLAlchemyConnectionField(DtbDeliveryConnections)

    # Get DtbDeliveryDuration by id
    dtbDeliveryDuration = graphene.relay.Node.Field(DtbDeliveryDuration)
    # List all DtbDeliveryDuration
    getAllDtbDeliveryDuration = SQLAlchemyConnectionField(DtbDeliveryDurationConnections)

    # Get DtbDeliveryFee by id
    dtbDeliveryFee = graphene.relay.Node.Field(DtbDeliveryFee)
    # List all DtbDeliveryFee
    getAllDtbDeliveryFee = SQLAlchemyConnectionField(DtbDeliveryFeeConnections)

    # Get DtbDeliveryTime by id
    dtbDeliveryTime = graphene.relay.Node.Field(DtbDeliveryTime)
    # List all DtbDeliveryTime
    getAllDtbDeliveryTime = SQLAlchemyConnectionField(DtbDeliveryTimeConnections)

    # Get DtbLayout by id
    dtbLayout = graphene.relay.Node.Field(DtbLayout)
    # List all DtbLayout
    getAllDtbLayout = SQLAlchemyConnectionField(DtbLayoutConnections)

    # Get DtbMailHistory by id
    dtbMailHistory = graphene.relay.Node.Field(DtbMailHistory)
    # List all DtbMailHistory
    getAllDtbMailHistory = SQLAlchemyConnectionField(DtbMailHistoryConnections)

    # Get DtbMailTemplate by id
    dtbMailTemplate = graphene.relay.Node.Field(DtbMailTemplate)
    # List all DtbMailTemplate
    getAllDtbMailTemplate = SQLAlchemyConnectionField(DtbMailTemplateConnections)

    # Get DtbMember by id
    dtbMember = graphene.relay.Node.Field(DtbMember)
    # List all DtbMember
    getAllDtbMember = SQLAlchemyConnectionField(DtbMemberConnections)

    # Get DtbNews by id
    dtbNews = graphene.relay.Node.Field(DtbNews)
    # List all DtbNews
    getAllDtbNews = SQLAlchemyConnectionField(DtbNewsConnections)

    # Get DtbOrder by id
    dtbOrder = graphene.relay.Node.Field(DtbOrder)
    # List all DtbOrder
    getAllDtbOrder = SQLAlchemyConnectionField(DtbOrderConnections)

    # Get DtbOrderItem by id
    dtbOrderItem = graphene.relay.Node.Field(DtbOrderItem)
    # List all DtbOrderItem
    getAllDtbOrderItem = SQLAlchemyConnectionField(DtbOrderItemConnections)

    # Get DtbOrderPdf by id
    dtbOrderPdf = graphene.relay.Node.Field(DtbOrderPdf)
    # List all DtbOrderPdf
    getAllDtbOrderPdf = SQLAlchemyConnectionField(DtbOrderPdfConnections)

    # Get DtbPage by id
    dtbPage = graphene.relay.Node.Field(DtbPage)
    # List all DtbPage
    getAllDtbPage = SQLAlchemyConnectionField(DtbPageConnections)

    # Get DtbPageLayout by id
    dtbPageLayout = graphene.relay.Node.Field(DtbPageLayout)
    # List all DtbPageLayout
    getAllDtbPageLayout = SQLAlchemyConnectionField(DtbPageLayoutConnections)

    # Get DtbPayment by id
    dtbPayment = graphene.relay.Node.Field(DtbPayment)
    # List all DtbPayment
    getAllDtbPayment = SQLAlchemyConnectionField(DtbPaymentConnections)

    # Get DtbPaymentOption by id
    dtbPaymentOption = graphene.relay.Node.Field(DtbPaymentOption)
    # List all DtbPaymentOption
    getAllDtbPaymentOption = SQLAlchemyConnectionField(DtbPaymentOptionConnections)

    # Get DtbPlugin by id
    dtbPlugin = graphene.relay.Node.Field(DtbPlugin)
    # List all DtbPlugin
    getAllDtbPlugin = SQLAlchemyConnectionField(DtbPluginConnections)

    # Get DtbProduct by id
    dtbProduct = graphene.relay.Node.Field(DtbProduct)
    # List all DtbProduct
    getAllDtbProduct = SQLAlchemyConnectionField(DtbProductConnections)

    # Get DtbProductCategory by id
    dtbProductCategory = graphene.relay.Node.Field(DtbProductCategory)
    # List all DtbProductCategory
    getAllDtbProductCategory = SQLAlchemyConnectionField(DtbProductCategoryConnections)

    # Get DtbProductClass by id
    dtbProductClass = graphene.relay.Node.Field(DtbProductClass)
    # List all DtbProductClass
    getAllDtbProductClass = SQLAlchemyConnectionField(DtbProductClassConnections)

    # Get DtbProductImage by id
    dtbProductImage = graphene.relay.Node.Field(DtbProductImage)
    # List all DtbProductImage
    getAllDtbProductImage = SQLAlchemyConnectionField(DtbProductImageConnections)

    # Get DtbProductStock by id
    dtbProductStock = graphene.relay.Node.Field(DtbProductStock)
    # List all DtbProductStock
    getAllDtbProductStock = SQLAlchemyConnectionField(DtbProductStockConnections)

    # Get DtbProductTag by id
    dtbProductTag = graphene.relay.Node.Field(DtbProductTag)
    # List all DtbProductTag
    getAllDtbProductTag = SQLAlchemyConnectionField(DtbProductTagConnections)

    # Get DtbShipping by id
    dtbShipping = graphene.relay.Node.Field(DtbShipping)
    # List all DtbShipping
    getAllDtbShipping = SQLAlchemyConnectionField(DtbShippingConnections)

    # Get DtbTag by id
    dtbTag = graphene.relay.Node.Field(DtbTag)
    # List all DtbTag
    getAllDtbTag = SQLAlchemyConnectionField(DtbTagConnections)

    # Get DtbTaxRule by id
    dtbTaxRule = graphene.relay.Node.Field(DtbTaxRule)
    # List all DtbTaxRule
    getAllDtbTaxRule = SQLAlchemyConnectionField(DtbTaxRuleConnections)

    # Get DtbTemplate by id
    dtbTemplate = graphene.relay.Node.Field(DtbTemplate)
    # List all DtbTemplate
    getAllDtbTemplate = SQLAlchemyConnectionField(DtbTemplateConnections)

    # Get MtbAuthority by id
    mtbAuthority = graphene.relay.Node.Field(MtbAuthority)
    # List all MtbAuthority
    getAllMtbAuthority = SQLAlchemyConnectionField(MtbAuthorityConnections)

    # Get MtbCountry by id
    mtbCountry = graphene.relay.Node.Field(MtbCountry)
    # List all MtbCountry
    getAllMtbCountry = SQLAlchemyConnectionField(MtbCountryConnections)

    # Get MtbCsvType by id
    mtbCsvType = graphene.relay.Node.Field(MtbCsvType)
    # List all MtbCsvType
    getAllMtbCsvType = SQLAlchemyConnectionField(MtbCsvTypeConnections)

    # Get MtbCustomerOrderStatus by id
    mtbCustomerOrderStatus = graphene.relay.Node.Field(MtbCustomerOrderStatus)
    # List all MtbCustomerOrderStatus
    getAllMtbCustomerOrderStatus = SQLAlchemyConnectionField(MtbCustomerOrderStatusConnections)

    # Get MtbCustomerStatus by id
    mtbCustomerStatus = graphene.relay.Node.Field(MtbCustomerStatus)
    # List all MtbCustomerStatus
    getAllMtbCustomerStatus = SQLAlchemyConnectionField(MtbCustomerStatusConnections)

    # Get MtbDeviceType by id
    mtbDeviceType = graphene.relay.Node.Field(MtbDeviceType)
    # List all MtbDeviceType
    getAllMtbDeviceType = SQLAlchemyConnectionField(MtbDeviceTypeConnections)

    # Get MtbJob by id
    mtbJob = graphene.relay.Node.Field(MtbJob)
    # List all MtbJob
    getAllMtbJob = SQLAlchemyConnectionField(MtbJobConnections)

    # Get MtbOrderItemType by id
    mtbOrderItemType = graphene.relay.Node.Field(MtbOrderItemType)
    # List all MtbOrderItemType
    getAllMtbOrderItemType = SQLAlchemyConnectionField(MtbOrderItemTypeConnections)

    # Get MtbOrderStatus by id
    mtbOrderStatus = graphene.relay.Node.Field(MtbOrderStatus)
    # List all MtbOrderStatus
    getAllMtbOrderStatus = SQLAlchemyConnectionField(MtbOrderStatusConnections)

    # Get MtbOrderStatusColor by id
    mtbOrderStatusColor = graphene.relay.Node.Field(MtbOrderStatusColor)
    # List all MtbOrderStatusColor
    getAllMtbOrderStatusColor = SQLAlchemyConnectionField(MtbOrderStatusColorConnections)

    # Get MtbPageMax by id
    mtbPageMax = graphene.relay.Node.Field(MtbPageMax)
    # List all MtbPageMax
    getAllMtbPageMax = SQLAlchemyConnectionField(MtbPageMaxConnections)

    # Get MtbPref by id
    mtbPref = graphene.relay.Node.Field(MtbPref)
    # List all MtbPref
    getAllMtbPref = SQLAlchemyConnectionField(MtbPrefConnections)

    # Get MtbProductListMax by id
    mtbProductListMax = graphene.relay.Node.Field(MtbProductListMax)
    # List all MtbProductListMax
    getAllMtbProductListMax = SQLAlchemyConnectionField(MtbProductListMaxConnections)

    # Get MtbProductListOrderBy by id
    mtbProductListOrderBy = graphene.relay.Node.Field(MtbProductListOrderBy)
    # List all MtbProductListOrderBy
    getAllMtbProductListOrderBy = SQLAlchemyConnectionField(MtbProductListOrderByConnections)

    # Get MtbProductStatus by id
    mtbProductStatus = graphene.relay.Node.Field(MtbProductStatus)
    # List all MtbProductStatus
    getAllMtbProductStatus = SQLAlchemyConnectionField(MtbProductStatusConnections)

    # Get MtbRoundingType by id
    mtbRoundingType = graphene.relay.Node.Field(MtbRoundingType)
    # List all MtbRoundingType
    getAllMtbRoundingType = SQLAlchemyConnectionField(MtbRoundingTypeConnections)

    # Get MtbSaleType by id
    mtbSaleType = graphene.relay.Node.Field(MtbSaleType)
    # List all MtbSaleType
    getAllMtbSaleType = SQLAlchemyConnectionField(MtbSaleTypeConnections)

    # Get MtbSex by id
    mtbSex = graphene.relay.Node.Field(MtbSex)
    # List all MtbSex
    getAllMtbSex = SQLAlchemyConnectionField(MtbSexConnections)

    # Get MtbTaxDisplayType by id
    mtbTaxDisplayType = graphene.relay.Node.Field(MtbTaxDisplayType)
    # List all MtbTaxDisplayType
    getAllMtbTaxDisplayType = SQLAlchemyConnectionField(MtbTaxDisplayTypeConnections)

    # Get MtbTaxType by id
    mtbTaxType = graphene.relay.Node.Field(MtbTaxType)
    # List all MtbTaxType
    getAllMtbTaxType = SQLAlchemyConnectionField(MtbTaxTypeConnections)

    # Get MtbWork by id
    mtbWork = graphene.relay.Node.Field(MtbWork)
    # List all MtbWork
    getAllMtbWork = SQLAlchemyConnectionField(MtbWorkConnections)


schema = graphene.Schema(query=Query)