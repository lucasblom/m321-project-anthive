from field import Field
import random
import json

class Map:
    """
    represents the map for the game world
    faktor 4
    """

    def __init__(self):
        self._width = 0
        self._height = 0
        self.fields = []

    import json

    def create_world(self, number_of_hives: int):
        """
        create the game world
        :param number_of_hives: the number of hives in the game
        :return: JSON string of hive locations
        """
        factor = 8
        self._width = number_of_hives * factor + 2
        self._height = number_of_hives * factor + 2
        self.fields = [[Field('ground', 0, 0, None) for _ in range(self._width)] for _ in range(self._height)]

        # Create water border
        for i in range(self._width):
            self.fields[0][i] = Field('water', 0, 0, None)
            self.fields[self._height - 1][i] = Field('water', 0, 0, None)
        for i in range(self._height):
            self.fields[i][0] = Field('water', 0, 0, None)
            self.fields[i][self._width - 1] = Field('water', 0, 0, None)

        # Position the anthills
        border_distance = 2
        hive_locations = []
        for i in range(number_of_hives):
            if i == 0:
                x, y = border_distance, border_distance
            else:
                x += border_distance
                if x >= self._width - border_distance:
                    x = self._width - border_distance
                    y += border_distance
                if y >= self._height - border_distance:
                    y = self._height - border_distance
                    x -= border_distance
            self.fields[y][x] = Field('hive', 0, 0, 'red')
            hive_locations.append({"xcoord": x, "ycoord": y})

        # Distribute the food
        for _ in range(number_of_hives):
            while True:
                x = random.randint(0, self._width - 1)
                y = random.randint(0, self._height - 1)
                if self.fields[y][x].type == 'ground':
                    self.fields[y][x].food = random.randint(1, 99)
                    break
        print(json.dumps(hive_locations))
        return json.dumps(hive_locations)

    def show_area(self, xcoord, ycoord, view_range):
        result = []
        try:
            for field in self.fields[ycoord - 2: ycoord + 2]:
                pass
        except:
            result.append(None)
        pass

if __name__ == '__main__':
    map = Map()
    map.create_world(8)
