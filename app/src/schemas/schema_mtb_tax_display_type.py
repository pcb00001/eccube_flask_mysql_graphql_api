import graphene
from datetime import datetime
from graphene_sqlalchemy import SQLAlchemyObjectType
from config.database import db_session
from models.model_mtb_tax_display_type import ModelMtbTaxDisplayType
from common.util.graphene_util import input_to_dictionary


# Create a generic class to mutualize description of people attributes for both queries and mutations
class MtbTaxDisplayTypeAttribute:
    # example to create attribute name
    name = graphene.String(description="Name of the MtbTaxDisplayType.")
    

class MtbTaxDisplayType(SQLAlchemyObjectType):
    """MtbTaxDisplayType node."""

    class Meta:
        model = ModelMtbTaxDisplayType
        interfaces = (graphene.relay.Node,)


class CreateMtbTaxDisplayTypeInput(graphene.InputObjectType, MtbTaxDisplayTypeAttribute):
    """Arguments to create a MtbTaxDisplayType."""
    pass


class CreateMtbTaxDisplayType(graphene.Mutation):
    """Mutation to create a MtbTaxDisplayType."""
    mtbTaxDisplayType = graphene.Field(lambda: MtbTaxDisplayType, description="MtbTaxDisplayType created by this mutation.")

    class Arguments:
        input = CreateMtbTaxDisplayTypeInput(required=True)

    def mutate(self, info, input):
        data = input_to_dictionary(input)
        data['created'] = datetime.utcnow()
        data['edited'] = datetime.utcnow()

        mtbTaxDisplayType = MtbTaxDisplayType(**data)
        db_session.add(mtbTaxDisplayType)
        db_session.commit()

        return CreateMtbTaxDisplayType(mtbTaxDisplayType=mtbTaxDisplayType)


class UpdateMtbTaxDisplayTypeInput(graphene.InputObjectType, MtbTaxDisplayTypeAttribute):
    """Arguments to update a MtbTaxDisplayType."""
    id = graphene.ID(required=True, description="Global Id of the MtbTaxDisplayType.")


class UpdateMtbTaxDisplayType(graphene.Mutation):
    """Update a person."""
    mtbTaxDisplayType = graphene.Field(lambda: MtbTaxDisplayType, description="MtbTaxDisplayType updated by this mutation.")

    class Arguments:
        input = UpdateMtbTaxDisplayTypeInput(required=True)

    def mutate(self, info, input):
        data = input_to_dictionary(input)
        data['edited'] = datetime.utcnow()

        mtbTaxDisplayType = db_session.query(MtbTaxDisplayType).filter_by(id=data['id'])
        mtbTaxDisplayType.update(data)
        db_session.commit()
        mtbTaxDisplayType = db_session.query(MtbTaxDisplayType).filter_by(id=data['id']).first()

        return UpdateMtbTaxDisplayType(mtbTaxDisplayType=mtbTaxDisplayType)