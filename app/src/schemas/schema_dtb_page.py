import graphene
from datetime import datetime
from graphene_sqlalchemy import SQLAlchemyObjectType
from config.database import db_session
from models.model_dtb_page import ModelDtbPage
from common.util.graphene_util import input_to_dictionary


# Create a generic class to mutualize description of people attributes for both queries and mutations
class DtbPageAttribute:
    # example to create attribute name
    name = graphene.String(description="Name of the DtbPage.")
    

class DtbPage(SQLAlchemyObjectType):
    """DtbPage node."""

    class Meta:
        model = ModelDtbPage
        interfaces = (graphene.relay.Node,)


class CreateDtbPageInput(graphene.InputObjectType, DtbPageAttribute):
    """Arguments to create a DtbPage."""
    pass


class CreateDtbPage(graphene.Mutation):
    """Mutation to create a DtbPage."""
    dtbPage = graphene.Field(lambda: DtbPage, description="DtbPage created by this mutation.")

    class Arguments:
        input = CreateDtbPageInput(required=True)

    def mutate(self, info, input):
        data = input_to_dictionary(input)
        data['created'] = datetime.utcnow()
        data['edited'] = datetime.utcnow()

        dtbPage = DtbPage(**data)
        db_session.add(dtbPage)
        db_session.commit()

        return CreateDtbPage(dtbPage=dtbPage)


class UpdateDtbPageInput(graphene.InputObjectType, DtbPageAttribute):
    """Arguments to update a DtbPage."""
    id = graphene.ID(required=True, description="Global Id of the DtbPage.")


class UpdateDtbPage(graphene.Mutation):
    """Update a person."""
    dtbPage = graphene.Field(lambda: DtbPage, description="DtbPage updated by this mutation.")

    class Arguments:
        input = UpdateDtbPageInput(required=True)

    def mutate(self, info, input):
        data = input_to_dictionary(input)
        data['edited'] = datetime.utcnow()

        dtbPage = db_session.query(DtbPage).filter_by(id=data['id'])
        dtbPage.update(data)
        db_session.commit()
        dtbPage = db_session.query(DtbPage).filter_by(id=data['id']).first()

        return UpdateDtbPage(dtbPage=dtbPage)