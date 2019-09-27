import graphene
from datetime import datetime
from graphene_sqlalchemy import SQLAlchemyObjectType
from config.database import db_session
from models.model_mtb_sex import ModelMtbSex
from common.util.graphene_util import input_to_dictionary


# Create a generic class to mutualize description of people attributes for both queries and mutations
class MtbSexAttribute:
    # example to create attribute name
    name = graphene.String(description="Name of the MtbSex.")
    

class MtbSex(SQLAlchemyObjectType):
    """MtbSex node."""

    class Meta:
        model = ModelMtbSex
        interfaces = (graphene.relay.Node,)


class CreateMtbSexInput(graphene.InputObjectType, MtbSexAttribute):
    """Arguments to create a MtbSex."""
    pass


class CreateMtbSex(graphene.Mutation):
    """Mutation to create a MtbSex."""
    mtbSex = graphene.Field(lambda: MtbSex, description="MtbSex created by this mutation.")

    class Arguments:
        input = CreateMtbSexInput(required=True)

    def mutate(self, info, input):
        data = input_to_dictionary(input)
        data['created'] = datetime.utcnow()
        data['edited'] = datetime.utcnow()

        mtbSex = MtbSex(**data)
        db_session.add(mtbSex)
        db_session.commit()

        return CreateMtbSex(mtbSex=mtbSex)


class UpdateMtbSexInput(graphene.InputObjectType, MtbSexAttribute):
    """Arguments to update a MtbSex."""
    id = graphene.ID(required=True, description="Global Id of the MtbSex.")


class UpdateMtbSex(graphene.Mutation):
    """Update a person."""
    mtbSex = graphene.Field(lambda: MtbSex, description="MtbSex updated by this mutation.")

    class Arguments:
        input = UpdateMtbSexInput(required=True)

    def mutate(self, info, input):
        data = input_to_dictionary(input)
        data['edited'] = datetime.utcnow()

        mtbSex = db_session.query(MtbSex).filter_by(id=data['id'])
        mtbSex.update(data)
        db_session.commit()
        mtbSex = db_session.query(MtbSex).filter_by(id=data['id']).first()

        return UpdateMtbSex(mtbSex=mtbSex)