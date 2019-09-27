import graphene
from datetime import datetime
from graphene_sqlalchemy import SQLAlchemyObjectType
from config.database import db_session
from models.model_dtb_mail_history import ModelDtbMailHistory
from common.util.graphene_util import input_to_dictionary


# Create a generic class to mutualize description of people attributes for both queries and mutations
class DtbMailHistoryAttribute:
    # example to create attribute name
    name = graphene.String(description="Name of the DtbMailHistory.")
    

class DtbMailHistory(SQLAlchemyObjectType):
    """DtbMailHistory node."""

    class Meta:
        model = ModelDtbMailHistory
        interfaces = (graphene.relay.Node,)


class CreateDtbMailHistoryInput(graphene.InputObjectType, DtbMailHistoryAttribute):
    """Arguments to create a DtbMailHistory."""
    pass


class CreateDtbMailHistory(graphene.Mutation):
    """Mutation to create a DtbMailHistory."""
    dtbMailHistory = graphene.Field(lambda: DtbMailHistory, description="DtbMailHistory created by this mutation.")

    class Arguments:
        input = CreateDtbMailHistoryInput(required=True)

    def mutate(self, info, input):
        data = input_to_dictionary(input)
        data['created'] = datetime.utcnow()
        data['edited'] = datetime.utcnow()

        dtbMailHistory = DtbMailHistory(**data)
        db_session.add(dtbMailHistory)
        db_session.commit()

        return CreateDtbMailHistory(dtbMailHistory=dtbMailHistory)


class UpdateDtbMailHistoryInput(graphene.InputObjectType, DtbMailHistoryAttribute):
    """Arguments to update a DtbMailHistory."""
    id = graphene.ID(required=True, description="Global Id of the DtbMailHistory.")


class UpdateDtbMailHistory(graphene.Mutation):
    """Update a person."""
    dtbMailHistory = graphene.Field(lambda: DtbMailHistory, description="DtbMailHistory updated by this mutation.")

    class Arguments:
        input = UpdateDtbMailHistoryInput(required=True)

    def mutate(self, info, input):
        data = input_to_dictionary(input)
        data['edited'] = datetime.utcnow()

        dtbMailHistory = db_session.query(DtbMailHistory).filter_by(id=data['id'])
        dtbMailHistory.update(data)
        db_session.commit()
        dtbMailHistory = db_session.query(DtbMailHistory).filter_by(id=data['id']).first()

        return UpdateDtbMailHistory(dtbMailHistory=dtbMailHistory)