import graphene
from datetime import datetime
from graphene_sqlalchemy import SQLAlchemyObjectType
from config.database import db_session
from models.model_dtb_shipping import ModelDtbShipping
from common.util.graphene_util import input_to_dictionary


# Create a generic class to mutualize description of people attributes for both queries and mutations
class DtbShippingAttribute:
    # example to create attribute name
    name = graphene.String(description="Name of the DtbShipping.")
    

class DtbShipping(SQLAlchemyObjectType):
    """DtbShipping node."""

    class Meta:
        model = ModelDtbShipping
        interfaces = (graphene.relay.Node,)


class CreateDtbShippingInput(graphene.InputObjectType, DtbShippingAttribute):
    """Arguments to create a DtbShipping."""
    pass


class CreateDtbShipping(graphene.Mutation):
    """Mutation to create a DtbShipping."""
    dtbShipping = graphene.Field(lambda: DtbShipping, description="DtbShipping created by this mutation.")

    class Arguments:
        input = CreateDtbShippingInput(required=True)

    def mutate(self, info, input):
        data = input_to_dictionary(input)
        data['created'] = datetime.utcnow()
        data['edited'] = datetime.utcnow()

        dtbShipping = DtbShipping(**data)
        db_session.add(dtbShipping)
        db_session.commit()

        return CreateDtbShipping(dtbShipping=dtbShipping)


class UpdateDtbShippingInput(graphene.InputObjectType, DtbShippingAttribute):
    """Arguments to update a DtbShipping."""
    id = graphene.ID(required=True, description="Global Id of the DtbShipping.")


class UpdateDtbShipping(graphene.Mutation):
    """Update a person."""
    dtbShipping = graphene.Field(lambda: DtbShipping, description="DtbShipping updated by this mutation.")

    class Arguments:
        input = UpdateDtbShippingInput(required=True)

    def mutate(self, info, input):
        data = input_to_dictionary(input)
        data['edited'] = datetime.utcnow()

        dtbShipping = db_session.query(DtbShipping).filter_by(id=data['id'])
        dtbShipping.update(data)
        db_session.commit()
        dtbShipping = db_session.query(DtbShipping).filter_by(id=data['id']).first()

        return UpdateDtbShipping(dtbShipping=dtbShipping)