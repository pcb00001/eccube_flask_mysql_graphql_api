import graphene
from datetime import datetime
from graphene_sqlalchemy import SQLAlchemyObjectType
from config.database import db_session
from models.model_dtb_layout import ModelDtbLayout
from common.util.graphene_util import input_to_dictionary


# Create a generic class to mutualize description of people attributes for both queries and mutations
class DtbLayoutAttribute:
    # example to create attribute name
    name = graphene.String(description="Name of the DtbLayout.")
    

class DtbLayout(SQLAlchemyObjectType):
    """DtbLayout node."""

    class Meta:
        model = ModelDtbLayout
        interfaces = (graphene.relay.Node,)


class CreateDtbLayoutInput(graphene.InputObjectType, DtbLayoutAttribute):
    """Arguments to create a DtbLayout."""
    pass


class CreateDtbLayout(graphene.Mutation):
    """Mutation to create a DtbLayout."""
    dtbLayout = graphene.Field(lambda: DtbLayout, description="DtbLayout created by this mutation.")

    class Arguments:
        input = CreateDtbLayoutInput(required=True)

    def mutate(self, info, input):
        data = input_to_dictionary(input)
        data['created'] = datetime.utcnow()
        data['edited'] = datetime.utcnow()

        dtbLayout = DtbLayout(**data)
        db_session.add(dtbLayout)
        db_session.commit()

        return CreateDtbLayout(dtbLayout=dtbLayout)


class UpdateDtbLayoutInput(graphene.InputObjectType, DtbLayoutAttribute):
    """Arguments to update a DtbLayout."""
    id = graphene.ID(required=True, description="Global Id of the DtbLayout.")


class UpdateDtbLayout(graphene.Mutation):
    """Update a person."""
    dtbLayout = graphene.Field(lambda: DtbLayout, description="DtbLayout updated by this mutation.")

    class Arguments:
        input = UpdateDtbLayoutInput(required=True)

    def mutate(self, info, input):
        data = input_to_dictionary(input)
        data['edited'] = datetime.utcnow()

        dtbLayout = db_session.query(DtbLayout).filter_by(id=data['id'])
        dtbLayout.update(data)
        db_session.commit()
        dtbLayout = db_session.query(DtbLayout).filter_by(id=data['id']).first()

        return UpdateDtbLayout(dtbLayout=dtbLayout)