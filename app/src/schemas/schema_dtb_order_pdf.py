import graphene
from datetime import datetime
from graphene_sqlalchemy import SQLAlchemyObjectType
from config.database import db_session
from models.model_dtb_order_pdf import ModelDtbOrderPdf
from common.util.graphene_util import input_to_dictionary


# Create a generic class to mutualize description of people attributes for both queries and mutations
class DtbOrderPdfAttribute:
    # example to create attribute name
    name = graphene.String(description="Name of the DtbOrderPdf.")
    

class DtbOrderPdf(SQLAlchemyObjectType):
    """DtbOrderPdf node."""

    class Meta:
        model = ModelDtbOrderPdf
        interfaces = (graphene.relay.Node,)


class CreateDtbOrderPdfInput(graphene.InputObjectType, DtbOrderPdfAttribute):
    """Arguments to create a DtbOrderPdf."""
    pass


class CreateDtbOrderPdf(graphene.Mutation):
    """Mutation to create a DtbOrderPdf."""
    dtbOrderPdf = graphene.Field(lambda: DtbOrderPdf, description="DtbOrderPdf created by this mutation.")

    class Arguments:
        input = CreateDtbOrderPdfInput(required=True)

    def mutate(self, info, input):
        data = input_to_dictionary(input)
        data['created'] = datetime.utcnow()
        data['edited'] = datetime.utcnow()

        dtbOrderPdf = DtbOrderPdf(**data)
        db_session.add(dtbOrderPdf)
        db_session.commit()

        return CreateDtbOrderPdf(dtbOrderPdf=dtbOrderPdf)


class UpdateDtbOrderPdfInput(graphene.InputObjectType, DtbOrderPdfAttribute):
    """Arguments to update a DtbOrderPdf."""
    id = graphene.ID(required=True, description="Global Id of the DtbOrderPdf.")


class UpdateDtbOrderPdf(graphene.Mutation):
    """Update a person."""
    dtbOrderPdf = graphene.Field(lambda: DtbOrderPdf, description="DtbOrderPdf updated by this mutation.")

    class Arguments:
        input = UpdateDtbOrderPdfInput(required=True)

    def mutate(self, info, input):
        data = input_to_dictionary(input)
        data['edited'] = datetime.utcnow()

        dtbOrderPdf = db_session.query(DtbOrderPdf).filter_by(id=data['id'])
        dtbOrderPdf.update(data)
        db_session.commit()
        dtbOrderPdf = db_session.query(DtbOrderPdf).filter_by(id=data['id']).first()

        return UpdateDtbOrderPdf(dtbOrderPdf=dtbOrderPdf)