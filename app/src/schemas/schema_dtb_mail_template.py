import graphene
from datetime import datetime
from graphene_sqlalchemy import SQLAlchemyObjectType
from config.database import db_session
from models.model_dtb_mail_template import ModelDtbMailTemplate
from common.util.graphene_util import input_to_dictionary


# Create a generic class to mutualize description of people attributes for both queries and mutations
class DtbMailTemplateAttribute:
    # example to create attribute name
    name = graphene.String(description="Name of the DtbMailTemplate.")
    

class DtbMailTemplate(SQLAlchemyObjectType):
    """DtbMailTemplate node."""

    class Meta:
        model = ModelDtbMailTemplate
        interfaces = (graphene.relay.Node,)


class CreateDtbMailTemplateInput(graphene.InputObjectType, DtbMailTemplateAttribute):
    """Arguments to create a DtbMailTemplate."""
    pass


class CreateDtbMailTemplate(graphene.Mutation):
    """Mutation to create a DtbMailTemplate."""
    dtbMailTemplate = graphene.Field(lambda: DtbMailTemplate, description="DtbMailTemplate created by this mutation.")

    class Arguments:
        input = CreateDtbMailTemplateInput(required=True)

    def mutate(self, info, input):
        data = input_to_dictionary(input)
        data['created'] = datetime.utcnow()
        data['edited'] = datetime.utcnow()

        dtbMailTemplate = DtbMailTemplate(**data)
        db_session.add(dtbMailTemplate)
        db_session.commit()

        return CreateDtbMailTemplate(dtbMailTemplate=dtbMailTemplate)


class UpdateDtbMailTemplateInput(graphene.InputObjectType, DtbMailTemplateAttribute):
    """Arguments to update a DtbMailTemplate."""
    id = graphene.ID(required=True, description="Global Id of the DtbMailTemplate.")


class UpdateDtbMailTemplate(graphene.Mutation):
    """Update a person."""
    dtbMailTemplate = graphene.Field(lambda: DtbMailTemplate, description="DtbMailTemplate updated by this mutation.")

    class Arguments:
        input = UpdateDtbMailTemplateInput(required=True)

    def mutate(self, info, input):
        data = input_to_dictionary(input)
        data['edited'] = datetime.utcnow()

        dtbMailTemplate = db_session.query(DtbMailTemplate).filter_by(id=data['id'])
        dtbMailTemplate.update(data)
        db_session.commit()
        dtbMailTemplate = db_session.query(DtbMailTemplate).filter_by(id=data['id']).first()

        return UpdateDtbMailTemplate(dtbMailTemplate=dtbMailTemplate)