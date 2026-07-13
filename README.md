# OpenAI Cookbook Learning Roadmap

The Cookbook is a continuously updated collection rather than a fixed course. Its current high-level areas include **Text, Multimodal, Agents, Evals, Guardrails, Optimization, ChatGPT, Codex, and gpt-oss**, while recipes also carry more specific labels such as Responses API, tools, embeddings, fine-tuning, audio, image generation, computer use, and scaling. ([OpenAI Developers][1])

The roadmap below reorganizes those recipes into a sensible learning sequence. It is designed as a **24-week path at 7–10 hours per week**.

---

## Learning method for every chapter

For each topic:

1. Read the relevant API documentation.
2. Run the Cookbook notebook unchanged.
3. Rewrite it as a normal Python application.
4. Change the dataset, prompt, or use case.
5. Add error handling and logging.
6. Add at least five evaluation examples.
7. Record cost, latency, and output quality.
8. Integrate the capability into the ongoing capstone project.

Use one GitHub repository:

```text
openai-cookbook-learning/
├── 01-api-foundations/
├── 02-prompting/
├── 03-structured-output/
├── 04-tools/
├── 05-embeddings-rag/
├── 06-multimodal/
├── 07-realtime-voice/
├── 08-agents/
├── 09-evals/
├── 10-guardrails/
├── 11-optimization/
├── 12-fine-tuning/
├── 13-codex/
├── 14-chatgpt-apps/
├── 15-gpt-oss/
└── capstone/
```

---

# Phase 1 — OpenAI API foundations

## Week 1: Platform setup and first API application

### Chapter 1: API fundamentals

Study:

* OpenAI SDK installation
* API-key management
* Environment variables
* Request and response structure
* Model selection
* Input and output tokens
* Context windows
* Streaming
* Usage metadata
* API errors
* Timeouts and retries
* Rate limits
* Cost tracking

### Practice

Build a command-line assistant that:

* Accepts a user prompt
* Calls the Responses API
* Streams the answer
* Displays token usage
* Handles authentication and rate-limit errors
* Logs request duration

### Completion criteria

You should be able to explain:

* Why API keys must remain server-side
* When to stream responses
* How input length affects cost and latency
* How retry logic differs from normal application retries

The current developer documentation positions the Responses API alongside text generation, structured output, function calling, and tool use as core concepts. ([OpenAI Developers][2])

---

## Week 2: Model selection and reasoning

### Chapter 2: Choosing the right model

Study:

* General-purpose models
* Reasoning models
* Coding-oriented models
* Small versus large models
* Latency, cost, and quality trade-offs
* Reasoning effort
* Maximum output length
* Determinism and output variability
* Model fallback strategies

Recommended Cookbook material:

* Practical Guide for Model Selection
* GPT prompting guides
* Better performance from reasoning models
* Model migration guides

### Practice

Create a model-comparison harness that runs the same 20 tasks across several models and records:

```text
Task
Model
Accuracy
Latency
Input tokens
Output tokens
Estimated cost
Human rating
```

### Deliverable

Write a model-routing function:

```python
def select_model(
    task_type: str,
    complexity: str,
    latency_sensitive: bool,
    budget_sensitive: bool,
) -> str:
    ...
```

---

# Phase 2 — Text, prompting, and reliable outputs

## Week 3: Prompt engineering

### Chapter 3: Prompt construction

Study:

* System and developer instructions
* User messages
* Instruction hierarchy
* Clear task definitions
* Context placement
* Delimiters
* Few-shot examples
* Positive and negative examples
* Constraints
* Output contracts
* Prompt decomposition
* Long-context prompting
* Prompt injection awareness
* Prompt migration
* Prompt optimization

Recommended Cookbook sequence:

1. GPT prompting guide
2. Prompt migration guide
3. Optimize Prompts
4. Resilient-prompt evaluation workflows
5. Frontend coding prompting examples

### Practice

Take five weak prompts and improve each through:

1. Baseline prompt
2. Structured instructions
3. Few-shot examples
4. Explicit acceptance criteria
5. Evaluation-driven revision

### Deliverable

Create a reusable prompt template:

```text
Role
Objective
Available context
Required process
Constraints
Output schema
Examples
Failure behavior
Quality checklist
```

---

## Week 4: Structured Outputs and extraction

### Chapter 4: Generating machine-readable data

Study:

* JSON output
* JSON Schema
* Structured Outputs
* Pydantic models
* Optional and required fields
* Enumerations
* Nested structures
* Validation
* Refusal handling
* Parsing failures
* Schema versioning

Recommended Cookbook material:

* Introduction to Structured Outputs
* Entity extraction examples
* Function-schema examples

### Practice projects

Build:

* Invoice information extractor
* Resume parser
* Support-ticket classifier
* Meeting-note action-item extractor

### Completion criteria

Your program must:

* Validate every response
* Reject malformed objects
* Distinguish extraction failure from empty data
* Store the schema version with the result

Structured Outputs appears as a foundational Cookbook recipe and supports later work with tools and agents. ([OpenAI Developers][1])

---

## Week 5: Classification, transformation, and text workflows

### Chapter 5: Common language-model patterns

Study:

* Classification
* Summarization
* Information extraction
* Rewriting
* Translation
* Question answering
* Intent detection
* Topic labeling
* Sentiment analysis
* Document comparison
* Code generation
* Log-probability-based confidence
* Batch processing

Recommended Cookbook topics:

* Text generation
* Completions
* Reasoning
* Log probabilities
* Code-quality and security analysis
* Batch-oriented processing patterns

### Practice

Create a document-processing pipeline:

```text
Document
  ↓
Classification
  ↓
Structured extraction
  ↓
Summary
  ↓
Risk flags
  ↓
Validated JSON result
```

---

# Phase 3 — Tools, retrieval, and application integration

## Week 6: Function calling and custom tools

### Chapter 6: Connecting models to application logic

Study:

* Function/tool definitions
* JSON parameters
* Tool selection
* Tool-call responses
* Multiple tool calls
* Parallel tool calls
* Tool-result injection
* Validation before execution
* Idempotency
* Tool permissions
* Side-effect control
* Human approval
* Tool errors
* Tool timeouts

### Practice

Build an assistant with tools for:

* Weather lookup using a mock service
* Currency conversion
* Database query
* Calendar availability
* Internal knowledge search

Do not allow the model to execute arbitrary SQL directly. Place an application-controlled validation layer between model output and execution.

### Deliverable

Implement the loop:

```text
User request
  ↓
Model decides whether a tool is needed
  ↓
Application validates the tool call
  ↓
Application executes it
  ↓
Tool result returned to model
  ↓
Final response
```

---

## Week 7: Built-in tools and Responses API state

### Chapter 7: Platform-provided tools

Study:

* Web search
* File search
* Code execution patterns
* Computer use
* Conversation state
* Previous response identifiers
* Multi-turn workflows
* Background or long-running API patterns, where supported
* Tool-result citations
* Trust boundaries

Recommended Cookbook material:

* Web Search and States with Responses API
* PDF RAG with File Search
* Deep Research API introduction
* Skills in the OpenAI API
* Computer-use examples

### Practice

Build a research assistant that:

* Searches approved sources
* Produces a cited answer
* Maintains conversation state
* Records which claims came from which source
* Clearly separates retrieved facts from model inference

---

## Weeks 8–9: Embeddings, semantic search, and RAG

### Chapter 8: Embeddings

Study:

* What embeddings represent
* Vector dimensions
* Similarity metrics
* Cosine similarity
* Semantic search
* Classification using embeddings
* Clustering
* Deduplication
* Recommendation
* Query and document embeddings
* Batch embedding
* Rate-limit handling

Recommended recipes:

* Using embeddings
* Embedding Wikipedia articles for search
* Rate-limit handling

The Cookbook’s embedding example demonstrates generating vectors and recommends exponential backoff for high-volume calls. ([OpenAI Developers][3])

### Chapter 9: Retrieval-augmented generation

Study:

* Document ingestion
* Text extraction
* Chunking
* Chunk overlap
* Metadata
* Vector stores
* Hybrid retrieval
* Query rewriting
* Reranking
* Context assembly
* Source citations
* Grounded generation
* Retrieval evaluation
* Index updates
* Access control

Recommended recipes:

* PDF RAG using File Search
* Image Understanding with RAG
* Multi-tool orchestration with a RAG approach
* Deep Research with Agents SDK
* MCP-based research systems

### Practice project

Build a private documentation assistant supporting:

* PDF ingestion
* Metadata filters
* Semantic retrieval
* Exact source citations
* “Insufficient evidence” responses
* Retrieval-quality evaluation

### Essential lesson

Do not evaluate only the final answer. Measure:

1. Whether the correct document was retrieved
2. Whether the correct chunk was retrieved
3. Whether the answer used the retrieved evidence correctly

---

# Phase 4 — Multimodal AI

## Week 10: Vision and document understanding

### Chapter 10: Image input and visual reasoning

Study:

* Image URLs and uploaded images
* Base64 image inputs
* Resolution and detail
* Multiple images
* OCR
* Chart interpretation
* Screenshot understanding
* Document-page analysis
* Visual question answering
* Image-grounded extraction
* Spatial reasoning
* Vision limitations

Recommended recipes:

* Vision and document-understanding prompting guides
* Image Understanding with RAG
* Grounded spatial-reasoning evaluation
* Vision fine-tuning

The Multimodal section explicitly covers vision, images, and speech and includes document understanding, image RAG, image generation, audio, and vision fine-tuning. ([OpenAI Developers][4])

### Practice

Build a document analyst that can process:

* Invoices
* Architecture diagrams
* Dashboard screenshots
* Forms
* Tables
* Scanned documents

Require structured output and include a confidence field supported by explicit evidence—not merely the model’s self-reported certainty.

---

## Week 11: Image generation and editing

### Chapter 11: Generative image workflows

Study:

* Text-to-image prompting
* Composition
* Subject consistency
* Style and visual direction
* Aspect ratio
* Text rendering
* Image editing
* Mask-based editing
* Input fidelity
* Iterative refinement
* Image quality evaluation
* Safety constraints

Recommended recipes:

* Generate images with GPT Image
* High-input-fidelity generation
* Current image-model prompting guides
* Image-generation and editing evals

### Practice

Create:

* Product-marketing visual generator
* Diagram-illustration generator
* Image-editing workflow
* Automated image-evaluation rubric

---

## Week 12: Audio, speech, and realtime systems

### Chapter 12: Audio fundamentals

Study:

* Speech-to-text
* Text-to-speech
* Audio input
* Audio output
* Transcription quality
* Speaker and noise considerations
* Streaming audio
* Voice activity detection
* Turn detection
* Interruptions
* Latency management

### Chapter 13: Realtime API

Study:

* Realtime sessions
* WebSocket or WebRTC architecture
* Session configuration
* Audio buffers
* Tool use during voice conversations
* Realtime prompting
* Context summarization
* Long-session management
* Voice-agent evaluation

Recommended recipes:

* Comparing speech-to-text methods
* Realtime Prompting Guide
* Realtime Eval Guide
* Context summarization with Realtime API
* Live translation
* MCP-powered agentic voice framework

### Practice project

Build a voice support agent that:

* Accepts spoken requests
* Calls one external tool
* Supports interruption
* Reads back the result
* Stores a text transcript
* Measures first-response latency and task success

---

## Optional Week 13: Video generation

### Chapter 14: Video workflows

Study:

* Video-generation concepts
* Prompt planning
* Shot composition
* Motion descriptions
* Camera movement
* Temporal consistency
* Storyboarding
* Asset preparation
* Generation lifecycle
* Output evaluation
* Safety and rights considerations

### Practice

Create a 15–30 second product explainer from:

* A storyboard
* Scene prompts
* Visual references
* An evaluation checklist

Treat video as an optional specialization after image-generation fundamentals.

---

# Phase 5 — Agent engineering

## Week 14: Agent fundamentals

### Chapter 15: From workflows to agents

Study:

* What makes a system agentic
* Instructions
* Tools
* State
* Memory
* Planning
* Execution loops
* Stop conditions
* Handoffs
* Approvals
* Tracing
* Deterministic workflow versus autonomous agent

OpenAI describes agents as systems that use models to execute instructions, make decisions, collect context through tools, and take actions within defined guardrails. ([OpenAI Developers][1])

### Decision framework

Use a deterministic workflow when:

* Steps are known
* Compliance requires a fixed sequence
* Failures are expensive
* The model does not need to choose the next action

Use an agent when:

* The next step depends on discovered information
* Tool selection is dynamic
* The task requires iterative investigation
* Multiple valid solution paths exist

---

## Week 15: Agents SDK

### Chapter 16: Building a single agent

Study:

* Agent definitions
* Instructions
* Models and providers
* Running agents
* Results
* Session state
* Tools
* Traces
* Error handling
* Output types

### Chapter 17: Orchestration

Study:

* Manager-agent pattern
* Handoffs
* Specialist agents
* Sequential orchestration
* Parallel orchestration
* Agent-as-tool
* Routing
* Shared state
* Context isolation
* Result synthesis

The current Agents SDK documentation divides the subject into agent definitions, execution, sandbox agents, orchestration, guardrails, state, observability, evaluation, and voice agents. ([OpenAI Developers][2])

### Practice

Build:

```text
Research Manager
├── Web Research Agent
├── Document Analysis Agent
├── Data Analysis Agent
└── Report Writing Agent
```

Start with one agent using multiple tools. Introduce multiple agents only when specialization creates measurable improvements.

---

## Week 16: Advanced agents, memory, and MCP

### Chapter 18: Reliable long-running agents

Study:

* Short-term conversation state
* Persistent memory
* Memory retrieval
* Context compaction
* Summarization
* Checkpoints
* Resumability
* Execution budgets
* Maximum iterations
* Loop detection
* Cancellation
* Recovery
* Human escalation

Recommended Cookbook material:

* Reliable agents with memory and compaction
* Multi-agent portfolio collaboration
* Parallel agents
* Supply-chain copilot with MCP servers
* Deep Research MCP Server
* Temporal agents with knowledge graphs
* Workspace-agent examples

### Chapter 19: Model Context Protocol

Study:

* MCP servers and clients
* Tools, resources, and prompts
* Authentication
* Remote versus local servers
* Trust boundaries
* Tool discovery
* Tool descriptions
* Connector security
* Auditing

### Practice

Expose one internal system as an MCP server, then allow your agent to use it under read-only permissions.

---

## Week 17: Computer-use and sandbox agents

### Chapter 20: Agents that interact with environments

Study:

* Computer-use loops
* Screenshot observation
* Action proposals
* Browser interaction
* Sandboxed execution
* Coding agents
* Filesystem boundaries
* Network restrictions
* Credential isolation
* Human approval for risky actions
* Verifying action completion

Recommended recipes:

* Computer Use Agents in sandbox environments
* Migrating legacy codebases with sandbox agents
* Code Interpreter-style tool generation
* Coding agents using the Agents SDK

### Practice

Build a sandboxed coding agent that:

* Reads a small repository
* Proposes a change
* Modifies a branch
* Runs tests
* Produces a patch
* Never merges or deploys automatically

---

# Phase 6 — Evals and quality engineering

## Week 18: Evaluation fundamentals

### Chapter 21: Building an eval dataset

Study:

* Task definition
* Evaluation criteria
* Representative examples
* Edge cases
* Negative cases
* Adversarial cases
* Train/dev/test separation
* Dataset versioning
* Regression suites
* Human review

### Chapter 22: Graders

Study:

* Exact-match graders
* Schema-validation graders
* String and regex graders
* Semantic-similarity graders
* Model-based graders
* Pairwise comparison
* Reference-free evaluation
* Human grading
* Multi-grader aggregation

### Practice

Build an evaluation set containing:

```text
40 normal cases
20 difficult cases
15 edge cases
10 adversarial cases
10 tool-failure cases
5 safety cases
```

The Cookbook’s Evals collection covers prompt resilience, agent evaluation, multimodal evaluation, macro evaluation, governed agents, and agent-improvement loops. ([OpenAI Developers][5])

---

## Week 19: Agent and multimodal evals

### Chapter 23: Evaluating complete systems

Study:

* Final-answer evaluation
* Tool-selection accuracy
* Tool-argument accuracy
* Handoff correctness
* Trajectory evaluation
* Trace evaluation
* Retrieval evaluation
* Latency
* Cost
* Number of steps
* Failure recovery
* Audio evaluation
* Image evaluation
* Macro evals for multi-agent systems

Recommended sequence:

1. Eval-Driven System Design
2. Evaluating Agents
3. Realtime Eval Guide
4. Image Evals
5. Macro Evals for Agentic Systems
6. Agent Improvement Loop

### Practice

Create a dashboard showing:

* Task success rate
* Groundedness
* Tool-call success rate
* Average number of agent turns
* P50/P95 latency
* Average token cost
* Safety failure rate
* Regression count

---

# Phase 7 — Guardrails, security, and governance

## Week 20: Guardrails

### Chapter 24: Input and output protection

Study:

* Moderation
* Prompt injection
* Indirect prompt injection
* Jailbreak resistance
* PII handling
* Secret leakage
* Output validation
* Topic restrictions
* Tool permissioning
* Data exfiltration
* Human approval
* Audit logs
* Policy-as-code
* Least privilege
* Fail-closed versus fail-open behavior

The Cookbook defines guardrails as controls that keep agents safe, consistent, and within their intended boundaries. ([OpenAI Developers][6])

### Guardrail layers

```text
1. User authentication
2. Input validation
3. Moderation
4. Prompt-injection detection
5. Tool allowlist
6. Argument validation
7. Human approval
8. Output validation
9. Data-loss prevention
10. Logging and monitoring
```

### Practice

Threat-model your research agent:

* Identify assets
* Identify trust boundaries
* List attack scenarios
* Add preventive controls
* Add detection controls
* Add recovery procedures
* Create adversarial eval cases

---

# Phase 8 — Optimization and customization

## Week 21: Cost, latency, and scaling

### Chapter 25: Production optimization

Study:

* Prompt caching
* Response streaming
* Parallel requests
* Batch processing
* Asynchronous application architecture
* Rate-limit management
* Exponential backoff
* Concurrency control
* Model routing
* Context pruning
* Retrieval before generation
* Token budgeting
* Cost attribution
* Observability
* Load testing

Recommended Cookbook material:

* Rate-limit handling
* Prompt Caching
* Batch workflows
* Model selection
* Scaling examples

### Practice

Optimize one existing application against:

```text
Baseline cost per request
Optimized cost per request
Baseline P95 latency
Optimized P95 latency
Task-success change
```

Never accept a cost improvement that silently causes an unacceptable quality regression.

---

## Week 22: Fine-tuning

### Chapter 26: Choosing a customization technique

Learn this decision order:

```text
Prompting
   ↓
Few-shot examples
   ↓
RAG
   ↓
Tool use
   ↓
Fine-tuning
```

Study:

* Dataset preparation
* Training and validation split
* JSONL formats
* Data quality
* Baseline evaluation
* Supervised fine-tuning
* Vision fine-tuning
* Preference optimization
* Reinforcement fine-tuning
* Model distillation
* Hyperparameters
* Overfitting
* Post-training evaluation
* Deployment and monitoring

The Cookbook’s fine-tuning guide distinguishes supervised fine-tuning, vision fine-tuning, direct preference optimization, and reinforcement fine-tuning, each suited to different kinds of customization. ([OpenAI Developers][7])

### Recommended sequence

1. How to fine-tune chat models
2. Model distillation
3. Vision fine-tuning
4. DPO guide
5. Reinforcement fine-tuning
6. RFT with domain-specific evaluation

### Practice

Fine-tune only after establishing:

* A reproducible baseline
* A stable evaluation set
* At least 50–100 high-quality examples for experimentation
* A measurable target improvement
* A deployment rollback plan

---

# Phase 9 — Codex, ChatGPT apps, and open models

## Week 23: Codex and software-engineering agents

### Chapter 27: Codex workflows

Study:

* Repository instructions
* Coding-agent prompts
* Planning files
* Goals
* Iterative repair
* Test-driven changes
* Code review
* Legacy migration
* Sandbox execution
* CI integration
* Agent SDK integration
* Trace-to-improvement loops

Recommended recipes:

* Codex Prompting Guide
* PLANS.md for extended problem solving
* Consistent workflows with Codex CLI and Agents SDK
* Build a coding agent
* Iterative repair loops
* Using Goals in Codex
* Legacy-codebase migration
* Agent improvement loop with Codex

The Codex Cookbook includes prompting, planning, repair, evaluation, migration, and integration with Agents SDK workflows. ([OpenAI Developers][1])

### Practice

Use Codex on a real but noncritical repository to:

* Create a plan
* Implement one feature
* Add tests
* Run static analysis
* Document assumptions
* Produce a reviewable pull request

---

## Week 24: ChatGPT apps, workspace agents, and gpt-oss

### Chapter 28: ChatGPT integrations

Study:

* Apps SDK concepts
* MCP-backed ChatGPT apps
* Tool definitions
* UI components
* Authentication
* Workspace agents
* Repeatable workflows
* Triggering published agents through APIs
* Enterprise permissions
* Deployment and review

### Chapter 29: gpt-oss and local/open-model workflows

Study:

* Open-weight model fundamentals
* Local inference
* Hardware requirements
* Quantization
* Serving
* Prompt formats
* Tool use
* Reasoning behavior
* Safety models
* Evaluation
* Routing between local and hosted models

Recommended Cookbook areas:

* gpt-oss setup and inference
* gpt-oss safeguard
* Reasoning use cases
* Local/hosted hybrid architectures
* Domain-specific applications

### Practice

Build a hybrid router:

```text
Simple/private/local task
        ↓
    gpt-oss model

Complex/high-accuracy/tool task
        ↓
    Hosted OpenAI model
```

Compare quality, privacy, latency, operational complexity, and total cost.

---

# Capstone project

Build an **Enterprise AI Research and Architecture Assistant**.

This aligns well with your solution-architecture and AI-leadership goals.

## Required capabilities

### 1. Text and reasoning

* Analyze technical questions
* Produce structured architecture recommendations
* Generate JSON and Markdown outputs

### 2. Document intelligence

* Read PDFs and design documents
* Retrieve relevant passages
* Cite source material
* Interpret architecture diagrams

### 3. Tools

* Web search
* File search
* Internal knowledge retrieval
* Calculator or code execution
* Optional Jira, GitHub, or cloud-inventory integration

### 4. Agents

```text
Coordinator
├── Requirements Analyst
├── Research Agent
├── Architecture Agent
├── Security Reviewer
└── Report Generator
```

### 5. Guardrails

* Read-only tools by default
* Source allowlists
* PII redaction
* Prompt-injection checks
* Approval before external actions
* Complete audit trail

### 6. Evals

Evaluate:

* Factual correctness
* Citation correctness
* Requirement coverage
* Architecture quality
* Security-risk detection
* Tool-selection accuracy
* Cost
* Latency
* Agent-loop frequency

### 7. Production characteristics

* Retry handling
* Rate limiting
* Tracing
* Prompt versioning
* Eval dataset versioning
* Model fallback
* Cost dashboard
* Regression testing

---

# Suggested weekly schedule

| Day       | Activity                                 |      Time |
| --------- | ---------------------------------------- | --------: |
| Monday    | Read concepts and official documentation | 60–90 min |
| Tuesday   | Run one Cookbook recipe                  | 60–90 min |
| Wednesday | Reimplement it independently             | 60–90 min |
| Thursday  | Adapt it to your own use case            | 60–90 min |
| Friday    | Add tests, evals, and error handling     | 60–90 min |
| Saturday  | Integrate it into the capstone           |   2–3 hrs |
| Sunday    | Review notes or rest                     |  Optional |

---

# Priority levels

The Cookbook contains many overlapping, specialized, and older recipes. Do not give every notebook equal weight.

## Priority 1 — Must master

* Responses API
* Prompting
* Structured Outputs
* Function calling
* Tool use
* Embeddings
* RAG and File Search
* Vision
* Agents SDK
* Evals
* Guardrails
* Rate limits, cost, and latency

## Priority 2 — Strong AI architect knowledge

* Realtime voice
* Multi-agent orchestration
* MCP
* Deep research
* Computer use
* Prompt caching
* Fine-tuning
* Codex workflows
* ChatGPT apps

## Priority 3 — Specialization

* Image generation
* Video generation
* Reinforcement fine-tuning
* Advanced multimodal evals
* Macro agent evals
* gpt-oss deployment
* Knowledge-graph agents
* Large-scale sandbox-agent systems

## Archive material

Study archived Cookbook recipes only when they explain a still-relevant principle. Archived examples may reference superseded APIs or models, so port the idea to current APIs rather than copying their implementation directly. The Cookbook maintains a separate archive for these recipes. ([OpenAI Developers][8])

---

# Progress milestones

| Milestone | Expected capability                            |
| --------- | ---------------------------------------------- |
| Week 4    | Build reliable structured text applications    |
| Week 7    | Connect models safely to tools                 |
| Week 9    | Build a cited document-RAG system              |
| Week 12   | Build vision and voice applications            |
| Week 16   | Build stateful single- and multi-agent systems |
| Week 19   | Create systematic AI evaluations               |
| Week 20   | Threat-model and guardrail an agent            |
| Week 22   | Optimize and customize model behavior          |
| Week 24   | Design production-grade OpenAI solutions       |

The most important progression is:

```text
API calls
→ reliable structured outputs
→ tools
→ retrieval
→ multimodal
→ agents
→ evals
→ guardrails
→ optimization
→ fine-tuning
→ production architecture
```

This order prevents a common mistake: building autonomous multi-agent systems before learning how to produce, validate, retrieve, measure, and secure a single model response.

[1]: https://developers.openai.com/cookbook/topic/agents "
  Agents • Cookbook
"
[2]: https://developers.openai.com/cookbook/topic/codex "
  Codex • Cookbook
"
[3]: https://developers.openai.com/cookbook/examples/using_embeddings?utm_source=chatgpt.com "Using embeddings"
[4]: https://developers.openai.com/cookbook/topic/multimodal "
  Multimodal • Cookbook
"
[5]: https://developers.openai.com/cookbook/topic/evals "
  Evals • Cookbook
"
[6]: https://developers.openai.com/cookbook/topic/guardrails "
  Guardrails • Cookbook
"
[7]: https://developers.openai.com/cookbook/examples/fine_tuning_direct_preference_optimization_guide?utm_source=chatgpt.com "Fine-Tuning Techniques - Choosing Between SFT, DPO ..."
[8]: https://developers.openai.com/cookbook/archive?utm_source=chatgpt.com "Cookbook Archive"
