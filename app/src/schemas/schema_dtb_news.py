import graphene
from datetime import datetime
from graphene_sqlalchemy import SQLAlchemyObjectType
from config.database import db_session
from models.model_dtb_news import ModelDtbNews
from common.util.graphene_util import input_to_dictionary


# Create a generic class to mutualize description of people attributes for both queries and mutations
class DtbNewsAttribute:
    # example to create attribute name
    name = graphene.String(description="Name of the DtbNews.")
    

class DtbNews(SQLAlchemyObjectType):
    """DtbNews node."""

    class Meta:
        model = ModelDtbNews
        interfaces = (graphene.relay.Node,)


class CreateDtbNewsInput(graphene.InputObjectType, DtbNewsAttribute):
    """Arguments to create a DtbNews."""
    pass


class CreateDtbNews(graphene.Mutation):
    """Mutation to create a DtbNews."""
    dtbNews = graphene.Field(lambda: DtbNews, description="DtbNews created by this mutation.")

    class Arguments:
        input = CreateDtbNewsInput(required=True)

    def mutate(self, info, input):
        data = input_to_dictionary(input)
        data['created'] = datetime.utcnow()
        data['edited'] = datetime.utcnow()

        dtbNews = DtbNews(**data)
        db_session.add(dtbNews)
        db_session.commit()

        return CreateDtbNews(dtbNews=dtbNews)


class UpdateDtbNewsInput(graphene.InputObjectType, DtbNewsAttribute):
    """Arguments to update a DtbNews."""
    id = graphene.ID(required=True, description="Global Id of the DtbNews.")


class UpdateDtbNews(graphene.Mutation):
    """Update a person."""
    dtbNews = graphene.Field(lambda: DtbNews, description="DtbNews updated by this mutation.")

    class Arguments:
        input = UpdateDtbNewsInput(required=True)

    def mutate(self, info, input):
        data = input_to_dictionary(input)
        data['edited'] = datetime.utcnow()

        dtbNews = db_session.query(DtbNews).filter_by(id=data['id'])
        dtbNews.update(data)
        db_session.commit()
        dtbNews = db_session.query(DtbNews).filter_by(id=data['id']).first()

        return UpdateDtbNews(dtbNews=dtbNews)