import re

# XML detecting regular expression
XML = re.compile(r"(?P<xml_candidate>(<\?[^>]*\?>[\s\t\n]*)?<([a-zA-Z][a-zA-Z:\-0-9]*).*?</\3>)", re.DOTALL)

# find white characters outside of XML tags
XML_CLEANUP = re.compile(r"([\s\n]+)<")


def indent(xml: str) -> str:
    """
    Dummy implementation of XML string indent. Might be improved at some point, but for now it'll have
    to suffice. We really want to avoid parsing/pretty-printing XML here, since this affects the XML
    contents in a way that might not be acceptable.
    :param xml: XML string
    :return: indented version
    """
    output_xml: str = ''
    indent_step: int = 3
    indentation: int = 0
    skip_next = False

    values = re.split('><', xml)
    for i in range(len(values)):
        if skip_next:
            skip_next = False
            continue
        value: str = values[i]
        if value[0] == '/':
            # closing tag
            indentation = indentation - indent_step
            output = '\n' + ''.rjust(indentation, ' ')
            output = output + '<' + value
        elif value[0] == '<':
            # first line
            output = ''.rjust(indentation, ' ')
            output = output + value
        else:
            # opening tag
            output = '\n' + ''.rjust(indentation, ' ')
            output = output + "<" + value
            if i < len(values) - 1:
                next_value: str = values[i + 1]
                if "/" + value == next_value:
                    skip_next = True
                    output = output + "><" + next_value
        if output[len(output) - 1] != ">":
            output = output + ">"
        if '</' not in output and value[len(value) - 1] != '/' and value[1] != "?" and value[0] != "!":
            indentation = indentation + indent_step
        output_xml = output_xml + output
    return output_xml


def extract_xml_attachments(value: str):
    # find all possible XML documents
    match = XML.findall(value)
    if match and len(match) > 0:
        for candidate in match:
            # clean-up / format / return
            yield indent(XML_CLEANUP.sub('', (candidate[0])))
