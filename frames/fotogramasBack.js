const express = require("express");
const multer = require("multer");
const ffmpeg = require("fluent-ffmpeg");
const fs = require("fs");
const path = require("path");
const cors = require("cors");

const app = express();
app.use(cors());
const upload = multer({ dest: "uploads/" });

app.post("/upload", upload.single("video"), (req, res) => {
    if (!req.file) return res.status(400).send("No video uploaded");

    const videoPath = req.file.path;
    const outputDir = path.join(__dirname, "frames");

    if (!fs.existsSync(outputDir)) fs.mkdirSync(outputDir, { recursive: true });

    ffmpeg(videoPath)
        .output(`${outputDir}/frame-%04d.png`)
        .outputOptions(["-vf fps=1"]) // Extrae un fotograma por segundo
        .on("end", () => {
            fs.readdir(outputDir, (err, files) => {
                if (err) return res.status(500).send("Error leyendo fotogramas");

                const images = files.map(file =>
                    fs.readFileSync(path.join(outputDir, file), { encoding: "base64" })
                );
                res.json(images);
            });
        })
        .on("error", (err) => res.status(500).send("Error procesando video: " + err.message))
        .run();
});

app.listen(5000, () => console.log("Server running on http://localhost:5000"));
