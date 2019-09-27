import inspect
import os

import generate_config as config
import generate_util as util


def create_schema(model_file_param):

    class_name = model_file_param.replace('model_', '').split('.')[0]
    schema_file = "schema_{0}.py".format(class_name)
    f = open(config.schema_folder + "/" + schema_file, "w+")

    content = """import graphene
            from datetime import datetime
            from graphene_sqlalchemy import SQLAlchemyObjectType
            from config.database import db_session
            from models.model_{2} import Model{0}
            from common.util.graphene_util import input_to_dictionary
            
            
            # Create a generic class to mutualize description of people attributes for both queries and mutations
            class {0}Attribute:
                # example to create attribute name
                name = graphene.String(description="Name of the {0}.")
                
            
            class {0}(SQLAlchemyObjectType):
                \"\"\"{0} node.\"\"\"
            
                class Meta:
                    model = Model{0}
                    interfaces = (graphene.relay.Node,)
            
            
            class Create{0}Input(graphene.InputObjectType, {0}Attribute):
                \"\"\"Arguments to create a {0}.\"\"\"
                pass
            
            
            class Create{0}(graphene.Mutation):
                \"\"\"Mutation to create a {0}.\"\"\"
                {1} = graphene.Field(lambda: {0}, description="{0} created by this mutation.")
            
                class Arguments:
                    input = Create{0}Input(required=True)
            
                def mutate(self, info, input):
                    data = input_to_dictionary(input)
                    data['created'] = datetime.utcnow()
                    data['edited'] = datetime.utcnow()
            
                    {1} = {0}(**data)
                    db_session.add({1})
                    db_session.commit()
            
                    return Create{0}({1}={1})
            
            
            class Update{0}Input(graphene.InputObjectType, {0}Attribute):
                \"\"\"Arguments to update a {0}.\"\"\"
                id = graphene.ID(required=True, description="Global Id of the {0}.")
            
            
            class Update{0}(graphene.Mutation):
                \"\"\"Update a person.\"\"\"
                {1} = graphene.Field(lambda: {0}, description="{0} updated by this mutation.")
            
                class Arguments:
                    input = Update{0}Input(required=True)
            
                def mutate(self, info, input):
                    data = input_to_dictionary(input)
                    data['edited'] = datetime.utcnow()
            
                    {1} = db_session.query({0}).filter_by(id=data['id'])
                    {1}.update(data)
                    db_session.commit()
                    {1} = db_session.query({0}).filter_by(id=data['id']).first()
            
                    return Update{0}({1}={1})""".format(util.convertSnackToPascal(class_name), util.convertSnackToCamel(class_name), class_name)

    f.write(inspect.cleandoc(content))
    f.close()


for model_file in os.listdir(config.model_folder):
    if model_file.endswith(".py"):
        create_schema(model_file)
