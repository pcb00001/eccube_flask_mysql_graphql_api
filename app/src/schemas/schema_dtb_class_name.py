import graphene
from datetime import datetime
from graphene_sqlalchemy import SQLAlchemyObjectType
from config.database import db_session
from models.model_dtb_class_name import ModelDtbClassName
from common.util.graphene_util import input_to_dictionary


# Create a generic class to mutualize description of people attributes for both queries and mutations
class DtbClassNameAttribute:
    # example to create attribute name
    name = graphene.String(description="Name of the DtbClassName.")
    

class DtbClassName(SQLAlchemyObjectType):
    """DtbClassName node."""

    class Meta:
        model = ModelDtbClassName
        interfaces = (graphene.relay.Node,)


class CreateDtbClassNameInput(graphene.InputObjectType, DtbClassNameAttribute):
    """Arguments to create a DtbClassName."""
    pass


class CreateDtbClassName(graphene.Mutation):
    """Mutation to create a DtbClassName."""
    dtbClassName = graphene.Field(lambda: DtbClassName, description="DtbClassName created by this mutation.")

    class Arguments:
        input = CreateDtbClassNameInput(required=True)

    def mutate(self, info, input):
        data = input_to_dictionary(input)
        data['created'] = datetime.utcnow()
        data['edited'] = datetime.utcnow()

        dtbClassName = DtbClassName(**data)
        db_session.add(dtbClassName)
        db_session.commit()

        return CreateDtbClassName(dtbClassName=dtbClassName)


class UpdateDtbClassNameInput(graphene.InputObjectType, DtbClassNameAttribute):
    """Arguments to update a DtbClassName."""
    id = graphene.ID(required=True, description="Global Id of the DtbClassName.")


class UpdateDtbClassName(graphene.Mutation):
    """Update a person."""
    dtbClassName = graphene.Field(lambda: DtbClassName, description="DtbClassName updated by this mutation.")

    class Arguments:
        input = UpdateDtbClassNameInput(required=True)

    def mutate(self, info, input):
        data = input_to_dictionary(input)
        data['edited'] = datetime.utcnow()

        dtbClassName = db_session.query(DtbClassName).filter_by(id=data['id'])
        dtbClassName.update(data)
        db_session.commit()
        dtbClassName = db_session.query(DtbClassName).filter_by(id=data['id']).first()

        return UpdateDtbClassName(dtbClassName=dtbClassName)