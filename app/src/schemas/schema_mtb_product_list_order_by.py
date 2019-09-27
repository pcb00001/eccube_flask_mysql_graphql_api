import graphene
from datetime import datetime
from graphene_sqlalchemy import SQLAlchemyObjectType
from config.database import db_session
from models.model_mtb_product_list_order_by import ModelMtbProductListOrderBy
from common.util.graphene_util import input_to_dictionary


# Create a generic class to mutualize description of people attributes for both queries and mutations
class MtbProductListOrderByAttribute:
    # example to create attribute name
    name = graphene.String(description="Name of the MtbProductListOrderBy.")
    

class MtbProductListOrderBy(SQLAlchemyObjectType):
    """MtbProductListOrderBy node."""

    class Meta:
        model = ModelMtbProductListOrderBy
        interfaces = (graphene.relay.Node,)


class CreateMtbProductListOrderByInput(graphene.InputObjectType, MtbProductListOrderByAttribute):
    """Arguments to create a MtbProductListOrderBy."""
    pass


class CreateMtbProductListOrderBy(graphene.Mutation):
    """Mutation to create a MtbProductListOrderBy."""
    mtbProductListOrderBy = graphene.Field(lambda: MtbProductListOrderBy, description="MtbProductListOrderBy created by this mutation.")

    class Arguments:
        input = CreateMtbProductListOrderByInput(required=True)

    def mutate(self, info, input):
        data = input_to_dictionary(input)
        data['created'] = datetime.utcnow()
        data['edited'] = datetime.utcnow()

        mtbProductListOrderBy = MtbProductListOrderBy(**data)
        db_session.add(mtbProductListOrderBy)
        db_session.commit()

        return CreateMtbProductListOrderBy(mtbProductListOrderBy=mtbProductListOrderBy)


class UpdateMtbProductListOrderByInput(graphene.InputObjectType, MtbProductListOrderByAttribute):
    """Arguments to update a MtbProductListOrderBy."""
    id = graphene.ID(required=True, description="Global Id of the MtbProductListOrderBy.")


class UpdateMtbProductListOrderBy(graphene.Mutation):
    """Update a person."""
    mtbProductListOrderBy = graphene.Field(lambda: MtbProductListOrderBy, description="MtbProductListOrderBy updated by this mutation.")

    class Arguments:
        input = UpdateMtbProductListOrderByInput(required=True)

    def mutate(self, info, input):
        data = input_to_dictionary(input)
        data['edited'] = datetime.utcnow()

        mtbProductListOrderBy = db_session.query(MtbProductListOrderBy).filter_by(id=data['id'])
        mtbProductListOrderBy.update(data)
        db_session.commit()
        mtbProductListOrderBy = db_session.query(MtbProductListOrderBy).filter_by(id=data['id']).first()

        return UpdateMtbProductListOrderBy(mtbProductListOrderBy=mtbProductListOrderBy)