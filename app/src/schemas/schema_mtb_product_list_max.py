import graphene
from datetime import datetime
from graphene_sqlalchemy import SQLAlchemyObjectType
from config.database import db_session
from models.model_mtb_product_list_max import ModelMtbProductListMax
from common.util.graphene_util import input_to_dictionary


# Create a generic class to mutualize description of people attributes for both queries and mutations
class MtbProductListMaxAttribute:
    # example to create attribute name
    name = graphene.String(description="Name of the MtbProductListMax.")
    

class MtbProductListMax(SQLAlchemyObjectType):
    """MtbProductListMax node."""

    class Meta:
        model = ModelMtbProductListMax
        interfaces = (graphene.relay.Node,)


class CreateMtbProductListMaxInput(graphene.InputObjectType, MtbProductListMaxAttribute):
    """Arguments to create a MtbProductListMax."""
    pass


class CreateMtbProductListMax(graphene.Mutation):
    """Mutation to create a MtbProductListMax."""
    mtbProductListMax = graphene.Field(lambda: MtbProductListMax, description="MtbProductListMax created by this mutation.")

    class Arguments:
        input = CreateMtbProductListMaxInput(required=True)

    def mutate(self, info, input):
        data = input_to_dictionary(input)
        data['created'] = datetime.utcnow()
        data['edited'] = datetime.utcnow()

        mtbProductListMax = MtbProductListMax(**data)
        db_session.add(mtbProductListMax)
        db_session.commit()

        return CreateMtbProductListMax(mtbProductListMax=mtbProductListMax)


class UpdateMtbProductListMaxInput(graphene.InputObjectType, MtbProductListMaxAttribute):
    """Arguments to update a MtbProductListMax."""
    id = graphene.ID(required=True, description="Global Id of the MtbProductListMax.")


class UpdateMtbProductListMax(graphene.Mutation):
    """Update a person."""
    mtbProductListMax = graphene.Field(lambda: MtbProductListMax, description="MtbProductListMax updated by this mutation.")

    class Arguments:
        input = UpdateMtbProductListMaxInput(required=True)

    def mutate(self, info, input):
        data = input_to_dictionary(input)
        data['edited'] = datetime.utcnow()

        mtbProductListMax = db_session.query(MtbProductListMax).filter_by(id=data['id'])
        mtbProductListMax.update(data)
        db_session.commit()
        mtbProductListMax = db_session.query(MtbProductListMax).filter_by(id=data['id']).first()

        return UpdateMtbProductListMax(mtbProductListMax=mtbProductListMax)