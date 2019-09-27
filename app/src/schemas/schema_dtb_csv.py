import graphene
from datetime import datetime
from graphene_sqlalchemy import SQLAlchemyObjectType
from config.database import db_session
from models.model_dtb_csv import ModelDtbCsv
from common.util.graphene_util import input_to_dictionary


# Create a generic class to mutualize description of people attributes for both queries and mutations
class DtbCsvAttribute:
    # example to create attribute name
    name = graphene.String(description="Name of the DtbCsv.")
    

class DtbCsv(SQLAlchemyObjectType):
    """DtbCsv node."""

    class Meta:
        model = ModelDtbCsv
        interfaces = (graphene.relay.Node,)


class CreateDtbCsvInput(graphene.InputObjectType, DtbCsvAttribute):
    """Arguments to create a DtbCsv."""
    pass


class CreateDtbCsv(graphene.Mutation):
    """Mutation to create a DtbCsv."""
    dtbCsv = graphene.Field(lambda: DtbCsv, description="DtbCsv created by this mutation.")

    class Arguments:
        input = CreateDtbCsvInput(required=True)

    def mutate(self, info, input):
        data = input_to_dictionary(input)
        data['created'] = datetime.utcnow()
        data['edited'] = datetime.utcnow()

        dtbCsv = DtbCsv(**data)
        db_session.add(dtbCsv)
        db_session.commit()

        return CreateDtbCsv(dtbCsv=dtbCsv)


class UpdateDtbCsvInput(graphene.InputObjectType, DtbCsvAttribute):
    """Arguments to update a DtbCsv."""
    id = graphene.ID(required=True, description="Global Id of the DtbCsv.")


class UpdateDtbCsv(graphene.Mutation):
    """Update a person."""
    dtbCsv = graphene.Field(lambda: DtbCsv, description="DtbCsv updated by this mutation.")

    class Arguments:
        input = UpdateDtbCsvInput(required=True)

    def mutate(self, info, input):
        data = input_to_dictionary(input)
        data['edited'] = datetime.utcnow()

        dtbCsv = db_session.query(DtbCsv).filter_by(id=data['id'])
        dtbCsv.update(data)
        db_session.commit()
        dtbCsv = db_session.query(DtbCsv).filter_by(id=data['id']).first()

        return UpdateDtbCsv(dtbCsv=dtbCsv)