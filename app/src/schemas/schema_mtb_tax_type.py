import graphene
from datetime import datetime
from graphene_sqlalchemy import SQLAlchemyObjectType
from config.database import db_session
from models.model_mtb_tax_type import ModelMtbTaxType
from common.util.graphene_util import input_to_dictionary


# Create a generic class to mutualize description of people attributes for both queries and mutations
class MtbTaxTypeAttribute:
    # example to create attribute name
    name = graphene.String(description="Name of the MtbTaxType.")
    

class MtbTaxType(SQLAlchemyObjectType):
    """MtbTaxType node."""

    class Meta:
        model = ModelMtbTaxType
        interfaces = (graphene.relay.Node,)


class CreateMtbTaxTypeInput(graphene.InputObjectType, MtbTaxTypeAttribute):
    """Arguments to create a MtbTaxType."""
    pass


class CreateMtbTaxType(graphene.Mutation):
    """Mutation to create a MtbTaxType."""
    mtbTaxType = graphene.Field(lambda: MtbTaxType, description="MtbTaxType created by this mutation.")

    class Arguments:
        input = CreateMtbTaxTypeInput(required=True)

    def mutate(self, info, input):
        data = input_to_dictionary(input)
        data['created'] = datetime.utcnow()
        data['edited'] = datetime.utcnow()

        mtbTaxType = MtbTaxType(**data)
        db_session.add(mtbTaxType)
        db_session.commit()

        return CreateMtbTaxType(mtbTaxType=mtbTaxType)


class UpdateMtbTaxTypeInput(graphene.InputObjectType, MtbTaxTypeAttribute):
    """Arguments to update a MtbTaxType."""
    id = graphene.ID(required=True, description="Global Id of the MtbTaxType.")


class UpdateMtbTaxType(graphene.Mutation):
    """Update a person."""
    mtbTaxType = graphene.Field(lambda: MtbTaxType, description="MtbTaxType updated by this mutation.")

    class Arguments:
        input = UpdateMtbTaxTypeInput(required=True)

    def mutate(self, info, input):
        data = input_to_dictionary(input)
        data['edited'] = datetime.utcnow()

        mtbTaxType = db_session.query(MtbTaxType).filter_by(id=data['id'])
        mtbTaxType.update(data)
        db_session.commit()
        mtbTaxType = db_session.query(MtbTaxType).filter_by(id=data['id']).first()

        return UpdateMtbTaxType(mtbTaxType=mtbTaxType)