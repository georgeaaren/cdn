To install and use [`ffmpeg.wasm`](%2Fffmpegwasm%2Fffmpeg.wasm%2FREADME.md#L4) in a TypeScript web application, follow these steps.

### Installation

First, install the necessary packages using npm or yarn:

```bash
bun install @ffmpeg/ffmpeg @ffmpeg/util
```

(See [Installation](#example-applications-and-integration-installation))

### Webpack/Vite Configuration (if applicable)

If you are using a bundler like Vite, you may need to configure it to handle [`ffmpeg.wasm`](%2Fffmpegwasm%2Fffmpeg.wasm%2FREADME.md#L4) correctly. For example, with Vite, you need to set `optimizeDeps.exclude` and `server.headers` to enable [`SharedArrayBuffer`](%2Fffmpegwasm%2Fffmpeg.wasm%2Fpackage.json#L13) for multi-threading (see `apps/react-vite-app/vite.config.ts`, `apps/vue-vite-app/vite.config.ts`, `apps/solidstart-app/src/entry-server.tsx`, and `apps/sveltekit-app/vite.config.ts` for examples):

```typescript
// vite.config.ts example for React-Vite app
import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

export default defineConfig({
  plugins: [react()],
  optimizeDeps: {
    exclude: ["@ffmpeg/ffmpeg", "@ffmpeg/util"],
  },
  server: {
    headers: {
      "Cross-Origin-Opener-Policy": "same-origin",
      "Cross-Origin-Embedder-Policy": "require-corp",
    },
  },
});
```

### Usage in a TypeScript Web App

Here's a basic example of how to load [`ffmpeg.wasm`](%2Fffmpegwasm%2Fffmpeg.wasm%2FREADME.md#L4) and transcode a video file in a TypeScript web application. This example uses a pattern similar to the React, Vue, and Angular examples (`apps/react-vite-app/src/App.tsx`, `apps/vue-vite-app/src/components/FFmpegDemo.vue`, `apps/angular-app/src/app/app.component.ts`).

```typescript
import { FFmpeg } from "@ffmpeg/ffmpeg";
import { fetchFile, toBlobURL } from "@ffmpeg/util";

// Define the base URL for ffmpeg-core. Use 'esm' for Vite and modern bundlers.
// For multi-threaded support, use @ffmpeg/core-mt.
const baseURL = "https://cdn.jsdelivr.net/npm/@ffmpeg/core-mt@0.12.10/dist/esm";

// Initialize FFmpeg instance
const ffmpeg = new FFmpeg();

// Optional: Display log messages from FFmpeg
ffmpeg.on("log", ({ message }) => {
  console.log(message);
});

// Optional: Listen for progress updates (experimental)
ffmpeg.on("progress", ({ progress, time }) => {
  console.log(`Progress: ${progress * 100}% (Time: ${time / 1000000}s)`);
});

/**
 * Loads the FFmpeg core and associated WebAssembly modules.
 * This must be called before any FFmpeg operations.
 */
async function loadFFmpeg() {
  try {
    await ffmpeg.load({
      coreURL: await toBlobURL(`${baseURL}/ffmpeg-core.js`, "text/javascript"),
      wasmURL: await toBlobURL(
        `${baseURL}/ffmpeg-core.wasm`,
        "application/wasm",
      ),
      workerURL: await toBlobURL(
        `${baseURL}/ffmpeg-core.worker.js`,
        "text/javascript",
      ),
    });
    console.log("FFmpeg loaded successfully!");
    return true;
  } catch (error) {
    console.error("Failed to load FFmpeg:", error);
    return false;
  }
}

/**
 * Transcodes an AVI video to MP4.
 * This demonstrates reading a file into the virtual filesystem, executing a command,
 * and reading the output file.
 */
async function transcodeVideo() {
  if (!ffmpeg.loaded) {
    console.error("FFmpeg is not loaded. Call loadFFmpeg() first.");
    return;
  }

  const inputVideoUrl =
    "https://raw.githubusercontent.com/ffmpegwasm/testdata/master/video-15s.avi";
  const inputFileName = "input.avi";
  const outputFileName = "output.mp4";

  console.log(`Fetching ${inputVideoUrl}...`);
  // Fetch the video file and write it to FFmpeg's virtual file system
  await ffmpeg.writeFile(inputFileName, await fetchFile(inputVideoUrl));
  console.log(`${inputFileName} written to virtual file system.`);

  console.log(
    `Executing FFmpeg command: -i ${inputFileName} ${outputFileName}`,
  );
  // Execute the transcoding command
  await ffmpeg.exec(["-i", inputFileName, outputFileName]);
  console.log("Transcoding complete!");

  // Read the output file from FFmpeg's virtual file system
  const fileData = await ffmpeg.readFile(outputFileName);

  // Convert the Uint8Array data to a Blob and create a URL for playback
  const data = new Uint8Array(fileData as ArrayBuffer);
  const videoBlob = new Blob([data.buffer], { type: "video/mp4" });
  const videoObjectURL = URL.createObjectURL(videoBlob);

  console.log("Output video URL:", videoObjectURL);

  // You can then use this URL to display the video in an HTML <video> element
  const videoElement = document.createElement("video");
  videoElement.src = videoObjectURL;
  videoElement.controls = true;
  document.body.appendChild(videoElement);
}

// Example usage:
async function runApp() {
  const loaded = await loadFFmpeg();
  if (loaded) {
    await transcodeVideo();
  }
}

runApp();
```

### Key Concepts

1.  **Installation**: Add [`@ffmpeg/ffmpeg`](%2Fffmpegwasm%2Fffmpeg.wasm%2FREADME.md#L13) and [`@ffmpeg/util`](%2Fffmpegwasm%2Fffmpeg.wasm%2Fapps%2Fwebsite%2Fpackage.json#L28) to your project dependencies (see `apps/website/docs/getting-started/installation.md`).
2.  **[`FFmpeg`](%2Fffmpegwasm%2Fffmpeg.wasm%2Fpackages%2Fffmpeg%2Fsrc%2Fclasses.ts#L35) Class**: Create an instance of the [`FFmpeg`](%2Fffmpegwasm%2Fffmpeg.wasm%2Fpackages%2Fffmpeg%2Fsrc%2Fclasses.ts#L35) class, which is the primary interface for interacting with the FFmpeg Web Worker (see [FFmpeg Class: Lifecycle and Asynchronous Operations](#asynchronous-ffmpeg-api-and-types-ffmpeg-class-lifecycle-and-asynchronous-operations)).
3.  **Loading Core**: Call [`ffmpeg.load()`](%2Fffmpegwasm%2Fffmpeg.wasm%2Fpackages%2Fffmpeg%2Fsrc%2Ftypes.ts#L27) to asynchronously load the [`ffmpeg-core.js`](%2Fffmpegwasm%2Fffmpeg.wasm%2FDockerfile#L197), [`ffmpeg-core.wasm`](%2Fffmpegwasm%2Fffmpeg.wasm%2FDockerfile#L203), and [`ffmpeg-core.worker.js`](%2Fffmpegwasm%2Fffmpeg.wasm%2Fsrc%2Fbind%2Fffmpeg%2Fbind.js#L103) files. The [`toBlobURL`](%2Fffmpegwasm%2Fffmpeg.wasm%2Fpackages%2Futil%2Fsrc%2Findex.ts#L170) utility from [`@ffmpeg/util`](%2Fffmpegwasm%2Fffmpeg.wasm%2Fapps%2Fwebsite%2Fpackage.json#L28) is recommended to bypass CORS issues when fetching from CDNs (see [Common FFmpeg.wasm Integration Patterns](#example-applications-and-integration-common-ffmpegwasm-integration-patterns)). Ensure you specify the correct [`baseURL`](%2Fffmpegwasm%2Fffmpeg.wasm%2Fapps%2Fangular-app%2Fsrc%2Fapp%2Fapp.component.ts#L7) (e.g., [`esm`](%2Fffmpegwasm%2Fffmpeg.wasm%2FDockerfile#L198) for Vite, [`umd`](%2Fffmpegwasm%2Fffmpeg.wasm%2FDockerfile#L195) for others) and use the multi-threaded [`core-mt`](%2Fffmpegwasm%2Fffmpeg.wasm%2Fpackage.json#L14) version if desired for performance.
4.  **Virtual File System**: [`ffmpeg.wasm`](%2Fffmpegwasm%2Fffmpeg.wasm%2FREADME.md#L4) operates on an in-memory virtual file system. Use [`ffmpeg.writeFile()`](%2Fffmpegwasm%2Fffmpeg.wasm%2Fapps%2Fwebsite%2Fdocs%2Fmigration.md#L31) to transfer input files into this system and [`ffmpeg.readFile()`](%2Fffmpegwasm%2Fffmpeg.wasm%2Fapps%2Fwebsite%2Fdocs%2Fmigration.md#L32) to retrieve output files (see `FFmpeg.writeFile()` and `FFmpeg.readFile()` in `packages/ffmpeg/src/classes.ts`). The [`fetchFile`](%2Fffmpegwasm%2Fffmpeg.wasm%2Fpackages%2Futil%2Fsrc%2Findex.ts#L49) utility from [`@ffmpeg/util`](%2Fffmpegwasm%2Fffmpeg.wasm%2Fapps%2Fwebsite%2Fpackage.json#L28) can help fetch files from various sources.
5.  **Executing Commands**: Use [`ffmpeg.exec()`](%2Fffmpegwasm%2Fffmpeg.wasm%2Fpackages%2Fffmpeg%2Fsrc%2Fclasses.ts#L122) to run FFmpeg commands with an array of arguments, similar to how you would use the command-line FFmpeg tool (see [`FFmpeg.exec()`](%2Fffmpegwasm%2Fffmpeg.wasm%2Ftests%2Fffmpeg.test.js#L98) in `packages/ffmpeg/src/classes.ts`).
6.  **Event Handling**: Register event listeners using [`ffmpeg.on('log', ...)`](%2Fffmpegwasm%2Fffmpeg.wasm%2Fapps%2Fwebsite%2Fdocs%2Fgetting-started%2Fusage.md#L182) and [`ffmpeg.on('progress', ...)`](%2Fffmpegwasm%2Fffmpeg.wasm%2Fapps%2Fwebsite%2Fdocs%2Fgetting-started%2Fusage.md#L182) to get real-time feedback during operations (see `FFmpeg.on()` in `packages/ffmpeg/src/classes.ts`).
7.  **Resource Cleanup**: Call [`ffmpeg.terminate()`](%2Fffmpegwasm%2Fffmpeg.wasm%2Fpackages%2Fffmpeg%2Fsrc%2Ferrors.ts#L5) when the FFmpeg instance is no longer needed to release resources (see [`FFmpeg.terminate()`](%2Fffmpegwasm%2Fffmpeg.wasm%2Fpackages%2Fffmpeg%2Fsrc%2Ferrors.ts#L5) in `packages/ffmpeg/src/classes.ts`).
