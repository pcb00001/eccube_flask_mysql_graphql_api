import graphene
from datetime import datetime
from graphene_sqlalchemy import SQLAlchemyObjectType
from config.database import db_session
from models.model_dtb_template import ModelDtbTemplate
from common.util.graphene_util import input_to_dictionary


# Create a generic class to mutualize description of people attributes for both queries and mutations
class DtbTemplateAttribute:
    # example to create attribute name
    name = graphene.String(description="Name of the DtbTemplate.")
    

class DtbTemplate(SQLAlchemyObjectType):
    """DtbTemplate node."""

    class Meta:
        model = ModelDtbTemplate
        interfaces = (graphene.relay.Node,)


class CreateDtbTemplateInput(graphene.InputObjectType, DtbTemplateAttribute):
    """Arguments to create a DtbTemplate."""
    pass


class CreateDtbTemplate(graphene.Mutation):
    """Mutation to create a DtbTemplate."""
    dtbTemplate = graphene.Field(lambda: DtbTemplate, description="DtbTemplate created by this mutation.")

    class Arguments:
        input = CreateDtbTemplateInput(required=True)

    def mutate(self, info, input):
        data = input_to_dictionary(input)
        data['created'] = datetime.utcnow()
        data['edited'] = datetime.utcnow()

        dtbTemplate = DtbTemplate(**data)
        db_session.add(dtbTemplate)
        db_session.commit()

        return CreateDtbTemplate(dtbTemplate=dtbTemplate)


class UpdateDtbTemplateInput(graphene.InputObjectType, DtbTemplateAttribute):
    """Arguments to update a DtbTemplate."""
    id = graphene.ID(required=True, description="Global Id of the DtbTemplate.")


class UpdateDtbTemplate(graphene.Mutation):
    """Update a person."""
    dtbTemplate = graphene.Field(lambda: DtbTemplate, description="DtbTemplate updated by this mutation.")

    class Arguments:
        input = UpdateDtbTemplateInput(required=True)

    def mutate(self, info, input):
        data = input_to_dictionary(input)
        data['edited'] = datetime.utcnow()

        dtbTemplate = db_session.query(DtbTemplate).filter_by(id=data['id'])
        dtbTemplate.update(data)
        db_session.commit()
        dtbTemplate = db_session.query(DtbTemplate).filter_by(id=data['id']).first()

        return UpdateDtbTemplate(dtbTemplate=dtbTemplate)