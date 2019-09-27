import graphene
from datetime import datetime
from graphene_sqlalchemy import SQLAlchemyObjectType
from config.database import db_session
from models.model_dtb_class_category import ModelDtbClassCategory
from common.util.graphene_util import input_to_dictionary


# Create a generic class to mutualize description of people attributes for both queries and mutations
class DtbClassCategoryAttribute:
    # example to create attribute name
    name = graphene.String(description="Name of the DtbClassCategory.")
    

class DtbClassCategory(SQLAlchemyObjectType):
    """DtbClassCategory node."""

    class Meta:
        model = ModelDtbClassCategory
        interfaces = (graphene.relay.Node,)


class CreateDtbClassCategoryInput(graphene.InputObjectType, DtbClassCategoryAttribute):
    """Arguments to create a DtbClassCategory."""
    pass


class CreateDtbClassCategory(graphene.Mutation):
    """Mutation to create a DtbClassCategory."""
    dtbClassCategory = graphene.Field(lambda: DtbClassCategory, description="DtbClassCategory created by this mutation.")

    class Arguments:
        input = CreateDtbClassCategoryInput(required=True)

    def mutate(self, info, input):
        data = input_to_dictionary(input)
        data['created'] = datetime.utcnow()
        data['edited'] = datetime.utcnow()

        dtbClassCategory = DtbClassCategory(**data)
        db_session.add(dtbClassCategory)
        db_session.commit()

        return CreateDtbClassCategory(dtbClassCategory=dtbClassCategory)


class UpdateDtbClassCategoryInput(graphene.InputObjectType, DtbClassCategoryAttribute):
    """Arguments to update a DtbClassCategory."""
    id = graphene.ID(required=True, description="Global Id of the DtbClassCategory.")


class UpdateDtbClassCategory(graphene.Mutation):
    """Update a person."""
    dtbClassCategory = graphene.Field(lambda: DtbClassCategory, description="DtbClassCategory updated by this mutation.")

    class Arguments:
        input = UpdateDtbClassCategoryInput(required=True)

    def mutate(self, info, input):
        data = input_to_dictionary(input)
        data['edited'] = datetime.utcnow()

        dtbClassCategory = db_session.query(DtbClassCategory).filter_by(id=data['id'])
        dtbClassCategory.update(data)
        db_session.commit()
        dtbClassCategory = db_session.query(DtbClassCategory).filter_by(id=data['id']).first()

        return UpdateDtbClassCategory(dtbClassCategory=dtbClassCategory)