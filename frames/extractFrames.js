const ffmpeg = require('fluent-ffmpeg');
const path = require('path');
const fs = require('fs');

async function extractFrames(videoPath, outputDir, interval = 1) {
    return new Promise((resolve, reject) => {
        const absoluteVideoPath = path.resolve(videoPath);
        const absoluteOutputDir = path.resolve(outputDir);

        if (!fs.existsSync(absoluteOutputDir)) {
            fs.mkdirSync(absoluteOutputDir, { recursive: true });
        }

        const frames = [];
        ffmpeg(absoluteVideoPath)
            .output(path.join(absoluteOutputDir, 'frame-%04d.png'))
            .outputOptions([`-vf fps=1/${interval}`]) // Extrae 1 fotograma cada X segundos
            .on('end', () => {
                fs.readdir(absoluteOutputDir, (err, files) => {
                    if (err) return reject(err);
                    resolve(files.map(file => path.join(absoluteOutputDir, file)));
                });
            })
            .on('error', reject)
            .run();
    });
}

// ⚡ Ejemplo de uso:
const videoPath = "C:/Users/User/Downloads/Download.mp4";
const outputDir = "C:/Users/User/Downloads/frames";

extractFrames(videoPath, outputDir, 1)
    .then(frames => console.log("Fotogramas extraídos:", frames))
    .catch(err => console.error("Error:", err));
