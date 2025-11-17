# Tone.js

> Web Audio Framework for creating interactive music in the browser

## Overview

Tone.js is a Web Audio Framework that provides objects for generating, processing, and scheduling audio directly in the browser. It enables web applications to create complex interactive musical experiences and audio applications.

The framework manages the underlying Web Audio API context, ensuring consistent audio processing across different environments. It includes a precise global timing and transport system that orchestrates musical events and tempo changes. High-performance audio processing integrates with Web Audio AudioWorklet Integration for High Performance.

Audio signal generation starts with fundamental building blocks such as oscillators, noise generators, and sample players. These sources combine and modify using core Digital Signal Processing (DSP) operations. Signal parameters can be automated over time, allowing for dynamic sound shaping.

The library offers a collection of pre-built musical instruments, including various synthesizers and samplers. These instruments produce melodic and harmonic content, with capabilities for polyphonic playback and voice management.

A diverse range of audio effects and processing components are available for sonic manipulation. These include filters, modulation effects, distortion, and delays, alongside real-time signal analysis tools and dynamic range processors. Effects typically incorporate dry/wet mixing and feedback loops for versatile sound design.

Precise event scheduling and sequencing mechanisms allow for the creation of intricate musical patterns. These systems manage individual events, collections of events, and algorithmic pattern generation.

## Web Audio Framework Core

The Tone.js library provides a foundational architecture for Web Audio applications, managing audio context, base classes for all audio objects, precise timing, and high-performance audio processing through AudioWorklets. These core components enable the creation and extension of the framework for interactive music experiences.

### Context Management

Central to Tone.js is its approach to context management. The library abstracts the native Web Audio API `AudioContext` and `OfflineAudioContext` into `Context` and `OfflineContext` classes, ensuring consistent behavior across different environments and facilitating non-realtime audio rendering.

The Global utility provides a singular point for managing the active audio context, including methods to retrieve the current context and ensure it is properly started, addressing browser autoplay policies.

A key feature, implemented by the `Tone/fromContext.ts` utility, allows for the creation of independent Tone.js environments, each bound to its own audio context. This mechanism enables developers to run multiple, isolated audio graphs within a single application, preventing global state conflicts by dynamically overriding the `defaultContext` property of newly instantiated Tone.js objects.

### Base Classes

All audio-related objects within Tone.js inherit from the abstract `Tone` class, defined in `Tone/core/Tone.ts`. This base class establishes common properties and methods, such as version tracking, debugging utilities, and a standardized resource cleanup mechanism via its `dispose` method.

`ToneAudioNode` further extends this concept, serving as the base for all audio processing nodes, standardizing connections and channel control within the audio graph.

### Timing and Transport

Tone.js implements a comprehensive timing and scheduling system, critical for musical applications. The `Transport` acts as the global musical timeline, orchestrating:
- BPM (beats per minute)
- Time signature
- Event scheduling
- Looping
- Overall playback control

It relies on internal components such as:
- `Clock` for rhythmic pulsing
- `TickSource` for tracking musical time (in ticks and seconds)
- `Timeline` structures for managing time-ordered events

This system allows for precise scheduling of musical events and dynamic changes to the musical timeline.

### Parameter Automation

Advanced control over AudioParams is provided by `AbstractParam` and `Param`. These classes offer enhanced automation capabilities, allowing for:
- Precise scheduling of value changes
- Ramp automation
- Unit conversions directly within the Web Audio graph

This ensures smooth and musically expressive parameter modulation.

### AudioWorklet Integration

For high-performance audio processing, Tone.js integrates with Web Audio AudioWorklets. The `Tone/core/worklet` directory contains the architecture for this integration, including:
- `ToneAudioWorklet` as an abstract base class for worklet nodes
- `WorkletGlobalScope` for managing code injection into the worklet's global scope
- Specialized processors like `SingleIOProcessor` and `DelayLine`

These components facilitate block-level audio processing with minimal latency.

### Utility Functions

The `Tone/core` directory also provides a rich set of utility functions and type definitions crucial for robust audio development. These include:
- Runtime type-checking
- Debugging tools
- Property decorators for value constraints
- Default argument handling
- Event emission
- Various timeline management classes that underpin the scheduling mechanisms

These foundational elements ensure consistency, precision, and extensibility throughout the Tone.js library.

## Context Management and Offline Rendering

Tone.js establishes a robust system for managing the Web Audio API's core contexts, abstracting away complexities to provide a consistent environment for audio processing. This system is built upon foundational `BaseContext` and `Context` classes, facilitating both real-time and offline audio rendering.

### BaseContext

At its core, the `BaseContext` class defines an abstract interface for all audio contexts within Tone.js, outlining common methods for:
- Creating standard Web Audio API nodes (e.g., `createAnalyser`, `createOscillator`, `createGain`)
- Creating Tone.js-specific features like `createAudioWorkletNode`
- Precise timing functions such as `now`, `immediate`, `setTimeout`, and `setInterval`

This abstract layer ensures that all context implementations adhere to a unified API.

### Context

The concrete implementation is provided by the `Context` class, which wraps a standard `AudioContext` or `OfflineAudioContext`. It enhances the native context with crucial features for:
- Timing
- Scheduling
- Resource management

The Context integrates:
- A `Ticker` for reliable, high-resolution scheduling
- A `Timeline` for managing scheduled timeouts
- Management of AudioWorklet module loading
- Lifecycle management, including `resume()` to start audio processing and `dispose()` for cleanup

Critically, the Context class initializes and manages core Tone.js components such as the Global Timing and Transport System, the audio listener, and the master audio output destination.

The `ContextInitialization` module further orchestrates this by providing a mechanism to register and invoke callbacks when a new Context is created or closed, allowing other modules to synchronize their lifecycle with the audio context.

### Offline Rendering

For scenarios requiring non-real-time audio generation, Tone.js offers the `OfflineContext`. This specialized Context extends the standard Context and is built around an `OfflineAudioContext`. It is specifically designed for:
- Rendering audio into an `AudioBuffer`
- Simulating time progression
- Faster-than-real-time processing

The `Offline` utility function simplifies this process by:
1. Temporarily switching the global Tone.js Context to an `OfflineContext`
2. Executing a user-defined audio graph
3. Returning the rendered audio as a `ToneAudioBuffer`

This capability is essential for:
- Pre-rendering audio assets
- Performing batch processing
- Conducting deterministic tests of audio algorithms

## Advanced Audio Parameter Automation

Tone.js provides enhanced automation capabilities for Web Audio API AudioParams through the `AbstractParam` and `Param` classes, enabling precise scheduling of value changes, ramp automation, and unit conversions within the audio graph.

### AbstractParam

The `AbstractParam` class, defined in `/tonejs/tone.js/Tone/core/context/AbstractParam.ts`, establishes a common interface for all automatable audio parameters. This abstract blueprint outlines methods for:
- Value scheduling (e.g., `setValueAtTime`)
- Ramp automation (e.g., `linearRampToValueAtTime`, `exponentialRampToValueAtTime`, `targetRampTo`)
- Managing scheduled changes (e.g., `cancelScheduledValues`)

This abstraction ensures a consistent API for controlling diverse audio properties, regardless of their underlying implementation.

### Param

The concrete implementation of this interface is the `Param` class, located in `/tonejs/tone.js/Tone/core/context/Param.ts`. This class wraps a native Web Audio `AudioParam`, extending its functionality with advanced features:

#### Timeline Management
Param internally maintains a timeline of all scheduled automation events, allowing it to accurately determine the parameter's value at any given time, even between scheduled events, through interpolation functions. This timeline is critical for its `getValueAtTime` method, which calculates the parameter's exact state at a specified moment by analyzing the scheduled events.

#### Unit Conversion
Param provides comprehensive unit conversion capabilities. It can interpret and convert values between various musical or audio-centric units (such as "time," "decibels," or "frequency") and the raw numerical values required by the AudioParam.

This simplifies working with audio parameters by allowing developers to specify values in intuitive units, with Param handling the necessary conversions. For example, when setting a gain value in decibels, Param converts it to the linear gain value expected by the Web Audio GainNode.

Furthermore, Param enforces minimum and maximum value constraints based on its assigned units, ensuring that parameter values remain within a valid and expected range.

#### Advanced Methods
- **apply()**: Transfers an entire scheduled automation curve from one Param instance to another AudioParam. This is particularly useful for dynamically re-routing audio signals or applying predefined complex automation sequences to different parts of the audio graph.

- **setParam()**: Supports the dynamic replacement of its underlying AudioParam, which is valuable in scenarios where the target AudioParam might change during the lifetime of the Param instance.

## Global Timing and Transport System

Tone.js centralizes musical timing and playback control through its Transport system, which acts as a global musical timeline orchestrating BPM, time signature, event scheduling, looping, and synchronization of various audio parameters.

### Transport

The `Transport` (Tone/core/clock/Transport.ts) manages the overall state of a musical piece. It can be started, stopped, or paused, and it provides control over the tempo via its `bpm` property.

This `bpm` property, an instance of `TickParam`, allows for the precise scheduling of tempo changes over time, including linear and exponential ramps. The Transport also supports dynamic `timeSignature` changes, enabling complex rhythmic structures.

### Clock and TickSource

Underpinning the Transport's timing capabilities is an internal `Clock` (Tone/core/clock/Clock.ts) instance, which generates rhythmic pulses based on the BPM.

The Clock in turn delegates the intricate logic of managing musical ticks, calculating elapsed time, and handling automated frequency changes to a `TickSource` (Tone/core/clock/TickSource.ts).

The TickSource keeps track of both ticks and seconds, supporting dynamic tempo adjustments and providing mechanisms to query the clock's state at any given time. It also manages playback state ("started", "stopped", "paused") and tick offsets, all stored and efficiently retrieved using Timeline data structures.

### Event Scheduling

For scheduling musical events, the Transport leverages specialized event classes:
- `TransportEvent` for one-time occurrences
- `TransportRepeatEvent` for recurring events

These events are processed on each tick of the internal clock, ensuring precise timing. The Transport manages these events using:
- `Timeline` for one-shot events
- `IntervalTimeline` for repeated events

These are efficient data structures for storing and retrieving events based on their scheduled tick times.

### Looping and Synchronization

Looping functionality is built into the Transport, allowing developers to define `loopStart` and `loopEnd` points and enabling continuous playback of a section.

The system also incorporates swing quantization, with configurable:
- Swing amount
- Swing subdivision

This adds rhythmic variation to playback.

Furthermore, the Transport can synchronize other Signal objects to its tempo, ensuring that parameters like frequencies or durations adjust proportionally with tempo changes. This synchronization is achieved by dynamically creating signal chains that modulate the target signal's value based on the BPM.

## AudioWorklet Integration for High Performance

Tone.js integrates Web Audio AudioWorklets to enable high-performance, block-level audio processing in a separate thread from the main JavaScript thread. This prevents UI blocking and improves audio stability.

### ToneAudioWorklet

The core of this integration is the `ToneAudioWorklet` abstract class, located at `Tone/core/worklet/ToneAudioWorklet.ts`. This class extends `ToneAudioNode` and provides a standardized way to incorporate `AudioWorkletNode` functionality within Tone.js.

It handles the lifecycle of an AudioWorkletNode, including:
- Lazy loading and registration of the AudioWorklet module globally per AudioContext
- Instantiation of the AudioWorkletNode
- Proper disposal by sending a "dispose" message to the worklet's port for internal cleanup

Subclasses must implement:
- `_audioWorkletName` to specify the processor's name
- `onReady` for post-instantiation setup

### WorkletGlobalScope

The `WorkletGlobalScope` utilities, found in `Tone/core/worklet/WorkletGlobalScope.ts`, manage the registration of JavaScript classes and functions within the `AudioWorkletGlobalScope`.

This is crucial for defining custom audio processing logic that runs in the worklet thread. It collects code snippets (classes or functions) and prepares them for injection and evaluation within an `AudioWorkletGlobalScope`, ensuring that necessary components are available to the worklet.

### Specialized Processors

#### SingleIOProcessor
`SingleIOProcessor`, defined in `Tone/core/worklet/SingleIOProcessor.worklet.ts`, provides an abstract `AudioWorkletProcessor` designed for single input/output audio processing.

It handles:
- Sample-by-sample processing within its `process` method
- Parameter updates
- Requires subclasses to implement a `generate` method for custom audio transformation

This simplifies the creation of worklets by abstracting away buffer management and parameter interpolation.

#### DelayLine
The `DelayLine` class, located at `Tone/core/worklet/DelayLine.worklet.ts`, implements a multi-channel circular buffer within the AudioWorkletGlobalScope.

This enables efficient audio delay effects by allowing samples to be pushed to and retrieved from specific channels with a specified delay, managing buffer wrapping through a circular buffer algorithm.

#### ToneAudioWorkletProcessor
The base `ToneAudioWorkletProcessor`, provided as a JavaScript string in `Tone/core/worklet/ToneAudioWorkletProcessor.worklet.ts`, serves as a foundation for all Tone.js audio processing within an AudioWorklet.

It initializes common properties like:
- `disposed`
- `blockSize` (128 samples)
- `sampleRate`

And establishes a message port listener to handle disposal signals from the main thread, facilitating proper resource management.

## Audio Signal Generation and Manipulation

This section introduces the foundational components for creating and modifying audio signals. It covers the various audio sources capable of generating sound, such as oscillators, noise generators, and buffer players, and outlines the mechanisms for scheduling and controlling their output.

Additionally, it describes core Digital Signal Processing (DSP) building blocks, explaining how signals can be transformed, combined, and routed within the audio graph to achieve complex sonic manipulations.

### Audio Signal Sources

The framework provides a collection of audio sources for generating sound, abstracted by the base class `Tone/source/Source.ts`. This class establishes fundamental behaviors such as:
- Start and stop scheduling
- Volume control
- Muting
- Synchronization with a global transport system

For sources that play for a defined duration, the `Tone/source/OneShotSource.ts` class handles amplitude envelopes with `fadeIn` and `fadeOut` effects, along with an `onended` callback for lifecycle management.

#### Oscillators
A comprehensive set of periodic waveform generators are available in `Tone/source/oscillator`:

- **Oscillator** (`Tone/source/oscillator/Oscillator.ts`): Supports various waveform types, frequency, detune, and phase control
- **AMOscillator** (`Tone/source/oscillator/AMOscillator.ts`): Amplitude modulation
- **FMOscillator** (`Tone/source/oscillator/FMOscillator.ts`): Frequency modulation
- **PWMOscillator**: Pulse width modulation
- **FatOscillator** (`Tone/source/oscillator/FatOscillator.ts`): "Fat" sounds using detuned multiple oscillators
- **LFO** (`Tone/source/oscillator/LFO.ts`): Low-frequency oscillation for modulation purposes
- **OmniOscillator** (`Tone/source/oscillator/OmniOscillator.ts`): Unified interface to dynamically switch between oscillator types

#### Noise Generators
The `Tone/source/Noise.ts` class provides "white," "pink," and "brown" noise, using pre-generated and cached audio buffers for efficiency. Its `type` and `playbackRate` can be dynamically adjusted.

#### Buffer Players
For playing audio from pre-recorded samples, the `Tone/source/buffer` directory offers several options:

- **ToneBufferSource** (`Tone/source/buffer/ToneBufferSource.ts`): Directly plays audio buffers with scheduling, looping, and rate control
- **Player** (`Tone/source/buffer/Player.ts`): Adds robust features like asynchronous loading, seeking, and restart capabilities
- **GrainPlayer** (`Tone/source/buffer/GrainPlayer.ts`): For granular synthesis, uses a clock to schedule individual buffer instances as "grains"
- **Players** (`Tone/source/buffer/Players.ts`): Manages multiple Player instances

#### User Media Input
The `Tone/source/UserMedia.ts` component integrates user audio input (e.g., a microphone) into the audio graph, allowing for recording or live processing of external audio sources. It provides methods to open and close input streams, and to `enumerateDevices()` for device selection.

### Core Digital Signal Processing (DSP) Building Blocks

The `Tone/signal` directory contains a set of fundamental DSP components for manipulating audio signals. These are designed to operate as audio nodes, allowing them to be chained together to form complex processing graphs.

Central to these components is the `Tone/signal/Signal.ts` class, which represents a schedulable audio-rate parameter. It enables precise automation of values over time using Web Audio API methods, allowing signals to control various parameters within the audio graph.

#### Arithmetic Operations
- **Add** (`Tone/signal/Add.ts`): Sums an input signal with a configurable addend
- **Multiply** (`Tone/signal/Multiply.ts`): Multiplies an input signal by a factor
- **Negate** (`Tone/signal/Negate.ts`): Inverts the sign of an input signal
- **Subtract** (`Tone/signal/Subtract.ts`): Subtracts a subtrahend from an input signal

#### Signal Scaling and Range Conversion
- **Scale** and **ScaleExp** (`Tone/signal/Scale.ts`, `Tone/signal/ScaleExp.ts`): Linearly or exponentially scale a signal's range
- **AudioToGain** (`Tone/signal/AudioToGain.ts`): Converts audio range [-1, 1] to gain range [0, 1]
- **GainToAudio** (`Tone/signal/GainToAudio.ts`): Converts gain range [0, 1] to audio range [-1, 1]
- **Pow** (`Tone/signal/Pow.ts`): Applies an exponent to an input signal

#### Logical and Utility Operations
- **Abs** (`Tone/signal/Abs.ts`): Outputs the absolute value of an input signal
- **GreaterThan** (`Tone/signal/GreaterThan.ts`): Outputs 1 if input > comparator, else 0
- **GreaterThanZero** (`Tone/signal/GreaterThanZero.ts`): Outputs 1 if input > 0, else 0
- **WaveShaper** (`Tone/signal/WaveShaper.ts`): Custom, non-linear shaping using a user-defined mapping
- **Zero** (`Tone/signal/Zero.ts`): Generates a continuous audio-rate stream of zero values

#### Transport-Synchronized Parameters
**SyncedSignal** (`Tone/signal/SyncedSignal.ts`): Extends Signal to synchronize its value changes with the global Global Timing and Transport System, enabling musical-time scheduling of audio parameters.

## Musical Instruments and Synthesizers

This section covers the collection of musical instrument synthesizers and samplers within the library, providing tools for generating melodic and harmonic content. These instruments are built upon a common architectural pattern that defines how they manage audio output, control volume, and synchronize with the global musical timeline.

### Instrument Base Classes

#### Instrument
The fundamental behavior for all instruments is established by the abstract base class found in `/tonejs/tone.js/Tone/instrument/Instrument.ts`. This class:
- Manages audio output via an internal volume node
- Allows for gain control in decibels
- Provides mechanisms for synchronizing note-on and note-off events (`triggerAttack`, `triggerRelease`) with the global transport system

When synchronized, instrument methods are scheduled on the transport to ensure precise timing.

#### Monophonic
For instruments that produce a single voice at a time, the abstract `/tonejs/tone.js/Tone/instrument/Monophonic.ts` class extends this foundation. It:
- Manages the lifecycle of a single note (attack, release, dynamic frequency changes)
- Handles portamento (smooth glide between notes)
- Requires subclasses to implement specific sound-generating logic for their envelopes
- Defines frequency and detune signals for automation and modulation

#### PolySynth
Polyphonic instruments, capable of playing multiple notes simultaneously, are managed by the `/tonejs/tone.js/Tone/instrument/PolySynth.ts` class. This class:
- Acts as a container for multiple instances of a monophonic synthesizer
- Efficiently allocates and deallocates voices as notes are played
- Includes a garbage collection mechanism to dispose of unused voices
- Provides a unified control interface for parameters across all internal voices

### Specific Synthesizer Architectures

#### Modulation Synthesizers
The abstract `/tonejs/tone.js/Tone/instrument/ModulationSynth.ts` class serves as a base for AM and FM synthesizers. It orchestrates two internal synthesizer instances:
- A **carrier** that produces the primary sound
- A **modulator** that alters an aspect of the carrier's sound
- **Harmonicity** controls the frequency ratio between carrier and modulator

Specific implementations include:
- **AMSynth** (`/tonejs/tone.js/Tone/instrument/AMSynth.ts`): Modulator controls the amplitude of the carrier
- **FMSynth** (`/tonejs/tone.js/Tone/instrument/FMSynth.ts`): Modulator modulates the frequency of the carrier

#### Dual-Voice Synthesizer
**DuoSynth** (`/tonejs/tone.js/Tone/instrument/DuoSynth.ts`): Combines two monophonic synthesizer instances, providing interconnected control over their frequencies and an applied vibrato effect. This allows for rich, layered monophonic sounds with adjustable harmonic relationships between the voices.

#### Percussive Synthesizers
- **MembraneSynth** (`/tonejs/tone.js/Tone/instrument/MembraneSynth.ts`): Generates percussive drum sounds by using an oscillator with a rapid frequency ramp and an amplitude envelope. Parameters like `octaves` and `pitch decay` control the character of the sound.

- **MetalSynth** (`/tonejs/tone.js/Tone/instrument/MetalSynth.ts`): Synthesizes metallic percussion sounds by combining multiple frequency-modulated oscillators with specific inharmonic frequency ratios. An envelope-controlled highpass filter further shapes the timbre, allowing for cymbal-like sounds.

#### Noise Synthesizer
**NoiseSynth** (`/tonejs/tone.js/Tone/instrument/NoiseSynth.ts`): Combines a noise source with an amplitude envelope to create synthesizable noise instruments, offering customizable amplitude shaping for various noise types.

#### Physical Modeling
**PluckSynth** (`/tonejs/tone.js/Tone/instrument/PluckSynth.ts`): Implements Karplus-Strong string synthesis, simulating plucked string sounds by feeding a noise burst into a lowpass comb filter. It offers controls for:
- Attack noise
- Dampening
- Resonance
- To shape the string's character and decay

### Sampler
**Sampler** (`/tonejs/tone.js/Tone/instrument/Sampler.ts`): An instrument for playing back pre-recorded audio samples. It:
- Loads and manages audio buffers
- Automatically re-pitches samples across a wider musical range
- Supports looping
- Allows samples to be dynamically added for creating sample-based instruments

#### Usage Example
```typescript
const sampler = new Sampler({
  urls: {
    // You can use MIDI notes (e.g., 60 for C4)
    60: "C4.mp3",
    // Or scientific pitch notation (e.g., "A4")
    A4: "A4.mp3",
  },
  baseUrl: "https://tonejs.github.io/audio/synthesis/",
  onload: () => {
    // The samples are loaded, now trigger playback
    sampler.triggerAttackRelease("C4", 0.5); // Play C4 for 0.5 seconds
    sampler.triggerAttackRelease("A4", 0.8, "+1"); // Play A4 for 0.8 seconds, 1 second from now
  },
  onerror: (error) => {
    console.error("Error loading samples:", error);
  },
}).toDestination(); // Connect the sampler to the master output
```

## Audio Effects and Processing Components

The library provides a diverse array of audio effects and processing components for sonic manipulation, ranging from real-time signal analysis and channel strip controls to dynamic range processing and specialized envelope generation.

### Core Effect Architecture

The core architecture for effects is established by the abstract `Effect` class defined in `/tonejs/tone.js/Tone/effect/Effect.ts`. This class provides fundamental functionalities such as:
- Dry/wet signal mixing via an internal `CrossFade` component
- Defines `effectSend` and `effectReturn` nodes (clear insertion points for specific effect processing logic)

Many effects also incorporate feedback loops, managed by base classes like `FeedbackEffect` or `StereoFeedbackEffect`, allowing for time-based effects such as delays and reverbs.

### Effect Categories

#### Filtering and Modulation
- **AutoFilter** (`/tonejs/tone.js/Tone/effect/AutoFilter.ts`): Uses an LFO to modulate a filter's cutoff frequency
- **AutoWah** (`/tonejs/tone.js/Tone/effect/AutoWah.ts`): Employs an envelope follower to control filter frequency based on input amplitude
- **Phaser** (`/tonejs/tone.js/Tone/effect/Phaser.ts`): Creates a phasing effect by modulating a series of all-pass filters in stereo

#### Distortion and Waveshaping
- **Distortion** (`/tonejs/tone.js/Tone/effect/Distortion.ts`): Applies a non-linear wave-shaping function
- **Chebyshev** (`/tonejs/tone.js/Tone/effect/Chebyshev.ts`): Uses Chebyshev polynomials to create distinct distortion characteristics
- **BitCrusher** (`/tonejs/tone.js/Tone/effect/BitCrusher.ts`): Reduces the bit depth of an audio signal, resulting in quantization noise and a lo-fi sound (uses AudioWorklet for high performance)

#### Delay Effects
- **FeedbackDelay** (`/tonejs/tone.js/Tone/effect/FeedbackDelay.ts`): Basic delayed repetitions with feedback
- **PingPongDelay** (`/tonejs/tone.js/Tone/effect/PingPongDelay.ts`): Creates a stereo effect where echoes alternate between left and right channels
- **Chorus** (`/tonejs/tone.js/Tone/effect/Chorus.ts`): Applies LFO-modulated delay times to create a rich, detuned stereo effect

#### Reverb Effects
- **Freeverb** (`/tonejs/tone.js/Tone/effect/Freeverb.ts`): Digital reverberation simulating acoustic spaces with adjustable room size and dampening
- **JCReverb** (`/tonejs/tone.js/Tone/effect/JCReverb.ts`): Schroeder reverberator model with specific tunings

#### Pitch and Stereo Manipulation
- **FrequencyShifter** (`/tonejs/tone.js/Tone/effect/FrequencyShifter.ts`): Alters the pitch of a signal by a fixed amount, destroying harmonic relationships
- **PitchShift** (`/tonejs/tone.js/Tone/effect/PitchShift.ts`): Performs near-realtime pitch alteration without changing tempo
- **AutoPanner** (`/tonejs/tone.js/Tone/effect/AutoPanner.ts`): Automatically modulates an audio signal's position across the stereo field using an LFO

### Core Components

#### Real-time Signal Analysis
- **Analyser** (`/tonejs/tone.js/Tone/component/analysis/Analyser.ts`): Interface to Web Audio's AnalyserNode for FFT or waveform data
- **Meter** (`/tonejs/tone.js/Tone/component/analysis/Meter.ts`): RMS level measurement in decibels or normalized 0-1 range
- **FFT** (`/tonejs/tone.js/Tone/component/analysis/FFT.ts`): Frequency domain analysis
- **Waveform** (`/tonejs/tone.js/Tone/component/analysis/Waveform.ts`): Raw audio waveform data
- **Follower** (`/tonejs/tone.js/Tone/component/analysis/Follower.ts`): Extracts the amplitude envelope of a signal
- **DCMeter**: Measures the immediate DC component of an audio signal

#### Channel Strip Components
- **Volume** (`/tonejs/tone.js/Tone/component/channel/Volume.ts`): Adjusts signal gain in decibels with mute function
- **Panner** (`/tonejs/tone.js/Tone/component/channel/Panner.ts`): Equal power left/right stereo panning
- **Panner3D** (`/tonejs/tone.js/Tone/component/channel/Panner3D.ts`): Spatialized panning with HRTF or equalpower models
- **Channel** (`/tonejs/tone.js/Tone/component/channel/Channel.ts`): Bundles volume, pan, mute, and solo controls with a global bus system
- **MultibandSplit** (`/tonejs/tone.js/Tone/component/channel/MultibandSplit.ts`): Divides audio into frequency bands
- **MidSideSplit** and **MidSideMerge**: Enable mid/side processing for stereo signals
- **PanVol** (`/tonejs/tone.js/Tone/component/channel/PanVol.ts`): Combines panner and volume control
- **Recorder** (`/tonejs/tone.js/Tone/component/channel/Recorder.ts`): Wrapper around MediaRecorder API for audio recording
- **CrossFade** (`/tonejs/tone.js/Tone/component/channel/CrossFade.ts`): Equal power fading between two inputs
- **Merge** and **Split**: Combine/divide multichannel signals
- **Mono** (`/tonejs/tone.js/Tone/component/channel/Mono.ts`): Converts to monophonic audio
- **Solo** (`/tonejs/tone.js/Tone/component/channel/Solo.ts`): Isolates an audio stream

#### Dynamic Range Processors
- **Compressor** (`/tonejs/tone.js/Tone/component/dynamics/Compressor.ts`): Wraps native DynamicsCompressorNode with automatable parameters
- **Limiter** (`/tonejs/tone.js/Tone/component/dynamics/Limiter.ts`): Prevents audio signals from exceeding a specified amplitude threshold
- **Gate** (`/tonejs/tone.js/Tone/component/dynamics/Gate.ts`): Audio gate allowing signals to pass only when amplitude surpasses threshold
- **MidSideCompressor** (`/tonejs/tone.js/Tone/component/dynamics/MidSideCompressor.ts`): Independent compression of mid and side components
- **MultibandCompressor** (`/tonejs/tone.js/Tone/component/dynamics/MultibandCompressor.ts`): Frequency-specific dynamic range processing

#### Envelope Generators
- **Envelope** (`/tonejs/tone.js/Tone/component/envelope/Envelope.ts`): ADSR envelope generation with configurable curve shapes
- **AmplitudeEnvelope** (`/tonejs/tone.js/Tone/component/envelope/AmplitudeEnvelope.ts`): Directly applies ADSR envelope to amplitude
- **FrequencyEnvelope** (`/tonejs/tone.js/Tone/component/envelope/FrequencyEnvelope.ts`): Generates frequency ramps for dynamic pitch control

#### Advanced Audio Filters and Convolution
- **BiquadFilter** (`/tonejs/tone.js/Tone/component/filter/BiquadFilter.ts`): Interface to Web Audio's BiquadFilterNode
- **Filter** (`/tonejs/tone.js/Tone/component/filter/Filter.ts`): Variable rolloff (-12, -24, -48, -96 dB/octave)
- **EQ3** (`/tonejs/tone.js/Tone/component/filter/EQ3.ts`): 3-band equalizer
- **FeedbackCombFilter** (`/tonejs/tone.js/Tone/component/filter/FeedbackCombFilter.ts`): For physical modeling and intricate delay effects
- **LowpassCombFilter** (`/tonejs/tone.js/Tone/component/filter/LowpassCombFilter.ts`): Comb filter with lowpass in feedback path
- **OnePoleFilter** (`/tonejs/tone.js/Tone/component/filter/OnePoleFilter.ts`): Simple 6dB-per-octave lowpass/highpass
- **PhaseShiftAllpass** (`/tonejs/tone.js/Tone/component/filter/PhaseShiftAllpass.ts`): Efficient Hilbert Transform for phase manipulation
- **Convolver** (`/tonejs/tone.js/Tone/component/filter/Convolver.ts`): Impulse response-based effects for acoustic simulation

## Event Scheduling and Sequencing

The library provides core mechanisms for scheduling, sequencing, and generating musical patterns. These components enable the precise triggering and management of events over time, facilitating the creation of complex rhythmic and melodic structures.

### ToneEvent

At the foundation is `ToneEvent` (defined in `/tonejs/tone.js/Tone/event/ToneEvent.ts`), which schedules a callback function to execute at specific times on the musical transport. This class supports:
- Looping
- Playback rate adjustments
- Event probability
- Humanization for subtle timing variations

ToneEvent relies on an internal `StateTimeline` to efficiently manage its lifecycle, including starting, stopping, and canceling events.

#### Usage Example
```typescript
const synth = new Tone.PolySynth().toDestination();

// Create a ToneEvent with a callback and initial value
const chordEvent = new Tone.ToneEvent(((time, chord) => {
  // The callback receives the scheduled time and the event's value
  synth.triggerAttackRelease(chord, 0.5, time);
}), ["D4", "E4", "F4"]); // Initial value is a chord array

// Start the event at the beginning of the transport timeline
chordEvent.start();

// Configure looping: loop every measure for 8 measures
chordEvent.loop = 8;
chordEvent.loopEnd = "1m";

// You can later stop the event
// chordEvent.stop("+2m");
```

### Loop

For rhythmic repetition, the `Loop` class (defined in `/tonejs/tone.js/Tone/event/Loop.ts`) extends `ToneEvent`, offering a specialized interface for continuous looping. It allows for a callback to be invoked repeatedly at a regular interval, with controls for:
- Playback rate
- Humanization
- Number of iterations

### Part

To manage collections of events, the `Part` class (defined in `/tonejs/tone.js/Tone/event/Part.ts`) acts as a container for multiple `ToneEvent` objects, enabling unified control over a group of events.

This means a set of events can be started, stopped, and looped together, with global properties like probability and playback rate propagating to all contained events. The Part class also supports dynamic event management, allowing events to be added or removed at runtime.

### Sequence

The `Sequence` class (defined in `/tonejs/tone.js/Tone/event/Sequence.ts`) provides an array-based approach to rhythmic event scheduling. It processes a list of events and a subdivision parameter to schedule events rhythmically.

Nested arrays within a sequence allow for the creation of intricate rhythmic patterns with subdivided timings. A key feature of Sequence is its use of a Proxy around its events array, which automatically triggers rescheduling when the array's contents are modified, enabling dynamic updates to the sequence.

### Pattern

For algorithmic pattern generation, the `Pattern` class (defined in `/tonejs/tone.js/Tone/event/Pattern.ts`) extends Loop to generate events based on a sequence of values and various predefined pattern types (e.g., "up," "down," "random").

It repeatedly calls a user-defined callback with a value from its internal sequence, advancing through the values according to the chosen pattern. This capability is underpinned by the `PatternGenerator` module (defined in `/tonejs/tone.js/Tone/event/PatternGenerator.ts`), which provides generator functions for producing diverse numerical sequences.

## Development Workflow and Examples

The Tone.js repository includes systems for managing project versions, automating builds, and providing interactive examples to showcase library features.

### Project Versioning

Project versioning is handled by the script found at `scripts/increment_version.cjs`. This script automatically updates the project's version number by:
- Comparing existing `tone` and `tone@next` package versions on npm
- Incrementing the patch version of the higher one

It ensures that the local project aligns with the most recent npm release and only modifies `package.json` and `Tone/version.ts` within a continuous integration (CI) environment.

### Build Automation

Build automation is configured through Webpack, as defined in `scripts/webpack.config.cjs`. This configuration supports different build environments:
- **Default setup**: Common settings for output paths, filenames, and TypeScript compilation
- **Production build**: Optimized with "production" mode and detailed source-map
- **Scratchpad environment**: For local development with HtmlWebpackPlugin and devServer with hot reloading

### Interactive Examples

The repository features an extensive collection of interactive examples located in the `examples` directory. These examples demonstrate various aspects of the Tone.js library, including:
- Synthesis
- Effects
- Sequencing
- Audio analysis

#### Running Examples
To run examples locally:
1. Install dependencies: `npm install`
2. Build the project: `npm run build`
3. Serve the built files with a simple HTTP server

New examples, typically structured as web components, require an entry in `js/ExampleList.json` to be discoverable.

#### Example Categories

**Synthesis Examples:**
- `examples/amSynth.html`: Amplitude modulation synthesis
- `examples/fmSynth.html`: Frequency modulation synthesis
- `examples/monoSynth.html`: Monophonic synthesis
- `examples/polySynth.html`: Polyphonic synthesis
- `examples/sampler.html`: Sample playback
- `examples/grainPlayer.html`: Granular synthesis
- `examples/bembe.html`: Percussive sounds using MetalSynth and MembraneSynth
- `examples/jump.html`: Supersaw and FatOscillator effects
- `examples/noises.html`: Noise generation

**Effects and Processing:**
- `examples/buses.html`: Effect bussing and wet/dry mixing
- `examples/lfoEffects.html`: LFO-driven effects (AutoPanner, AutoFilter, Tremolo)
- `examples/pingPongDelay.html`: Stereo delay effect
- `examples/reverb.html`: Reverb effects
- `examples/pitchShift.html`: Real-time pitch modification

**Scheduling and Sequencing:**
- `examples/events.html`: Loop, Part, and Sequence for musical patterns
- `examples/daw.html`: DAW-like beat synchronization
- `examples/pianoPhase.html`: Steve Reich's "Piano Phase" effect
- `examples/stepSequencer.html`: Step sequencer for rhythmic playback

**Analysis and Visualization:**
- `examples/analysis.html`: FFT and waveform visualization
- `examples/meter.html`: RMS meter display
- `examples/mic.html`: Microphone input processing

**Advanced Topics:**
- `examples/offline.html`: Offline rendering using Tone.Offline
- `examples/rampTo.html`: Smooth parameter changes
- `examples/animationSync.html`: Synchronizing audio with visual animations using Tone.Draw
- `examples/spatialPanner.html`: 3D audio with Panner3D and Listener

### Custom UI Components

The examples utilize a custom web component framework built with:
- **lit-element**: Base for web components
- **Material Design Components (MDC) Web**: Consistent UI aesthetics
- **AudioKeys**: Keyboard input for triggering musical notes

Key UI components defined in `examples/js/tone-ui.js` include:
- `tone-play-toggle`
- `tone-slider`
- `tone-momentary-button`
- `tone-mic-button`
- AudioNode components for modifying audio object properties

This modular approach enables consistent and interactive user experiences across all examples.

## References

- **Official Documentation**: [Tone.js Documentation](https://tonejs.github.io/docs/)
- **GitHub Repository**: [tonejs/tone.js](https://github.com/Tonejs/Tone.js)
- **Examples**: [Interactive Examples](https://tonejs.github.io/examples/)
- **API Reference**: [Full API Documentation](https://tonejs.github.io/docs/latest/)
