import express from 'express';
import { runPipeline } from './pipeline.js';

const app = express();
app.use(express.json());

app.get('/', (req, res) => res.send({ status: 'healthy' }));

app.post('/evaluate', async (req, res) => {
  try {
    const { expectedVerse, userTranscript, ruleToCheck } = req.body;
    const feedback = await runPipeline(expectedVerse, userTranscript, ruleToCheck);
    res.json({ success: true, feedback });
  } catch (error) {
    res.status(500).json({ success: false, error: error.message });
  }
});

const PORT = process.env.PORT || 8080;
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
