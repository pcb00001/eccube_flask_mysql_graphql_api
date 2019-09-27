import graphene
from datetime import datetime
from graphene_sqlalchemy import SQLAlchemyObjectType
from config.database import db_session
from models.model_mtb_sale_type import ModelMtbSaleType
from common.util.graphene_util import input_to_dictionary


# Create a generic class to mutualize description of people attributes for both queries and mutations
class MtbSaleTypeAttribute:
    # example to create attribute name
    name = graphene.String(description="Name of the MtbSaleType.")
    

class MtbSaleType(SQLAlchemyObjectType):
    """MtbSaleType node."""

    class Meta:
        model = ModelMtbSaleType
        interfaces = (graphene.relay.Node,)


class CreateMtbSaleTypeInput(graphene.InputObjectType, MtbSaleTypeAttribute):
    """Arguments to create a MtbSaleType."""
    pass


class CreateMtbSaleType(graphene.Mutation):
    """Mutation to create a MtbSaleType."""
    mtbSaleType = graphene.Field(lambda: MtbSaleType, description="MtbSaleType created by this mutation.")

    class Arguments:
        input = CreateMtbSaleTypeInput(required=True)

    def mutate(self, info, input):
        data = input_to_dictionary(input)
        data['created'] = datetime.utcnow()
        data['edited'] = datetime.utcnow()

        mtbSaleType = MtbSaleType(**data)
        db_session.add(mtbSaleType)
        db_session.commit()

        return CreateMtbSaleType(mtbSaleType=mtbSaleType)


class UpdateMtbSaleTypeInput(graphene.InputObjectType, MtbSaleTypeAttribute):
    """Arguments to update a MtbSaleType."""
    id = graphene.ID(required=True, description="Global Id of the MtbSaleType.")


class UpdateMtbSaleType(graphene.Mutation):
    """Update a person."""
    mtbSaleType = graphene.Field(lambda: MtbSaleType, description="MtbSaleType updated by this mutation.")

    class Arguments:
        input = UpdateMtbSaleTypeInput(required=True)

    def mutate(self, info, input):
        data = input_to_dictionary(input)
        data['edited'] = datetime.utcnow()

        mtbSaleType = db_session.query(MtbSaleType).filter_by(id=data['id'])
        mtbSaleType.update(data)
        db_session.commit()
        mtbSaleType = db_session.query(MtbSaleType).filter_by(id=data['id']).first()

        return UpdateMtbSaleType(mtbSaleType=mtbSaleType)