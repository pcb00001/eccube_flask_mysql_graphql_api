import graphene
from datetime import datetime
from graphene_sqlalchemy import SQLAlchemyObjectType
from config.database import db_session
from models.model_dtb_member import ModelDtbMember
from common.util.graphene_util import input_to_dictionary


# Create a generic class to mutualize description of people attributes for both queries and mutations
class DtbMemberAttribute:
    # example to create attribute name
    name = graphene.String(description="Name of the DtbMember.")
    

class DtbMember(SQLAlchemyObjectType):
    """DtbMember node."""

    class Meta:
        model = ModelDtbMember
        interfaces = (graphene.relay.Node,)


class CreateDtbMemberInput(graphene.InputObjectType, DtbMemberAttribute):
    """Arguments to create a DtbMember."""
    pass


class CreateDtbMember(graphene.Mutation):
    """Mutation to create a DtbMember."""
    dtbMember = graphene.Field(lambda: DtbMember, description="DtbMember created by this mutation.")

    class Arguments:
        input = CreateDtbMemberInput(required=True)

    def mutate(self, info, input):
        data = input_to_dictionary(input)
        data['created'] = datetime.utcnow()
        data['edited'] = datetime.utcnow()

        dtbMember = DtbMember(**data)
        db_session.add(dtbMember)
        db_session.commit()

        return CreateDtbMember(dtbMember=dtbMember)


class UpdateDtbMemberInput(graphene.InputObjectType, DtbMemberAttribute):
    """Arguments to update a DtbMember."""
    id = graphene.ID(required=True, description="Global Id of the DtbMember.")


class UpdateDtbMember(graphene.Mutation):
    """Update a person."""
    dtbMember = graphene.Field(lambda: DtbMember, description="DtbMember updated by this mutation.")

    class Arguments:
        input = UpdateDtbMemberInput(required=True)

    def mutate(self, info, input):
        data = input_to_dictionary(input)
        data['edited'] = datetime.utcnow()

        dtbMember = db_session.query(DtbMember).filter_by(id=data['id'])
        dtbMember.update(data)
        db_session.commit()
        dtbMember = db_session.query(DtbMember).filter_by(id=data['id']).first()

        return UpdateDtbMember(dtbMember=dtbMember)