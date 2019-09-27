import graphene
from datetime import datetime
from graphene_sqlalchemy import SQLAlchemyObjectType
from config.database import db_session
from models.model_dtb_product_tag import ModelDtbProductTag
from common.util.graphene_util import input_to_dictionary


# Create a generic class to mutualize description of people attributes for both queries and mutations
class DtbProductTagAttribute:
    # example to create attribute name
    name = graphene.String(description="Name of the DtbProductTag.")
    

class DtbProductTag(SQLAlchemyObjectType):
    """DtbProductTag node."""

    class Meta:
        model = ModelDtbProductTag
        interfaces = (graphene.relay.Node,)


class CreateDtbProductTagInput(graphene.InputObjectType, DtbProductTagAttribute):
    """Arguments to create a DtbProductTag."""
    pass


class CreateDtbProductTag(graphene.Mutation):
    """Mutation to create a DtbProductTag."""
    dtbProductTag = graphene.Field(lambda: DtbProductTag, description="DtbProductTag created by this mutation.")

    class Arguments:
        input = CreateDtbProductTagInput(required=True)

    def mutate(self, info, input):
        data = input_to_dictionary(input)
        data['created'] = datetime.utcnow()
        data['edited'] = datetime.utcnow()

        dtbProductTag = DtbProductTag(**data)
        db_session.add(dtbProductTag)
        db_session.commit()

        return CreateDtbProductTag(dtbProductTag=dtbProductTag)


class UpdateDtbProductTagInput(graphene.InputObjectType, DtbProductTagAttribute):
    """Arguments to update a DtbProductTag."""
    id = graphene.ID(required=True, description="Global Id of the DtbProductTag.")


class UpdateDtbProductTag(graphene.Mutation):
    """Update a person."""
    dtbProductTag = graphene.Field(lambda: DtbProductTag, description="DtbProductTag updated by this mutation.")

    class Arguments:
        input = UpdateDtbProductTagInput(required=True)

    def mutate(self, info, input):
        data = input_to_dictionary(input)
        data['edited'] = datetime.utcnow()

        dtbProductTag = db_session.query(DtbProductTag).filter_by(id=data['id'])
        dtbProductTag.update(data)
        db_session.commit()
        dtbProductTag = db_session.query(DtbProductTag).filter_by(id=data['id']).first()

        return UpdateDtbProductTag(dtbProductTag=dtbProductTag)