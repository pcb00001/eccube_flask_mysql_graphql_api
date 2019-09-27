import graphene
from datetime import datetime
from graphene_sqlalchemy import SQLAlchemyObjectType
from config.database import db_session
from models.model_mtb_country import ModelMtbCountry
from common.util.graphene_util import input_to_dictionary


# Create a generic class to mutualize description of people attributes for both queries and mutations
class MtbCountryAttribute:
    # example to create attribute name
    name = graphene.String(description="Name of the MtbCountry.")
    

class MtbCountry(SQLAlchemyObjectType):
    """MtbCountry node."""

    class Meta:
        model = ModelMtbCountry
        interfaces = (graphene.relay.Node,)


class CreateMtbCountryInput(graphene.InputObjectType, MtbCountryAttribute):
    """Arguments to create a MtbCountry."""
    pass


class CreateMtbCountry(graphene.Mutation):
    """Mutation to create a MtbCountry."""
    mtbCountry = graphene.Field(lambda: MtbCountry, description="MtbCountry created by this mutation.")

    class Arguments:
        input = CreateMtbCountryInput(required=True)

    def mutate(self, info, input):
        data = input_to_dictionary(input)
        data['created'] = datetime.utcnow()
        data['edited'] = datetime.utcnow()

        mtbCountry = MtbCountry(**data)
        db_session.add(mtbCountry)
        db_session.commit()

        return CreateMtbCountry(mtbCountry=mtbCountry)


class UpdateMtbCountryInput(graphene.InputObjectType, MtbCountryAttribute):
    """Arguments to update a MtbCountry."""
    id = graphene.ID(required=True, description="Global Id of the MtbCountry.")


class UpdateMtbCountry(graphene.Mutation):
    """Update a person."""
    mtbCountry = graphene.Field(lambda: MtbCountry, description="MtbCountry updated by this mutation.")

    class Arguments:
        input = UpdateMtbCountryInput(required=True)

    def mutate(self, info, input):
        data = input_to_dictionary(input)
        data['edited'] = datetime.utcnow()

        mtbCountry = db_session.query(MtbCountry).filter_by(id=data['id'])
        mtbCountry.update(data)
        db_session.commit()
        mtbCountry = db_session.query(MtbCountry).filter_by(id=data['id']).first()

        return UpdateMtbCountry(mtbCountry=mtbCountry)