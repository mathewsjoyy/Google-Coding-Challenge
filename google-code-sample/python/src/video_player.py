"""A video player class."""

from .video_library import VideoLibrary
from random import choice # To get random video


class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        # Declaring certain attributes
        self._video_library = VideoLibrary()
        self._current_video = None
        self._paused = False


    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")


    def show_all_videos(self):
        """Returns all videos."""
        # Sort in lexicographical (alphabetically) order by title using - sorted(array, what to sort by)
        all_videos = sorted(self._video_library.get_all_videos(), key=lambda x: x.title)
        
        for video in all_videos:
            print(f"{video.title} ({video.video_id}) [{str(video.tags).strip('()')}]")


    def play_video(self, video_id):
        """Plays the respective video.
        Args:
            video_id: The video_id to be played.
        """
        
        video = self._video_library.get_video(video_id)
        
        if video is None:
            print('Cannot play video: Video does not not exist')
            return
        
        if self._current_video:
            self.stop_video()
            
        print(f"Playing video: {video.title}")
        self._current_video = video
        self._paused = False
        return


    def stop_video(self):
        """Stops the current video."""

        if self._current_video is None:
            print("Cannot stop video: No video is currently playing")
            return
        
        print(f"Stopping video: {self._current_video.title}")
        self._current_video = None
        return
        
        
    def play_random_video(self):
        """Plays a random video from the video library."""

        if len(self._video_library.get_all_videos()) < 1:
            print("No videos avaliable")
            return
        
        # Make an array of all videos
        all_videos = [video for video in self._video_library.get_all_videos()]
        
        # Call play_video we made earlier, we don't need to stop any existing video as that is handled in play_video
        self.play_video(choice(all_videos).video_id)

        
    def pause_video(self):
        """Pauses the current video."""
        if self._current_video is None:
            print("Cannot pause video: No video is currently playing")
            return
        
        if self._paused is True:
            print(f"Video already paused: {self._current_video.title}")
            return
                    
        print(f"Pausing video: {self._current_video.title}")
        self._paused = True
        return


    def continue_video(self):
        """Resumes playing the current video."""
        if self._current_video is None: # Check there us a video
            print(f"Cannot continue video: No video is currently playing")
            return
        elif self._paused is False: # Check video is actually paused
            print(f"Cannot continue video: Video is not paused")
            return
        
        print(f"Continuing video: {self._current_video.title}")
        self._paused = False
        return
        
        
    def show_playing(self):
        """Displays video currently playing."""
        if self._current_video is None:
            print("No video is currently playing")
            return
        
        # Displays all information
        print(f"Currently playing: {self._current_video.title} ({self._current_video.video_id}) \
[{str(self._current_video.tags).strip('()')}] {'- PAUSED' if self._paused else '- NOT PAUSED'}") # Sneeky way to show if paused or not
        return


    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("create_playlist needs implementation")









    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        print("add_to_playlist needs implementation")

    def show_all_playlists(self):
        """Display all playlists."""

        print("show_all_playlists needs implementation")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("show_playlist needs implementation")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        print("remove_from_playlist needs implementation")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("clears_playlist needs implementation")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("deletes_playlist needs implementation")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        print("search_videos needs implementation")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        print("search_videos_tag needs implementation")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
