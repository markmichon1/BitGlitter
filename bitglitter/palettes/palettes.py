import datetime
import math


class AbstractPalette:
    """Setting a foundation for DefaultPalette and CustomPalette objects by defining some functionality.
    AbstractPalette is not meant to be instantiated, only it's children!
    """

    def __init__(self, name, description, color_set, color_distance):
        self.name = name
        self.description = description
        self.color_set = color_set
        self.color_distance = color_distance

        self.palette_id = None
        self.number_of_colors = len(self.color_set)
        self.bit_length = int(math.log(self.number_of_colors, 2))

        self.palette_type = None

    def __getitem__(self, item):
        return self.color_set[item]

    def __repr__(self):
        return f'{self.name} [{self.palette_type}]'


class DefaultPalette(AbstractPalette):
    """These are palettes that come default with BitGlitter.  They cannot be changed or removed."""

    def __init__(self, name, description, color_set, color_distance, palette_id):
        super().__init__(name, description, color_set, color_distance)
        self.palette_id = str(palette_id)
        self.palette_type = 'default'

    def __str__(self):
        return (f'Name: {self.name}\nIdentification Code: {str(self.palette_id)}\nDescription: {self.description}'
                f'\nBit Length: '
                f'{str(self.bit_length)}\nNumber of Colors: {str(self.number_of_colors)}'
                f'\nColor Set: {str(self.color_set)}'
                f'\nColor Distance: {str(self.color_distance)}\n')

    def return_as_dict(self):
        return {'name': self.name, 'description': self.description, 'color_set': self.color_set, 'color_distance':
            self.color_distance, 'id': self.palette_id, 'palette_type': self.palette_type, 'number_of_colors':
                    self.number_of_colors, 'bit_length': self.bit_length
                }


class CustomPalette(AbstractPalette):
    """This is what custom color palettes become.  It blindly accepts all values; all necessary checks are performed in
    add_custom_palette() in bitglitter.palettes.palettefunctions.
    """

    def __init__(self, name, description, color_set, color_distance, datetime_created, palette_id, nickname):
        super().__init__(name, description, color_set, color_distance)

        self.datetime_created = int(datetime_created)
        self.palette_id = palette_id
        self.nickname = nickname
        self.palette_type = 'custom'

    def __str__(self):
        return (f"Name: {self.name}\nIdentification Code: {str(self.palette_id)}\nNickname: {self.nickname}"
                f"\nDescription: "
                f"{self.description}"
                f"\nDate Created:"
                f" {datetime.datetime.fromtimestamp(self.datetime_created).strftime('%A, %B %d, %Y - %I:%M:%S %p')}"
                f"\nBit Length: {str(self.bit_length)}"
                f"\nNumber of Colors: {str(self.number_of_colors)}\nColor Set: {str(self.color_set)}"
                f"\nColor Distance: {str(self.color_distance)}\n")

    def return_as_dict(self):
        return {'name': self.name, 'description': self.description, 'color_set': self.color_set, 'color_distance':
            self.color_distance, 'datetime_created': self.datetime_created, 'id': self.palette_id, 'nickname':
                    self.nickname, 'palette_type': self.palette_type, 'number_of_colors': self.number_of_colors,
                'bit_length': self.bit_length}


class TwentyFourBitPalette:
    """This class doesn't function exactly like the other two classes.  You'll notice it takes no arguments and there
    are no colors in colorSet.  There is only one object that can exist of this class, because of the specific values
    needed.  This object is what represents the 24 bit color set.
    """

    def __init__(self):
        self.name = "24 bit default"
        self.description = "EXPERIMENTAL!  ~16.7 million colors.  This will only work in lossless" \
                           " environments, any sort of compression will corrupt the data."
        self.color_set = None
        self.number_of_colors = 16777216
        self.bit_length = 24
        self.id = str(self.bit_length)
        self.color_distance = 0
        self.palette_type = 'default'

    def __str__(self):
        return (f'Name: {self.name}\nIdentification Code: {str(self.id)}\nDescription: {self.description}\nBit Length: '
                f'{str(self.bit_length)}\nNumber of Colors: {str(self.number_of_colors)}\nColor Set: Too many '
                f'to list (see directly above)\nColor Distance: {str(self.color_distance)}\n')

    def return_as_dict(self):
        return {'name': self.name, 'description': self.description, 'color_set': self.color_set, 'color_distance':
            self.color_distance, 'id': self.id, 'palette_type': self.palette_type, 'number_of_colors':
                    self.number_of_colors, 'bit_length': self.bit_length
                }
