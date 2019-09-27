import graphene
from datetime import datetime
from graphene_sqlalchemy import SQLAlchemyObjectType
from config.database import db_session
from models.model_dtb_cart import ModelDtbCart
from common.util.graphene_util import input_to_dictionary


# Create a generic class to mutualize description of people attributes for both queries and mutations
class DtbCartAttribute:
    # example to create attribute name
    name = graphene.String(description="Name of the DtbCart.")
    

class DtbCart(SQLAlchemyObjectType):
    """DtbCart node."""

    class Meta:
        model = ModelDtbCart
        interfaces = (graphene.relay.Node,)


class CreateDtbCartInput(graphene.InputObjectType, DtbCartAttribute):
    """Arguments to create a DtbCart."""
    pass


class CreateDtbCart(graphene.Mutation):
    """Mutation to create a DtbCart."""
    dtbCart = graphene.Field(lambda: DtbCart, description="DtbCart created by this mutation.")

    class Arguments:
        input = CreateDtbCartInput(required=True)

    def mutate(self, info, input):
        data = input_to_dictionary(input)
        data['created'] = datetime.utcnow()
        data['edited'] = datetime.utcnow()

        dtbCart = DtbCart(**data)
        db_session.add(dtbCart)
        db_session.commit()

        return CreateDtbCart(dtbCart=dtbCart)


class UpdateDtbCartInput(graphene.InputObjectType, DtbCartAttribute):
    """Arguments to update a DtbCart."""
    id = graphene.ID(required=True, description="Global Id of the DtbCart.")


class UpdateDtbCart(graphene.Mutation):
    """Update a person."""
    dtbCart = graphene.Field(lambda: DtbCart, description="DtbCart updated by this mutation.")

    class Arguments:
        input = UpdateDtbCartInput(required=True)

    def mutate(self, info, input):
        data = input_to_dictionary(input)
        data['edited'] = datetime.utcnow()

        dtbCart = db_session.query(DtbCart).filter_by(id=data['id'])
        dtbCart.update(data)
        db_session.commit()
        dtbCart = db_session.query(DtbCart).filter_by(id=data['id']).first()

        return UpdateDtbCart(dtbCart=dtbCart)