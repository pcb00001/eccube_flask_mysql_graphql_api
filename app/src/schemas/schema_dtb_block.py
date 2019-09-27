import graphene
from datetime import datetime
from graphene_sqlalchemy import SQLAlchemyObjectType
from config.database import db_session
from models.model_dtb_block import ModelDtbBlock
from common.util.graphene_util import input_to_dictionary


# Create a generic class to mutualize description of people attributes for both queries and mutations
class DtbBlockAttribute:
    # example to create attribute name
    name = graphene.String(description="Name of the DtbBlock.")
    

class DtbBlock(SQLAlchemyObjectType):
    """DtbBlock node."""

    class Meta:
        model = ModelDtbBlock
        interfaces = (graphene.relay.Node,)


class CreateDtbBlockInput(graphene.InputObjectType, DtbBlockAttribute):
    """Arguments to create a DtbBlock."""
    pass


class CreateDtbBlock(graphene.Mutation):
    """Mutation to create a DtbBlock."""
    dtbBlock = graphene.Field(lambda: DtbBlock, description="DtbBlock created by this mutation.")

    class Arguments:
        input = CreateDtbBlockInput(required=True)

    def mutate(self, info, input):
        data = input_to_dictionary(input)
        data['created'] = datetime.utcnow()
        data['edited'] = datetime.utcnow()

        dtbBlock = DtbBlock(**data)
        db_session.add(dtbBlock)
        db_session.commit()

        return CreateDtbBlock(dtbBlock=dtbBlock)


class UpdateDtbBlockInput(graphene.InputObjectType, DtbBlockAttribute):
    """Arguments to update a DtbBlock."""
    id = graphene.ID(required=True, description="Global Id of the DtbBlock.")


class UpdateDtbBlock(graphene.Mutation):
    """Update a person."""
    dtbBlock = graphene.Field(lambda: DtbBlock, description="DtbBlock updated by this mutation.")

    class Arguments:
        input = UpdateDtbBlockInput(required=True)

    def mutate(self, info, input):
        data = input_to_dictionary(input)
        data['edited'] = datetime.utcnow()

        dtbBlock = db_session.query(DtbBlock).filter_by(id=data['id'])
        dtbBlock.update(data)
        db_session.commit()
        dtbBlock = db_session.query(DtbBlock).filter_by(id=data['id']).first()

        return UpdateDtbBlock(dtbBlock=dtbBlock)