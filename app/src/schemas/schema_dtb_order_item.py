import graphene
from datetime import datetime
from graphene_sqlalchemy import SQLAlchemyObjectType
from config.database import db_session
from models.model_dtb_order_item import ModelDtbOrderItem
from common.util.graphene_util import input_to_dictionary


# Create a generic class to mutualize description of people attributes for both queries and mutations
class DtbOrderItemAttribute:
    # example to create attribute name
    name = graphene.String(description="Name of the DtbOrderItem.")
    

class DtbOrderItem(SQLAlchemyObjectType):
    """DtbOrderItem node."""

    class Meta:
        model = ModelDtbOrderItem
        interfaces = (graphene.relay.Node,)


class CreateDtbOrderItemInput(graphene.InputObjectType, DtbOrderItemAttribute):
    """Arguments to create a DtbOrderItem."""
    pass


class CreateDtbOrderItem(graphene.Mutation):
    """Mutation to create a DtbOrderItem."""
    dtbOrderItem = graphene.Field(lambda: DtbOrderItem, description="DtbOrderItem created by this mutation.")

    class Arguments:
        input = CreateDtbOrderItemInput(required=True)

    def mutate(self, info, input):
        data = input_to_dictionary(input)
        data['created'] = datetime.utcnow()
        data['edited'] = datetime.utcnow()

        dtbOrderItem = DtbOrderItem(**data)
        db_session.add(dtbOrderItem)
        db_session.commit()

        return CreateDtbOrderItem(dtbOrderItem=dtbOrderItem)


class UpdateDtbOrderItemInput(graphene.InputObjectType, DtbOrderItemAttribute):
    """Arguments to update a DtbOrderItem."""
    id = graphene.ID(required=True, description="Global Id of the DtbOrderItem.")


class UpdateDtbOrderItem(graphene.Mutation):
    """Update a person."""
    dtbOrderItem = graphene.Field(lambda: DtbOrderItem, description="DtbOrderItem updated by this mutation.")

    class Arguments:
        input = UpdateDtbOrderItemInput(required=True)

    def mutate(self, info, input):
        data = input_to_dictionary(input)
        data['edited'] = datetime.utcnow()

        dtbOrderItem = db_session.query(DtbOrderItem).filter_by(id=data['id'])
        dtbOrderItem.update(data)
        db_session.commit()
        dtbOrderItem = db_session.query(DtbOrderItem).filter_by(id=data['id']).first()

        return UpdateDtbOrderItem(dtbOrderItem=dtbOrderItem)