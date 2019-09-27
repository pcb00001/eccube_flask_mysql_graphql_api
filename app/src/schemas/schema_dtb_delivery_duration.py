import graphene
from datetime import datetime
from graphene_sqlalchemy import SQLAlchemyObjectType
from config.database import db_session
from models.model_dtb_delivery_duration import ModelDtbDeliveryDuration
from common.util.graphene_util import input_to_dictionary


# Create a generic class to mutualize description of people attributes for both queries and mutations
class DtbDeliveryDurationAttribute:
    # example to create attribute name
    name = graphene.String(description="Name of the DtbDeliveryDuration.")
    

class DtbDeliveryDuration(SQLAlchemyObjectType):
    """DtbDeliveryDuration node."""

    class Meta:
        model = ModelDtbDeliveryDuration
        interfaces = (graphene.relay.Node,)


class CreateDtbDeliveryDurationInput(graphene.InputObjectType, DtbDeliveryDurationAttribute):
    """Arguments to create a DtbDeliveryDuration."""
    pass


class CreateDtbDeliveryDuration(graphene.Mutation):
    """Mutation to create a DtbDeliveryDuration."""
    dtbDeliveryDuration = graphene.Field(lambda: DtbDeliveryDuration, description="DtbDeliveryDuration created by this mutation.")

    class Arguments:
        input = CreateDtbDeliveryDurationInput(required=True)

    def mutate(self, info, input):
        data = input_to_dictionary(input)
        data['created'] = datetime.utcnow()
        data['edited'] = datetime.utcnow()

        dtbDeliveryDuration = DtbDeliveryDuration(**data)
        db_session.add(dtbDeliveryDuration)
        db_session.commit()

        return CreateDtbDeliveryDuration(dtbDeliveryDuration=dtbDeliveryDuration)


class UpdateDtbDeliveryDurationInput(graphene.InputObjectType, DtbDeliveryDurationAttribute):
    """Arguments to update a DtbDeliveryDuration."""
    id = graphene.ID(required=True, description="Global Id of the DtbDeliveryDuration.")


class UpdateDtbDeliveryDuration(graphene.Mutation):
    """Update a person."""
    dtbDeliveryDuration = graphene.Field(lambda: DtbDeliveryDuration, description="DtbDeliveryDuration updated by this mutation.")

    class Arguments:
        input = UpdateDtbDeliveryDurationInput(required=True)

    def mutate(self, info, input):
        data = input_to_dictionary(input)
        data['edited'] = datetime.utcnow()

        dtbDeliveryDuration = db_session.query(DtbDeliveryDuration).filter_by(id=data['id'])
        dtbDeliveryDuration.update(data)
        db_session.commit()
        dtbDeliveryDuration = db_session.query(DtbDeliveryDuration).filter_by(id=data['id']).first()

        return UpdateDtbDeliveryDuration(dtbDeliveryDuration=dtbDeliveryDuration)