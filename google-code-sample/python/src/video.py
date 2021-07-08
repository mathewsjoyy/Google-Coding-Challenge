"""A video class."""

from _typeshed import NoneType
from typing import Sequence


class Video:
    """A class used to represent a Video."""

    def __init__(self, video_title: str, video_id: str, video_tags: Sequence[str]):
        """Video constructor."""
        self._title = video_title # The _ indicated private attribute so we shouldn't directly access them
        self._video_id = video_id
        self._flag = None

        # Turn the tags into a tuple here so it's unmodifiable,
        # in case the caller changes the 'video_tags' they passed to us
        self._tags = tuple(video_tags)

    @property
    def title(self) -> str: # -> str is used to specify our return type
        """Returns the title of a video."""
        return self._title

    @property
    def video_id(self) -> str:
        """Returns the video id of a video."""
        return self._video_id

    @property
    def tags(self) -> Sequence[str]:
        """Returns the list of tags of a video."""
        return self._tags
    
    @property
    def flag(self) -> str:
        """Returns the flag reason if any
        Flag tells if user doesn't like the video
        """
        return self._flag
    
    # Setter Method to set a custom flag message
    def set_flag(self, message):
        self._flag = message
    
    # What gets printed when printing a video
    def __str__(self):
        """What gets returned when printing object of Video"""
        flagged = ""
        if self.flag is not None:
            flagged = f" - FLAGGED (reason: {self.flag})"
        return f"{self.title} ({self.video_id}) [{' '.join(self._tags)}] {flagged}"     
