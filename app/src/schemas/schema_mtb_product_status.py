import graphene
from datetime import datetime
from graphene_sqlalchemy import SQLAlchemyObjectType
from config.database import db_session
from models.model_mtb_product_status import ModelMtbProductStatus
from common.util.graphene_util import input_to_dictionary


# Create a generic class to mutualize description of people attributes for both queries and mutations
class MtbProductStatusAttribute:
    # example to create attribute name
    name = graphene.String(description="Name of the MtbProductStatus.")
    

class MtbProductStatus(SQLAlchemyObjectType):
    """MtbProductStatus node."""

    class Meta:
        model = ModelMtbProductStatus
        interfaces = (graphene.relay.Node,)


class CreateMtbProductStatusInput(graphene.InputObjectType, MtbProductStatusAttribute):
    """Arguments to create a MtbProductStatus."""
    pass


class CreateMtbProductStatus(graphene.Mutation):
    """Mutation to create a MtbProductStatus."""
    mtbProductStatus = graphene.Field(lambda: MtbProductStatus, description="MtbProductStatus created by this mutation.")

    class Arguments:
        input = CreateMtbProductStatusInput(required=True)

    def mutate(self, info, input):
        data = input_to_dictionary(input)
        data['created'] = datetime.utcnow()
        data['edited'] = datetime.utcnow()

        mtbProductStatus = MtbProductStatus(**data)
        db_session.add(mtbProductStatus)
        db_session.commit()

        return CreateMtbProductStatus(mtbProductStatus=mtbProductStatus)


class UpdateMtbProductStatusInput(graphene.InputObjectType, MtbProductStatusAttribute):
    """Arguments to update a MtbProductStatus."""
    id = graphene.ID(required=True, description="Global Id of the MtbProductStatus.")


class UpdateMtbProductStatus(graphene.Mutation):
    """Update a person."""
    mtbProductStatus = graphene.Field(lambda: MtbProductStatus, description="MtbProductStatus updated by this mutation.")

    class Arguments:
        input = UpdateMtbProductStatusInput(required=True)

    def mutate(self, info, input):
        data = input_to_dictionary(input)
        data['edited'] = datetime.utcnow()

        mtbProductStatus = db_session.query(MtbProductStatus).filter_by(id=data['id'])
        mtbProductStatus.update(data)
        db_session.commit()
        mtbProductStatus = db_session.query(MtbProductStatus).filter_by(id=data['id']).first()

        return UpdateMtbProductStatus(mtbProductStatus=mtbProductStatus)