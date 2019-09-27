import graphene
from datetime import datetime
from graphene_sqlalchemy import SQLAlchemyObjectType
from config.database import db_session
from models.model_dtb_base_info import ModelDtbBaseInfo
from common.util.graphene_util import input_to_dictionary


# Create a generic class to mutualize description of people attributes for both queries and mutations
class DtbBaseInfoAttribute:
    # example to create attribute name
    name = graphene.String(description="Name of the DtbBaseInfo.")
    

class DtbBaseInfo(SQLAlchemyObjectType):
    """DtbBaseInfo node."""

    class Meta:
        model = ModelDtbBaseInfo
        interfaces = (graphene.relay.Node,)


class CreateDtbBaseInfoInput(graphene.InputObjectType, DtbBaseInfoAttribute):
    """Arguments to create a DtbBaseInfo."""
    pass


class CreateDtbBaseInfo(graphene.Mutation):
    """Mutation to create a DtbBaseInfo."""
    dtbBaseInfo = graphene.Field(lambda: DtbBaseInfo, description="DtbBaseInfo created by this mutation.")

    class Arguments:
        input = CreateDtbBaseInfoInput(required=True)

    def mutate(self, info, input):
        data = input_to_dictionary(input)
        data['created'] = datetime.utcnow()
        data['edited'] = datetime.utcnow()

        dtbBaseInfo = DtbBaseInfo(**data)
        db_session.add(dtbBaseInfo)
        db_session.commit()

        return CreateDtbBaseInfo(dtbBaseInfo=dtbBaseInfo)


class UpdateDtbBaseInfoInput(graphene.InputObjectType, DtbBaseInfoAttribute):
    """Arguments to update a DtbBaseInfo."""
    id = graphene.ID(required=True, description="Global Id of the DtbBaseInfo.")


class UpdateDtbBaseInfo(graphene.Mutation):
    """Update a person."""
    dtbBaseInfo = graphene.Field(lambda: DtbBaseInfo, description="DtbBaseInfo updated by this mutation.")

    class Arguments:
        input = UpdateDtbBaseInfoInput(required=True)

    def mutate(self, info, input):
        data = input_to_dictionary(input)
        data['edited'] = datetime.utcnow()

        dtbBaseInfo = db_session.query(DtbBaseInfo).filter_by(id=data['id'])
        dtbBaseInfo.update(data)
        db_session.commit()
        dtbBaseInfo = db_session.query(DtbBaseInfo).filter_by(id=data['id']).first()

        return UpdateDtbBaseInfo(dtbBaseInfo=dtbBaseInfo)