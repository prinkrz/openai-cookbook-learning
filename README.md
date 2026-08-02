# OpenAI Cookbook Learning Roadmap with Resources

The roadmap below maps each chapter to a **primary learning resource**, relevant **Cookbook recipes**, and a practical outcome. Because the Cookbook is continuously updated, use its topic pages as the live index and individual recipes as hands-on chapters.

## Phase 1 — API foundations

### Chapter 1: OpenAI API fundamentals

**Topics**

* [OpenAI SDK setup](https://developers.openai.com/api/docs/quickstart#install-the-openai-sdk-and-run-an-api-call)
* [API keys and environment variables](https://developers.openai.com/api/docs/quickstart#create-and-export-an-api-key)
* [Responses API](https://developers.openai.com/api/docs/guides/migrate-to-responses)
* [Request and response structure](https://developers.openai.com/api/reference/resources/responses)
* [Streaming](https://openai.github.io/openai-agents-python/streaming)
* [Token usage](https://developers.openai.com/api/docs/guides/token-counting)
* [Errors, retries and rate limits](https://developers.openai.com/api/docs/guides/rate-limits#error-mitigation)

**Practice**

Create a Python command-line assistant that streams its answer, displays token usage and handles timeout, authentication and rate-limit errors.

---

### Chapter 2: Models and model selection

**Topics**

* [Model families](https://developers.openai.com/api/docs/models)
* [Reasoning versus non-reasoning models](https://developers.openai.com/api/docs/guides/reasoning)
* [Speed, quality and cost](https://developers.openai.com/api/docs/guides/model-selection#2-optimize-cost-and-latency)
* [Context windows](https://developers.openai.com/api/docs/guides/reasoning#managing-the-context-window)
* [Reasoning effort](https://developers.openai.com/api/docs/guides/reasoning#reasoning-effort)
* [Model fallback](https://developers.openai.com/api/docs/guides/production-best-practices)
* [Task-based model routing](https://developers.openai.com/api/docs/guides/agents/models)

**Practice**

Run 20 representative tasks through different models and compare:

* Accuracy
* Latency
* Token usage
* Estimated cost
* Output consistency

The official model comparison page should be treated as the current source for supported capabilities, context limits and pricing because these details change over time.

---

## Phase 2 — Text and reliable outputs

### Chapter 3: Prompt engineering

**Topics**

* [Instruction hierarchy](https://developers.openai.com/api/docs/guides/prompt-engineering)
* [Developer and user messages](https://developers.openai.com/api/docs/guides/prompt-engineering#message-roles-and-instruction-following)
* [Clear objectives](https://developers.openai.com/api/docs/guides/prompt-engineering#developer-messages)
* [Context placement](https://developers.openai.com/cookbook/examples/gpt4-1_prompting_guide)
* [Delimiters](https://developers.openai.com/api/docs/guides/prompt-engineering#prompt-engineering)
* [Few-shot examples](https://developers.openai.com/plugins/build/examples#few-shot-learning)
* [Acceptance criteria](https://developers.openai.com/api/docs/guides/evaluation-best-practices#evaluate-early-and-often)
* [Long-context prompting](https://developers.openai.com/api/docs/guides/prompt-engineering#version-prompts-in-code)
* [Prompt migration](https://developers.openai.com/api/docs/guides/prompt-guidance-gpt-5p6#prompt-migration-workflow)
* [Prompt iteration](https://developers.openai.com/api/docs/guides/prompt-optimizer)

**Suggested study order**

1. Basic instruction design
2. Few-shot prompting
3. Context organization
4. Long-document prompting
5. Reasoning-model prompting
6. Prompt evaluation
7. Prompt optimization

**Practice**

Create five versions of the same prompt and measure which version produces the highest evaluation score.

---

### Chapter 4: Structured Outputs

**Topics**

* [JSON generation](https://developers.openai.com/api/docs/guides/structured-outputs#json-mode)
* [JSON Schema](https://developers.openai.com/api/docs/guides/structured-outputs#tips-for-your-json-schema)
* [Pydantic models](https://developers.openai.com/api/docs/guides/structured-outputs)
* [Required and optional fields](https://developers.openai.com/api/docs/guides/structured-outputs#all-fields-must-be-required)
* [Enumerations](https://developers.openai.com/cookbook/examples/structured_outputs_intro)
* [Nested objects](https://developers.openai.com/api/docs/guides/structured-outputs#objects-have-limitations-on-nesting-depth-and-size)
* [Schema validation](https://developers.openai.com/cookbook/examples/structured_outputs_multi_agent)
* [Refusal handling](https://developers.openai.com/api/docs/guides/structured-outputs#refusals-with-structured-outputs)
* [Schema versioning](https://json-schema.org/learn/getting-started-step-by-step)

**Practice projects**

* Resume parser
* Invoice extractor
* Meeting action-item extractor
* Support-ticket classifier
* Architecture-requirement extractor

Structured Outputs constrains model responses to a supplied JSON Schema, making it an important foundation for tool use and production integrations.

---

### Chapter 5: Core text application patterns

**Topics**

* [Classification](https://developers.openai.com/cookbook/examples/multiclass_classification_for_transactions)
* [Summarization](https://developers.openai.com/cookbook/examples/summarizing_long_documents)
* [Translation](https://developers.deepl.com/docs/best-practices/working-with-context)
* [Rewriting](https://developers.openai.com/api/docs/guides/text#message-roles-and-instruction-following)
* [Information extraction](https://developers.openai.com/cookbook/examples/entity_extraction_for_long_documents)
* [Question answering](https://developers.openai.com/cookbook/examples/question_answering_using_embeddings)
* [Intent detection](https://developers.openai.com/cookbook/examples/multiclass_classification_for_transactions#zero-shot-classification)
* [Sentiment analysis](https://developers.openai.com/api/docs/tutorials/meeting-minutes#sentiment-analysis)
* [Code generation](https://developers.openai.com/api/docs/guides/code-generation)
* [Document comparison](https://developers.openai.com/api/docs/guides/prompt-engineering#few-shot-learning)

**Practice**

Build a processing pipeline:

```text
Document
   ↓
Document classification
   ↓
Structured extraction
   ↓
Summary
   ↓
Risk and action identification
   ↓
Validated JSON
```

---

## Phase 3 — Tools and application integration

### Chapter 6: Function calling

**Topics**

* [Function definitions](https://developers.openai.com/api/docs/guides/function-calling)
* [Tool schemas](https://developers.openai.com/api/docs/guides/function-calling#the-tool-calling-flow)
* [Tool selection](https://developers.openai.com/api/docs/guides/function-calling#tool-choice)
* [Tool-call arguments](https://developers.openai.com/api/docs/guides/tools)
* [Multiple tool calls](https://developers.openai.com/cookbook/examples/how_to_call_functions_with_chat_models)
* [Parallel tool calls](https://developers.openai.com/api/docs/guides/function-calling#parallel-function-calling)
* [Tool result submission](https://developers.openai.com/api/docs/guides/function-calling#handling-function-calls)
* [Input validation](https://owasp.org/www-project-top-10-for-large-language-model-applications)
* [Idempotency](https://stripe.com/docs/idempotency)
* [Error handling](https://openai.github.io/openai-agents-python/running_agents)
* [Human approval](https://developers.openai.com/api/docs/guides/node-reference#human-approval)

**Practice**

Build an assistant with application-controlled tools for:

* Currency conversion
* Weather lookup
* Calendar availability
* Database search
* Internal documentation search

Function calling connects models to external data and application capabilities, but the application should validate arguments and control execution.

---

### Chapter 7: Responses API and built-in tools

**Topics**

* [Responses API](https://developers.openai.com/api/docs/guides/tools-web-search#responses-api)
* [Conversation state](https://developers.openai.com/api/docs/guides/conversation-state)
* [Previous response IDs](https://developers.openai.com/api/docs/guides/conversation-state#openai-managed-conversation-state)
* [Web search](https://developers.openai.com/api/docs/guides/tools-web-search)
* [File search](https://developers.openai.com/api/docs/guides/tools-file-search)
* [Code execution](https://developers.openai.com/api/docs/guides/tools-code-interpreter)
* [Tool citations](https://developers.openai.com/api/docs/guides/citation-formatting#format-citations-for-retrieved-tool-context)
* [Multi-turn workflows](https://developers.openai.com/api/docs/guides/tools-shell#multi-turn-workflows)
* [Background processing](https://developers.openai.com/api/docs/guides/background#polling-background-responses)
* [Tool permissions](https://developers.openai.com/api/docs/guides/terraform/project-controls)

**Practice**

Build a research assistant that:

* Searches the web
* Searches private documents
* Maintains conversation state
* Generates cited answers
* Separates sourced facts from model inference

---

### Chapter 8: Embeddings

**Topics**

* [Embedding vectors](https://developers.openai.com/api/docs/guides/embeddings)
* [Semantic similarity](https://www.sbert.net/docs/sentence_transformer/usage/semantic_textual_similarity.html)
* [Cosine similarity](https://developers.openai.com/cookbook/examples/semantic_text_search_using_embeddings)
* [Semantic search](https://developers.openai.com/api/docs/guides/retrieval#semantic-search)
* [Classification](https://developers.openai.com/cookbook/examples/classification_using_embeddings)
* [Clustering](https://developers.openai.com/cookbook/examples/clustering)
* [Recommendations](https://developers.openai.com/cookbook/examples/recommendation_using_embeddings)
* [Deduplication](https://developers.openai.com/api/docs/guides/embeddings#use-cases)
* [Batch embedding](https://developers.openai.com/api/docs/guides/embeddings#embedding-models)
* [Vector databases](https://developers.openai.com/api/docs/actions/data-retrieval#middleware-for-vector-databases)

**Practice**

Create a semantic search engine for architecture documents and compare it with keyword search.

---

### Chapter 9: Retrieval-augmented generation

**Topics**

* [Document ingestion](https://developers.openai.com/api/docs/guides/retrieval)
* [Chunking](https://developers.openai.com/api/docs/guides/retrieval#chunking)
* [Chunk overlap](https://www.pinecone.io/learn/chunking-strategies)
* [Metadata](https://developers.openai.com/plugins/guides/optimize-metadata)
* [Vector stores](https://developers.openai.com/api/docs/guides/retrieval#vector-stores)
* [Semantic retrieval](https://developers.openai.com/api/docs/guides/retrieval#performing-semantic-search)
* [Hybrid retrieval](https://www.elastic.co/what-is/hybrid-search)
* [Query rewriting](https://developers.openai.com/api/docs/guides/retrieval#query-rewriting)
* [Reranking](https://www.sbert.net/examples/sparse_encoder/applications/retrieve_rerank/README.html)
* [Context assembly](https://developers.openai.com/api/docs/guides/tools-file-search#include-search-results-in-the-response)
* [Grounded answers](https://developers.openai.com/api/docs/guides/prompt-guidance-gpt-5p6#grounding-citations-and-retrieval-budgets)
* [Citations](https://developers.openai.com/api/docs/guides/citation-formatting#citations)
* [Retrieval evaluation](https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/context_precision)

**Practice**

Build a PDF knowledge assistant that:

* Uploads and indexes PDFs
* Retrieves relevant passages
* Includes citations
* Uses metadata filtering
* Returns “insufficient evidence” when appropriate
* Measures retrieval recall separately from answer quality

The Deep Research API Cookbook demonstrates workflows involving reasoning, planning and synthesis across external information.

---

## Phase 4 — Multimodal development

### Chapter 10: Vision and document understanding

**Topics**

* [Image input](https://developers.openai.com/api/docs/guides/images-vision)
* [Multiple images](https://developers.openai.com/api/docs/guides/images-vision#analyze-multiple-images)
* [Image resolution](https://developers.openai.com/api/docs/guides/images-vision#specify-image-input-detail-level)
* [OCR](https://tesseract-ocr.github.io/tessdoc/ImproveQuality.html)
* [Chart analysis](https://developers.openai.com/api/docs/guides/file-inputs#non-pdf-image-and-chart-limitations)
* [Screenshot understanding](https://developers.openai.com/cookbook/examples/multimodal/image_understanding_with_rag)
* [Diagram interpretation](https://developers.openai.com/cookbook/examples/multimodal/document_and_multimodal_understanding_tips)
* [PDF-page analysis](https://developers.openai.com/api/docs/guides/file-inputs#pdf-detail-levels)
* [Visual question answering](https://developers.openai.com/api/docs/guides/images-vision#analyze-images)
* [Structured visual extraction](https://developers.openai.com/cookbook/examples/multimodal/using_gpt4_vision_with_function_calling)

**Practice**

Create an architecture-document analyzer that understands:

* Text
* Tables
* Cloud architecture diagrams
* Dashboard screenshots
* Scanned pages
* Configuration screenshots

The current multimodal Cookbook area covers text, images, audio and video-related workflows.

---

### Chapter 11: Image generation and editing

**Topics**

* [Text-to-image generation](https://developers.openai.com/api/docs/guides/image-generation)
* [Image prompting](https://developers.openai.com/api/docs/guides/tools-image-generation)
* [Composition](https://developers.openai.com/api/docs/models/gpt-image-2)
* [Aspect ratio](https://developers.openai.com/api/docs/guides/image-generation#size-and-quality-options)
* [Text rendering](https://developers.openai.com/api/docs/guides/image-generation#limitations)
* [Visual consistency](https://developers.openai.com/api/docs/guides/image-generation#multi-turn-image-generation)
* [Image editing](https://developers.openai.com/api/docs/guides/image-generation#image-api)
* [Masking](https://developers.openai.com/api/docs/guides/image-generation#edit-images)
* [Input fidelity](https://developers.openai.com/api/docs/guides/image-generation#input-fidelity)
* [Iterative refinement](https://developers.openai.com/cookbook/examples/generate_images_with_gpt_image)
* [Image evaluation](https://developers.openai.com/api/docs/guides/image-generation#image-generation-evals)

**Practice**

Build a marketing-asset generator that accepts:

* Product description
* Audience
* Brand constraints
* Aspect ratio
* Reference image
* Required text

---

### Chapter 12: Speech and audio

**Topics**

* [Speech-to-text](https://developers.openai.com/api/docs/guides/audio)
* [Audio transcription](https://developers.openai.com/api/reference/resources/audio/subresources/transcriptions/methods/create)
* [Text-to-speech](https://developers.openai.com/api/docs/guides/text-to-speech)
* [Audio input](https://developers.openai.com/api/docs/guides/realtime-conversations#audio-inputs-and-outputs)
* [Audio output](https://developers.openai.com/api/docs/guides/text-to-speech#supported-output-formats)
* [Streaming](https://developers.openai.com/api/docs/guides/speech-to-text#streaming-transcriptions)
* [Noise handling](https://developers.openai.com/api/docs/guides/realtime-transcription#handling-silence-and-background-noise)
* [Speaker considerations](https://developers.openai.com/api/docs/guides/speech-to-text#speaker-diarization)
* [Transcription evaluation](https://developers.openai.com/api/docs/guides/transcription#evaluate-transcription-quality)

**Practice**

Create a meeting assistant that transcribes audio, extracts decisions and produces structured action items.

---

### Chapter 13: Realtime API and voice agents

**Topics**

* [Realtime sessions](https://developers.openai.com/api/docs/guides/realtime#realtime-sessions)
* [WebRTC](https://developers.openai.com/api/docs/guides/realtime-webrtc)
* [WebSocket](https://developers.openai.com/api/docs/guides/realtime-websocket)
* [Audio buffers](https://developers.openai.com/api/docs/guides/realtime-conversations)
* [Voice activity detection](https://developers.openai.com/api/docs/guides/realtime-vad)
* [Turn detection](https://developers.openai.com/api/docs/guides/realtime-vad#turn-detection)
* [Interruptions](https://openai.github.io/openai-agents-python/realtime/guide)
* [Realtime tools](https://developers.openai.com/api/docs/guides/realtime-mcp)
* [Context management](https://developers.openai.com/api/docs/guides/realtime-conversations#managing-conversations)
* [Voice-agent latency](https://developers.openai.com/api/docs/guides/latency-optimization#seven-principles)
* [Voice-agent evaluation](https://developers.openai.com/cookbook/examples/realtime_eval_guide)

**Practice**

Build a bilingual English–Japanese voice assistant that:

* Handles interruption
* Calls one tool
* Maintains conversation context
* Stores a transcript
* Measures response latency

---

### Chapter 14: Video generation — optional specialization

**Topics**

* [Storyboarding](https://www.studiobinder.com/blog/types-of-camera-shots-sizes-in-film)
* [Scene prompts](https://developers.openai.com/api/docs/guides/video-generation)
* [Camera directions](https://developers.openai.com/api/docs/guides/video-generation#effective-prompting)
* [Motion description](https://developers.openai.com/api/docs/guides/video-generation#generate-a-video)
* [Temporal consistency](https://developers.openai.com/api/docs/guides/video-generation#use-characters-for-consistency)
* [Reference assets](https://developers.openai.com/api/reference/resources/videos)
* [Generation lifecycle](https://developers.openai.com/api/docs/models/sora-2)
* [Video evaluation](https://github.com/Netflix/vmaf)

**Practice**

Generate a short technical product explainer from a storyboard and evaluate visual consistency between scenes.

---

## Phase 5 — Agent engineering

### Chapter 15: Agent fundamentals

**Topics**

* [Agent versus workflow](https://developers.openai.com/api/docs/guides/agents/guardrails-approvals#workflow-boundaries-matter)
* [Instructions](https://developers.openai.com/api/docs/guides/agents/define-agents#shape-instructions-handoffs-and-outputs)
* [Tools](https://openai.github.io/openai-agents-python/tools)
* [State](https://developers.openai.com/api/docs/guides/agents/results)
* [Memory](https://developers.openai.com/api/docs/guides/agents/sandboxes#persist-memory-across-runs)
* [Planning](https://developers.openai.com/plugins/build/examples#planning-for-the-context-window)
* [Execution loops](https://developers.openai.com/api/docs/guides/agents)
* [Stop conditions](https://openai.github.io/openai-agents-python/running_agents/#exceptions)
* [Human approval](https://openai.github.io/openai-agents-python/human_in_the_loop)
* [Tracing](https://openai.github.io/openai-agents-python/tracing)
* [Handoffs](https://openai.github.io/openai-agents-python/handoffs)

**Practice**

Convert an existing deterministic workflow into a bounded agent and compare both approaches.

OpenAI’s guidance distinguishes a Responses API application—where one model call plus tools and application logic may be sufficient—from systems that need SDK-managed orchestration.

---

### Chapter 16: Agents SDK fundamentals

**Topics**

* [Agent definitions](https://developers.openai.com/api/docs/guides/agents/define-agents)
* [Agent instructions](https://openai.github.io/openai-agents-python/agents)
* [Agent runner](https://developers.openai.com/api/docs/guides/agents/running-agents)
* [Results](https://openai.github.io/openai-agents-python/results)
* [Output types](https://openai.github.io/openai-agents-python/agents/#output-types)
* [Sessions](https://openai.github.io/openai-agents-python/sessions)
* [Tools](https://openai.github.io/openai-agents-python/tools#common-tools)
* [Model configuration](https://openai.github.io/openai-agents-python/config)
* [Error handling](https://openai.github.io/openai-agents-python/tools/#handling-errors-in-function-tools)
* [Tracing](https://developers.openai.com/api/docs/guides/agents/integrations-observability#tracing)

**Practice**

Build a single research agent with:

* Web-search tool
* File-search tool
* Structured report output
* Maximum-step limit
* Complete trace

---

### Chapter 17: Multi-agent orchestration

**Topics**

* [Manager pattern](https://developers.openai.com/api/docs/guides/agents/orchestration)
* [Specialist agents](https://developers.openai.com/api/docs/guides/agents/orchestration#add-specialists-only-when-the-contract-changes)
* [Handoffs](https://developers.openai.com/api/docs/guides/agents/orchestration#use-handoffs-for-delegated-ownership)
* [Agent-as-tool](https://developers.openai.com/api/docs/guides/agents/orchestration#use-agents-as-tools-for-manager-style-workflows)
* [Sequential execution](https://openai.github.io/openai-agents-python/examples/#deterministic-flows)
* [Parallel execution](https://openai.github.io/openai-agents-python/examples/#parallelization)
* [Routing](https://openai.github.io/openai-agents-python/examples)
* [Context isolation](https://openai.github.io/openai-agents-python/context)
* [Shared state](https://openai.github.io/openai-agents-python/context/#local-context)
* [Result synthesis](https://openai.github.io/openai-agents-python/results/#final-output)

**Practice architecture**

```text
Architecture Research Manager
├── Requirements Agent
├── Technical Research Agent
├── Security Review Agent
├── Cost Analysis Agent
└── Report Generation Agent
```

Start with a single agent and split it only when evaluations show that specialization improves quality or reliability.

---

### Chapter 18: Agent memory and long-running workflows

**Topics**

* [Session state](https://openai.github.io/openai-agents-python/ref/run_state)
* [Short-term memory](https://openai.github.io/openai-agents-python/sessions/#core-session-behavior)
* [Persistent memory](https://openai.github.io/openai-agents-python/sessions/#memory-persistence)
* [Context compaction](https://developers.openai.com/api/docs/guides/compaction)
* [Summarization](https://developers.openai.com/api/docs/guides/compaction#client-side-compaction)
* [Checkpoints](https://developers.openai.com/api/docs/guides/supervised-fine-tuning#use-checkpoints-if-needed)
* [Resumability](https://openai.github.io/openai-agents-python/human_in_the_loop/#long-running-approvals)
* [Execution budgets](https://openai.github.io/openai-agents-python/usage)
* [Maximum iterations](https://openai.github.io/openai-agents-python/running_agents/#max-turns)
* [Loop detection](https://openai.github.io/openai-agents-python/tools/#tool-use-behavior)
* [Cancellation](https://openai.github.io/openai-agents-python/results/#streaming-lifecycle-and-diagnostics)
* [Recovery](https://openai.github.io/openai-agents-python/running_agents/#errors-and-recovery)

**Practice**

Build a resumable research agent with:

* Maximum execution budget
* Saved checkpoints
* Context summarization
* Duplicate-work detection
* User cancellation
* Recovery from tool failure

---

### Chapter 19: Model Context Protocol

**Topics**

* [MCP clients and servers](https://modelcontextprotocol.io/docs/learn/architecture)
* [MCP tools](https://modelcontextprotocol.io/specification/2025-06-18/server/tools)
* [MCP resources](https://modelcontextprotocol.io/specification/2025-06-18/server/resources)
* [Tool discovery](https://openai.github.io/openai-agents-python/mcp)
* [Authentication](https://developers.openai.com/api/docs/guides/tools-connectors-mcp#authentication)
* [Local versus remote MCP](https://developers.openai.com/api/docs/guides/tools-connectors-mcp)
* [Approval controls](https://developers.openai.com/api/docs/guides/tools-connectors-mcp#approvals)
* [Trust boundaries](https://developers.openai.com/api/docs/guides/secure-mcp-tunnels#logging-boundaries)
* [Auditing](https://developers.openai.com/codex/enterprise/compliance-api)

**Practice**

Expose a read-only internal architecture repository through an MCP server and connect it to your research agent.

---

### Chapter 20: Computer use and sandbox agents

**Topics**

* [Computer interaction loops](https://developers.openai.com/api/docs/guides/tools-computer-use#option-1-run-the-built-in-computer-use-loop)
* [Screenshots](https://developers.openai.com/api/docs/guides/tools-computer-use)
* [Browser actions](https://developers.openai.com/api/docs/guides/tools-computer-use#3-run-every-returned-action)
* [Action verification](https://developers.openai.com/api/docs/guides/tools-computer-use#4-acknowledge-safety-checks)
* [Sandboxed code execution](https://developers.openai.com/api/docs/guides/agents/sandboxes)
* [Filesystem boundaries](https://developers.openai.com/codex/sandboxing#filesystem-access)
* [Network restrictions](https://developers.openai.com/api/docs/guides/tools-shell#network-access)
* [Credential protection](https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html)
* [Human approval](https://developers.openai.com/api/docs/guides/tools-computer-use#human-in-the-loop)
* [Coding agents](https://developers.openai.com/codex/guides/build-ai-native-engineering-team)

**Practice**

Build a sandbox coding agent that can:

* Read a repository
* Create a plan
* Modify files
* Run tests
* Generate a patch
* Require approval before external or destructive actions

---

## Phase 6 — Evals and quality engineering

### Chapter 21: Evaluation fundamentals

**Topics**

* [Eval datasets](https://developers.openai.com/api/docs/guides/evals)
* [Representative cases](https://developers.openai.com/api/docs/guides/evaluation-best-practices#handle-edge-cases)
* [Edge cases](https://developers.openai.com/api/docs/guides/evaluation-best-practices)
* [Adversarial cases](https://developers.openai.com/api/docs/guides/red-teaming)
* [Regression tests](https://developers.openai.com/api/docs/guides/evals#uploading-test-data)
* [Dataset versioning](https://developers.openai.com/api/docs/guides/evaluation-getting-started)
* [Human evaluation](https://huggingface.co/docs/evaluate/main/a_quick_tour)
* [Automated graders](https://developers.openai.com/api/docs/guides/evaluation-getting-started#add-graders)

**Practice**

Create an initial dataset containing:

| Test type          | Cases |
| ------------------ | ----: |
| Normal cases       |    40 |
| Difficult cases    |    20 |
| Edge cases         |    15 |
| Adversarial cases  |    10 |
| Tool-failure cases |    10 |
| Safety cases       |     5 |

OpenAI defines evals as tests used to determine whether model outputs meet specified content and style criteria.

---

### Chapter 22: Graders

**Topics**

* [Exact-match grading](https://docs.python.org/3/howto/regex.html)
* [Schema validation](https://python-jsonschema.readthedocs.io/en/stable/validate)
* [Regex grading](https://developers.openai.com/api/docs/guides/graders#python-graders)
* [Semantic similarity](https://developers.openai.com/api/docs/guides/graders#text-similarity-graders)
* [Model-based grading](https://developers.openai.com/api/docs/guides/graders#model-graders)
* [Pairwise comparison](https://developers.openai.com/cookbook/examples/evaluation/how_to_eval_abstractive_summarization)
* [Human grading](https://developers.openai.com/api/docs/guides/evaluation-best-practices#human-evals)
* [Multi-grader aggregation](https://scikit-learn.org/stable/modules/calibration.html)

**Practice**

Build separate graders for:

* Correctness
* Citation quality
* Completeness
* Format compliance
* Safety
* Writing quality

---

### Chapter 23: Agent, RAG and multimodal evaluation

**Topics**

* [Tool-selection accuracy](https://openai.github.io/openai-agents-python/ref/tracing)
* [Tool-argument accuracy](https://developers.openai.com/api/docs/guides/agent-evals#evaluate-tool-calls)
* [Agent trajectory](https://developers.openai.com/api/docs/guides/agent-evals)
* [Handoff correctness](https://developers.openai.com/api/docs/guides/agent-evals#evaluate-handoffs)
* [Retrieval recall](https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/context_recall)
* [Citation correctness](https://developers.openai.com/api/docs/guides/citation-formatting#validate-citations)
* [Image understanding](https://developers.openai.com/api/docs/guides/vision-fine-tuning)
* [Voice-agent quality](https://developers.openai.com/cookbook/examples/realtime_eval_guide#evaluating-a-realtime-agent)
* [Latency and cost](https://developers.openai.com/api/docs/guides/prompt-caching)
* [Failure recovery](https://developers.openai.com/api/docs/guides/agent-evals#evaluate-failure-recovery)

**Practice dashboard**

Track:

* Task success rate
* Retrieval recall
* Citation accuracy
* Tool-call success
* Average agent steps
* P50 and P95 latency
* Average cost per task
* Safety failures
* Regression count

---

## Phase 7 — Guardrails and security

### Chapter 24: AI security and guardrails

**Topics**

* [Moderation](https://developers.openai.com/api/docs/guides/moderation)
* [Prompt injection](https://developers.openai.com/api/docs/guides/tools-connectors-mcp#prompt-injection)
* [Indirect prompt injection](https://developers.openai.com/api/docs/guides/agent-builder-safety#prompt-injections)
* [Jailbreaks](https://genai.owasp.org/llmrisk/llm01-prompt-injection)
* [PII protection](https://www.nist.gov/privacy-framework)
* [Secret leakage](https://developers.openai.com/api/docs/guides/agent-builder-safety#private-data-leakage)
* [Tool allowlists](https://developers.openai.com/api/docs/guides/secure-mcp-tunnels#advanced-allowlisted-http-callouts)
* [Output validation](https://developers.openai.com/api/docs/guides/agent-builder-safety#use-structured-outputs-to-constrain-data-flow)
* [Data exfiltration](https://developers.openai.com/api/docs/guides/deep-research#prompt-injection-and-exfiltration)
* [Human approval](https://developers.openai.com/api/docs/guides/agent-builder-safety#keep-tool-approvals-on)
* [Audit logs](https://developers.openai.com/api/docs/guides/admin-apis#retrieve-audit-logs)
* [Least privilege](https://developers.openai.com/api/docs/guides/rbac)

**Guardrail architecture**

```text
Authentication
   ↓
Input validation
   ↓
Moderation
   ↓
Prompt-injection detection
   ↓
Tool allowlist
   ↓
Argument validation
   ↓
Human approval
   ↓
Output validation
   ↓
Data-loss prevention
   ↓
Audit logging
```

Guardrails are controls intended to keep agents operating safely, consistently and within defined boundaries.

---

## Phase 8 — Optimization and customization

### Chapter 25: Cost and latency optimization

**Topics**

* [Prompt caching](https://developers.openai.com/api/docs/guides/upgrading-to-gpt-5p6-sol#prompt-caching)
* [Streaming](https://developers.openai.com/api/docs/guides/structured-outputs#streaming)
* [Batch processing](https://developers.openai.com/api/docs/guides/latency-optimization#process-tokens-faster)
* [Parallel requests](https://developers.openai.com/cookbook/examples/how_to_handle_rate_limits)
* [Rate limits](https://developers.openai.com/api/docs/guides/rate-limits)
* [Exponential backoff](https://developers.openai.com/api/docs/guides/rate-limits#retrying-with-exponential-backoff)
* [Concurrency](https://developers.openai.com/api/docs/guides/cost-optimization#cost-and-latency)
* [Model routing](https://developers.openai.com/api/docs/guides/latency-optimization#dont-default-to-an-llm)
* [Context pruning](https://developers.openai.com/api/docs/guides/compaction#when-to-compact)
* [Token budgets](https://developers.openai.com/api/docs/guides/spend-limits)
* [Load testing](https://grafana.com/docs/k6/latest/testing-guides/load-testing-websites)
* [Cost attribution](https://developers.openai.com/api/docs/guides/cost-optimization)

**Practice**

Optimize one project and compare:

```text
Cost per successful request
P50 latency
P95 latency
Task success rate
Token consumption
Retry rate
```

---

### Chapter 26: Fine-tuning

**Topics**

* [When to fine-tune](https://developers.openai.com/api/docs/guides/model-optimization#fine-tune-a-model)
* [Dataset creation](https://developers.openai.com/api/docs/guides/supervised-fine-tuning#build-your-dataset)
* [Training and validation splits](https://developers.openai.com/api/docs/guides/fine-tuning-best-practices)
* [Supervised fine-tuning](https://developers.openai.com/api/docs/guides/supervised-fine-tuning)
* [Vision fine-tuning](https://developers.openai.com/api/docs/guides/vision-fine-tuning#control-image-quality)
* [Preference optimization](https://developers.openai.com/api/docs/guides/direct-preference-optimization)
* [Reinforcement fine-tuning](https://developers.openai.com/api/docs/guides/reinforcement-fine-tuning)
* [Distillation](https://developers.openai.com/api/reference/resources/fine_tuning)
* [Overfitting](https://developers.openai.com/api/docs/guides/model-optimization#fine-tuning-methods)
* [Post-training evaluation](https://developers.openai.com/api/docs/guides/supervised-fine-tuning#compare-to-evals)

**Recommended decision order**

```text
Improve prompt
   ↓
Add few-shot examples
   ↓
Add retrieval
   ↓
Add tools
   ↓
Evaluate again
   ↓
Fine-tune only when justified
```

Vision fine-tuning can specialize a model for image-based tasks, but it should be backed by a baseline evaluation and representative training data.

---

## Phase 9 — Codex, ChatGPT apps and open-weight models

### Chapter 27: Codex and coding agents

**Topics**

* [Repository instructions](https://developers.openai.com/codex/guides/agents-md)
* [Coding-agent prompts](https://developers.openai.com/api/docs/guides/latest-model/gpt-5.4#keep-tool-boundaries-explicit-in-coding-and-terminal-agents)
* [Planning](https://developers.openai.com/api/docs/guides/latest-model/gpt-5#maximizing-coding-performance-from-planning-to-execution)
* [Goal definition](https://developers.openai.com/codex/prompting#write-a-clear-task)
* [Test-driven changes](https://docs.pytest.org/en/stable/how-to/assert.html)
* [Iterative repair](https://developers.openai.com/codex/prompting#iterate-on-the-result)
* [Code review](https://developers.openai.com/codex/code-review)
* [Legacy migration](https://martinfowler.com/articles/patterns-legacy-displacement)
* [CI integration](https://developers.openai.com/codex/noninteractive)
* [Sandboxed execution](https://developers.openai.com/codex/sandboxing)

**Practice**

Use Codex on a noncritical repository to:

1. Understand the repository
2. Produce a change plan
3. Implement one feature
4. Add unit tests
5. Run static analysis
6. Explain assumptions
7. Produce a reviewable change

The Codex Cookbook is the live collection for coding-agent automation and development workflows.

---

### Chapter 28: ChatGPT Apps SDK

**Topics**

* [Apps SDK architecture](https://developers.openai.com/apps-sdk)
* [MCP server integration](https://developers.openai.com/apps-sdk/build/mcp-server)
* [Tool definitions](https://developers.openai.com/apps-sdk/build/mcp-server#define-tools)
* [UI components](https://developers.openai.com/apps-sdk/build/chatgpt-ui)
* [Authentication](https://developers.openai.com/apps-sdk/build/auth)
* [ChatGPT components](https://developers.openai.com/apps-sdk/build/chatgpt-ui#use-components)
* [Application state](https://developers.openai.com/apps-sdk/build/state-management)
* [Deployment](https://developers.openai.com/apps-sdk/deploy)
* [Security and review](https://developers.openai.com/apps-sdk/deploy#security-reminders)

**Practice**

Build a ChatGPT app that searches your architecture standards and displays structured recommendations in an interactive UI.

---

### Chapter 29: gpt-oss and local AI

**Topics**

* [Open-weight models](https://developers.openai.com/api/docs/models/gpt-oss-120b)
* [Local inference](https://huggingface.co/docs/transformers/main/model_doc/gpt_oss)
* [Hardware requirements](https://huggingface.co/openai/gpt-oss-120b#hardware-requirements)
* [Quantization](https://huggingface.co/docs/transformers/quantization/overview)
* [Model serving](https://docs.vllm.ai/en/latest/serving/openai_compatible_server)
* [Prompt formats](https://huggingface.co/docs/transformers/main/model_doc/gpt_oss#usage-tips)
* [Tool use](https://developers.openai.com/api/docs/guides/latest-model/gpt-5.4#make-tool-use-persistent-when-correctness-depends-on-it)
* [Fine-tuning](https://developers.openai.com/cookbook/articles/gpt-oss/fine-tune-transfomers)
* [Safety models](https://huggingface.co/openai/gpt-oss-safeguard-120b)
* [Hosted/local model routing](https://developers.openai.com/api/docs/guides/agents/models#choose-models-per-agent)

**Practice**

Build a hybrid model router:

```text
Private or straightforward task
             ↓
       Local gpt-oss

Complex reasoning or tool task
             ↓
      Hosted OpenAI model
```

Compare:

* Quality
* Latency
* Hardware utilization
* Privacy
* Hosted API cost
* Local operating cost
* Operational complexity

The gpt-oss Cookbook covers OpenAI’s open-weight model ecosystem, including local deployment and customization examples.

---

# Recommended 24-week sequence

| Week | Chapter              | Main resource                                                                                                                 | Deliverable                  |
| ---: | -------------------- | ----------------------------------------------------------------------------------------------------------------------------- | ---------------------------- |
|    1 | API fundamentals     | API documentation                                                                   | Streaming CLI assistant      |
|    2 | Model selection      | Model selection guide | Model comparison harness     |
|    3 | Prompt engineering   | Prompt engineering                                        | Prompt experiment report     |
|    4 | Structured Outputs   | Structured Outputs introduction                   | Document extractor           |
|    5 | Text patterns        | Text Cookbook                                                            | Text-processing pipeline     |
|    6 | Function calling     | Function calling                                            | Tool-enabled assistant       |
|    7 | Built-in tools       | Using tools                                                            | Cited research assistant     |
|    8 | Embeddings           | Embeddings                                                        | Semantic search              |
|    9 | RAG                  | Retrieval                                                          | PDF knowledge assistant      |
|   10 | Vision               | Multimodal Cookbook                                                | Document-vision analyzer     |
|   11 | Image generation     | Image generation                                            | Image-generation application |
|   12 | Audio                | Speech-to-text                                                | Meeting transcription app    |
|   13 | Realtime             | Realtime API                                                        | Bilingual voice assistant    |
|   14 | Agent fundamentals   | Agents guide                                                          | Single research agent        |
|   15 | Agents SDK           | Agents SDK quickstart                                            | Traced agent application     |
|   16 | Multi-agent systems  | Multi-agent orchestration                                       | Specialist-agent workflow    |
|   17 | MCP and computer use | MCP guide                                               | Read-only MCP integration    |
|   18 | Eval fundamentals    | Evals guide                                                            | 100-case eval dataset        |
|   19 | System evals         | Evals Cookbook                                                          | Quality dashboard            |
|   20 | Guardrails           | Guardrails Cookbook                                                | Threat model and controls    |
|   21 | Optimization         | Optimization Cookbook                                            | Cost and latency report      |
|   22 | Fine-tuning          | Model optimization                                        | Fine-tuning experiment       |
|   23 | Codex                | Codex Cookbook                                                          | Tested repository change     |
|   24 | Apps SDK and gpt-oss | Apps SDK                                                                            | Final integrated capstone    |

## Capstone outcome

By the end, build an **Enterprise AI Architecture Assistant** with:

* Structured requirement analysis
* PDF and diagram understanding
* RAG with citations
* Web research
* Tool calling
* Multi-agent review
* English and Japanese voice support
* Evaluation suite
* Guardrails
* Tracing
* Cost and latency monitoring
* Optional local gpt-oss routing

Use the [Cookbook archive](https://developers.openai.com/cookbook/archive) only for concepts not covered by current recipes; archived notebooks may use older APIs or models and may need migration to the Responses API.

## Link policy

- Every study URL appears once; the sequence table uses resource names without repeating links.
- Each chapter keeps its detailed topic checklist, adds topic-specific study links, and retains its original practice exercise and explanatory notes.
- Prefer current maintained guides; archived recipes may require migration to the Responses API.
