import graphene
from datetime import datetime
from graphene_sqlalchemy import SQLAlchemyObjectType
from config.database import db_session
from models.model_mtb_csv_type import ModelMtbCsvType
from common.util.graphene_util import input_to_dictionary


# Create a generic class to mutualize description of people attributes for both queries and mutations
class MtbCsvTypeAttribute:
    # example to create attribute name
    name = graphene.String(description="Name of the MtbCsvType.")
    

class MtbCsvType(SQLAlchemyObjectType):
    """MtbCsvType node."""

    class Meta:
        model = ModelMtbCsvType
        interfaces = (graphene.relay.Node,)


class CreateMtbCsvTypeInput(graphene.InputObjectType, MtbCsvTypeAttribute):
    """Arguments to create a MtbCsvType."""
    pass


class CreateMtbCsvType(graphene.Mutation):
    """Mutation to create a MtbCsvType."""
    mtbCsvType = graphene.Field(lambda: MtbCsvType, description="MtbCsvType created by this mutation.")

    class Arguments:
        input = CreateMtbCsvTypeInput(required=True)

    def mutate(self, info, input):
        data = input_to_dictionary(input)
        data['created'] = datetime.utcnow()
        data['edited'] = datetime.utcnow()

        mtbCsvType = MtbCsvType(**data)
        db_session.add(mtbCsvType)
        db_session.commit()

        return CreateMtbCsvType(mtbCsvType=mtbCsvType)


class UpdateMtbCsvTypeInput(graphene.InputObjectType, MtbCsvTypeAttribute):
    """Arguments to update a MtbCsvType."""
    id = graphene.ID(required=True, description="Global Id of the MtbCsvType.")


class UpdateMtbCsvType(graphene.Mutation):
    """Update a person."""
    mtbCsvType = graphene.Field(lambda: MtbCsvType, description="MtbCsvType updated by this mutation.")

    class Arguments:
        input = UpdateMtbCsvTypeInput(required=True)

    def mutate(self, info, input):
        data = input_to_dictionary(input)
        data['edited'] = datetime.utcnow()

        mtbCsvType = db_session.query(MtbCsvType).filter_by(id=data['id'])
        mtbCsvType.update(data)
        db_session.commit()
        mtbCsvType = db_session.query(MtbCsvType).filter_by(id=data['id']).first()

        return UpdateMtbCsvType(mtbCsvType=mtbCsvType)