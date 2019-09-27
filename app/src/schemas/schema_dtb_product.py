import graphene
from datetime import datetime
from graphene_sqlalchemy import SQLAlchemyObjectType
from config.database import db_session
from models.model_dtb_product import ModelDtbProduct
from common.util.graphene_util import input_to_dictionary


# Create a generic class to mutualize description of people attributes for both queries and mutations
class DtbProductAttribute:
    # example to create attribute name
    name = graphene.String(description="Name of the DtbProduct.")
    

class DtbProduct(SQLAlchemyObjectType):
    """DtbProduct node."""

    class Meta:
        model = ModelDtbProduct
        interfaces = (graphene.relay.Node,)


class CreateDtbProductInput(graphene.InputObjectType, DtbProductAttribute):
    """Arguments to create a DtbProduct."""
    pass


class CreateDtbProduct(graphene.Mutation):
    """Mutation to create a DtbProduct."""
    dtbProduct = graphene.Field(lambda: DtbProduct, description="DtbProduct created by this mutation.")

    class Arguments:
        input = CreateDtbProductInput(required=True)

    def mutate(self, info, input):
        data = input_to_dictionary(input)
        data['created'] = datetime.utcnow()
        data['edited'] = datetime.utcnow()

        dtbProduct = DtbProduct(**data)
        db_session.add(dtbProduct)
        db_session.commit()

        return CreateDtbProduct(dtbProduct=dtbProduct)


class UpdateDtbProductInput(graphene.InputObjectType, DtbProductAttribute):
    """Arguments to update a DtbProduct."""
    id = graphene.ID(required=True, description="Global Id of the DtbProduct.")


class UpdateDtbProduct(graphene.Mutation):
    """Update a person."""
    dtbProduct = graphene.Field(lambda: DtbProduct, description="DtbProduct updated by this mutation.")

    class Arguments:
        input = UpdateDtbProductInput(required=True)

    def mutate(self, info, input):
        data = input_to_dictionary(input)
        data['edited'] = datetime.utcnow()

        dtbProduct = db_session.query(DtbProduct).filter_by(id=data['id'])
        dtbProduct.update(data)
        db_session.commit()
        dtbProduct = db_session.query(DtbProduct).filter_by(id=data['id']).first()

        return UpdateDtbProduct(dtbProduct=dtbProduct)