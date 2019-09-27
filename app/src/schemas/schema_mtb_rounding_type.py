import graphene
from datetime import datetime
from graphene_sqlalchemy import SQLAlchemyObjectType
from config.database import db_session
from models.model_mtb_rounding_type import ModelMtbRoundingType
from common.util.graphene_util import input_to_dictionary


# Create a generic class to mutualize description of people attributes for both queries and mutations
class MtbRoundingTypeAttribute:
    # example to create attribute name
    name = graphene.String(description="Name of the MtbRoundingType.")
    

class MtbRoundingType(SQLAlchemyObjectType):
    """MtbRoundingType node."""

    class Meta:
        model = ModelMtbRoundingType
        interfaces = (graphene.relay.Node,)


class CreateMtbRoundingTypeInput(graphene.InputObjectType, MtbRoundingTypeAttribute):
    """Arguments to create a MtbRoundingType."""
    pass


class CreateMtbRoundingType(graphene.Mutation):
    """Mutation to create a MtbRoundingType."""
    mtbRoundingType = graphene.Field(lambda: MtbRoundingType, description="MtbRoundingType created by this mutation.")

    class Arguments:
        input = CreateMtbRoundingTypeInput(required=True)

    def mutate(self, info, input):
        data = input_to_dictionary(input)
        data['created'] = datetime.utcnow()
        data['edited'] = datetime.utcnow()

        mtbRoundingType = MtbRoundingType(**data)
        db_session.add(mtbRoundingType)
        db_session.commit()

        return CreateMtbRoundingType(mtbRoundingType=mtbRoundingType)


class UpdateMtbRoundingTypeInput(graphene.InputObjectType, MtbRoundingTypeAttribute):
    """Arguments to update a MtbRoundingType."""
    id = graphene.ID(required=True, description="Global Id of the MtbRoundingType.")


class UpdateMtbRoundingType(graphene.Mutation):
    """Update a person."""
    mtbRoundingType = graphene.Field(lambda: MtbRoundingType, description="MtbRoundingType updated by this mutation.")

    class Arguments:
        input = UpdateMtbRoundingTypeInput(required=True)

    def mutate(self, info, input):
        data = input_to_dictionary(input)
        data['edited'] = datetime.utcnow()

        mtbRoundingType = db_session.query(MtbRoundingType).filter_by(id=data['id'])
        mtbRoundingType.update(data)
        db_session.commit()
        mtbRoundingType = db_session.query(MtbRoundingType).filter_by(id=data['id']).first()

        return UpdateMtbRoundingType(mtbRoundingType=mtbRoundingType)