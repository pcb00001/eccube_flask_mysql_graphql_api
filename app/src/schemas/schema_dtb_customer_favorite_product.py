import graphene
from datetime import datetime
from graphene_sqlalchemy import SQLAlchemyObjectType
from config.database import db_session
from models.model_dtb_customer_favorite_product import ModelDtbCustomerFavoriteProduct
from common.util.graphene_util import input_to_dictionary


# Create a generic class to mutualize description of people attributes for both queries and mutations
class DtbCustomerFavoriteProductAttribute:
    # example to create attribute name
    name = graphene.String(description="Name of the DtbCustomerFavoriteProduct.")
    

class DtbCustomerFavoriteProduct(SQLAlchemyObjectType):
    """DtbCustomerFavoriteProduct node."""

    class Meta:
        model = ModelDtbCustomerFavoriteProduct
        interfaces = (graphene.relay.Node,)


class CreateDtbCustomerFavoriteProductInput(graphene.InputObjectType, DtbCustomerFavoriteProductAttribute):
    """Arguments to create a DtbCustomerFavoriteProduct."""
    pass


class CreateDtbCustomerFavoriteProduct(graphene.Mutation):
    """Mutation to create a DtbCustomerFavoriteProduct."""
    dtbCustomerFavoriteProduct = graphene.Field(lambda: DtbCustomerFavoriteProduct, description="DtbCustomerFavoriteProduct created by this mutation.")

    class Arguments:
        input = CreateDtbCustomerFavoriteProductInput(required=True)

    def mutate(self, info, input):
        data = input_to_dictionary(input)
        data['created'] = datetime.utcnow()
        data['edited'] = datetime.utcnow()

        dtbCustomerFavoriteProduct = DtbCustomerFavoriteProduct(**data)
        db_session.add(dtbCustomerFavoriteProduct)
        db_session.commit()

        return CreateDtbCustomerFavoriteProduct(dtbCustomerFavoriteProduct=dtbCustomerFavoriteProduct)


class UpdateDtbCustomerFavoriteProductInput(graphene.InputObjectType, DtbCustomerFavoriteProductAttribute):
    """Arguments to update a DtbCustomerFavoriteProduct."""
    id = graphene.ID(required=True, description="Global Id of the DtbCustomerFavoriteProduct.")


class UpdateDtbCustomerFavoriteProduct(graphene.Mutation):
    """Update a person."""
    dtbCustomerFavoriteProduct = graphene.Field(lambda: DtbCustomerFavoriteProduct, description="DtbCustomerFavoriteProduct updated by this mutation.")

    class Arguments:
        input = UpdateDtbCustomerFavoriteProductInput(required=True)

    def mutate(self, info, input):
        data = input_to_dictionary(input)
        data['edited'] = datetime.utcnow()

        dtbCustomerFavoriteProduct = db_session.query(DtbCustomerFavoriteProduct).filter_by(id=data['id'])
        dtbCustomerFavoriteProduct.update(data)
        db_session.commit()
        dtbCustomerFavoriteProduct = db_session.query(DtbCustomerFavoriteProduct).filter_by(id=data['id']).first()

        return UpdateDtbCustomerFavoriteProduct(dtbCustomerFavoriteProduct=dtbCustomerFavoriteProduct)