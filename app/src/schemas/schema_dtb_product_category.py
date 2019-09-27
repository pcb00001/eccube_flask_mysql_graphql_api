import graphene
from datetime import datetime
from graphene_sqlalchemy import SQLAlchemyObjectType
from config.database import db_session
from models.model_dtb_product_category import ModelDtbProductCategory
from common.util.graphene_util import input_to_dictionary


# Create a generic class to mutualize description of people attributes for both queries and mutations
class DtbProductCategoryAttribute:
    # example to create attribute name
    name = graphene.String(description="Name of the DtbProductCategory.")
    

class DtbProductCategory(SQLAlchemyObjectType):
    """DtbProductCategory node."""

    class Meta:
        model = ModelDtbProductCategory
        interfaces = (graphene.relay.Node,)


class CreateDtbProductCategoryInput(graphene.InputObjectType, DtbProductCategoryAttribute):
    """Arguments to create a DtbProductCategory."""
    pass


class CreateDtbProductCategory(graphene.Mutation):
    """Mutation to create a DtbProductCategory."""
    dtbProductCategory = graphene.Field(lambda: DtbProductCategory, description="DtbProductCategory created by this mutation.")

    class Arguments:
        input = CreateDtbProductCategoryInput(required=True)

    def mutate(self, info, input):
        data = input_to_dictionary(input)
        data['created'] = datetime.utcnow()
        data['edited'] = datetime.utcnow()

        dtbProductCategory = DtbProductCategory(**data)
        db_session.add(dtbProductCategory)
        db_session.commit()

        return CreateDtbProductCategory(dtbProductCategory=dtbProductCategory)


class UpdateDtbProductCategoryInput(graphene.InputObjectType, DtbProductCategoryAttribute):
    """Arguments to update a DtbProductCategory."""
    id = graphene.ID(required=True, description="Global Id of the DtbProductCategory.")


class UpdateDtbProductCategory(graphene.Mutation):
    """Update a person."""
    dtbProductCategory = graphene.Field(lambda: DtbProductCategory, description="DtbProductCategory updated by this mutation.")

    class Arguments:
        input = UpdateDtbProductCategoryInput(required=True)

    def mutate(self, info, input):
        data = input_to_dictionary(input)
        data['edited'] = datetime.utcnow()

        dtbProductCategory = db_session.query(DtbProductCategory).filter_by(id=data['id'])
        dtbProductCategory.update(data)
        db_session.commit()
        dtbProductCategory = db_session.query(DtbProductCategory).filter_by(id=data['id']).first()

        return UpdateDtbProductCategory(dtbProductCategory=dtbProductCategory)