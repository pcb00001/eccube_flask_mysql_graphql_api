import graphene
from datetime import datetime
from graphene_sqlalchemy import SQLAlchemyObjectType
from config.database import db_session
from models.model_dtb_delivery_fee import ModelDtbDeliveryFee
from common.util.graphene_util import input_to_dictionary


# Create a generic class to mutualize description of people attributes for both queries and mutations
class DtbDeliveryFeeAttribute:
    # example to create attribute name
    name = graphene.String(description="Name of the DtbDeliveryFee.")
    

class DtbDeliveryFee(SQLAlchemyObjectType):
    """DtbDeliveryFee node."""

    class Meta:
        model = ModelDtbDeliveryFee
        interfaces = (graphene.relay.Node,)


class CreateDtbDeliveryFeeInput(graphene.InputObjectType, DtbDeliveryFeeAttribute):
    """Arguments to create a DtbDeliveryFee."""
    pass


class CreateDtbDeliveryFee(graphene.Mutation):
    """Mutation to create a DtbDeliveryFee."""
    dtbDeliveryFee = graphene.Field(lambda: DtbDeliveryFee, description="DtbDeliveryFee created by this mutation.")

    class Arguments:
        input = CreateDtbDeliveryFeeInput(required=True)

    def mutate(self, info, input):
        data = input_to_dictionary(input)
        data['created'] = datetime.utcnow()
        data['edited'] = datetime.utcnow()

        dtbDeliveryFee = DtbDeliveryFee(**data)
        db_session.add(dtbDeliveryFee)
        db_session.commit()

        return CreateDtbDeliveryFee(dtbDeliveryFee=dtbDeliveryFee)


class UpdateDtbDeliveryFeeInput(graphene.InputObjectType, DtbDeliveryFeeAttribute):
    """Arguments to update a DtbDeliveryFee."""
    id = graphene.ID(required=True, description="Global Id of the DtbDeliveryFee.")


class UpdateDtbDeliveryFee(graphene.Mutation):
    """Update a person."""
    dtbDeliveryFee = graphene.Field(lambda: DtbDeliveryFee, description="DtbDeliveryFee updated by this mutation.")

    class Arguments:
        input = UpdateDtbDeliveryFeeInput(required=True)

    def mutate(self, info, input):
        data = input_to_dictionary(input)
        data['edited'] = datetime.utcnow()

        dtbDeliveryFee = db_session.query(DtbDeliveryFee).filter_by(id=data['id'])
        dtbDeliveryFee.update(data)
        db_session.commit()
        dtbDeliveryFee = db_session.query(DtbDeliveryFee).filter_by(id=data['id']).first()

        return UpdateDtbDeliveryFee(dtbDeliveryFee=dtbDeliveryFee)