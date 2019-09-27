import graphene
from datetime import datetime
from graphene_sqlalchemy import SQLAlchemyObjectType
from config.database import db_session
from models.model_dtb_cart_item import ModelDtbCartItem
from common.util.graphene_util import input_to_dictionary


# Create a generic class to mutualize description of people attributes for both queries and mutations
class DtbCartItemAttribute:
    # example to create attribute name
    name = graphene.String(description="Name of the DtbCartItem.")
    

class DtbCartItem(SQLAlchemyObjectType):
    """DtbCartItem node."""

    class Meta:
        model = ModelDtbCartItem
        interfaces = (graphene.relay.Node,)


class CreateDtbCartItemInput(graphene.InputObjectType, DtbCartItemAttribute):
    """Arguments to create a DtbCartItem."""
    pass


class CreateDtbCartItem(graphene.Mutation):
    """Mutation to create a DtbCartItem."""
    dtbCartItem = graphene.Field(lambda: DtbCartItem, description="DtbCartItem created by this mutation.")

    class Arguments:
        input = CreateDtbCartItemInput(required=True)

    def mutate(self, info, input):
        data = input_to_dictionary(input)
        data['created'] = datetime.utcnow()
        data['edited'] = datetime.utcnow()

        dtbCartItem = DtbCartItem(**data)
        db_session.add(dtbCartItem)
        db_session.commit()

        return CreateDtbCartItem(dtbCartItem=dtbCartItem)


class UpdateDtbCartItemInput(graphene.InputObjectType, DtbCartItemAttribute):
    """Arguments to update a DtbCartItem."""
    id = graphene.ID(required=True, description="Global Id of the DtbCartItem.")


class UpdateDtbCartItem(graphene.Mutation):
    """Update a person."""
    dtbCartItem = graphene.Field(lambda: DtbCartItem, description="DtbCartItem updated by this mutation.")

    class Arguments:
        input = UpdateDtbCartItemInput(required=True)

    def mutate(self, info, input):
        data = input_to_dictionary(input)
        data['edited'] = datetime.utcnow()

        dtbCartItem = db_session.query(DtbCartItem).filter_by(id=data['id'])
        dtbCartItem.update(data)
        db_session.commit()
        dtbCartItem = db_session.query(DtbCartItem).filter_by(id=data['id']).first()

        return UpdateDtbCartItem(dtbCartItem=dtbCartItem)