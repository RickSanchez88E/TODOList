document.addEventListener('DOMContentLoaded', () => {
    const audioPlayer = document.getElementById('audio-player');
    const playButton = document.querySelector('.play-button');
    const rewindButton = document.querySelector('.rewind-button');
    const forwardButton = document.querySelector('.fast-forward-button');
    const backButton = document.querySelector('.back-button');
    const skipButton = document.querySelector('.skip-button');
    const progressBar = document.querySelector('.progress-bar');
    const currentTimeDisplay = document.querySelector('.progress-time-current');
    const totalTimeDisplay = document.querySelector('.progress-time-total');

    // Set the total time
    audioPlayer.addEventListener('loadedmetadata', () => {
        const totalSeconds = audioPlayer.duration;
        totalTimeDisplay.textContent = formatTime(totalSeconds);
    });

    // Update progress bar
    audioPlayer.addEventListener('timeupdate', () => {
        const currentSeconds = audioPlayer.currentTime;
        const totalSeconds = audioPlayer.duration;
        currentTimeDisplay.textContent = formatTime(currentSeconds);
        progressBar.style.width = `${(currentSeconds / totalSeconds) * 100}%`;
    });

    // Play / Pause functionality
    playButton.addEventListener('click', () => {
        if (audioPlayer.paused) {
            audioPlayer.play();
            playButton.querySelector('i').classList.replace('fa-play', 'fa-pause');
            playButton.querySelector('.button-text').textContent = 'Pause';
        } else {
            audioPlayer.pause();
            playButton.querySelector('i').classList.replace('fa-pause', 'fa-play');
            playButton.querySelector('.button-text').textContent = 'Play';
        }
    });

    // Rewind functionality
    rewindButton.addEventListener('click', () => {
        audioPlayer.currentTime -= 10;
    });

    // Fast forward functionality
    forwardButton.addEventListener('click', () => {
        audioPlayer.currentTime += 10;
    });

    // Back to start
    backButton.addEventListener('click', () => {
        audioPlayer.currentTime = 0;
    });

    // Skip functionality
    skipButton.addEventListener('click', () => {
        audioPlayer.currentTime = audioPlayer.duration;
    });

    // Format time in mm:ss
    function formatTime(seconds) {
        const minutes = Math.floor(seconds / 60);
        seconds = Math.floor(seconds % 60);
        return `${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}`;
    }
});


function setSong(songName) {
            document.getElementById('selectedSong').value = songName;
            let songUrl = "{% url 'play_song' 'song_name_placeholder' %}".replace('song_name_placeholder', songName);
            document.getElementById('audioSource').src = songUrl;
            document.getElementById('audioPlayer').load();
        }