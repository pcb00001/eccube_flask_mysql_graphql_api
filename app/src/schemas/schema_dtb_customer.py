import graphene
from datetime import datetime
from graphene_sqlalchemy import SQLAlchemyObjectType
from config.database import db_session
from models.model_dtb_customer import ModelDtbCustomer
from common.util.graphene_util import input_to_dictionary


# Create a generic class to mutualize description of people attributes for both queries and mutations
class DtbCustomerAttribute:
    # example to create attribute name
    name = graphene.String(description="Name of the DtbCustomer.")
    

class DtbCustomer(SQLAlchemyObjectType):
    """DtbCustomer node."""

    class Meta:
        model = ModelDtbCustomer
        interfaces = (graphene.relay.Node,)


class CreateDtbCustomerInput(graphene.InputObjectType, DtbCustomerAttribute):
    """Arguments to create a DtbCustomer."""
    pass


class CreateDtbCustomer(graphene.Mutation):
    """Mutation to create a DtbCustomer."""
    dtbCustomer = graphene.Field(lambda: DtbCustomer, description="DtbCustomer created by this mutation.")

    class Arguments:
        input = CreateDtbCustomerInput(required=True)

    def mutate(self, info, input):
        data = input_to_dictionary(input)
        data['created'] = datetime.utcnow()
        data['edited'] = datetime.utcnow()

        dtbCustomer = DtbCustomer(**data)
        db_session.add(dtbCustomer)
        db_session.commit()

        return CreateDtbCustomer(dtbCustomer=dtbCustomer)


class UpdateDtbCustomerInput(graphene.InputObjectType, DtbCustomerAttribute):
    """Arguments to update a DtbCustomer."""
    id = graphene.ID(required=True, description="Global Id of the DtbCustomer.")


class UpdateDtbCustomer(graphene.Mutation):
    """Update a person."""
    dtbCustomer = graphene.Field(lambda: DtbCustomer, description="DtbCustomer updated by this mutation.")

    class Arguments:
        input = UpdateDtbCustomerInput(required=True)

    def mutate(self, info, input):
        data = input_to_dictionary(input)
        data['edited'] = datetime.utcnow()

        dtbCustomer = db_session.query(DtbCustomer).filter_by(id=data['id'])
        dtbCustomer.update(data)
        db_session.commit()
        dtbCustomer = db_session.query(DtbCustomer).filter_by(id=data['id']).first()

        return UpdateDtbCustomer(dtbCustomer=dtbCustomer)