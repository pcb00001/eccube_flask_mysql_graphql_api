import graphene
from datetime import datetime
from graphene_sqlalchemy import SQLAlchemyObjectType
from config.database import db_session
from models.model_mtb_work import ModelMtbWork
from common.util.graphene_util import input_to_dictionary


# Create a generic class to mutualize description of people attributes for both queries and mutations
class MtbWorkAttribute:
    # example to create attribute name
    name = graphene.String(description="Name of the MtbWork.")
    

class MtbWork(SQLAlchemyObjectType):
    """MtbWork node."""

    class Meta:
        model = ModelMtbWork
        interfaces = (graphene.relay.Node,)


class CreateMtbWorkInput(graphene.InputObjectType, MtbWorkAttribute):
    """Arguments to create a MtbWork."""
    pass


class CreateMtbWork(graphene.Mutation):
    """Mutation to create a MtbWork."""
    mtbWork = graphene.Field(lambda: MtbWork, description="MtbWork created by this mutation.")

    class Arguments:
        input = CreateMtbWorkInput(required=True)

    def mutate(self, info, input):
        data = input_to_dictionary(input)
        data['created'] = datetime.utcnow()
        data['edited'] = datetime.utcnow()

        mtbWork = MtbWork(**data)
        db_session.add(mtbWork)
        db_session.commit()

        return CreateMtbWork(mtbWork=mtbWork)


class UpdateMtbWorkInput(graphene.InputObjectType, MtbWorkAttribute):
    """Arguments to update a MtbWork."""
    id = graphene.ID(required=True, description="Global Id of the MtbWork.")


class UpdateMtbWork(graphene.Mutation):
    """Update a person."""
    mtbWork = graphene.Field(lambda: MtbWork, description="MtbWork updated by this mutation.")

    class Arguments:
        input = UpdateMtbWorkInput(required=True)

    def mutate(self, info, input):
        data = input_to_dictionary(input)
        data['edited'] = datetime.utcnow()

        mtbWork = db_session.query(MtbWork).filter_by(id=data['id'])
        mtbWork.update(data)
        db_session.commit()
        mtbWork = db_session.query(MtbWork).filter_by(id=data['id']).first()

        return UpdateMtbWork(mtbWork=mtbWork)