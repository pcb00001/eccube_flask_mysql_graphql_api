import graphene
from datetime import datetime
from graphene_sqlalchemy import SQLAlchemyObjectType
from config.database import db_session
from models.model_dtb_category import ModelDtbCategory
from common.util.graphene_util import input_to_dictionary


# Create a generic class to mutualize description of people attributes for both queries and mutations
class DtbCategoryAttribute:
    # example to create attribute name
    name = graphene.String(description="Name of the DtbCategory.")
    

class DtbCategory(SQLAlchemyObjectType):
    """DtbCategory node."""

    class Meta:
        model = ModelDtbCategory
        interfaces = (graphene.relay.Node,)


class CreateDtbCategoryInput(graphene.InputObjectType, DtbCategoryAttribute):
    """Arguments to create a DtbCategory."""
    pass


class CreateDtbCategory(graphene.Mutation):
    """Mutation to create a DtbCategory."""
    dtbCategory = graphene.Field(lambda: DtbCategory, description="DtbCategory created by this mutation.")

    class Arguments:
        input = CreateDtbCategoryInput(required=True)

    def mutate(self, info, input):
        data = input_to_dictionary(input)
        data['created'] = datetime.utcnow()
        data['edited'] = datetime.utcnow()

        dtbCategory = DtbCategory(**data)
        db_session.add(dtbCategory)
        db_session.commit()

        return CreateDtbCategory(dtbCategory=dtbCategory)


class UpdateDtbCategoryInput(graphene.InputObjectType, DtbCategoryAttribute):
    """Arguments to update a DtbCategory."""
    id = graphene.ID(required=True, description="Global Id of the DtbCategory.")


class UpdateDtbCategory(graphene.Mutation):
    """Update a person."""
    dtbCategory = graphene.Field(lambda: DtbCategory, description="DtbCategory updated by this mutation.")

    class Arguments:
        input = UpdateDtbCategoryInput(required=True)

    def mutate(self, info, input):
        data = input_to_dictionary(input)
        data['edited'] = datetime.utcnow()

        dtbCategory = db_session.query(DtbCategory).filter_by(id=data['id'])
        dtbCategory.update(data)
        db_session.commit()
        dtbCategory = db_session.query(DtbCategory).filter_by(id=data['id']).first()

        return UpdateDtbCategory(dtbCategory=dtbCategory)