class OptionsParser:
    @staticmethod
    def parse_options(directions, enum_type):
        valid_directions = []
        for direction in directions:
            try:
                valid_directions.append(enum_type(direction))
            except ValueError:
                continue
        return valid_directions
