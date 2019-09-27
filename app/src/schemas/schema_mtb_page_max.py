import graphene
from datetime import datetime
from graphene_sqlalchemy import SQLAlchemyObjectType
from config.database import db_session
from models.model_mtb_page_max import ModelMtbPageMax
from common.util.graphene_util import input_to_dictionary


# Create a generic class to mutualize description of people attributes for both queries and mutations
class MtbPageMaxAttribute:
    # example to create attribute name
    name = graphene.String(description="Name of the MtbPageMax.")
    

class MtbPageMax(SQLAlchemyObjectType):
    """MtbPageMax node."""

    class Meta:
        model = ModelMtbPageMax
        interfaces = (graphene.relay.Node,)


class CreateMtbPageMaxInput(graphene.InputObjectType, MtbPageMaxAttribute):
    """Arguments to create a MtbPageMax."""
    pass


class CreateMtbPageMax(graphene.Mutation):
    """Mutation to create a MtbPageMax."""
    mtbPageMax = graphene.Field(lambda: MtbPageMax, description="MtbPageMax created by this mutation.")

    class Arguments:
        input = CreateMtbPageMaxInput(required=True)

    def mutate(self, info, input):
        data = input_to_dictionary(input)
        data['created'] = datetime.utcnow()
        data['edited'] = datetime.utcnow()

        mtbPageMax = MtbPageMax(**data)
        db_session.add(mtbPageMax)
        db_session.commit()

        return CreateMtbPageMax(mtbPageMax=mtbPageMax)


class UpdateMtbPageMaxInput(graphene.InputObjectType, MtbPageMaxAttribute):
    """Arguments to update a MtbPageMax."""
    id = graphene.ID(required=True, description="Global Id of the MtbPageMax.")


class UpdateMtbPageMax(graphene.Mutation):
    """Update a person."""
    mtbPageMax = graphene.Field(lambda: MtbPageMax, description="MtbPageMax updated by this mutation.")

    class Arguments:
        input = UpdateMtbPageMaxInput(required=True)

    def mutate(self, info, input):
        data = input_to_dictionary(input)
        data['edited'] = datetime.utcnow()

        mtbPageMax = db_session.query(MtbPageMax).filter_by(id=data['id'])
        mtbPageMax.update(data)
        db_session.commit()
        mtbPageMax = db_session.query(MtbPageMax).filter_by(id=data['id']).first()

        return UpdateMtbPageMax(mtbPageMax=mtbPageMax)