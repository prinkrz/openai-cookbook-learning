# OpenAI Cookbook Learning Roadmap with Resources

The roadmap below maps each chapter to a **primary learning resource**, relevant **Cookbook recipes**, and a practical outcome. Because the Cookbook is continuously updated, use its topic pages as the live index and individual recipes as hands-on chapters. ([OpenAI Developers][1])

## Phase 1 — API foundations

### Chapter 1: OpenAI API fundamentals

**Topics**

* OpenAI SDK setup
* API keys and environment variables
* Responses API
* Request and response structure
* Streaming
* Token usage
* Errors, retries and rate limits

**Study resources**

1. [OpenAI API documentation](https://developers.openai.com/api/docs)
2. [API reference overview](https://developers.openai.com/api/reference/overview/)
3. [OpenAI Cookbook](https://developers.openai.com/cookbook)
4. [Responses API reference](https://developers.openai.com/api/reference/responses/)
5. [Cookbook: How to handle rate limits](https://developers.openai.com/cookbook/examples/how_to_handle_rate_limits)

**Practice**

Create a Python command-line assistant that streams its answer, displays token usage and handles timeout, authentication and rate-limit errors.

---

### Chapter 2: Models and model selection

**Topics**

* Model families
* Reasoning versus non-reasoning models
* Speed, quality and cost
* Context windows
* Reasoning effort
* Model fallback
* Task-based model routing

**Study resources**

1. [Models overview](https://developers.openai.com/api/docs/models)
2. [Compare OpenAI models](https://developers.openai.com/api/docs/models/compare)
3. [Reasoning models guide](https://developers.openai.com/api/docs/guides/reasoning)
4. [Cookbook: Practical Guide for Model Selection](https://developers.openai.com/cookbook/examples/partners/model_selection_guide/model_selection_guide)
5. [Cookbook Text collection](https://developers.openai.com/cookbook/topic/text)

**Practice**

Run 20 representative tasks through different models and compare:

* Accuracy
* Latency
* Token usage
* Estimated cost
* Output consistency

The official model comparison page should be treated as the current source for supported capabilities, context limits and pricing because these details change over time. ([OpenAI Developers][2])

---

## Phase 2 — Text and reliable outputs

### Chapter 3: Prompt engineering

**Topics**

* Instruction hierarchy
* Developer and user messages
* Clear objectives
* Context placement
* Delimiters
* Few-shot examples
* Acceptance criteria
* Long-context prompting
* Prompt migration
* Prompt iteration

**Study resources**

1. [Prompt engineering guide](https://developers.openai.com/api/docs/guides/prompt-engineering)
2. [Cookbook: GPT-4.1 Prompting Guide](https://developers.openai.com/cookbook/examples/gpt4-1_prompting_guide)
3. [Cookbook Text collection](https://developers.openai.com/cookbook/topic/text)
4. [Reasoning best practices](https://developers.openai.com/api/docs/guides/reasoning-best-practices)
5. [Prompt optimizer](https://developers.openai.com/api/docs/guides/prompt-optimizer)

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

* JSON generation
* JSON Schema
* Pydantic models
* Required and optional fields
* Enumerations
* Nested objects
* Schema validation
* Refusal handling
* Schema versioning

**Study resources**

1. [Structured Outputs guide](https://developers.openai.com/api/docs/guides/structured-outputs)
2. [Cookbook: Introduction to Structured Outputs](https://developers.openai.com/cookbook/examples/structured_outputs_intro)
3. [Cookbook: Structured Outputs for Multi-Agent Systems](https://developers.openai.com/cookbook/examples/structured_outputs_multi_agent)
4. [Cookbook: Structured Outputs Evaluation](https://developers.openai.com/cookbook/examples/evaluation/use-cases/structured-outputs-evaluation)
5. [Function calling guide](https://developers.openai.com/api/docs/guides/function-calling)

**Practice projects**

* Resume parser
* Invoice extractor
* Meeting action-item extractor
* Support-ticket classifier
* Architecture-requirement extractor

Structured Outputs constrains model responses to a supplied JSON Schema, making it an important foundation for tool use and production integrations. ([OpenAI Developers][3])

---

### Chapter 5: Core text application patterns

**Topics**

* Classification
* Summarization
* Translation
* Rewriting
* Information extraction
* Question answering
* Intent detection
* Sentiment analysis
* Code generation
* Document comparison

**Study resources**

1. [Text generation guide](https://developers.openai.com/api/docs/guides/text)
2. [Cookbook Text collection](https://developers.openai.com/cookbook/topic/text)
3. [Cookbook: Summarizing long documents](https://developers.openai.com/cookbook/examples/summarizing_long_documents)
4. [Batch API guide](https://developers.openai.com/api/docs/guides/batch)
5. [Cookbook: Batch processing](https://developers.openai.com/cookbook/examples/batch_processing)

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

* Function definitions
* Tool schemas
* Tool selection
* Tool-call arguments
* Multiple tool calls
* Parallel tool calls
* Tool result submission
* Input validation
* Idempotency
* Error handling
* Human approval

**Study resources**

1. [Function calling guide](https://developers.openai.com/api/docs/guides/function-calling)
2. [Using tools guide](https://developers.openai.com/api/docs/guides/tools)
3. [Cookbook: How to call functions with chat models](https://developers.openai.com/cookbook/examples/how_to_call_functions_with_chat_models)
4. [Cookbook: Parallel function calling](https://developers.openai.com/cookbook/examples/how_to_call_functions_for_knowledge_retrieval)
5. [Structured Outputs guide](https://developers.openai.com/api/docs/guides/structured-outputs)

**Practice**

Build an assistant with application-controlled tools for:

* Currency conversion
* Weather lookup
* Calendar availability
* Database search
* Internal documentation search

Function calling connects models to external data and application capabilities, but the application should validate arguments and control execution. ([OpenAI Developers][4])

---

### Chapter 7: Responses API and built-in tools

**Topics**

* Responses API
* Conversation state
* Previous response IDs
* Web search
* File search
* Code execution
* Tool citations
* Multi-turn workflows
* Background processing
* Tool permissions

**Study resources**

1. [Responses API reference](https://developers.openai.com/api/reference/responses/)
2. [Using tools](https://developers.openai.com/api/docs/guides/tools)
3. [Web search guide](https://developers.openai.com/api/docs/guides/tools-web-search)
4. [File search guide](https://developers.openai.com/api/docs/guides/tools-file-search)
5. [Code Interpreter guide](https://developers.openai.com/api/docs/guides/tools-code-interpreter)
6. [Conversation state guide](https://developers.openai.com/api/docs/guides/conversation-state)
7. [Background mode](https://developers.openai.com/api/docs/guides/background)

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

* Embedding vectors
* Semantic similarity
* Cosine similarity
* Semantic search
* Classification
* Clustering
* Recommendations
* Deduplication
* Batch embedding
* Vector databases

**Study resources**

1. [Embeddings guide](https://developers.openai.com/api/docs/guides/embeddings)
2. [Embedding models](https://developers.openai.com/api/docs/models#embeddings)
3. [Cookbook: Using embeddings](https://developers.openai.com/cookbook/examples/using_embeddings)
4. [Cookbook: Semantic text search using embeddings](https://developers.openai.com/cookbook/examples/semantic_text_search_using_embeddings)
5. [Cookbook: Clustering using embeddings](https://developers.openai.com/cookbook/examples/clustering)
6. [Cookbook: Classification using embeddings](https://developers.openai.com/cookbook/examples/classification_using_embeddings)

**Practice**

Create a semantic search engine for architecture documents and compare it with keyword search.

---

### Chapter 9: Retrieval-augmented generation

**Topics**

* Document ingestion
* Chunking
* Chunk overlap
* Metadata
* Vector stores
* Semantic retrieval
* Hybrid retrieval
* Query rewriting
* Reranking
* Context assembly
* Grounded answers
* Citations
* Retrieval evaluation

**Study resources**

1. [Retrieval guide](https://developers.openai.com/api/docs/guides/retrieval)
2. [File search guide](https://developers.openai.com/api/docs/guides/tools-file-search)
3. [Vector stores API](https://developers.openai.com/api/reference/vector-stores/)
4. [Cookbook: PDF RAG with File Search](https://developers.openai.com/cookbook/examples/file_search_responses)
5. [Cookbook: Question answering using embeddings](https://developers.openai.com/cookbook/examples/question_answering_using_embeddings)
6. [Cookbook: Deep Research API introduction](https://developers.openai.com/cookbook/examples/deep_research_api/introduction_to_deep_research_api)

**Practice**

Build a PDF knowledge assistant that:

* Uploads and indexes PDFs
* Retrieves relevant passages
* Includes citations
* Uses metadata filtering
* Returns “insufficient evidence” when appropriate
* Measures retrieval recall separately from answer quality

The Deep Research API Cookbook demonstrates workflows involving reasoning, planning and synthesis across external information. ([OpenAI Developers][5])

---

## Phase 4 — Multimodal development

### Chapter 10: Vision and document understanding

**Topics**

* Image input
* Multiple images
* Image resolution
* OCR
* Chart analysis
* Screenshot understanding
* Diagram interpretation
* PDF-page analysis
* Visual question answering
* Structured visual extraction

**Study resources**

1. [Images and vision guide](https://developers.openai.com/api/docs/guides/images-vision)
2. [Cookbook Multimodal collection](https://developers.openai.com/cookbook/topic/multimodal)
3. [Cookbook: GPT-5.4 Vision and Document Understanding](https://developers.openai.com/cookbook/examples/multimodal/document_and_multimodal_understanding_tips)
4. [Cookbook: Introduction to GPT-4o](https://developers.openai.com/cookbook/examples/gpt4o/introduction_to_gpt4o)
5. [Cookbook: Image Understanding with RAG](https://developers.openai.com/cookbook/examples/multimodal/image_understanding_with_rag)

**Practice**

Create an architecture-document analyzer that understands:

* Text
* Tables
* Cloud architecture diagrams
* Dashboard screenshots
* Scanned pages
* Configuration screenshots

The current multimodal Cookbook area covers text, images, audio and video-related workflows. ([OpenAI Developers][6])

---

### Chapter 11: Image generation and editing

**Topics**

* Text-to-image generation
* Image prompting
* Composition
* Aspect ratio
* Text rendering
* Visual consistency
* Image editing
* Masking
* Input fidelity
* Iterative refinement
* Image evaluation

**Study resources**

1. [Image generation guide](https://developers.openai.com/api/docs/guides/image-generation)
2. [Images API reference](https://developers.openai.com/api/reference/images/)
3. [Cookbook Multimodal collection](https://developers.openai.com/cookbook/topic/multimodal)
4. [Cookbook: Generate images with GPT Image](https://developers.openai.com/cookbook/examples/generate_images_with_gpt_image)
5. [Cookbook: Image generation prompting guide](https://developers.openai.com/cookbook/examples/multimodal/image_generation_prompting_guide)

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

* Speech-to-text
* Audio transcription
* Text-to-speech
* Audio input
* Audio output
* Streaming
* Noise handling
* Speaker considerations
* Transcription evaluation

**Study resources**

1. [Speech-to-text guide](https://developers.openai.com/api/docs/guides/speech-to-text)
2. [Text-to-speech guide](https://developers.openai.com/api/docs/guides/text-to-speech)
3. [Audio API reference](https://developers.openai.com/api/reference/audio/)
4. [Cookbook Multimodal collection](https://developers.openai.com/cookbook/topic/multimodal)
5. [Cookbook: Comparing speech-to-text methods](https://developers.openai.com/cookbook/examples/comparing_speech_to_text_methods)

**Practice**

Create a meeting assistant that transcribes audio, extracts decisions and produces structured action items.

---

### Chapter 13: Realtime API and voice agents

**Topics**

* Realtime sessions
* WebRTC
* WebSocket
* Audio buffers
* Voice activity detection
* Turn detection
* Interruptions
* Realtime tools
* Context management
* Voice-agent latency
* Voice-agent evaluation

**Study resources**

1. [Realtime API guide](https://developers.openai.com/api/docs/guides/realtime)
2. [Realtime conversations](https://developers.openai.com/api/docs/guides/realtime-conversations)
3. [Realtime WebRTC guide](https://developers.openai.com/api/docs/guides/realtime-webrtc)
4. [Realtime WebSocket guide](https://developers.openai.com/api/docs/guides/realtime-websocket)
5. [Realtime API reference](https://developers.openai.com/api/reference/realtime/)
6. [Cookbook: Realtime Prompting Guide](https://developers.openai.com/cookbook/examples/realtime_prompting_guide)
7. [Cookbook: Realtime Eval Guide](https://developers.openai.com/cookbook/examples/realtime_eval_guide)

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

* Storyboarding
* Scene prompts
* Camera directions
* Motion description
* Temporal consistency
* Reference assets
* Generation lifecycle
* Video evaluation

**Study resources**

1. [Video generation guide](https://developers.openai.com/api/docs/guides/video-generation)
2. [Videos API reference](https://developers.openai.com/api/reference/videos/)
3. [Cookbook Multimodal collection](https://developers.openai.com/cookbook/topic/multimodal)

**Practice**

Generate a short technical product explainer from a storyboard and evaluate visual consistency between scenes.

---

## Phase 5 — Agent engineering

### Chapter 15: Agent fundamentals

**Topics**

* Agent versus workflow
* Instructions
* Tools
* State
* Memory
* Planning
* Execution loops
* Stop conditions
* Human approval
* Tracing
* Handoffs

**Study resources**

1. [Agents guide](https://developers.openai.com/api/docs/guides/agents)
2. [Agents Cookbook collection](https://developers.openai.com/cookbook/topic/agents)
3. [Agents SDK documentation](https://openai.github.io/openai-agents-python/)
4. [Agents SDK quickstart](https://openai.github.io/openai-agents-python/quickstart/)
5. [Practical guide to building agents](https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/)

**Practice**

Convert an existing deterministic workflow into a bounded agent and compare both approaches.

OpenAI’s guidance distinguishes a Responses API application—where one model call plus tools and application logic may be sufficient—from systems that need SDK-managed orchestration. ([OpenAI Developers][7])

---

### Chapter 16: Agents SDK fundamentals

**Topics**

* Agent definitions
* Agent instructions
* Agent runner
* Results
* Output types
* Sessions
* Tools
* Model configuration
* Error handling
* Tracing

**Study resources**

1. [Agents SDK overview](https://openai.github.io/openai-agents-python/)
2. [Agents SDK quickstart](https://openai.github.io/openai-agents-python/quickstart/)
3. [Defining agents](https://openai.github.io/openai-agents-python/agents/)
4. [Running agents](https://openai.github.io/openai-agents-python/running_agents/)
5. [Agent tools](https://openai.github.io/openai-agents-python/tools/)
6. [Agent results](https://openai.github.io/openai-agents-python/results/)
7. [Agent tracing](https://openai.github.io/openai-agents-python/tracing/)

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

* Manager pattern
* Specialist agents
* Handoffs
* Agent-as-tool
* Sequential execution
* Parallel execution
* Routing
* Context isolation
* Shared state
* Result synthesis

**Study resources**

1. [Multi-agent orchestration](https://openai.github.io/openai-agents-python/multi_agent/)
2. [Handoffs](https://openai.github.io/openai-agents-python/handoffs/)
3. [Agents as tools](https://openai.github.io/openai-agents-python/tools/)
4. [Cookbook: Structured Outputs for Multi-Agent Systems](https://developers.openai.com/cookbook/examples/structured_outputs_multi_agent)
5. [Agents Cookbook collection](https://developers.openai.com/cookbook/topic/agents)

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

* Session state
* Short-term memory
* Persistent memory
* Context compaction
* Summarization
* Checkpoints
* Resumability
* Execution budgets
* Maximum iterations
* Loop detection
* Cancellation
* Recovery

**Study resources**

1. [Agent sessions](https://openai.github.io/openai-agents-python/sessions/)
2. [Running agents](https://openai.github.io/openai-agents-python/running_agents/)
3. [Conversation state](https://developers.openai.com/api/docs/guides/conversation-state)
4. [Background mode](https://developers.openai.com/api/docs/guides/background)
5. [Agents Cookbook collection](https://developers.openai.com/cookbook/topic/agents)

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

* MCP clients and servers
* MCP tools
* MCP resources
* Tool discovery
* Authentication
* Local versus remote MCP
* Approval controls
* Trust boundaries
* Auditing

**Study resources**

1. [MCP guide](https://developers.openai.com/api/docs/guides/tools-connectors-mcp)
2. [Agents SDK MCP documentation](https://openai.github.io/openai-agents-python/mcp/)
3. [Using tools](https://developers.openai.com/api/docs/guides/tools)
4. [Agents Cookbook collection](https://developers.openai.com/cookbook/topic/agents)
5. [Deep Research API introduction](https://developers.openai.com/cookbook/examples/deep_research_api/introduction_to_deep_research_api)

**Practice**

Expose a read-only internal architecture repository through an MCP server and connect it to your research agent.

---

### Chapter 20: Computer use and sandbox agents

**Topics**

* Computer interaction loops
* Screenshots
* Browser actions
* Action verification
* Sandboxed code execution
* Filesystem boundaries
* Network restrictions
* Credential protection
* Human approval
* Coding agents

**Study resources**

1. [Computer use guide](https://developers.openai.com/api/docs/guides/tools-computer-use)
2. [Code Interpreter guide](https://developers.openai.com/api/docs/guides/tools-code-interpreter)
3. [Shell tool guide](https://developers.openai.com/api/docs/guides/tools-shell)
4. [Agents Cookbook collection](https://developers.openai.com/cookbook/topic/agents)
5. [Codex Cookbook collection](https://developers.openai.com/cookbook/topic/codex)

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

* Eval datasets
* Representative cases
* Edge cases
* Adversarial cases
* Regression tests
* Dataset versioning
* Human evaluation
* Automated graders

**Study resources**

1. [Evals guide](https://developers.openai.com/api/docs/guides/evals)
2. [Cookbook Evals collection](https://developers.openai.com/cookbook/topic/evals)
3. [Cookbook: Getting Started with OpenAI Evals](https://developers.openai.com/cookbook/examples/evaluation/getting_started_with_openai_evals)
4. [Evaluation best practices](https://developers.openai.com/api/docs/guides/evaluation-best-practices)
5. [Evals API reference](https://developers.openai.com/api/reference/evals/)

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

OpenAI defines evals as tests used to determine whether model outputs meet specified content and style criteria. ([OpenAI Developers][8])

---

### Chapter 22: Graders

**Topics**

* Exact-match grading
* Schema validation
* Regex grading
* Semantic similarity
* Model-based grading
* Pairwise comparison
* Human grading
* Multi-grader aggregation

**Study resources**

1. [Graders guide](https://developers.openai.com/api/docs/guides/graders)
2. [Evals guide](https://developers.openai.com/api/docs/guides/evals)
3. [Cookbook Evals collection](https://developers.openai.com/cookbook/topic/evals)
4. [Structured Outputs Evaluation](https://developers.openai.com/cookbook/examples/evaluation/use-cases/structured-outputs-evaluation)
5. [Evaluation best practices](https://developers.openai.com/api/docs/guides/evaluation-best-practices)

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

* Tool-selection accuracy
* Tool-argument accuracy
* Agent trajectory
* Handoff correctness
* Retrieval recall
* Citation correctness
* Image understanding
* Voice-agent quality
* Latency and cost
* Failure recovery

**Study resources**

1. [Cookbook Evals collection](https://developers.openai.com/cookbook/topic/evals)
2. [Agent evaluation](https://openai.github.io/openai-agents-python/agent_replay/)
3. [Tracing](https://openai.github.io/openai-agents-python/tracing/)
4. [Cookbook: Realtime Eval Guide](https://developers.openai.com/cookbook/examples/realtime_eval_guide)
5. [Cookbook: Structured Outputs Evaluation](https://developers.openai.com/cookbook/examples/evaluation/use-cases/structured-outputs-evaluation)

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

* Moderation
* Prompt injection
* Indirect prompt injection
* Jailbreaks
* PII protection
* Secret leakage
* Tool allowlists
* Output validation
* Data exfiltration
* Human approval
* Audit logs
* Least privilege

**Study resources**

1. [Cookbook Guardrails collection](https://developers.openai.com/cookbook/topic/guardrails)
2. [Safety best practices](https://developers.openai.com/api/docs/guides/safety-best-practices)
3. [Moderation guide](https://developers.openai.com/api/docs/guides/moderation)
4. [Agents SDK guardrails](https://openai.github.io/openai-agents-python/guardrails/)
5. [Safety checks](https://developers.openai.com/api/docs/guides/safety-checks)
6. [Building Governed AI Agents](https://developers.openai.com/cookbook/examples/partners/agentic_governance_guide/agentic_governance_cookbook)

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

Guardrails are controls intended to keep agents operating safely, consistently and within defined boundaries. ([OpenAI Developers][9])

---

## Phase 8 — Optimization and customization

### Chapter 25: Cost and latency optimization

**Topics**

* Prompt caching
* Streaming
* Batch processing
* Parallel requests
* Rate limits
* Exponential backoff
* Concurrency
* Model routing
* Context pruning
* Token budgets
* Load testing
* Cost attribution

**Study resources**

1. [Cookbook Optimization collection](https://developers.openai.com/cookbook/topic/optimization)
2. [Latency optimization](https://developers.openai.com/api/docs/guides/latency-optimization)
3. [Prompt caching](https://developers.openai.com/api/docs/guides/prompt-caching)
4. [Batch API](https://developers.openai.com/api/docs/guides/batch)
5. [Rate limits](https://developers.openai.com/api/docs/guides/rate-limits)
6. [Cookbook: How to handle rate limits](https://developers.openai.com/cookbook/examples/how_to_handle_rate_limits)
7. [Cookbook: Model Selection Guide](https://developers.openai.com/cookbook/examples/partners/model_selection_guide/model_selection_guide)

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

* When to fine-tune
* Dataset creation
* Training and validation splits
* Supervised fine-tuning
* Vision fine-tuning
* Preference optimization
* Reinforcement fine-tuning
* Distillation
* Overfitting
* Post-training evaluation

**Study resources**

1. [Model optimization overview](https://developers.openai.com/api/docs/guides/model-optimization)
2. [Supervised fine-tuning](https://developers.openai.com/api/docs/guides/supervised-fine-tuning)
3. [Vision fine-tuning](https://developers.openai.com/api/docs/guides/vision-fine-tuning)
4. [Direct Preference Optimization](https://developers.openai.com/api/docs/guides/direct-preference-optimization)
5. [Reinforcement fine-tuning](https://developers.openai.com/api/docs/guides/reinforcement-fine-tuning)
6. [Fine-tuning API reference](https://developers.openai.com/api/reference/fine-tuning/)
7. [Cookbook: Vision Fine-tuning for Visual Question Answering](https://developers.openai.com/cookbook/examples/multimodal/vision_fine_tuning_on_gpt4o_for_visual_question_answering)

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

Vision fine-tuning can specialize a model for image-based tasks, but it should be backed by a baseline evaluation and representative training data. ([OpenAI Developers][10])

---

## Phase 9 — Codex, ChatGPT apps and open-weight models

### Chapter 27: Codex and coding agents

**Topics**

* Repository instructions
* Coding-agent prompts
* Planning
* Goal definition
* Test-driven changes
* Iterative repair
* Code review
* Legacy migration
* CI integration
* Sandboxed execution

**Study resources**

1. [Codex documentation](https://developers.openai.com/codex)
2. [Codex Cookbook collection](https://developers.openai.com/cookbook/topic/codex)
3. [Codex CLI](https://developers.openai.com/codex/cli)
4. [Codex IDE integration](https://developers.openai.com/codex/ide)
5. [Codex GitHub integration](https://developers.openai.com/codex/integrations/github)
6. [Agents SDK](https://openai.github.io/openai-agents-python/)

**Practice**

Use Codex on a noncritical repository to:

1. Understand the repository
2. Produce a change plan
3. Implement one feature
4. Add unit tests
5. Run static analysis
6. Explain assumptions
7. Produce a reviewable change

The Codex Cookbook is the live collection for coding-agent automation and development workflows. ([OpenAI Developers][11])

---

### Chapter 28: ChatGPT Apps SDK

**Topics**

* Apps SDK architecture
* MCP server integration
* Tool definitions
* UI components
* Authentication
* ChatGPT components
* Application state
* Deployment
* Security and review

**Study resources**

1. [Apps SDK documentation](https://developers.openai.com/apps-sdk)
2. [Apps SDK quickstart](https://developers.openai.com/apps-sdk/quickstart)
3. [Build an MCP server](https://developers.openai.com/apps-sdk/build/mcp-server)
4. [Build a ChatGPT UI](https://developers.openai.com/apps-sdk/build/chatgpt-ui)
5. [Authentication](https://developers.openai.com/apps-sdk/build/auth)
6. [Apps SDK examples](https://developers.openai.com/apps-sdk/resources/examples)
7. [ChatGPT Cookbook collection](https://developers.openai.com/cookbook/topic/chatgpt)

**Practice**

Build a ChatGPT app that searches your architecture standards and displays structured recommendations in an interactive UI.

---

### Chapter 29: gpt-oss and local AI

**Topics**

* Open-weight models
* Local inference
* Hardware requirements
* Quantization
* Model serving
* Prompt formats
* Tool use
* Fine-tuning
* Safety models
* Hosted/local model routing

**Study resources**

1. [gpt-oss Cookbook collection](https://developers.openai.com/cookbook/topic/gpt-oss)
2. [gpt-oss model documentation](https://developers.openai.com/api/docs/models/gpt-oss-120b)
3. [Cookbook: Fine-tuning gpt-oss with Hugging Face](https://developers.openai.com/cookbook/articles/gpt-oss/fine-tune-transfomers)
4. [OpenAI Cookbook GitHub repository](https://github.com/openai/openai-cookbook)

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

The gpt-oss Cookbook covers OpenAI’s open-weight model ecosystem, including local deployment and customization examples. ([OpenAI Developers][12])

---

# Recommended 24-week sequence

| Week | Chapter              | Main resource                                                                                                                 | Deliverable                  |
| ---: | -------------------- | ----------------------------------------------------------------------------------------------------------------------------- | ---------------------------- |
|    1 | API fundamentals     | [API documentation](https://developers.openai.com/api/docs)                                                                   | Streaming CLI assistant      |
|    2 | Model selection      | [Model selection guide](https://developers.openai.com/cookbook/examples/partners/model_selection_guide/model_selection_guide) | Model comparison harness     |
|    3 | Prompt engineering   | [Prompt engineering](https://developers.openai.com/api/docs/guides/prompt-engineering)                                        | Prompt experiment report     |
|    4 | Structured Outputs   | [Structured Outputs introduction](https://developers.openai.com/cookbook/examples/structured_outputs_intro)                   | Document extractor           |
|    5 | Text patterns        | [Text Cookbook](https://developers.openai.com/cookbook/topic/text)                                                            | Text-processing pipeline     |
|    6 | Function calling     | [Function calling](https://developers.openai.com/api/docs/guides/function-calling)                                            | Tool-enabled assistant       |
|    7 | Built-in tools       | [Using tools](https://developers.openai.com/api/docs/guides/tools)                                                            | Cited research assistant     |
|    8 | Embeddings           | [Embeddings](https://developers.openai.com/api/docs/guides/embeddings)                                                        | Semantic search              |
|    9 | RAG                  | [Retrieval](https://developers.openai.com/api/docs/guides/retrieval)                                                          | PDF knowledge assistant      |
|   10 | Vision               | [Multimodal Cookbook](https://developers.openai.com/cookbook/topic/multimodal)                                                | Document-vision analyzer     |
|   11 | Image generation     | [Image generation](https://developers.openai.com/api/docs/guides/image-generation)                                            | Image-generation application |
|   12 | Audio                | [Speech-to-text](https://developers.openai.com/api/docs/guides/speech-to-text)                                                | Meeting transcription app    |
|   13 | Realtime             | [Realtime API](https://developers.openai.com/api/docs/guides/realtime)                                                        | Bilingual voice assistant    |
|   14 | Agent fundamentals   | [Agents guide](https://developers.openai.com/api/docs/guides/agents)                                                          | Single research agent        |
|   15 | Agents SDK           | [Agents SDK quickstart](https://openai.github.io/openai-agents-python/quickstart/)                                            | Traced agent application     |
|   16 | Multi-agent systems  | [Multi-agent orchestration](https://openai.github.io/openai-agents-python/multi_agent/)                                       | Specialist-agent workflow    |
|   17 | MCP and computer use | [MCP guide](https://developers.openai.com/api/docs/guides/tools-connectors-mcp)                                               | Read-only MCP integration    |
|   18 | Eval fundamentals    | [Evals guide](https://developers.openai.com/api/docs/guides/evals)                                                            | 100-case eval dataset        |
|   19 | System evals         | [Evals Cookbook](https://developers.openai.com/cookbook/topic/evals)                                                          | Quality dashboard            |
|   20 | Guardrails           | [Guardrails Cookbook](https://developers.openai.com/cookbook/topic/guardrails)                                                | Threat model and controls    |
|   21 | Optimization         | [Optimization Cookbook](https://developers.openai.com/cookbook/topic/optimization)                                            | Cost and latency report      |
|   22 | Fine-tuning          | [Model optimization](https://developers.openai.com/api/docs/guides/model-optimization)                                        | Fine-tuning experiment       |
|   23 | Codex                | [Codex Cookbook](https://developers.openai.com/cookbook/topic/codex)                                                          | Tested repository change     |
|   24 | Apps SDK and gpt-oss | [Apps SDK](https://developers.openai.com/apps-sdk)                                                                            | Final integrated capstone    |

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

Use the [Cookbook archive](https://developers.openai.com/cookbook/archive) only for concepts not covered by current recipes; archived notebooks may use older APIs or models and may need migration to the Responses API. ([OpenAI Developers][13])

[1]: https://developers.openai.com/cookbook?utm_source=chatgpt.com "Cookbook"
[2]: https://developers.openai.com/api/docs/guides/reasoning?utm_source=chatgpt.com "Reasoning models | OpenAI API"
[3]: https://developers.openai.com/api/docs/guides/structured-outputs?utm_source=chatgpt.com "Structured model outputs | OpenAI API"
[4]: https://developers.openai.com/api/docs/guides/function-calling?utm_source=chatgpt.com "Function calling | OpenAI API"
[5]: https://developers.openai.com/cookbook/examples/deep_research_api/introduction_to_deep_research_api?utm_source=chatgpt.com "Introduction to deep research in the OpenAI API"
[6]: https://developers.openai.com/cookbook/topic/multimodal?utm_source=chatgpt.com "Multimodal • Cookbook"
[7]: https://developers.openai.com/cookbook/topic/agents?utm_source=chatgpt.com "Agents • Cookbook"
[8]: https://developers.openai.com/api/docs/guides/evals?utm_source=chatgpt.com "Working with evals | OpenAI API"
[9]: https://developers.openai.com/cookbook/topic/guardrails?utm_source=chatgpt.com "Guardrails • Cookbook"
[10]: https://developers.openai.com/cookbook/examples/multimodal/vision_fine_tuning_on_gpt4o_for_visual_question_answering?utm_source=chatgpt.com "Vision Fine-tuning on GPT-4o for Visual Question Answering"
[11]: https://developers.openai.com/cookbook/topic/codex?utm_source=chatgpt.com "Codex • Cookbook"
[12]: https://developers.openai.com/cookbook/topic/gpt-oss?utm_source=chatgpt.com "gpt-oss • Cookbook"
[13]: https://developers.openai.com/cookbook/archive?utm_source=chatgpt.com "Cookbook Archive"
