import graphene
from datetime import datetime
from graphene_sqlalchemy import SQLAlchemyObjectType
from config.database import db_session
from models.model_dtb_tag import ModelDtbTag
from common.util.graphene_util import input_to_dictionary


# Create a generic class to mutualize description of people attributes for both queries and mutations
class DtbTagAttribute:
    # example to create attribute name
    name = graphene.String(description="Name of the DtbTag.")
    

class DtbTag(SQLAlchemyObjectType):
    """DtbTag node."""

    class Meta:
        model = ModelDtbTag
        interfaces = (graphene.relay.Node,)


class CreateDtbTagInput(graphene.InputObjectType, DtbTagAttribute):
    """Arguments to create a DtbTag."""
    pass


class CreateDtbTag(graphene.Mutation):
    """Mutation to create a DtbTag."""
    dtbTag = graphene.Field(lambda: DtbTag, description="DtbTag created by this mutation.")

    class Arguments:
        input = CreateDtbTagInput(required=True)

    def mutate(self, info, input):
        data = input_to_dictionary(input)
        data['created'] = datetime.utcnow()
        data['edited'] = datetime.utcnow()

        dtbTag = DtbTag(**data)
        db_session.add(dtbTag)
        db_session.commit()

        return CreateDtbTag(dtbTag=dtbTag)


class UpdateDtbTagInput(graphene.InputObjectType, DtbTagAttribute):
    """Arguments to update a DtbTag."""
    id = graphene.ID(required=True, description="Global Id of the DtbTag.")


class UpdateDtbTag(graphene.Mutation):
    """Update a person."""
    dtbTag = graphene.Field(lambda: DtbTag, description="DtbTag updated by this mutation.")

    class Arguments:
        input = UpdateDtbTagInput(required=True)

    def mutate(self, info, input):
        data = input_to_dictionary(input)
        data['edited'] = datetime.utcnow()

        dtbTag = db_session.query(DtbTag).filter_by(id=data['id'])
        dtbTag.update(data)
        db_session.commit()
        dtbTag = db_session.query(DtbTag).filter_by(id=data['id']).first()

        return UpdateDtbTag(dtbTag=dtbTag)