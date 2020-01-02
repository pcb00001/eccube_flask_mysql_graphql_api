import inspect
import os
import generate_config as config
import generate_util as util

import_packages = ["import graphene"]
queries_class = []
mutation_class = []

f = open("schema.py", "w+")

for model_file in os.listdir(config.schema_folder):
    if model_file.endswith(".py"):
        schema_name = model_file.split('.')[0]
        import_packages.append("from {0} import {1}".format(config.schema_folder, schema_name))
        queries_class.append("{}.Query".format(schema_name))
        mutation_class.append("{}.Mutation".format(schema_name))

query_inherit = ("class Query(graphene.ObjectType,\n\t{}):"
                 "\n\tpass").format(",\n\t".join(queries_class))

mutation_inherit = ("class Mutation(graphene.ObjectType,\n\t{}):"
                 "\n\tpass").format(",\n\t".join(mutation_class))

# f.write(util.black.format_str(inspect.cleandoc(
#     "\n".join(import_packages + [query_inherit] + [mutation_inherit] + ["\nschema = graphene.Schema(query=Query, mutation=Mutation)"])),
#     mode=util.black.FileMode()))
f.write(util.black.format_str(inspect.cleandoc(
    "\n".join(import_packages + [query_inherit] + ["\nschema = graphene.Schema(query=Query)"])),
    mode=util.black.FileMode()))
f.close()
