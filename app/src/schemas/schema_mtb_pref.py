import graphene
from datetime import datetime
from graphene_sqlalchemy import SQLAlchemyObjectType
from config.database import db_session
from models.model_mtb_pref import ModelMtbPref
from common.util.graphene_util import input_to_dictionary


# Create a generic class to mutualize description of people attributes for both queries and mutations
class MtbPrefAttribute:
    # example to create attribute name
    name = graphene.String(description="Name of the MtbPref.")
    

class MtbPref(SQLAlchemyObjectType):
    """MtbPref node."""

    class Meta:
        model = ModelMtbPref
        interfaces = (graphene.relay.Node,)


class CreateMtbPrefInput(graphene.InputObjectType, MtbPrefAttribute):
    """Arguments to create a MtbPref."""
    pass


class CreateMtbPref(graphene.Mutation):
    """Mutation to create a MtbPref."""
    mtbPref = graphene.Field(lambda: MtbPref, description="MtbPref created by this mutation.")

    class Arguments:
        input = CreateMtbPrefInput(required=True)

    def mutate(self, info, input):
        data = input_to_dictionary(input)
        data['created'] = datetime.utcnow()
        data['edited'] = datetime.utcnow()

        mtbPref = MtbPref(**data)
        db_session.add(mtbPref)
        db_session.commit()

        return CreateMtbPref(mtbPref=mtbPref)


class UpdateMtbPrefInput(graphene.InputObjectType, MtbPrefAttribute):
    """Arguments to update a MtbPref."""
    id = graphene.ID(required=True, description="Global Id of the MtbPref.")


class UpdateMtbPref(graphene.Mutation):
    """Update a person."""
    mtbPref = graphene.Field(lambda: MtbPref, description="MtbPref updated by this mutation.")

    class Arguments:
        input = UpdateMtbPrefInput(required=True)

    def mutate(self, info, input):
        data = input_to_dictionary(input)
        data['edited'] = datetime.utcnow()

        mtbPref = db_session.query(MtbPref).filter_by(id=data['id'])
        mtbPref.update(data)
        db_session.commit()
        mtbPref = db_session.query(MtbPref).filter_by(id=data['id']).first()

        return UpdateMtbPref(mtbPref=mtbPref)