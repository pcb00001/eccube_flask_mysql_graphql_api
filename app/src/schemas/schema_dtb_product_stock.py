import graphene
from datetime import datetime
from graphene_sqlalchemy import SQLAlchemyObjectType
from config.database import db_session
from models.model_dtb_product_stock import ModelDtbProductStock
from common.util.graphene_util import input_to_dictionary


# Create a generic class to mutualize description of people attributes for both queries and mutations
class DtbProductStockAttribute:
    # example to create attribute name
    name = graphene.String(description="Name of the DtbProductStock.")
    

class DtbProductStock(SQLAlchemyObjectType):
    """DtbProductStock node."""

    class Meta:
        model = ModelDtbProductStock
        interfaces = (graphene.relay.Node,)


class CreateDtbProductStockInput(graphene.InputObjectType, DtbProductStockAttribute):
    """Arguments to create a DtbProductStock."""
    pass


class CreateDtbProductStock(graphene.Mutation):
    """Mutation to create a DtbProductStock."""
    dtbProductStock = graphene.Field(lambda: DtbProductStock, description="DtbProductStock created by this mutation.")

    class Arguments:
        input = CreateDtbProductStockInput(required=True)

    def mutate(self, info, input):
        data = input_to_dictionary(input)
        data['created'] = datetime.utcnow()
        data['edited'] = datetime.utcnow()

        dtbProductStock = DtbProductStock(**data)
        db_session.add(dtbProductStock)
        db_session.commit()

        return CreateDtbProductStock(dtbProductStock=dtbProductStock)


class UpdateDtbProductStockInput(graphene.InputObjectType, DtbProductStockAttribute):
    """Arguments to update a DtbProductStock."""
    id = graphene.ID(required=True, description="Global Id of the DtbProductStock.")


class UpdateDtbProductStock(graphene.Mutation):
    """Update a person."""
    dtbProductStock = graphene.Field(lambda: DtbProductStock, description="DtbProductStock updated by this mutation.")

    class Arguments:
        input = UpdateDtbProductStockInput(required=True)

    def mutate(self, info, input):
        data = input_to_dictionary(input)
        data['edited'] = datetime.utcnow()

        dtbProductStock = db_session.query(DtbProductStock).filter_by(id=data['id'])
        dtbProductStock.update(data)
        db_session.commit()
        dtbProductStock = db_session.query(DtbProductStock).filter_by(id=data['id']).first()

        return UpdateDtbProductStock(dtbProductStock=dtbProductStock)