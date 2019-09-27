import graphene
from datetime import datetime
from graphene_sqlalchemy import SQLAlchemyObjectType
from config.database import db_session
from models.model_dtb_tax_rule import ModelDtbTaxRule
from common.util.graphene_util import input_to_dictionary


# Create a generic class to mutualize description of people attributes for both queries and mutations
class DtbTaxRuleAttribute:
    # example to create attribute name
    name = graphene.String(description="Name of the DtbTaxRule.")
    

class DtbTaxRule(SQLAlchemyObjectType):
    """DtbTaxRule node."""

    class Meta:
        model = ModelDtbTaxRule
        interfaces = (graphene.relay.Node,)


class CreateDtbTaxRuleInput(graphene.InputObjectType, DtbTaxRuleAttribute):
    """Arguments to create a DtbTaxRule."""
    pass


class CreateDtbTaxRule(graphene.Mutation):
    """Mutation to create a DtbTaxRule."""
    dtbTaxRule = graphene.Field(lambda: DtbTaxRule, description="DtbTaxRule created by this mutation.")

    class Arguments:
        input = CreateDtbTaxRuleInput(required=True)

    def mutate(self, info, input):
        data = input_to_dictionary(input)
        data['created'] = datetime.utcnow()
        data['edited'] = datetime.utcnow()

        dtbTaxRule = DtbTaxRule(**data)
        db_session.add(dtbTaxRule)
        db_session.commit()

        return CreateDtbTaxRule(dtbTaxRule=dtbTaxRule)


class UpdateDtbTaxRuleInput(graphene.InputObjectType, DtbTaxRuleAttribute):
    """Arguments to update a DtbTaxRule."""
    id = graphene.ID(required=True, description="Global Id of the DtbTaxRule.")


class UpdateDtbTaxRule(graphene.Mutation):
    """Update a person."""
    dtbTaxRule = graphene.Field(lambda: DtbTaxRule, description="DtbTaxRule updated by this mutation.")

    class Arguments:
        input = UpdateDtbTaxRuleInput(required=True)

    def mutate(self, info, input):
        data = input_to_dictionary(input)
        data['edited'] = datetime.utcnow()

        dtbTaxRule = db_session.query(DtbTaxRule).filter_by(id=data['id'])
        dtbTaxRule.update(data)
        db_session.commit()
        dtbTaxRule = db_session.query(DtbTaxRule).filter_by(id=data['id']).first()

        return UpdateDtbTaxRule(dtbTaxRule=dtbTaxRule)