import graphene
from datetime import datetime
from graphene_sqlalchemy import SQLAlchemyObjectType
from config.database import db_session
from models.model_dtb_page_layout import ModelDtbPageLayout
from common.util.graphene_util import input_to_dictionary


# Create a generic class to mutualize description of people attributes for both queries and mutations
class DtbPageLayoutAttribute:
    # example to create attribute name
    name = graphene.String(description="Name of the DtbPageLayout.")
    

class DtbPageLayout(SQLAlchemyObjectType):
    """DtbPageLayout node."""

    class Meta:
        model = ModelDtbPageLayout
        interfaces = (graphene.relay.Node,)


class CreateDtbPageLayoutInput(graphene.InputObjectType, DtbPageLayoutAttribute):
    """Arguments to create a DtbPageLayout."""
    pass


class CreateDtbPageLayout(graphene.Mutation):
    """Mutation to create a DtbPageLayout."""
    dtbPageLayout = graphene.Field(lambda: DtbPageLayout, description="DtbPageLayout created by this mutation.")

    class Arguments:
        input = CreateDtbPageLayoutInput(required=True)

    def mutate(self, info, input):
        data = input_to_dictionary(input)
        data['created'] = datetime.utcnow()
        data['edited'] = datetime.utcnow()

        dtbPageLayout = DtbPageLayout(**data)
        db_session.add(dtbPageLayout)
        db_session.commit()

        return CreateDtbPageLayout(dtbPageLayout=dtbPageLayout)


class UpdateDtbPageLayoutInput(graphene.InputObjectType, DtbPageLayoutAttribute):
    """Arguments to update a DtbPageLayout."""
    id = graphene.ID(required=True, description="Global Id of the DtbPageLayout.")


class UpdateDtbPageLayout(graphene.Mutation):
    """Update a person."""
    dtbPageLayout = graphene.Field(lambda: DtbPageLayout, description="DtbPageLayout updated by this mutation.")

    class Arguments:
        input = UpdateDtbPageLayoutInput(required=True)

    def mutate(self, info, input):
        data = input_to_dictionary(input)
        data['edited'] = datetime.utcnow()

        dtbPageLayout = db_session.query(DtbPageLayout).filter_by(id=data['id'])
        dtbPageLayout.update(data)
        db_session.commit()
        dtbPageLayout = db_session.query(DtbPageLayout).filter_by(id=data['id']).first()

        return UpdateDtbPageLayout(dtbPageLayout=dtbPageLayout)