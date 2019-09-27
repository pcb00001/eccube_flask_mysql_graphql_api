import graphene
from datetime import datetime
from graphene_sqlalchemy import SQLAlchemyObjectType
from config.database import db_session
from models.model_mtb_order_status import ModelMtbOrderStatus
from common.util.graphene_util import input_to_dictionary


# Create a generic class to mutualize description of people attributes for both queries and mutations
class MtbOrderStatusAttribute:
    # example to create attribute name
    name = graphene.String(description="Name of the MtbOrderStatus.")
    

class MtbOrderStatus(SQLAlchemyObjectType):
    """MtbOrderStatus node."""

    class Meta:
        model = ModelMtbOrderStatus
        interfaces = (graphene.relay.Node,)


class CreateMtbOrderStatusInput(graphene.InputObjectType, MtbOrderStatusAttribute):
    """Arguments to create a MtbOrderStatus."""
    pass


class CreateMtbOrderStatus(graphene.Mutation):
    """Mutation to create a MtbOrderStatus."""
    mtbOrderStatus = graphene.Field(lambda: MtbOrderStatus, description="MtbOrderStatus created by this mutation.")

    class Arguments:
        input = CreateMtbOrderStatusInput(required=True)

    def mutate(self, info, input):
        data = input_to_dictionary(input)
        data['created'] = datetime.utcnow()
        data['edited'] = datetime.utcnow()

        mtbOrderStatus = MtbOrderStatus(**data)
        db_session.add(mtbOrderStatus)
        db_session.commit()

        return CreateMtbOrderStatus(mtbOrderStatus=mtbOrderStatus)


class UpdateMtbOrderStatusInput(graphene.InputObjectType, MtbOrderStatusAttribute):
    """Arguments to update a MtbOrderStatus."""
    id = graphene.ID(required=True, description="Global Id of the MtbOrderStatus.")


class UpdateMtbOrderStatus(graphene.Mutation):
    """Update a person."""
    mtbOrderStatus = graphene.Field(lambda: MtbOrderStatus, description="MtbOrderStatus updated by this mutation.")

    class Arguments:
        input = UpdateMtbOrderStatusInput(required=True)

    def mutate(self, info, input):
        data = input_to_dictionary(input)
        data['edited'] = datetime.utcnow()

        mtbOrderStatus = db_session.query(MtbOrderStatus).filter_by(id=data['id'])
        mtbOrderStatus.update(data)
        db_session.commit()
        mtbOrderStatus = db_session.query(MtbOrderStatus).filter_by(id=data['id']).first()

        return UpdateMtbOrderStatus(mtbOrderStatus=mtbOrderStatus)