import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
import os

def generate_spectrogram(audio_path, output_path, duration=2.5):
    """Generate a compact spectrogram from the middle of the audio file"""
    print(f"Loading audio: {audio_path}")
    
    # Load full audio to get duration
    y_full, sr = librosa.load(audio_path, sr=None)
    total_duration = len(y_full) / sr
    
    # Calculate middle section
    start_time = (total_duration - duration) / 2
    end_time = start_time + duration
    
    print(f"  Total duration: {total_duration:.2f}s")
    print(f"  Extracting middle: {start_time:.2f}s to {end_time:.2f}s")
    
    # Load only the middle section
    y, sr = librosa.load(audio_path, sr=None, offset=start_time, duration=duration)
    
    # Compute STFT
    D = librosa.stft(y, n_fft=2048, hop_length=512)
    stft_db = librosa.amplitude_to_db(np.abs(D), ref=np.max)
    
    # Create compact square-ish figure
    fig = plt.figure(figsize=(4, 3), facecolor='none')
    ax = fig.add_subplot(111)
    
    # Plot spectrogram with better color scheme
    img = librosa.display.specshow(stft_db, x_axis='time', y_axis='log', 
                                    ax=ax, sr=sr, cmap='magma')
    
    # Remove axes for cleaner look
    ax.set_xlabel('')
    ax.set_ylabel('')
    ax.set_xticks([])
    ax.set_yticks([])
    
    # Remove frame
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)
    
    # Save with tight layout
    plt.tight_layout(pad=0)
    plt.savefig(output_path, dpi=120, bbox_inches='tight', 
                pad_inches=0, transparent=False, facecolor='#1a1a2e')
    plt.close()
    
    print(f"✓ Saved compact spectrogram: {output_path}")

if __name__ == "__main__":
    # Generate spectrograms for clean and noisy audio
    audio_files = [
        ("static/clean_10_soul-groove10_102_4-4_bluebird.wav", 
         "static/images/spec_clean.png"),
        ("static/noisy_10_soul-groove10_102_4-4_bluebird_v1_noisy.wav", 
         "static/images/spec_noisy.png")
    ]
    
    for audio_path, output_path in audio_files:
        if os.path.exists(audio_path):
            generate_spectrogram(audio_path, output_path)
        else:
            print(f"Warning: Audio file not found: {audio_path}")
    
    print("\n✓ All spectrograms generated successfully!")
