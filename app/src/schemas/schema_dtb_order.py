import graphene
from datetime import datetime
from graphene_sqlalchemy import SQLAlchemyObjectType
from config.database import db_session
from models.model_dtb_order import ModelDtbOrder
from common.util.graphene_util import input_to_dictionary


# Create a generic class to mutualize description of people attributes for both queries and mutations
class DtbOrderAttribute:
    # example to create attribute name
    name = graphene.String(description="Name of the DtbOrder.")
    

class DtbOrder(SQLAlchemyObjectType):
    """DtbOrder node."""

    class Meta:
        model = ModelDtbOrder
        interfaces = (graphene.relay.Node,)


class CreateDtbOrderInput(graphene.InputObjectType, DtbOrderAttribute):
    """Arguments to create a DtbOrder."""
    pass


class CreateDtbOrder(graphene.Mutation):
    """Mutation to create a DtbOrder."""
    dtbOrder = graphene.Field(lambda: DtbOrder, description="DtbOrder created by this mutation.")

    class Arguments:
        input = CreateDtbOrderInput(required=True)

    def mutate(self, info, input):
        data = input_to_dictionary(input)
        data['created'] = datetime.utcnow()
        data['edited'] = datetime.utcnow()

        dtbOrder = DtbOrder(**data)
        db_session.add(dtbOrder)
        db_session.commit()

        return CreateDtbOrder(dtbOrder=dtbOrder)


class UpdateDtbOrderInput(graphene.InputObjectType, DtbOrderAttribute):
    """Arguments to update a DtbOrder."""
    id = graphene.ID(required=True, description="Global Id of the DtbOrder.")


class UpdateDtbOrder(graphene.Mutation):
    """Update a person."""
    dtbOrder = graphene.Field(lambda: DtbOrder, description="DtbOrder updated by this mutation.")

    class Arguments:
        input = UpdateDtbOrderInput(required=True)

    def mutate(self, info, input):
        data = input_to_dictionary(input)
        data['edited'] = datetime.utcnow()

        dtbOrder = db_session.query(DtbOrder).filter_by(id=data['id'])
        dtbOrder.update(data)
        db_session.commit()
        dtbOrder = db_session.query(DtbOrder).filter_by(id=data['id']).first()

        return UpdateDtbOrder(dtbOrder=dtbOrder)