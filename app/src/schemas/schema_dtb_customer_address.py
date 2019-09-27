import graphene
from datetime import datetime
from graphene_sqlalchemy import SQLAlchemyObjectType
from config.database import db_session
from models.model_dtb_customer_address import ModelDtbCustomerAddress
from common.util.graphene_util import input_to_dictionary


# Create a generic class to mutualize description of people attributes for both queries and mutations
class DtbCustomerAddressAttribute:
    # example to create attribute name
    name = graphene.String(description="Name of the DtbCustomerAddress.")
    

class DtbCustomerAddress(SQLAlchemyObjectType):
    """DtbCustomerAddress node."""

    class Meta:
        model = ModelDtbCustomerAddress
        interfaces = (graphene.relay.Node,)


class CreateDtbCustomerAddressInput(graphene.InputObjectType, DtbCustomerAddressAttribute):
    """Arguments to create a DtbCustomerAddress."""
    pass


class CreateDtbCustomerAddress(graphene.Mutation):
    """Mutation to create a DtbCustomerAddress."""
    dtbCustomerAddress = graphene.Field(lambda: DtbCustomerAddress, description="DtbCustomerAddress created by this mutation.")

    class Arguments:
        input = CreateDtbCustomerAddressInput(required=True)

    def mutate(self, info, input):
        data = input_to_dictionary(input)
        data['created'] = datetime.utcnow()
        data['edited'] = datetime.utcnow()

        dtbCustomerAddress = DtbCustomerAddress(**data)
        db_session.add(dtbCustomerAddress)
        db_session.commit()

        return CreateDtbCustomerAddress(dtbCustomerAddress=dtbCustomerAddress)


class UpdateDtbCustomerAddressInput(graphene.InputObjectType, DtbCustomerAddressAttribute):
    """Arguments to update a DtbCustomerAddress."""
    id = graphene.ID(required=True, description="Global Id of the DtbCustomerAddress.")


class UpdateDtbCustomerAddress(graphene.Mutation):
    """Update a person."""
    dtbCustomerAddress = graphene.Field(lambda: DtbCustomerAddress, description="DtbCustomerAddress updated by this mutation.")

    class Arguments:
        input = UpdateDtbCustomerAddressInput(required=True)

    def mutate(self, info, input):
        data = input_to_dictionary(input)
        data['edited'] = datetime.utcnow()

        dtbCustomerAddress = db_session.query(DtbCustomerAddress).filter_by(id=data['id'])
        dtbCustomerAddress.update(data)
        db_session.commit()
        dtbCustomerAddress = db_session.query(DtbCustomerAddress).filter_by(id=data['id']).first()

        return UpdateDtbCustomerAddress(dtbCustomerAddress=dtbCustomerAddress)