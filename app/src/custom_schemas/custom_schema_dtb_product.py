# The file has been generated by tool- nguyennt2@rikkeisoft.com

import graphene
import sqlalchemy
from pprint import pprint
from common.util import varUtil

from models.model_dtb_product_category import ModelDtbProductCategory
from models.model_dtb_product_class import ModelDtbProductClass
from models.model_dtb_product_tag import ModelDtbProductTag
from schemas.schema_dtb_product import DtbProduct


class Query:
    get_all_dtb_product_order_by_price_desc = graphene.Field(
        lambda: graphene.List(DtbProduct)
    )

    def resolve_get_all_dtb_product_order_by_price_desc(self, info):
        query = DtbProduct.get_query(info)
        return query.join(ModelDtbProductClass).order_by(sqlalchemy.desc(ModelDtbProductClass.price02)).all()

    get_limit_dtb_product_by_category_id_order_by_price_desc = graphene.Field(
        lambda: graphene.List(DtbProduct),
        categoryId=graphene.Int(),
        offset=graphene.Int(),
        limit=graphene.Int(),
    )

    def resolve_get_limit_dtb_product_by_category_id_order_by_price_desc(self, info, categoryId, offset, limit):
        query = DtbProduct.get_query(info)
        return query.join(ModelDtbProductCategory).join(ModelDtbProductClass).filter(
            ModelDtbProductCategory.category_id == categoryId) \
            .order_by(sqlalchemy.desc(ModelDtbProductClass.price02)).offset(offset).limit(limit).all()

    get_limit_dtb_product_by_category_id_order_by_price_asc = graphene.Field(
        lambda: graphene.List(DtbProduct),
        categoryId=graphene.Int(),
        offset=graphene.Int(),
        limit=graphene.Int(),
    )

    def resolve_get_limit_dtb_product_by_category_id_order_by_price_asc(self, info, categoryId, offset, limit):
        query = DtbProduct.get_query(info)
        return query.join(ModelDtbProductCategory).join(ModelDtbProductClass).filter(
            ModelDtbProductCategory.category_id == categoryId) \
            .order_by(sqlalchemy.asc(ModelDtbProductClass.price02)).offset(offset).limit(limit).all()

    get_all_dtb_product_by_category_id_and_tag_ids = graphene.Field(
        lambda: graphene.List(DtbProduct),
        categoryId=graphene.Int(),
        tagIds=graphene.List(graphene.Int),
    )

    def resolve_get_all_dtb_product_by_category_id_and_tag_ids(self, info, categoryId, tagIds):

        if len(tagIds) > 0:
            query = DtbProduct.get_query(info).join(ModelDtbProductCategory) \
                .join(ModelDtbProductTag) \
                .join(ModelDtbProductClass) \
                .filter(ModelDtbProductCategory.category_id == categoryId) \
                .filter(ModelDtbProductTag.tag_id.in_(tagIds)) \
                .order_by(sqlalchemy.asc(ModelDtbProductClass.price02))
        else:
            query = DtbProduct.get_query(info).join(ModelDtbProductCategory) \
                .join(ModelDtbProductTag) \
                .join(ModelDtbProductClass) \
                .filter(ModelDtbProductCategory.category_id == categoryId) \
                .order_by(sqlalchemy.asc(ModelDtbProductClass.price02))

        # print(str(query))
        return query.all()

    get_all_dtb_product_by_category_id = graphene.Field(
        lambda: graphene.List(DtbProduct),
        categoryId=graphene.Int(),
    )

    def resolve_get_all_dtb_product_by_category_id(self, info, categoryId):

        query = DtbProduct.get_query(info).join(ModelDtbProductCategory) \
            .join(ModelDtbProductTag) \
            .join(ModelDtbProductClass) \
            .filter(ModelDtbProductCategory.category_id == categoryId) \
            .order_by(sqlalchemy.asc(ModelDtbProductClass.price02))

        # print(str(query))
        return query.all()