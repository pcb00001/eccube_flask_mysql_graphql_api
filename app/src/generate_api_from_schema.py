import inspect
import os

import generate_config as config
import generate_util as util


importsContent = [
    "from graphene_sqlalchemy import SQLAlchemyConnectionField",
    "import graphene\n"
]

connectionsContent = []

queriesContent = [
    "\n\nclass Query(graphene.ObjectType):"
]


def import_packages(schema):
    importsContent.append("from {0}.schema_{1} import {2}".format(config.schema_folder, schema.lower(), util.convertSnackToPascal(schema)))


def create_connection(schema):
    content = inspect.cleandoc("""
                class {0}Connections(graphene.relay.Connection):
                    class Meta:
                        node = {0}""".format(util.convertSnackToPascal(schema)))
    connectionsContent.append("\n\n" + content)


def create_queries(schema):
    content = ("    # Get {0} by id\n"
               "    {1} = graphene.relay.Node.Field({0})\n"
               "    # List all {0}\n"
               "    getAll{0} = SQLAlchemyConnectionField({0}Connections)").format(util.convertSnackToPascal(schema), util.convertSnackToCamel(schema))
    queriesContent.append(content + "\n")


f = open("schema.py", "w+")

for model_file in os.listdir(config.model_folder):
    if model_file.endswith(".py"):
        class_name = model_file.replace("model_", "").split('.')[0]
        import_packages(class_name)
        create_connection(class_name)
        create_queries(class_name)

f.write(inspect.cleandoc(
    "\n".join(importsContent + connectionsContent + queriesContent + ["\nschema = graphene.Schema(query=Query)"])))
f.close()
