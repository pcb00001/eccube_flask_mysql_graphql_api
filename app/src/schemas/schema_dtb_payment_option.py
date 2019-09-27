import graphene
from datetime import datetime
from graphene_sqlalchemy import SQLAlchemyObjectType
from config.database import db_session
from models.model_dtb_payment_option import ModelDtbPaymentOption
from common.util.graphene_util import input_to_dictionary


# Create a generic class to mutualize description of people attributes for both queries and mutations
class DtbPaymentOptionAttribute:
    # example to create attribute name
    name = graphene.String(description="Name of the DtbPaymentOption.")
    

class DtbPaymentOption(SQLAlchemyObjectType):
    """DtbPaymentOption node."""

    class Meta:
        model = ModelDtbPaymentOption
        interfaces = (graphene.relay.Node,)


class CreateDtbPaymentOptionInput(graphene.InputObjectType, DtbPaymentOptionAttribute):
    """Arguments to create a DtbPaymentOption."""
    pass


class CreateDtbPaymentOption(graphene.Mutation):
    """Mutation to create a DtbPaymentOption."""
    dtbPaymentOption = graphene.Field(lambda: DtbPaymentOption, description="DtbPaymentOption created by this mutation.")

    class Arguments:
        input = CreateDtbPaymentOptionInput(required=True)

    def mutate(self, info, input):
        data = input_to_dictionary(input)
        data['created'] = datetime.utcnow()
        data['edited'] = datetime.utcnow()

        dtbPaymentOption = DtbPaymentOption(**data)
        db_session.add(dtbPaymentOption)
        db_session.commit()

        return CreateDtbPaymentOption(dtbPaymentOption=dtbPaymentOption)


class UpdateDtbPaymentOptionInput(graphene.InputObjectType, DtbPaymentOptionAttribute):
    """Arguments to update a DtbPaymentOption."""
    id = graphene.ID(required=True, description="Global Id of the DtbPaymentOption.")


class UpdateDtbPaymentOption(graphene.Mutation):
    """Update a person."""
    dtbPaymentOption = graphene.Field(lambda: DtbPaymentOption, description="DtbPaymentOption updated by this mutation.")

    class Arguments:
        input = UpdateDtbPaymentOptionInput(required=True)

    def mutate(self, info, input):
        data = input_to_dictionary(input)
        data['edited'] = datetime.utcnow()

        dtbPaymentOption = db_session.query(DtbPaymentOption).filter_by(id=data['id'])
        dtbPaymentOption.update(data)
        db_session.commit()
        dtbPaymentOption = db_session.query(DtbPaymentOption).filter_by(id=data['id']).first()

        return UpdateDtbPaymentOption(dtbPaymentOption=dtbPaymentOption)