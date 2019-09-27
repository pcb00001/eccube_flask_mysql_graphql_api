import graphene
from datetime import datetime
from graphene_sqlalchemy import SQLAlchemyObjectType
from config.database import db_session
from models.model_mtb_authority import ModelMtbAuthority
from common.util.graphene_util import input_to_dictionary


# Create a generic class to mutualize description of people attributes for both queries and mutations
class MtbAuthorityAttribute:
    # example to create attribute name
    name = graphene.String(description="Name of the MtbAuthority.")
    

class MtbAuthority(SQLAlchemyObjectType):
    """MtbAuthority node."""

    class Meta:
        model = ModelMtbAuthority
        interfaces = (graphene.relay.Node,)


class CreateMtbAuthorityInput(graphene.InputObjectType, MtbAuthorityAttribute):
    """Arguments to create a MtbAuthority."""
    pass


class CreateMtbAuthority(graphene.Mutation):
    """Mutation to create a MtbAuthority."""
    mtbAuthority = graphene.Field(lambda: MtbAuthority, description="MtbAuthority created by this mutation.")

    class Arguments:
        input = CreateMtbAuthorityInput(required=True)

    def mutate(self, info, input):
        data = input_to_dictionary(input)
        data['created'] = datetime.utcnow()
        data['edited'] = datetime.utcnow()

        mtbAuthority = MtbAuthority(**data)
        db_session.add(mtbAuthority)
        db_session.commit()

        return CreateMtbAuthority(mtbAuthority=mtbAuthority)


class UpdateMtbAuthorityInput(graphene.InputObjectType, MtbAuthorityAttribute):
    """Arguments to update a MtbAuthority."""
    id = graphene.ID(required=True, description="Global Id of the MtbAuthority.")


class UpdateMtbAuthority(graphene.Mutation):
    """Update a person."""
    mtbAuthority = graphene.Field(lambda: MtbAuthority, description="MtbAuthority updated by this mutation.")

    class Arguments:
        input = UpdateMtbAuthorityInput(required=True)

    def mutate(self, info, input):
        data = input_to_dictionary(input)
        data['edited'] = datetime.utcnow()

        mtbAuthority = db_session.query(MtbAuthority).filter_by(id=data['id'])
        mtbAuthority.update(data)
        db_session.commit()
        mtbAuthority = db_session.query(MtbAuthority).filter_by(id=data['id']).first()

        return UpdateMtbAuthority(mtbAuthority=mtbAuthority)