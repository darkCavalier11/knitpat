import validictory
import json

validate_file = file("knitting_pattern_sample.json", "rb")
schema_file = file("knitting_pattern_schema.json", "rb")
data = json.load(validate_file)
schema = json.load(schema_file)
validictory.validate(data, schema)
