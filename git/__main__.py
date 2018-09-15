import sys
from decli import cli
from .commands import Add, Commit, Push

data = {
    "prog": "git",
    "description": "These are common Git commands used in various situations",
    "arguments": [
        {"name": ["-v", "--version"], "action": "store_true"},
        {"name": "--debug", "action": "store_true"},
    ],
    "subcommands": {
        "title": "main",
        "commands": [
            {
                "name": "add",
                "help": "Add file contents to the index",
                "func": Add,
                "arguments": [{"name": "--update", "action": "store_true"}],
            },
            {
                "name": "commit",
                "help": "Record changes to the repository",
                "func": Commit,
                "arguments": [
                    {
                        "name": "--amend",
                        "action": "store_true",
                        "help": (
                            "Replace the tip of the current "
                            "branch by creating a new commit."
                        ),
                    }
                ],
            },
            {
                "name": "push",
                "help": "Update remote refs along with associated objects",
                "func": Push,
                "arguments": [
                    {
                        "name": "--tags",
                        "action": "store_true",
                        "help": (
                            "All refs under refs/tags are pushed, in"
                            " addition to refspecs explicitly listed "
                            "on the command line."
                        ),
                    }
                ],
            },
        ],
    },
}

parser = cli(data)
args = parser.parse_args()

if args.version:
    print("0.1.0")
    sys.exit(0)

# print help if no arguments are provided
if len(sys.argv) < 2:
    parser.print_help()
    sys.exit()

cmd = args.func(**args.__dict__)
cmd.run()
