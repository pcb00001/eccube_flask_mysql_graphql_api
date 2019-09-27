import graphene
from datetime import datetime
from graphene_sqlalchemy import SQLAlchemyObjectType
from config.database import db_session
from models.model_dtb_plugin import ModelDtbPlugin
from common.util.graphene_util import input_to_dictionary


# Create a generic class to mutualize description of people attributes for both queries and mutations
class DtbPluginAttribute:
    # example to create attribute name
    name = graphene.String(description="Name of the DtbPlugin.")
    

class DtbPlugin(SQLAlchemyObjectType):
    """DtbPlugin node."""

    class Meta:
        model = ModelDtbPlugin
        interfaces = (graphene.relay.Node,)


class CreateDtbPluginInput(graphene.InputObjectType, DtbPluginAttribute):
    """Arguments to create a DtbPlugin."""
    pass


class CreateDtbPlugin(graphene.Mutation):
    """Mutation to create a DtbPlugin."""
    dtbPlugin = graphene.Field(lambda: DtbPlugin, description="DtbPlugin created by this mutation.")

    class Arguments:
        input = CreateDtbPluginInput(required=True)

    def mutate(self, info, input):
        data = input_to_dictionary(input)
        data['created'] = datetime.utcnow()
        data['edited'] = datetime.utcnow()

        dtbPlugin = DtbPlugin(**data)
        db_session.add(dtbPlugin)
        db_session.commit()

        return CreateDtbPlugin(dtbPlugin=dtbPlugin)


class UpdateDtbPluginInput(graphene.InputObjectType, DtbPluginAttribute):
    """Arguments to update a DtbPlugin."""
    id = graphene.ID(required=True, description="Global Id of the DtbPlugin.")


class UpdateDtbPlugin(graphene.Mutation):
    """Update a person."""
    dtbPlugin = graphene.Field(lambda: DtbPlugin, description="DtbPlugin updated by this mutation.")

    class Arguments:
        input = UpdateDtbPluginInput(required=True)

    def mutate(self, info, input):
        data = input_to_dictionary(input)
        data['edited'] = datetime.utcnow()

        dtbPlugin = db_session.query(DtbPlugin).filter_by(id=data['id'])
        dtbPlugin.update(data)
        db_session.commit()
        dtbPlugin = db_session.query(DtbPlugin).filter_by(id=data['id']).first()

        return UpdateDtbPlugin(dtbPlugin=dtbPlugin)