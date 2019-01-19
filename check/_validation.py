#
# Validation methods
#
import sys
from lxml import etree

import check


def colored(color, text):
    colors = {
        'normal': '\033[0m',
        'warning': '\033[93m',
        'fail': '\033[91m',
        'bold': '\033[1m',
        'underline': '\033[4m',
    }
    return colors[color] + str(text) + colors['normal']


def schema_1_0(filename):
    """
    Validates ``filename`` against the CellML 1.0 schema, prints the result and
    then exits.
    """
    # Create lxml parser
    parser = etree.XMLParser(no_network=True)
    parser.resolvers.add(check.SchemaResolver())

    # Create xml object
    xml = etree.parse(filename, parser)

    # Create schema object
    schema = etree.XMLSchema(
        etree.parse(check.cellml_1_0('cellml_1_0.xsd'), parser))

    # Validate
    if schema.validate(xml):
        print(
            colored('warning', '[pass]')
            + ' This file validates against the schema.')
        sys.exit(0)
    else:
        print('[fail] This file does not validate against the schema.')
        print()
        print(schema.error_log.last_error)
        print()
        sys.exit(1)

