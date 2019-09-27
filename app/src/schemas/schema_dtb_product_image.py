import graphene
from datetime import datetime
from graphene_sqlalchemy import SQLAlchemyObjectType
from config.database import db_session
from models.model_dtb_product_image import ModelDtbProductImage
from common.util.graphene_util import input_to_dictionary


# Create a generic class to mutualize description of people attributes for both queries and mutations
class DtbProductImageAttribute:
    # example to create attribute name
    name = graphene.String(description="Name of the DtbProductImage.")
    

class DtbProductImage(SQLAlchemyObjectType):
    """DtbProductImage node."""

    class Meta:
        model = ModelDtbProductImage
        interfaces = (graphene.relay.Node,)


class CreateDtbProductImageInput(graphene.InputObjectType, DtbProductImageAttribute):
    """Arguments to create a DtbProductImage."""
    pass


class CreateDtbProductImage(graphene.Mutation):
    """Mutation to create a DtbProductImage."""
    dtbProductImage = graphene.Field(lambda: DtbProductImage, description="DtbProductImage created by this mutation.")

    class Arguments:
        input = CreateDtbProductImageInput(required=True)

    def mutate(self, info, input):
        data = input_to_dictionary(input)
        data['created'] = datetime.utcnow()
        data['edited'] = datetime.utcnow()

        dtbProductImage = DtbProductImage(**data)
        db_session.add(dtbProductImage)
        db_session.commit()

        return CreateDtbProductImage(dtbProductImage=dtbProductImage)


class UpdateDtbProductImageInput(graphene.InputObjectType, DtbProductImageAttribute):
    """Arguments to update a DtbProductImage."""
    id = graphene.ID(required=True, description="Global Id of the DtbProductImage.")


class UpdateDtbProductImage(graphene.Mutation):
    """Update a person."""
    dtbProductImage = graphene.Field(lambda: DtbProductImage, description="DtbProductImage updated by this mutation.")

    class Arguments:
        input = UpdateDtbProductImageInput(required=True)

    def mutate(self, info, input):
        data = input_to_dictionary(input)
        data['edited'] = datetime.utcnow()

        dtbProductImage = db_session.query(DtbProductImage).filter_by(id=data['id'])
        dtbProductImage.update(data)
        db_session.commit()
        dtbProductImage = db_session.query(DtbProductImage).filter_by(id=data['id']).first()

        return UpdateDtbProductImage(dtbProductImage=dtbProductImage)