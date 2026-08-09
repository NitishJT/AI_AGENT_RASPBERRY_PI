from tools.system_tools import (
    get_system_info,
    open_terminal,
    open_browser,
    shutdown,
    reboot
)


TOOLS = {

    "system_info":
        get_system_info,

    "open_terminal":
        open_terminal,

    "open_browser":
        open_browser,

    "shutdown":
        shutdown,

    "reboot":
        reboot,
}


def execute_tool(tool_name, argument=None):

    tool = TOOLS.get(tool_name)

    if not tool:

        return f"I don't know how to use the tool {tool_name}."

    try:

        if argument:
            return tool(argument)

        return tool()

    except Exception as e:

        return f"Tool error: {e}"