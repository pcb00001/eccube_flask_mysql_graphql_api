import graphene
from datetime import datetime
from graphene_sqlalchemy import SQLAlchemyObjectType
from config.database import db_session
from models.model_dtb_block_position import ModelDtbBlockPosition
from common.util.graphene_util import input_to_dictionary


# Create a generic class to mutualize description of people attributes for both queries and mutations
class DtbBlockPositionAttribute:
    # example to create attribute name
    name = graphene.String(description="Name of the DtbBlockPosition.")
    

class DtbBlockPosition(SQLAlchemyObjectType):
    """DtbBlockPosition node."""

    class Meta:
        model = ModelDtbBlockPosition
        interfaces = (graphene.relay.Node,)


class CreateDtbBlockPositionInput(graphene.InputObjectType, DtbBlockPositionAttribute):
    """Arguments to create a DtbBlockPosition."""
    pass


class CreateDtbBlockPosition(graphene.Mutation):
    """Mutation to create a DtbBlockPosition."""
    dtbBlockPosition = graphene.Field(lambda: DtbBlockPosition, description="DtbBlockPosition created by this mutation.")

    class Arguments:
        input = CreateDtbBlockPositionInput(required=True)

    def mutate(self, info, input):
        data = input_to_dictionary(input)
        data['created'] = datetime.utcnow()
        data['edited'] = datetime.utcnow()

        dtbBlockPosition = DtbBlockPosition(**data)
        db_session.add(dtbBlockPosition)
        db_session.commit()

        return CreateDtbBlockPosition(dtbBlockPosition=dtbBlockPosition)


class UpdateDtbBlockPositionInput(graphene.InputObjectType, DtbBlockPositionAttribute):
    """Arguments to update a DtbBlockPosition."""
    id = graphene.ID(required=True, description="Global Id of the DtbBlockPosition.")


class UpdateDtbBlockPosition(graphene.Mutation):
    """Update a person."""
    dtbBlockPosition = graphene.Field(lambda: DtbBlockPosition, description="DtbBlockPosition updated by this mutation.")

    class Arguments:
        input = UpdateDtbBlockPositionInput(required=True)

    def mutate(self, info, input):
        data = input_to_dictionary(input)
        data['edited'] = datetime.utcnow()

        dtbBlockPosition = db_session.query(DtbBlockPosition).filter_by(id=data['id'])
        dtbBlockPosition.update(data)
        db_session.commit()
        dtbBlockPosition = db_session.query(DtbBlockPosition).filter_by(id=data['id']).first()

        return UpdateDtbBlockPosition(dtbBlockPosition=dtbBlockPosition)