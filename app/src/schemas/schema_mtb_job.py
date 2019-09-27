import graphene
from datetime import datetime
from graphene_sqlalchemy import SQLAlchemyObjectType
from config.database import db_session
from models.model_mtb_job import ModelMtbJob
from common.util.graphene_util import input_to_dictionary


# Create a generic class to mutualize description of people attributes for both queries and mutations
class MtbJobAttribute:
    # example to create attribute name
    name = graphene.String(description="Name of the MtbJob.")
    

class MtbJob(SQLAlchemyObjectType):
    """MtbJob node."""

    class Meta:
        model = ModelMtbJob
        interfaces = (graphene.relay.Node,)


class CreateMtbJobInput(graphene.InputObjectType, MtbJobAttribute):
    """Arguments to create a MtbJob."""
    pass


class CreateMtbJob(graphene.Mutation):
    """Mutation to create a MtbJob."""
    mtbJob = graphene.Field(lambda: MtbJob, description="MtbJob created by this mutation.")

    class Arguments:
        input = CreateMtbJobInput(required=True)

    def mutate(self, info, input):
        data = input_to_dictionary(input)
        data['created'] = datetime.utcnow()
        data['edited'] = datetime.utcnow()

        mtbJob = MtbJob(**data)
        db_session.add(mtbJob)
        db_session.commit()

        return CreateMtbJob(mtbJob=mtbJob)


class UpdateMtbJobInput(graphene.InputObjectType, MtbJobAttribute):
    """Arguments to update a MtbJob."""
    id = graphene.ID(required=True, description="Global Id of the MtbJob.")


class UpdateMtbJob(graphene.Mutation):
    """Update a person."""
    mtbJob = graphene.Field(lambda: MtbJob, description="MtbJob updated by this mutation.")

    class Arguments:
        input = UpdateMtbJobInput(required=True)

    def mutate(self, info, input):
        data = input_to_dictionary(input)
        data['edited'] = datetime.utcnow()

        mtbJob = db_session.query(MtbJob).filter_by(id=data['id'])
        mtbJob.update(data)
        db_session.commit()
        mtbJob = db_session.query(MtbJob).filter_by(id=data['id']).first()

        return UpdateMtbJob(mtbJob=mtbJob)