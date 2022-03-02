class tv:
    def __init__(self, channel, volume_level, on = False):
        self.channel = channel
        self.volume_level = volume_level
        self.on = on

    def turn_on(self):
        self.on = True

    def turn_off(self):
        self.on = False

    def get_channel(self):
        return self.channel

    def set_channel(self, channel):
        self.channel = channel

    def get_volume(self):
        return self.volume_level

    def set_volume(self, volume):
        self.volume_level = volume

    def channel_up(self):
        self.channel += 1        

    def channel_down(self):
        self.channel -= 1

    def volume_up(self):
        self.volume_level += 1

    def volume_down(self):
        self.volume_level -= 1
