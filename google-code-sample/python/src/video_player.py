"""A video player class."""

from .video_library import VideoLibrary
from .video_playlist import Playlist
from random import choice # To get random video


class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        # Declaring certain attributes
        self._video_library = VideoLibrary()
        self._current_video = None
        self._paused = False
        self._playlists = {}


    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")


    def show_all_videos(self):
        """Returns all videos."""
        # Sort in lexicographical (alphabetically) order by title using - sorted(array, what to sort by)
        all_videos = sorted(self._video_library.get_all_videos(), key=lambda x: x.title)
        
        for video in all_videos:
            print(video)


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
            
        if video.flag is not None:
            print(f"Cannot play video: Video is currently flagged (reason: {video.flag})")
            return
            
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
        if self._current_video is not None:
            self.stop_video()

        all_videos = [video for video in self._video_library.get_all_videos() if video.flag is None]
        if not all_videos: # Checks there are videos avaliable and they're not flagged
            print("No videos avaliable")
            return

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
        print(f"Currently playing: {self._current_video} {'- PAUSED' if self._paused else '- NOT PAUSED'}") # Sneeky way to show if paused or not
        return


    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.
        Args:
            playlist_name: The playlist name.
        """
        
        if playlist_name.lower().strip() in self._playlists: # Get rid of white space and lower chars
            print("Cannot create playlist: A playlist with the same name already exists")
            return
        
        print(f"Successfully created new playlist: {playlist_name}")
        self._playlists[playlist_name.lower().strip()] = Playlist(playlist_name) # Add to playlists new object of Playlist
        return


    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.
        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        video_to_add = self._video_library.get_video(video_id)
        
        if playlist_name.lower() not in self._playlists:
            print(f"Cannot add video to {playlist_name}: Playlist does not exist")
            return
        
        if video_to_add is None:
            print(f"Cannot add video to {playlist_name}: Video does not exist")
            return
        
        if video_to_add.flag is not None:
            print(f"Cannot add video to {playlist_name}: Video is currently flagged (reason: {video_to_add.flag})")
            return

        if video_to_add in self._playlists[playlist_name.lower()].videos:
            print(f"Cannot add video to {playlist_name}: Video already added")
            return
        
        self._playlists[playlist_name.lower()].videos.append(video_to_add) # Add video to playlist
        print(f"Added video to {playlist_name}: {video_to_add.title}") # Display playlist and video title 


    def show_all_playlists(self):
        """Display all playlists."""

        if not self._playlists: # If no playlists exit
            print("No playlists exist yet")
            return
        
        print("Showing all playlists:")
        for playlist in sorted(self._playlists): # Sort in lexicographical order
            print(f"{self._playlists[playlist].name}") # We don't do print(playlist) as this is the .lower version, we want the real name with .name
        return


    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.
        Args:
            playlist_name: The playlist name.
        """
        if playlist_name.lower() not in self._playlists:
            print(f"Cannot show playlist {playlist_name}: Playlist does not exist")
            return
        
        print(f"Showing playlist: {playlist_name}")
        if len(self._playlists[playlist_name.lower()].videos) < 1: # Check playlist has videos
            print("No videos here yet")
            return
        
        for video in self._playlists[playlist_name.lower()].videos:
            print(video)
        return
            
    
    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.
        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        the_video = self._video_library.get_video(video_id)
        
        if playlist_name.lower() not in self._playlists: # Check if play list exists
            print(f"Cannot remove video {playlist_name}: Playlist does not exist")
            return
        
        if the_video is None: # Check video even exists
            print(f"Cannot remove video from {playlist_name}: Video does not exist")
            return
        
        if the_video not in self._playlists[playlist_name.lower()].videos: # Check video is in playlist
            print(f"Cannot remove video from {playlist_name}: Video is not in playlist")
            return
        
        print(f"Removed video from {playlist_name}: {the_video.title}")
        self._playlists[playlist_name.lower()].videos.remove(the_video)
        return
        

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        
        if playlist_name.lower() not in self._playlists: # Check if play list exists
            print(f"Cannot clear playlist {playlist_name}: Playlist does not exist")
            return
        
        print(f"Successfully removed all videos from {playlist_name}")
        self._playlists[playlist_name.lower()].videos.clear()
        return
        

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.
        Args:
            playlist_name: The playlist name.
        """
        
        if playlist_name.lower() not in self._playlists: # Check if play list exists
            print(f"Cannot delete playlist {playlist_name}: Playlist does not exist")
            return
        
        print(f"Deleted playlist: {playlist_name}")
        self._playlists.pop(playlist_name.lower()) # cant use .remove in dict
        return


    def output_user_search_videos(self, videos, search_term):
        """ 2nd part! of search_videos function
        Args:
            videos: List of valid videos
            search_term: The query to be used in search.
        """
        if len(videos) == 0:
            print(f"No search results for {search_term}")
            return
        
        result = sorted(videos, key=lambda x:x.title) # Sorting the videos by title
        print(f"Here are the results for {search_term}:")
        
        for i, video in enumerate(result): # Simple way to loop over array and have a counter as well
            print(f"{i+1}) {video}") # Do + 1 otherwise it starts from 0
        
        print("Would you like to play any of the above? If yes, specify the number of the video.")
        print("If your answer is not a valid number, we will assume it's a no.")
        
        try:
            user_choice = int(input())
            if user_choice > 0 and user_choice <= len(videos): # See if its a valid range
                self.play_video(result[user_choice-1].video_id)
        except Exception:
            return
        return
        
    def search_videos(self, search_term):  # sourcery skip: list-comprehension
        """ 1st part!
        Display all the videos whose titles contain the search_term.
        Args:
            search_term: The query to be used in search.
        """
        valid_videos = [] # Keep track of found videos
        for video in self._video_library.get_all_videos():
            if video.flag is not None:
                continue
            if search_term.lower().strip() in video.title.lower():
                valid_videos.append(video)
        
        self.output_user_search_videos(valid_videos, search_term) # Call next function
    

    def search_videos_tag(self, video_tag):  # sourcery skip: list-comprehension
        """Display all videos whose tags contains the provided tag.
        Args:
            video_tag: The video tag to be used in search.
        """
        valid_videos = [] # Keep track of found videos
        for video in self._video_library.get_all_videos():
            if video.flag is not None:
                continue
            if video_tag.lower().strip() in video.tags:
                valid_videos.append(video)

        # We can just use the made function again as it still achieves desired result
        self.output_user_search_videos(valid_videos, video_tag)
        

    def flag_video(self, video_id, flag_reason="Not supplied"):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        
        video = self._video_library.get_video(video_id)
        
        if video is None:
            print("Cannot flag video: Video does not exist")
            return
            
        if video.flag is not None: # Check if video has already been flagged
            print("Cannot flag video: Video is already flagged")
            return
        
        video.set_flag(flag_reason)
        
        if self._current_video is not None and self._current_video.video_id == video.video_id: # Stop playing current video if its the flagged video
            self.stop_video()
        
        print(f"Successfully flagged video: {video.title} (reason: {flag_reason})")
        return
        

    def allow_video(self, video_id):
        """Removes a flag from a video.
        Args:
            video_id: The video_id to be allowed again.
        """
        
        video = self._video_library.get_video(video_id)
        
        if video is None:
            print("Cannot remove flag from video: Video does not exist")
            return
        
        if video.flag is None: # Check video has even been flagged yet
            print("Cannot remove flag from video: Video is not flagged")
            return
        
        print(f"Successfully removed flag from video: {video.title}")
        video.set_flag(None)
        return
        
        