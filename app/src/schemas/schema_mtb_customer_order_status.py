import graphene
from datetime import datetime
from graphene_sqlalchemy import SQLAlchemyObjectType
from config.database import db_session
from models.model_mtb_customer_order_status import ModelMtbCustomerOrderStatus
from common.util.graphene_util import input_to_dictionary


# Create a generic class to mutualize description of people attributes for both queries and mutations
class MtbCustomerOrderStatusAttribute:
    # example to create attribute name
    name = graphene.String(description="Name of the MtbCustomerOrderStatus.")
    

class MtbCustomerOrderStatus(SQLAlchemyObjectType):
    """MtbCustomerOrderStatus node."""

    class Meta:
        model = ModelMtbCustomerOrderStatus
        interfaces = (graphene.relay.Node,)


class CreateMtbCustomerOrderStatusInput(graphene.InputObjectType, MtbCustomerOrderStatusAttribute):
    """Arguments to create a MtbCustomerOrderStatus."""
    pass


class CreateMtbCustomerOrderStatus(graphene.Mutation):
    """Mutation to create a MtbCustomerOrderStatus."""
    mtbCustomerOrderStatus = graphene.Field(lambda: MtbCustomerOrderStatus, description="MtbCustomerOrderStatus created by this mutation.")

    class Arguments:
        input = CreateMtbCustomerOrderStatusInput(required=True)

    def mutate(self, info, input):
        data = input_to_dictionary(input)
        data['created'] = datetime.utcnow()
        data['edited'] = datetime.utcnow()

        mtbCustomerOrderStatus = MtbCustomerOrderStatus(**data)
        db_session.add(mtbCustomerOrderStatus)
        db_session.commit()

        return CreateMtbCustomerOrderStatus(mtbCustomerOrderStatus=mtbCustomerOrderStatus)


class UpdateMtbCustomerOrderStatusInput(graphene.InputObjectType, MtbCustomerOrderStatusAttribute):
    """Arguments to update a MtbCustomerOrderStatus."""
    id = graphene.ID(required=True, description="Global Id of the MtbCustomerOrderStatus.")


class UpdateMtbCustomerOrderStatus(graphene.Mutation):
    """Update a person."""
    mtbCustomerOrderStatus = graphene.Field(lambda: MtbCustomerOrderStatus, description="MtbCustomerOrderStatus updated by this mutation.")

    class Arguments:
        input = UpdateMtbCustomerOrderStatusInput(required=True)

    def mutate(self, info, input):
        data = input_to_dictionary(input)
        data['edited'] = datetime.utcnow()

        mtbCustomerOrderStatus = db_session.query(MtbCustomerOrderStatus).filter_by(id=data['id'])
        mtbCustomerOrderStatus.update(data)
        db_session.commit()
        mtbCustomerOrderStatus = db_session.query(MtbCustomerOrderStatus).filter_by(id=data['id']).first()

        return UpdateMtbCustomerOrderStatus(mtbCustomerOrderStatus=mtbCustomerOrderStatus)