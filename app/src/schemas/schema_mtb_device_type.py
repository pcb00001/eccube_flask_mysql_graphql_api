import graphene
from datetime import datetime
from graphene_sqlalchemy import SQLAlchemyObjectType
from config.database import db_session
from models.model_mtb_device_type import ModelMtbDeviceType
from common.util.graphene_util import input_to_dictionary


# Create a generic class to mutualize description of people attributes for both queries and mutations
class MtbDeviceTypeAttribute:
    # example to create attribute name
    name = graphene.String(description="Name of the MtbDeviceType.")
    

class MtbDeviceType(SQLAlchemyObjectType):
    """MtbDeviceType node."""

    class Meta:
        model = ModelMtbDeviceType
        interfaces = (graphene.relay.Node,)


class CreateMtbDeviceTypeInput(graphene.InputObjectType, MtbDeviceTypeAttribute):
    """Arguments to create a MtbDeviceType."""
    pass


class CreateMtbDeviceType(graphene.Mutation):
    """Mutation to create a MtbDeviceType."""
    mtbDeviceType = graphene.Field(lambda: MtbDeviceType, description="MtbDeviceType created by this mutation.")

    class Arguments:
        input = CreateMtbDeviceTypeInput(required=True)

    def mutate(self, info, input):
        data = input_to_dictionary(input)
        data['created'] = datetime.utcnow()
        data['edited'] = datetime.utcnow()

        mtbDeviceType = MtbDeviceType(**data)
        db_session.add(mtbDeviceType)
        db_session.commit()

        return CreateMtbDeviceType(mtbDeviceType=mtbDeviceType)


class UpdateMtbDeviceTypeInput(graphene.InputObjectType, MtbDeviceTypeAttribute):
    """Arguments to update a MtbDeviceType."""
    id = graphene.ID(required=True, description="Global Id of the MtbDeviceType.")


class UpdateMtbDeviceType(graphene.Mutation):
    """Update a person."""
    mtbDeviceType = graphene.Field(lambda: MtbDeviceType, description="MtbDeviceType updated by this mutation.")

    class Arguments:
        input = UpdateMtbDeviceTypeInput(required=True)

    def mutate(self, info, input):
        data = input_to_dictionary(input)
        data['edited'] = datetime.utcnow()

        mtbDeviceType = db_session.query(MtbDeviceType).filter_by(id=data['id'])
        mtbDeviceType.update(data)
        db_session.commit()
        mtbDeviceType = db_session.query(MtbDeviceType).filter_by(id=data['id']).first()

        return UpdateMtbDeviceType(mtbDeviceType=mtbDeviceType)