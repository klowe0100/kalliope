from kalliope.core.Models.settings.SettingsEntry import SettingsEntry


class Tts(SettingsEntry):
    """
    This Class is representing a Text To Speech (TTS) with its name and parameters

    .. note:: must be defined in the settings.yml
    """

    def __init__(self, name=None, parameters=None):
        super(Tts, self).__init__(name=name)
        self.parameters = parameters

    def __str__(self):
        return str(self.serialize())

    def serialize(self):
        return {
            'name': self.name,
            'parameters': self.parameters
        }

    def __eq__(self, other):
        """
        This is used to compare 2 objects
        :param other: the Tts to compare
        :return: True if both ttss are similar, False otherwise
        """
        return self.__dict__ == other.__dict__
