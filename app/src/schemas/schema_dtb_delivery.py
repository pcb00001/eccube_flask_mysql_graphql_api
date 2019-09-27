import graphene
from datetime import datetime
from graphene_sqlalchemy import SQLAlchemyObjectType
from config.database import db_session
from models.model_dtb_delivery import ModelDtbDelivery
from common.util.graphene_util import input_to_dictionary


# Create a generic class to mutualize description of people attributes for both queries and mutations
class DtbDeliveryAttribute:
    # example to create attribute name
    name = graphene.String(description="Name of the DtbDelivery.")
    

class DtbDelivery(SQLAlchemyObjectType):
    """DtbDelivery node."""

    class Meta:
        model = ModelDtbDelivery
        interfaces = (graphene.relay.Node,)


class CreateDtbDeliveryInput(graphene.InputObjectType, DtbDeliveryAttribute):
    """Arguments to create a DtbDelivery."""
    pass


class CreateDtbDelivery(graphene.Mutation):
    """Mutation to create a DtbDelivery."""
    dtbDelivery = graphene.Field(lambda: DtbDelivery, description="DtbDelivery created by this mutation.")

    class Arguments:
        input = CreateDtbDeliveryInput(required=True)

    def mutate(self, info, input):
        data = input_to_dictionary(input)
        data['created'] = datetime.utcnow()
        data['edited'] = datetime.utcnow()

        dtbDelivery = DtbDelivery(**data)
        db_session.add(dtbDelivery)
        db_session.commit()

        return CreateDtbDelivery(dtbDelivery=dtbDelivery)


class UpdateDtbDeliveryInput(graphene.InputObjectType, DtbDeliveryAttribute):
    """Arguments to update a DtbDelivery."""
    id = graphene.ID(required=True, description="Global Id of the DtbDelivery.")


class UpdateDtbDelivery(graphene.Mutation):
    """Update a person."""
    dtbDelivery = graphene.Field(lambda: DtbDelivery, description="DtbDelivery updated by this mutation.")

    class Arguments:
        input = UpdateDtbDeliveryInput(required=True)

    def mutate(self, info, input):
        data = input_to_dictionary(input)
        data['edited'] = datetime.utcnow()

        dtbDelivery = db_session.query(DtbDelivery).filter_by(id=data['id'])
        dtbDelivery.update(data)
        db_session.commit()
        dtbDelivery = db_session.query(DtbDelivery).filter_by(id=data['id']).first()

        return UpdateDtbDelivery(dtbDelivery=dtbDelivery)