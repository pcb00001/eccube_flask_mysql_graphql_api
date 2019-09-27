import graphene
from datetime import datetime
from graphene_sqlalchemy import SQLAlchemyObjectType
from config.database import db_session
from models.model_mtb_order_status_color import ModelMtbOrderStatusColor
from common.util.graphene_util import input_to_dictionary


# Create a generic class to mutualize description of people attributes for both queries and mutations
class MtbOrderStatusColorAttribute:
    # example to create attribute name
    name = graphene.String(description="Name of the MtbOrderStatusColor.")
    

class MtbOrderStatusColor(SQLAlchemyObjectType):
    """MtbOrderStatusColor node."""

    class Meta:
        model = ModelMtbOrderStatusColor
        interfaces = (graphene.relay.Node,)


class CreateMtbOrderStatusColorInput(graphene.InputObjectType, MtbOrderStatusColorAttribute):
    """Arguments to create a MtbOrderStatusColor."""
    pass


class CreateMtbOrderStatusColor(graphene.Mutation):
    """Mutation to create a MtbOrderStatusColor."""
    mtbOrderStatusColor = graphene.Field(lambda: MtbOrderStatusColor, description="MtbOrderStatusColor created by this mutation.")

    class Arguments:
        input = CreateMtbOrderStatusColorInput(required=True)

    def mutate(self, info, input):
        data = input_to_dictionary(input)
        data['created'] = datetime.utcnow()
        data['edited'] = datetime.utcnow()

        mtbOrderStatusColor = MtbOrderStatusColor(**data)
        db_session.add(mtbOrderStatusColor)
        db_session.commit()

        return CreateMtbOrderStatusColor(mtbOrderStatusColor=mtbOrderStatusColor)


class UpdateMtbOrderStatusColorInput(graphene.InputObjectType, MtbOrderStatusColorAttribute):
    """Arguments to update a MtbOrderStatusColor."""
    id = graphene.ID(required=True, description="Global Id of the MtbOrderStatusColor.")


class UpdateMtbOrderStatusColor(graphene.Mutation):
    """Update a person."""
    mtbOrderStatusColor = graphene.Field(lambda: MtbOrderStatusColor, description="MtbOrderStatusColor updated by this mutation.")

    class Arguments:
        input = UpdateMtbOrderStatusColorInput(required=True)

    def mutate(self, info, input):
        data = input_to_dictionary(input)
        data['edited'] = datetime.utcnow()

        mtbOrderStatusColor = db_session.query(MtbOrderStatusColor).filter_by(id=data['id'])
        mtbOrderStatusColor.update(data)
        db_session.commit()
        mtbOrderStatusColor = db_session.query(MtbOrderStatusColor).filter_by(id=data['id']).first()

        return UpdateMtbOrderStatusColor(mtbOrderStatusColor=mtbOrderStatusColor)