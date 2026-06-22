import { traceable } from 'langsmith/traceable';
import { OpenAI } from 'openai';

// Initialize the OpenAI client
const openai = new OpenAI();

// 1. Your exact formatPrompt function, filled with Tajweed logic
const formatPrompt = traceable(
  (expectedVerse, userTranscript, ruleToCheck) => {
    return [
      {
        role: 'system',
        content: 'You are an expert Quranic scholar. Evaluate if the transcript matches the rule. Respond with Pass or Fail followed by a short reason.',
      },
      {
        role: 'user',
        content: `Expected Verse: ${expectedVerse}\nUser Transcript: ${userTranscript}\nTajweed Rule: ${ruleToCheck}`,
      },
    ];
  },
  { name: 'formatPrompt' }
);

// 2. Your exact invokeLLM function, filled with the live network call
const invokeLLM = traceable(
  async (messages) => {
    const response = await openai.chat.completions.create({
      model: 'gpt-4o-mini',
      messages: messages,
      temperature: 0.0,
    });
    return response;
  },
  { run_type: 'llm', name: 'invokeLLM' }
);

// 3. Your exact parseOutput function, extracting the clean text response
const parseOutput = traceable(
  (response) => {
    return response.choices[0].message.content;
  },
  { name: 'parseOutput' }
);

// 4. Your exact runPipeline function coordinating the data flow
export const runPipeline = traceable(
  async (expectedVerse, userTranscript, ruleToCheck) => {
    const messages = await formatPrompt(expectedVerse, userTranscript, ruleToCheck);
    const response = await invokeLLM(messages);
    return parseOutput(response);
  },
  { name: 'runPipeline' }
);
