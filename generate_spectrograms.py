import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
import os

def generate_spectrogram(audio_path, output_path, duration=None):
    """Generate a full-length spectrogram from the entire audio file"""
    print(f"Loading audio: {audio_path}")
    
    # Load full audio
    y, sr = librosa.load(audio_path, sr=None)
    total_duration = len(y) / sr
    
    print(f"  Total duration: {total_duration:.2f}s")
    print(f"  Generating full-length spectrogram")
    
    # Compute STFT
    D = librosa.stft(y, n_fft=1024, hop_length=128)
    stft_db = librosa.amplitude_to_db(np.abs(D), ref=np.max)
    
    # Calculate width based on duration (wider for longer audio)
    # Use approximately 100 pixels per second for good detail
    width_in_inches = max(8, total_duration * 1.2)  # At least 8 inches, scale with duration
    
    # Create figure with dynamic width
    fig = plt.figure(figsize=(width_in_inches, 3), facecolor='none')
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
    plt.savefig(output_path, dpi=150, bbox_inches='tight', 
                pad_inches=0, transparent=False, facecolor='#1a1a2e')
    plt.close()
    
    print(f"✓ Saved full-length spectrogram: {output_path} ({width_in_inches:.1f} inches wide)")

if __name__ == "__main__":
    # Generate spectrograms for clean and noisy audio
    # audio_files = [
    #     ("static/clean_10_soul-groove10_102_4-4_bluebird.wav", 
    #      "static/images/spec_clean.png"),
    #     ("static/noisy_10_soul-groove10_102_4-4_bluebird_v1_noisy.wav", 
    #      "static/images/spec_noisy.png")
    # ]
    
    # # Add baseline folder spectrograms
    baseline_files = [
        "epoch=0_10_soul-groove10_102_4-4_bluebird_v1_noisy.wav",
        "epoch=10_10_soul-groove10_102_4-4_bluebird_v1_noisy.wav",
        "epoch=20_10_soul-groove10_102_4-4_bluebird_v1_noisy.wav",
        "epoch=30_10_soul-groove10_102_4-4_bluebird_v1_noisy.wav"
    ]
    audio_files = []
    epochs = [0, 10, 20, 30, 40, 50]
    for epoch in epochs:
        audio_path = f"static/audio/baseline/version_83/enhancement/use_midi=False_epoch_{epoch}/drummer1_1_funk-groove1_138_beat_4-4_bluebird.wav"
        output_path = f"static/images/baseline_epoch_{epoch}.png"
        audio_files.append((audio_path, output_path))
    
    for epoch in epochs:
        audio_path = f"static/audio/midi_conditioned/version_86/enhancement/use_midi=True_epoch_{epoch}/drummer1_1_funk-groove1_138_beat_4-4_bluebird.wav"
        output_path = f"static/images/midi_film_conditioned_epoch_{epoch}.png"
        audio_files.append((audio_path, output_path))

    # Add midi_conditioned folder spectrograms
    # midi_files = [
    #     "epoch=0_10_soul-groove10_102_4-4_bluebird_v1_noisy.wav",
    #     "epoch=10_10_soul-groove10_102_4-4_bluebird_v1_noisy.wav",
    #     "epoch=20_10_soul-groove10_102_4-4_bluebird_v1_noisy.wav",
    #     "epoch=30_10_soul-groove10_102_4-4_bluebird_v1_noisy.wav"
    # ]
    # audio_files =[]
    # velocities = [0, 1, 20, 40, 60, 80, 100, 127]
    # for velocity in velocities:
    #     filename = f"drummer1_1_funk-groove1_138_beat_4-4_bluebird_v{velocity}.wav"
    #     audio_path = f"static/audio/midi_conditioned/constant_velocity/v={velocity}/{filename}"
    #     output_path = f"static/images/midi_{filename.replace('.wav', '.png')}"
    #     audio_files.append((audio_path, output_path))
    
    # Add CFG spectrograms
    cfg_files = [
        # Baseline (w=0)
        ("static/audio/baseline/version_83/enhancement/use_midi=False_epoch_50/drummer1_1_funk-groove1_138_beat_4-4_bluebird.wav",
         "static/images/cfg_baseline.png"),
        # w=1.0
        ("static/audio/midi_conditioned/cfg/w_1.0/drummer1_1_funk-groove1_138_beat_4-4_bluebird.wav",
         "static/images/cfg_w_1.0.png"),
        # w=2.0
        ("static/audio/midi_conditioned/cfg/w_2.0/drummer1_1_funk-groove1_138_beat_4-4_bluebird.wav",
         "static/images/cfg_w_2.0.png"),
        # w=3.0
        ("static/audio/midi_conditioned/cfg/w_3.0/drummer1_1_funk-groove1_138_beat_4-4_bluebird.wav",
         "static/images/cfg_w_3.0.png"),
    ]
    audio_files.extend(cfg_files)

    for audio_path, output_path in audio_files:
        if os.path.exists(audio_path):
            generate_spectrogram(audio_path, output_path)
        else:
            print(f"Warning: Audio file not found: {audio_path}")
    
    print("\n✓ All spectrograms generated successfully!")
