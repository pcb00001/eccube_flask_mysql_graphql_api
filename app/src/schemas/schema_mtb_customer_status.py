import graphene
from datetime import datetime
from graphene_sqlalchemy import SQLAlchemyObjectType
from config.database import db_session
from models.model_mtb_customer_status import ModelMtbCustomerStatus
from common.util.graphene_util import input_to_dictionary


# Create a generic class to mutualize description of people attributes for both queries and mutations
class MtbCustomerStatusAttribute:
    # example to create attribute name
    name = graphene.String(description="Name of the MtbCustomerStatus.")
    

class MtbCustomerStatus(SQLAlchemyObjectType):
    """MtbCustomerStatus node."""

    class Meta:
        model = ModelMtbCustomerStatus
        interfaces = (graphene.relay.Node,)


class CreateMtbCustomerStatusInput(graphene.InputObjectType, MtbCustomerStatusAttribute):
    """Arguments to create a MtbCustomerStatus."""
    pass


class CreateMtbCustomerStatus(graphene.Mutation):
    """Mutation to create a MtbCustomerStatus."""
    mtbCustomerStatus = graphene.Field(lambda: MtbCustomerStatus, description="MtbCustomerStatus created by this mutation.")

    class Arguments:
        input = CreateMtbCustomerStatusInput(required=True)

    def mutate(self, info, input):
        data = input_to_dictionary(input)
        data['created'] = datetime.utcnow()
        data['edited'] = datetime.utcnow()

        mtbCustomerStatus = MtbCustomerStatus(**data)
        db_session.add(mtbCustomerStatus)
        db_session.commit()

        return CreateMtbCustomerStatus(mtbCustomerStatus=mtbCustomerStatus)


class UpdateMtbCustomerStatusInput(graphene.InputObjectType, MtbCustomerStatusAttribute):
    """Arguments to update a MtbCustomerStatus."""
    id = graphene.ID(required=True, description="Global Id of the MtbCustomerStatus.")


class UpdateMtbCustomerStatus(graphene.Mutation):
    """Update a person."""
    mtbCustomerStatus = graphene.Field(lambda: MtbCustomerStatus, description="MtbCustomerStatus updated by this mutation.")

    class Arguments:
        input = UpdateMtbCustomerStatusInput(required=True)

    def mutate(self, info, input):
        data = input_to_dictionary(input)
        data['edited'] = datetime.utcnow()

        mtbCustomerStatus = db_session.query(MtbCustomerStatus).filter_by(id=data['id'])
        mtbCustomerStatus.update(data)
        db_session.commit()
        mtbCustomerStatus = db_session.query(MtbCustomerStatus).filter_by(id=data['id']).first()

        return UpdateMtbCustomerStatus(mtbCustomerStatus=mtbCustomerStatus)