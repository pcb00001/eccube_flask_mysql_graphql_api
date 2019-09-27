import graphene
from datetime import datetime
from graphene_sqlalchemy import SQLAlchemyObjectType
from config.database import db_session
from models.model_dtb_authority_role import ModelDtbAuthorityRole
from common.util.graphene_util import input_to_dictionary


# Create a generic class to mutualize description of people attributes for both queries and mutations
class DtbAuthorityRoleAttribute:
    # example to create attribute name
    name = graphene.String(description="Name of the DtbAuthorityRole.")
    

class DtbAuthorityRole(SQLAlchemyObjectType):
    """DtbAuthorityRole node."""

    class Meta:
        model = ModelDtbAuthorityRole
        interfaces = (graphene.relay.Node,)


class CreateDtbAuthorityRoleInput(graphene.InputObjectType, DtbAuthorityRoleAttribute):
    """Arguments to create a DtbAuthorityRole."""
    pass


class CreateDtbAuthorityRole(graphene.Mutation):
    """Mutation to create a DtbAuthorityRole."""
    dtbAuthorityRole = graphene.Field(lambda: DtbAuthorityRole, description="DtbAuthorityRole created by this mutation.")

    class Arguments:
        input = CreateDtbAuthorityRoleInput(required=True)

    def mutate(self, info, input):
        data = input_to_dictionary(input)
        data['created'] = datetime.utcnow()
        data['edited'] = datetime.utcnow()

        dtbAuthorityRole = DtbAuthorityRole(**data)
        db_session.add(dtbAuthorityRole)
        db_session.commit()

        return CreateDtbAuthorityRole(dtbAuthorityRole=dtbAuthorityRole)


class UpdateDtbAuthorityRoleInput(graphene.InputObjectType, DtbAuthorityRoleAttribute):
    """Arguments to update a DtbAuthorityRole."""
    id = graphene.ID(required=True, description="Global Id of the DtbAuthorityRole.")


class UpdateDtbAuthorityRole(graphene.Mutation):
    """Update a person."""
    dtbAuthorityRole = graphene.Field(lambda: DtbAuthorityRole, description="DtbAuthorityRole updated by this mutation.")

    class Arguments:
        input = UpdateDtbAuthorityRoleInput(required=True)

    def mutate(self, info, input):
        data = input_to_dictionary(input)
        data['edited'] = datetime.utcnow()

        dtbAuthorityRole = db_session.query(DtbAuthorityRole).filter_by(id=data['id'])
        dtbAuthorityRole.update(data)
        db_session.commit()
        dtbAuthorityRole = db_session.query(DtbAuthorityRole).filter_by(id=data['id']).first()

        return UpdateDtbAuthorityRole(dtbAuthorityRole=dtbAuthorityRole)