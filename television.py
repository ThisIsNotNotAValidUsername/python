class Television:
  # Declaration of class variables (Constants)
  MIN_VOLUME = 0
  MAX_VOLUME = 2
  MIN_CHANNEL = 0
  MAX_CHANNEL = 3

  def __init__(self) -> None:
    # Method to set default values
    self.__status = False
    self.__mute = False
    self.__channel = Television.MIN_CHANNEL
    self.__volume = Television.MIN_VOLUME

  def power(self) -> None:
    # Method to turn on/off the TV
    self.__status = not self.__status

  def mute(self) -> None:
    # Method to mute the TV
    if self.__status:
      self.__mute = not self.__mute

  def channel_up(self) -> None:
    # Method to increase channel
    if self.__status:
      if self.__channel == Television.MAX_CHANNEL:
        self.__channel = Television.MIN_CHANNEL
      else:
        self.__channel += 1

  def channel_down(self) -> None:
    # Method to decrease channel
    if self.__status:
      if self.__channel == Television.MIN_CHANNEL:
        self.__channel = Television.MAX_CHANNEL
      else:
        self.__channel -= 1

  def volume_up(self) -> None:
    # Method to increase TV volume
    if self.__status:
      if self.__mute:
        self.mute()
      if self.__volume != Television.MAX_VOLUME:
        self.__volume += 1

  def volume_down(self) -> None:
    # Method to reduce TV volume
    if self.__status:
      if self.__mute:
        self.mute()
      if self.__volume != Television.MIN_VOLUME:
        self.__volume -= 1

  def __str__(self) -> str:
  # Method to return TV status
    vol = self.__volume
    if self.__mute:
      vol = Television.MIN_VOLUME
    return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {vol}'