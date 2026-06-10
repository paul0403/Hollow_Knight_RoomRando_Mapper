import graphviz
from graphviz import Graph

from room_colors import get_room_and_text_color


class Transition:
    def __init__(self, from_room, exit_from_room, to_room, entry_to_room):
        self.from_room = from_room
        self.exit_from_room = exit_from_room
        self.to_room = to_room
        self.entry_to_room = entry_to_room

    def __eq__(self, other):
        if (
            self.from_room == other.to_room
            and self.exit_from_room == other.entry_to_room
        ):
            assert (
                self.entry_to_room == other.exit_from_room
                and self.to_room == other.from_room
            )
            return True
        return False

    def __hash__(self):
        return (
            hash(self.from_room)
            + hash(self.exit_from_room)
            + hash(self.to_room)
            + hash(self.entry_to_room)
        )

    def __str__(self):
        return f"From {self.from_room} through {self.exit_from_room} to {self.to_room} through {self.entry_to_room}"

    def __repr__(self):
        return str(self)


def parse_room_data(room_data):
    """
    Parses a string like
    '  Fungus2_19[top1]  -->  Deepnest_East_07[bot1]'
    i.e. a single line in raw data, into 2 `Transition` objects.
    """
    room1, room2 = room_data.replace("*", "").replace(" ", "").split("-->")
    return Transition(*room1.strip("]").split("["), *room2.strip("]").split("["))


def read_data(file):
    with open(file, "r") as f:
        lines = [l.strip("\n") for l in f.readlines()]
        _UNCHECKED_REACHABLE_TRANSITIONS = lines.index(
            "UNCHECKED REACHABLE TRANSITIONS"
        )
        _CHECKED_TRANSITIONS = lines.index("CHECKED TRANSITIONS")
        _REACHABLE_VANILLA_PLACEMENTS = lines.index("REACHABLE VANILLA PLACEMENTS")
        unchecked_transitions = lines[
            _UNCHECKED_REACHABLE_TRANSITIONS + 1 : _CHECKED_TRANSITIONS - 1
        ]
        checked_transitions = lines[
            _CHECKED_TRANSITIONS + 1 : _REACHABLE_VANILLA_PLACEMENTS - 1
        ]

    all_transitions = set()
    for t in checked_transitions:
        parsed_transition = parse_room_data(t)
        all_transitions.add(parsed_transition)

    for i, unchecked_transition in enumerate(unchecked_transitions):
        known_room, known_exit = (
            unchecked_transition.replace("*", "").replace(" ", "").strip("]").split("[")
        )
        to_unknown = Transition(known_room, known_exit, f"???_{i}", "???")
        all_transitions.add(to_unknown)

    return all_transitions


def draw(transitions):
    g = Graph(engine="neato")
    g.attr(forcelabels="true")

    g.attr(overlap="false")  # Forces nodes to push away from each other if they overlap
    g.attr(splines="true")  # Forces edges to curve  around nodes
    g.attr(sep="+15")  # Adds padding around every node margin
    g.attr(mindist="2.5")  # Minimum distance between two node centers

    # 1. Collect all rooms
    unique_rooms = set()
    for t in transitions:
        unique_rooms.add(t.from_room)
        unique_rooms.add(t.to_room)

    # 2. Set room colors
    for room in unique_rooms:
        room_color, text_color = get_room_and_text_color(room)
        g.node(
            room,
            style="filled",
            fillcolor=room_color,
            color="black",
            fontcolor=text_color,
        )

    # 3. Build graph edges
    for t in transitions:
        g.edge(
            t.from_room,
            t.to_room,
            taillabel=t.exit_from_room,
            headlabel=t.entry_to_room,
        )

    g.render(filename="map", view=True)


if __name__ == "__main__":
    all_checked_transitions = read_data("data.txt")
    draw(all_checked_transitions)
