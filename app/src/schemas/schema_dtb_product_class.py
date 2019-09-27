import graphene
from datetime import datetime
from graphene_sqlalchemy import SQLAlchemyObjectType
from config.database import db_session
from models.model_dtb_product_class import ModelDtbProductClass
from common.util.graphene_util import input_to_dictionary


# Create a generic class to mutualize description of people attributes for both queries and mutations
class DtbProductClassAttribute:
    # example to create attribute name
    name = graphene.String(description="Name of the DtbProductClass.")
    

class DtbProductClass(SQLAlchemyObjectType):
    """DtbProductClass node."""

    class Meta:
        model = ModelDtbProductClass
        interfaces = (graphene.relay.Node,)


class CreateDtbProductClassInput(graphene.InputObjectType, DtbProductClassAttribute):
    """Arguments to create a DtbProductClass."""
    pass


class CreateDtbProductClass(graphene.Mutation):
    """Mutation to create a DtbProductClass."""
    dtbProductClass = graphene.Field(lambda: DtbProductClass, description="DtbProductClass created by this mutation.")

    class Arguments:
        input = CreateDtbProductClassInput(required=True)

    def mutate(self, info, input):
        data = input_to_dictionary(input)
        data['created'] = datetime.utcnow()
        data['edited'] = datetime.utcnow()

        dtbProductClass = DtbProductClass(**data)
        db_session.add(dtbProductClass)
        db_session.commit()

        return CreateDtbProductClass(dtbProductClass=dtbProductClass)


class UpdateDtbProductClassInput(graphene.InputObjectType, DtbProductClassAttribute):
    """Arguments to update a DtbProductClass."""
    id = graphene.ID(required=True, description="Global Id of the DtbProductClass.")


class UpdateDtbProductClass(graphene.Mutation):
    """Update a person."""
    dtbProductClass = graphene.Field(lambda: DtbProductClass, description="DtbProductClass updated by this mutation.")

    class Arguments:
        input = UpdateDtbProductClassInput(required=True)

    def mutate(self, info, input):
        data = input_to_dictionary(input)
        data['edited'] = datetime.utcnow()

        dtbProductClass = db_session.query(DtbProductClass).filter_by(id=data['id'])
        dtbProductClass.update(data)
        db_session.commit()
        dtbProductClass = db_session.query(DtbProductClass).filter_by(id=data['id']).first()

        return UpdateDtbProductClass(dtbProductClass=dtbProductClass)