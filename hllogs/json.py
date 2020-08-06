import json
from typing import List


def detect_in_string(value: str):
    """
    Detect (possible) JSON elements in a string
    :param value: text
    :return: possible JSON descriptions
    """

    position: int = 0
    while position < len(value):

        open_index: int = value.find('{', position)
        open_index_2: int = value.find('[', position)

        if open_index >= 0:
            if 0 <= open_index_2 < open_index:
                open_index = open_index_2
        elif open_index_2 >= 0:
            open_index = open_index_2
            pass

        if open_index < 0:
            break

        # locate matching closing bracket
        stack: List[str] = []
        located: bool = False
        for i in range(len(value) - open_index):
            if value[i + open_index] == "{":
                stack.append("{")
                continue
            elif value[i + open_index] == "[":
                stack.append("[")
                continue
            elif value[i + open_index] == "}":
                expect: str = "{"
            elif value[i + open_index] == "]":
                expect: str = "["
            else:
                continue

            val: str = stack.pop()
            if val != expect:
                # malformed
                break
            if len(stack) == 0:
                position = i + open_index + 1
                yield value[open_index:position]
                located = True
                break

        if not located:
            position = position + 1


def extract_json_attachments(value: str):
    for possible_json in detect_in_string(value):
        try:
            parsed = json.loads(possible_json)
            if len(parsed) > 0:
                yield json.dumps(parsed, indent=3, sort_keys=False)
        except ValueError:
            # ignore errors, since it's apparently not a valid JSON, so won't be added to the
            # list of displayed attachments
            pass
