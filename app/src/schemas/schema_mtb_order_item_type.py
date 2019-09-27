import graphene
from datetime import datetime
from graphene_sqlalchemy import SQLAlchemyObjectType
from config.database import db_session
from models.model_mtb_order_item_type import ModelMtbOrderItemType
from common.util.graphene_util import input_to_dictionary


# Create a generic class to mutualize description of people attributes for both queries and mutations
class MtbOrderItemTypeAttribute:
    # example to create attribute name
    name = graphene.String(description="Name of the MtbOrderItemType.")
    

class MtbOrderItemType(SQLAlchemyObjectType):
    """MtbOrderItemType node."""

    class Meta:
        model = ModelMtbOrderItemType
        interfaces = (graphene.relay.Node,)


class CreateMtbOrderItemTypeInput(graphene.InputObjectType, MtbOrderItemTypeAttribute):
    """Arguments to create a MtbOrderItemType."""
    pass


class CreateMtbOrderItemType(graphene.Mutation):
    """Mutation to create a MtbOrderItemType."""
    mtbOrderItemType = graphene.Field(lambda: MtbOrderItemType, description="MtbOrderItemType created by this mutation.")

    class Arguments:
        input = CreateMtbOrderItemTypeInput(required=True)

    def mutate(self, info, input):
        data = input_to_dictionary(input)
        data['created'] = datetime.utcnow()
        data['edited'] = datetime.utcnow()

        mtbOrderItemType = MtbOrderItemType(**data)
        db_session.add(mtbOrderItemType)
        db_session.commit()

        return CreateMtbOrderItemType(mtbOrderItemType=mtbOrderItemType)


class UpdateMtbOrderItemTypeInput(graphene.InputObjectType, MtbOrderItemTypeAttribute):
    """Arguments to update a MtbOrderItemType."""
    id = graphene.ID(required=True, description="Global Id of the MtbOrderItemType.")


class UpdateMtbOrderItemType(graphene.Mutation):
    """Update a person."""
    mtbOrderItemType = graphene.Field(lambda: MtbOrderItemType, description="MtbOrderItemType updated by this mutation.")

    class Arguments:
        input = UpdateMtbOrderItemTypeInput(required=True)

    def mutate(self, info, input):
        data = input_to_dictionary(input)
        data['edited'] = datetime.utcnow()

        mtbOrderItemType = db_session.query(MtbOrderItemType).filter_by(id=data['id'])
        mtbOrderItemType.update(data)
        db_session.commit()
        mtbOrderItemType = db_session.query(MtbOrderItemType).filter_by(id=data['id']).first()

        return UpdateMtbOrderItemType(mtbOrderItemType=mtbOrderItemType)