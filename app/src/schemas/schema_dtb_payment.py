import graphene
from datetime import datetime
from graphene_sqlalchemy import SQLAlchemyObjectType
from config.database import db_session
from models.model_dtb_payment import ModelDtbPayment
from common.util.graphene_util import input_to_dictionary


# Create a generic class to mutualize description of people attributes for both queries and mutations
class DtbPaymentAttribute:
    # example to create attribute name
    name = graphene.String(description="Name of the DtbPayment.")
    

class DtbPayment(SQLAlchemyObjectType):
    """DtbPayment node."""

    class Meta:
        model = ModelDtbPayment
        interfaces = (graphene.relay.Node,)


class CreateDtbPaymentInput(graphene.InputObjectType, DtbPaymentAttribute):
    """Arguments to create a DtbPayment."""
    pass


class CreateDtbPayment(graphene.Mutation):
    """Mutation to create a DtbPayment."""
    dtbPayment = graphene.Field(lambda: DtbPayment, description="DtbPayment created by this mutation.")

    class Arguments:
        input = CreateDtbPaymentInput(required=True)

    def mutate(self, info, input):
        data = input_to_dictionary(input)
        data['created'] = datetime.utcnow()
        data['edited'] = datetime.utcnow()

        dtbPayment = DtbPayment(**data)
        db_session.add(dtbPayment)
        db_session.commit()

        return CreateDtbPayment(dtbPayment=dtbPayment)


class UpdateDtbPaymentInput(graphene.InputObjectType, DtbPaymentAttribute):
    """Arguments to update a DtbPayment."""
    id = graphene.ID(required=True, description="Global Id of the DtbPayment.")


class UpdateDtbPayment(graphene.Mutation):
    """Update a person."""
    dtbPayment = graphene.Field(lambda: DtbPayment, description="DtbPayment updated by this mutation.")

    class Arguments:
        input = UpdateDtbPaymentInput(required=True)

    def mutate(self, info, input):
        data = input_to_dictionary(input)
        data['edited'] = datetime.utcnow()

        dtbPayment = db_session.query(DtbPayment).filter_by(id=data['id'])
        dtbPayment.update(data)
        db_session.commit()
        dtbPayment = db_session.query(DtbPayment).filter_by(id=data['id']).first()

        return UpdateDtbPayment(dtbPayment=dtbPayment)