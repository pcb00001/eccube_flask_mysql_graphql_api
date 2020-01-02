import graphene
from schemas import schema_dtb_authority_role
from schemas import schema_dtb_base_info
from schemas import schema_dtb_block
from schemas import schema_dtb_block_position
from schemas import schema_dtb_cart
from schemas import schema_dtb_cart_item
from schemas import schema_dtb_category
from schemas import schema_dtb_class_category
from schemas import schema_dtb_class_name
from schemas import schema_dtb_csv
from schemas import schema_dtb_customer
from schemas import schema_dtb_customer_address
from schemas import schema_dtb_customer_favorite_product
from schemas import schema_dtb_delivery
from schemas import schema_dtb_delivery_duration
from schemas import schema_dtb_delivery_fee
from schemas import schema_dtb_delivery_time
from schemas import schema_dtb_layout
from schemas import schema_dtb_mail_history
from schemas import schema_dtb_mail_template
from schemas import schema_dtb_member
from schemas import schema_dtb_news
from schemas import schema_dtb_order
from schemas import schema_dtb_order_item
from schemas import schema_dtb_order_pdf
from schemas import schema_dtb_page
from schemas import schema_dtb_page_layout
from schemas import schema_dtb_payment
from schemas import schema_dtb_payment_option
from schemas import schema_dtb_plugin
from schemas import schema_dtb_product
from schemas import schema_dtb_product_category
from schemas import schema_dtb_product_class
from schemas import schema_dtb_product_image
from schemas import schema_dtb_product_stock
from schemas import schema_dtb_product_tag
from schemas import schema_dtb_shipping
from schemas import schema_dtb_tag
from schemas import schema_dtb_tax_rule
from schemas import schema_dtb_template
from schemas import schema_mtb_authority
from schemas import schema_mtb_country
from schemas import schema_mtb_csv_type
from schemas import schema_mtb_customer_order_status
from schemas import schema_mtb_customer_status
from schemas import schema_mtb_device_type
from schemas import schema_mtb_job
from schemas import schema_mtb_order_item_type
from schemas import schema_mtb_order_status
from schemas import schema_mtb_order_status_color
from schemas import schema_mtb_page_max
from schemas import schema_mtb_pref
from schemas import schema_mtb_product_list_max
from schemas import schema_mtb_product_list_order_by
from schemas import schema_mtb_product_status
from schemas import schema_mtb_rounding_type
from schemas import schema_mtb_sale_type
from schemas import schema_mtb_sex
from schemas import schema_mtb_tax_display_type
from schemas import schema_mtb_tax_type
from schemas import schema_mtb_work
from custom_schemas import custom_schema_dtb_product


class Query(
    graphene.ObjectType,
    schema_dtb_authority_role.Query,
    schema_dtb_base_info.Query,
    schema_dtb_block.Query,
    schema_dtb_block_position.Query,
    schema_dtb_cart.Query,
    schema_dtb_cart_item.Query,
    schema_dtb_category.Query,
    schema_dtb_class_category.Query,
    schema_dtb_class_name.Query,
    schema_dtb_csv.Query,
    schema_dtb_customer.Query,
    schema_dtb_customer_address.Query,
    schema_dtb_customer_favorite_product.Query,
    schema_dtb_delivery.Query,
    schema_dtb_delivery_duration.Query,
    schema_dtb_delivery_fee.Query,
    schema_dtb_delivery_time.Query,
    schema_dtb_layout.Query,
    schema_dtb_mail_history.Query,
    schema_dtb_mail_template.Query,
    schema_dtb_member.Query,
    schema_dtb_news.Query,
    schema_dtb_order.Query,
    schema_dtb_order_item.Query,
    schema_dtb_order_pdf.Query,
    schema_dtb_page.Query,
    schema_dtb_page_layout.Query,
    schema_dtb_payment.Query,
    schema_dtb_payment_option.Query,
    schema_dtb_plugin.Query,
    schema_dtb_product.Query,
    schema_dtb_product_category.Query,
    schema_dtb_product_class.Query,
    schema_dtb_product_image.Query,
    schema_dtb_product_stock.Query,
    schema_dtb_product_tag.Query,
    schema_dtb_shipping.Query,
    schema_dtb_tag.Query,
    schema_dtb_tax_rule.Query,
    schema_dtb_template.Query,
    schema_mtb_authority.Query,
    schema_mtb_country.Query,
    schema_mtb_csv_type.Query,
    schema_mtb_customer_order_status.Query,
    schema_mtb_customer_status.Query,
    schema_mtb_device_type.Query,
    schema_mtb_job.Query,
    schema_mtb_order_item_type.Query,
    schema_mtb_order_status.Query,
    schema_mtb_order_status_color.Query,
    schema_mtb_page_max.Query,
    schema_mtb_pref.Query,
    schema_mtb_product_list_max.Query,
    schema_mtb_product_list_order_by.Query,
    schema_mtb_product_status.Query,
    schema_mtb_rounding_type.Query,
    schema_mtb_sale_type.Query,
    schema_mtb_sex.Query,
    schema_mtb_tax_display_type.Query,
    schema_mtb_tax_type.Query,
    schema_mtb_work.Query,
    custom_schema_dtb_product.Query,
):
    pass


schema = graphene.Schema(query=Query)
