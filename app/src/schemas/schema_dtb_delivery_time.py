import graphene
from datetime import datetime
from graphene_sqlalchemy import SQLAlchemyObjectType
from config.database import db_session
from models.model_dtb_delivery_time import ModelDtbDeliveryTime
from common.util.graphene_util import input_to_dictionary


# Create a generic class to mutualize description of people attributes for both queries and mutations
class DtbDeliveryTimeAttribute:
    # example to create attribute name
    name = graphene.String(description="Name of the DtbDeliveryTime.")
    

class DtbDeliveryTime(SQLAlchemyObjectType):
    """DtbDeliveryTime node."""

    class Meta:
        model = ModelDtbDeliveryTime
        interfaces = (graphene.relay.Node,)


class CreateDtbDeliveryTimeInput(graphene.InputObjectType, DtbDeliveryTimeAttribute):
    """Arguments to create a DtbDeliveryTime."""
    pass


class CreateDtbDeliveryTime(graphene.Mutation):
    """Mutation to create a DtbDeliveryTime."""
    dtbDeliveryTime = graphene.Field(lambda: DtbDeliveryTime, description="DtbDeliveryTime created by this mutation.")

    class Arguments:
        input = CreateDtbDeliveryTimeInput(required=True)

    def mutate(self, info, input):
        data = input_to_dictionary(input)
        data['created'] = datetime.utcnow()
        data['edited'] = datetime.utcnow()

        dtbDeliveryTime = DtbDeliveryTime(**data)
        db_session.add(dtbDeliveryTime)
        db_session.commit()

        return CreateDtbDeliveryTime(dtbDeliveryTime=dtbDeliveryTime)


class UpdateDtbDeliveryTimeInput(graphene.InputObjectType, DtbDeliveryTimeAttribute):
    """Arguments to update a DtbDeliveryTime."""
    id = graphene.ID(required=True, description="Global Id of the DtbDeliveryTime.")


class UpdateDtbDeliveryTime(graphene.Mutation):
    """Update a person."""
    dtbDeliveryTime = graphene.Field(lambda: DtbDeliveryTime, description="DtbDeliveryTime updated by this mutation.")

    class Arguments:
        input = UpdateDtbDeliveryTimeInput(required=True)

    def mutate(self, info, input):
        data = input_to_dictionary(input)
        data['edited'] = datetime.utcnow()

        dtbDeliveryTime = db_session.query(DtbDeliveryTime).filter_by(id=data['id'])
        dtbDeliveryTime.update(data)
        db_session.commit()
        dtbDeliveryTime = db_session.query(DtbDeliveryTime).filter_by(id=data['id']).first()

        return UpdateDtbDeliveryTime(dtbDeliveryTime=dtbDeliveryTime)