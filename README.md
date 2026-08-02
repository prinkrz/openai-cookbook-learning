# OpenAI Cookbook Learning Roadmap with Resources

The roadmap below maps each chapter to a **primary learning resource**, relevant **Cookbook recipes**, and a practical outcome. Because the Cookbook is continuously updated, use its topic pages as the live index and individual recipes as hands-on chapters.

## Phase 1 — API foundations

### Chapter 1: OpenAI API fundamentals

**Topics**

* **OpenAI SDK setup**
  Install the official SDK, configure the project correctly, and confirm the setup with a minimal working API request. [Study: Install the OpenAI SDK and Run an API Call](https://developers.openai.com/api/docs/quickstart#install-the-openai-sdk-and-run-an-api-call)
* **API keys and environment variables**
  Configure credentials without exposing them in code or logs, and understand the rotation and storage practices required in production. [Study: Create and export an API key](https://developers.openai.com/api/docs/quickstart#create-and-export-an-api-key)
* **Responses API**
  Understand the request fields, returned output items, and lifecycle needed to build a reliable Responses API integration. [Study: Migrate to the Responses API](https://developers.openai.com/api/docs/guides/migrate-to-responses)
* **Request and response structure**
  Understand the request fields, returned output items, and lifecycle needed to build a reliable Responses API integration. [Study: Request and response structure reference](https://developers.openai.com/api/reference/resources/responses)
* **Streaming**
  Learn how to consume incremental events, assemble partial output, and handle completion, cancellation, and stream failures. [Study: Streaming guide](https://openai.github.io/openai-agents-python/streaming)
* **Token usage**
  Understand how context and token limits affect quality, latency, and cost, then apply an appropriate budgeting or compaction strategy. [Study: Counting tokens](https://developers.openai.com/api/docs/guides/token-counting)
* **Errors, retries and rate limits**
  Identify likely failure modes, choose safe retry or fallback behavior, and verify that recovery does not duplicate consequential work. [Study: Error mitigation](https://developers.openai.com/api/docs/guides/rate-limits#error-mitigation)

**Practice**

Create a Python command-line assistant that streams its answer, displays token usage and handles timeout, authentication and rate-limit errors.

---

### Chapter 2: Models and model selection

**Topics**

* **Model families**
  Compare the available options by capability, quality, latency, cost, and operational constraints before defining a selection policy. [Study: Model families, capabilities, and model identifiers](https://developers.openai.com/api/docs/models)
* **Reasoning versus non-reasoning models**
  Compare the available options by capability, quality, latency, cost, and operational constraints before defining a selection policy. [Study: Reasoning models](https://developers.openai.com/api/docs/guides/reasoning)
* **Speed, quality and cost**
  Define representative cases, a measurable success criterion, and a repeatable grading method that can detect regressions. [Study: 2. Optimize cost and latency](https://developers.openai.com/api/docs/guides/model-selection#2-optimize-cost-and-latency)
* **Context windows**
  Understand how context and token limits affect quality, latency, and cost, then apply an appropriate budgeting or compaction strategy. [Study: Managing the context window](https://developers.openai.com/api/docs/guides/reasoning#managing-the-context-window)
* **Reasoning effort**
  Define the objective and reasoning budget clearly, then verify that the chosen approach improves results without unnecessary work. [Study: Reasoning effort](https://developers.openai.com/api/docs/guides/reasoning#reasoning-effort)
* **Model fallback**
  Identify likely failure modes, choose safe retry or fallback behavior, and verify that recovery does not duplicate consequential work. [Study: Production best practices](https://developers.openai.com/api/docs/guides/production-best-practices)
* **Task-based model routing**
  Compare the available options by capability, quality, latency, cost, and operational constraints before defining a selection policy. [Study: Models and providers](https://developers.openai.com/api/docs/guides/agents/models)

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

* **Instruction hierarchy**
  Structure instructions and context so the model can identify the objective, constraints, examples, and completion criteria unambiguously. [Study: Prompt engineering](https://developers.openai.com/api/docs/guides/prompt-engineering)
* **Developer and user messages**
  Structure instructions and context so the model can identify the objective, constraints, examples, and completion criteria unambiguously. [Study: Message roles and instruction following](https://developers.openai.com/api/docs/guides/prompt-engineering#message-roles-and-instruction-following)
* **Clear objectives**
  Structure instructions and context so the model can identify the objective, constraints, examples, and completion criteria unambiguously. [Study: Developer messages](https://developers.openai.com/api/docs/guides/prompt-engineering#developer-messages)
* **Context placement**
  Structure instructions and context so the model can identify the objective, constraints, examples, and completion criteria unambiguously. [Study: Few-shot examples and context organization](https://developers.openai.com/cookbook/examples/gpt4-1_prompting_guide)
* **Delimiters**
  Structure instructions and context so the model can identify the objective, constraints, examples, and completion criteria unambiguously. [Study: Separate instructions and context with delimiters](https://developers.openai.com/cookbook/examples/gpt4-1_prompting_guide#delimiters)
* **Few-shot examples**
  Structure instructions and context so the model can identify the objective, constraints, examples, and completion criteria unambiguously. [Study: Few-shot learning](https://developers.openai.com/plugins/build/examples#few-shot-learning)
* **Acceptance criteria**
  Structure instructions and context so the model can identify the objective, constraints, examples, and completion criteria unambiguously. [Study: Evaluate early and often](https://developers.openai.com/api/docs/guides/evaluation-best-practices#evaluate-early-and-often)
* **Long-context prompting**
  Structure instructions and context so the model can identify the objective, constraints, examples, and completion criteria unambiguously. [Study: Organize prompts for long context](https://developers.openai.com/cookbook/examples/gpt4-1_prompting_guide#long-context)
* **Prompt migration**
  Structure instructions and context so the model can identify the objective, constraints, examples, and completion criteria unambiguously. [Study: Prompt migration workflow](https://developers.openai.com/api/docs/guides/prompt-guidance-gpt-5p6#prompt-migration-workflow)
* **Prompt iteration**
  Structure instructions and context so the model can identify the objective, constraints, examples, and completion criteria unambiguously. [Study: Prompt optimizer](https://developers.openai.com/api/docs/guides/prompt-optimizer)

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

* **JSON generation**
  Define a strict machine-readable contract, handle invalid or refused outputs, and validate parsed data before downstream use. [Study: JSON mode](https://developers.openai.com/api/docs/guides/structured-outputs#json-mode)
* **JSON Schema**
  Define a strict machine-readable contract, handle invalid or refused outputs, and validate parsed data before downstream use. [Study: Tips for your JSON Schema](https://developers.openai.com/api/docs/guides/structured-outputs#tips-for-your-json-schema)
* **Pydantic models**
  Define a strict machine-readable contract, handle invalid or refused outputs, and validate parsed data before downstream use. [Study: Structured model outputs](https://developers.openai.com/api/docs/guides/structured-outputs)
* **Required and optional fields**
  Define a strict machine-readable contract, handle invalid or refused outputs, and validate parsed data before downstream use. [Study: All fields must be `required`](https://developers.openai.com/api/docs/guides/structured-outputs#all-fields-must-be-required)
* **Enumerations**
  Define a strict machine-readable contract, handle invalid or refused outputs, and validate parsed data before downstream use. [Study: Pydantic parsing, nested objects, and enumerations](https://developers.openai.com/cookbook/examples/structured_outputs_intro)
* **Nested objects**
  Define a strict machine-readable contract, handle invalid or refused outputs, and validate parsed data before downstream use. [Study: Objects have limitations on nesting depth and size](https://developers.openai.com/api/docs/guides/structured-outputs#objects-have-limitations-on-nesting-depth-and-size)
* **Schema validation**
  Define a strict machine-readable contract, handle invalid or refused outputs, and validate parsed data before downstream use. [Study: Schema validation in multi-agent data flows](https://developers.openai.com/cookbook/examples/structured_outputs_multi_agent)
* **Refusal handling**
  Define a strict machine-readable contract, handle invalid or refused outputs, and validate parsed data before downstream use. [Study: Refusals with structured outputs](https://developers.openai.com/api/docs/guides/structured-outputs#refusals-with-structured-outputs)
* **Schema versioning**
  Define a strict machine-readable contract, handle invalid or refused outputs, and validate parsed data before downstream use. [Study: JSON Schema fundamentals for schema versioning](https://json-schema.org/learn/getting-started-step-by-step)

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

* **Classification**
  Define clear labels and representative examples, then measure confusion between classes on realistic and edge-case inputs. [Study: Classification, sentiment, and intent detection](https://developers.openai.com/cookbook/examples/multiclass_classification_for_transactions)
* **Summarization**
  Preserve the source’s important facts and qualifications while controlling length, structure, and unsupported inference. [Study: Practical guide to summarization](https://developers.openai.com/cookbook/examples/summarizing_long_documents)
* **Translation**
  Preserve meaning, terminology, tone, and locale-specific conventions, then evaluate difficult multilingual examples. [Study: Translation quality and terminology evaluation](https://developers.deepl.com/docs/best-practices/working-with-context)
* **Rewriting**
  Structure instructions and context so the model can identify the objective, constraints, examples, and completion criteria unambiguously. [Study: Message roles and instruction following](https://developers.openai.com/api/docs/guides/text#message-roles-and-instruction-following)
* **Information extraction**
  Identify the required evidence and fields, extract them consistently, and retain enough source context for verification. [Study: Information extraction and question answering](https://developers.openai.com/cookbook/examples/entity_extraction_for_long_documents)
* **Question answering**
  Answer from available evidence, attach citations to supported claims, and return an insufficient-evidence result when grounding is weak. [Study: Grounded question answering with embeddings](https://developers.openai.com/cookbook/examples/question_answering_using_embeddings)
* **Intent detection**
  Define clear labels and representative examples, then measure confusion between classes on realistic and edge-case inputs. [Study: Zero shot classification](https://developers.openai.com/cookbook/examples/multiclass_classification_for_transactions#zero-shot-classification)
* **Sentiment analysis**
  Define clear labels and representative examples, then measure confusion between classes on realistic and edge-case inputs. [Study: Sentiment analysis](https://developers.openai.com/api/docs/tutorials/meeting-minutes#sentiment-analysis)
* **Code generation**
  Use repository context and tests to produce focused, reviewable changes, then verify behavior before accepting the implementation. [Study: Code generation](https://developers.openai.com/api/docs/guides/code-generation)
* **Document comparison**
  Identify the required evidence and fields, extract them consistently, and retain enough source context for verification. [Study: Few shot learning](https://developers.openai.com/api/docs/guides/prompt-engineering#few-shot-learning)

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

* **Function definitions**
  Define the capability and its input contract, validate every invocation, and enforce permissions or approval before execution. [Study: Function calling](https://developers.openai.com/api/docs/guides/function-calling)
* **Tool schemas**
  Define a strict machine-readable contract, handle invalid or refused outputs, and validate parsed data before downstream use. [Study: The tool calling flow](https://developers.openai.com/api/docs/guides/function-calling#the-tool-calling-flow)
* **Tool selection**
  Define the capability and its input contract, validate every invocation, and enforce permissions or approval before execution. [Study: Tool choice](https://developers.openai.com/api/docs/guides/function-calling#tool-choice)
* **Tool-call arguments**
  Define the capability and its input contract, validate every invocation, and enforce permissions or approval before execution. [Study: Using tools](https://developers.openai.com/api/docs/guides/tools)
* **Multiple tool calls**
  Define the capability and its input contract, validate every invocation, and enforce permissions or approval before execution. [Study: Multiple and parallel function calls](https://developers.openai.com/cookbook/examples/how_to_call_functions_with_chat_models)
* **Parallel tool calls**
  Define the capability and its input contract, validate every invocation, and enforce permissions or approval before execution. [Study: Parallel function calling](https://developers.openai.com/api/docs/guides/function-calling#parallel-function-calling)
* **Tool result submission**
  Define the capability and its input contract, validate every invocation, and enforce permissions or approval before execution. [Study: Handling function calls](https://developers.openai.com/api/docs/guides/function-calling#handling-function-calls)
* **Input validation**
  Validate types, ranges, formats, and authorization before execution, and return actionable errors without trusting model-generated arguments. [Study: Input validation and safe tool execution](https://owasp.org/www-project-top-10-for-large-language-model-applications)
* **Idempotency**
  Define the capability and its input contract, validate every invocation, and enforce permissions or approval before execution. [Study: Idempotency for retry-safe application actions](https://stripe.com/docs/idempotency)
* **Error handling**
  Identify likely failure modes, choose safe retry or fallback behavior, and verify that recovery does not duplicate consequential work. [Study: Handle function-calling errors](https://developers.openai.com/api/docs/guides/function-calling#handling-errors)
* **Human approval**
  Define the capability and its input contract, validate every invocation, and enforce permissions or approval before execution. [Study: Human approval](https://developers.openai.com/api/docs/guides/node-reference#human-approval)

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

* **Responses API**
  Understand the request fields, returned output items, and lifecycle needed to build a reliable Responses API integration. [Study: Responses API](https://developers.openai.com/api/docs/guides/tools-web-search#responses-api)
* **Conversation state**
  Choose where state lives, what must persist between turns, and how to prevent stale, duplicated, or sensitive context. [Study: Conversation state](https://developers.openai.com/api/docs/guides/conversation-state)
* **Previous response IDs**
  Choose where state lives, what must persist between turns, and how to prevent stale, duplicated, or sensitive context. [Study: Openai managed conversation state](https://developers.openai.com/api/docs/guides/conversation-state#openai-managed-conversation-state)
* **Web search**
  Configure the capability, understand the returned evidence or artifacts, and validate outputs before incorporating them into the final answer. [Study: Web search](https://developers.openai.com/api/docs/guides/tools-web-search)
* **File search**
  Configure the capability, understand the returned evidence or artifacts, and validate outputs before incorporating them into the final answer. [Study: File search](https://developers.openai.com/api/docs/guides/tools-file-search)
* **Code execution**
  Configure the capability, understand the returned evidence or artifacts, and validate outputs before incorporating them into the final answer. [Study: Code Interpreter](https://developers.openai.com/api/docs/guides/tools-code-interpreter)
* **Tool citations**
  Answer from available evidence, attach citations to supported claims, and return an insufficient-evidence result when grounding is weak. [Study: Format citations for retrieved tool context](https://developers.openai.com/api/docs/guides/citation-formatting#format-citations-for-retrieved-tool-context)
* **Multi-turn workflows**
  Choose where state lives, what must persist between turns, and how to prevent stale, duplicated, or sensitive context. [Study: Multi-turn workflows](https://developers.openai.com/api/docs/guides/tools-shell#multi-turn-workflows)
* **Background processing**
  Bound long-running work with saved progress, explicit limits, cancellation support, and a reliable resume or termination path. [Study: Polling background responses](https://developers.openai.com/api/docs/guides/background#polling-background-responses)
* **Tool permissions**
  Define the capability and its input contract, validate every invocation, and enforce permissions or approval before execution. [Study: Model, tool, and data controls with Terraform](https://developers.openai.com/api/docs/guides/terraform/project-controls)

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

* **Embedding vectors**
  Understand the vector operation behind this pattern, choose an appropriate similarity or indexing method, and evaluate retrieval quality. [Study: Vector embeddings](https://developers.openai.com/api/docs/guides/embeddings)
* **Semantic similarity**
  Understand the vector operation behind this pattern, choose an appropriate similarity or indexing method, and evaluate retrieval quality. [Study: Semantic similarity metrics](https://www.sbert.net/docs/sentence_transformer/usage/semantic_textual_similarity.html)
* **Cosine similarity**
  Understand the vector operation behind this pattern, choose an appropriate similarity or indexing method, and evaluate retrieval quality. [Study: Cosine similarity and nearest-neighbor search](https://developers.openai.com/cookbook/examples/semantic_text_search_using_embeddings)
* **Semantic search**
  Understand the vector operation behind this pattern, choose an appropriate similarity or indexing method, and evaluate retrieval quality. [Study: Semantic search](https://developers.openai.com/api/docs/guides/retrieval#semantic-search)
* **Classification**
  Define clear labels and representative examples, then measure confusion between classes on realistic and edge-case inputs. [Study: Classification with embeddings](https://developers.openai.com/cookbook/examples/classification_using_embeddings)
* **Clustering**
  Understand the vector operation behind this pattern, choose an appropriate similarity or indexing method, and evaluate retrieval quality. [Study: Clustering and visualization](https://developers.openai.com/cookbook/examples/clustering)
* **Recommendations**
  Understand the vector operation behind this pattern, choose an appropriate similarity or indexing method, and evaluate retrieval quality. [Study: Practical guide to recommendations](https://developers.openai.com/cookbook/examples/recommendation_using_embeddings)
* **Deduplication**
  Understand the vector operation behind this pattern, choose an appropriate similarity or indexing method, and evaluate retrieval quality. [Study: Use cases](https://developers.openai.com/api/docs/guides/embeddings#use-cases)
* **Batch embedding**
  Understand the vector operation behind this pattern, choose an appropriate similarity or indexing method, and evaluate retrieval quality. [Study: Embedding models](https://developers.openai.com/api/docs/guides/embeddings#embedding-models)
* **Vector databases**
  Understand the vector operation behind this pattern, choose an appropriate similarity or indexing method, and evaluate retrieval quality. [Study: Middleware for vector databases](https://developers.openai.com/api/docs/actions/data-retrieval#middleware-for-vector-databases)

**Practice**

Create a semantic search engine for architecture documents and compare it with keyword search.

---

### Chapter 9: Retrieval-augmented generation

**Topics**

* **Document ingestion**
  Design this retrieval stage deliberately, preserve useful metadata, and measure its effect on evidence recall and answer quality. [Study: Document ingestion guide](https://developers.openai.com/api/docs/guides/retrieval)
* **Chunking**
  Design this retrieval stage deliberately, preserve useful metadata, and measure its effect on evidence recall and answer quality. [Study: Chunking](https://developers.openai.com/api/docs/guides/retrieval#chunking)
* **Chunk overlap**
  Design this retrieval stage deliberately, preserve useful metadata, and measure its effect on evidence recall and answer quality. [Study: Chunking, overlap, metadata, and retrieval tuning](https://www.pinecone.io/learn/chunking-strategies)
* **Metadata**
  Design this retrieval stage deliberately, preserve useful metadata, and measure its effect on evidence recall and answer quality. [Study: Optimize Metadata](https://developers.openai.com/plugins/guides/optimize-metadata)
* **Vector stores**
  Design this retrieval stage deliberately, preserve useful metadata, and measure its effect on evidence recall and answer quality. [Study: Vector stores](https://developers.openai.com/api/docs/guides/retrieval#vector-stores)
* **Semantic retrieval**
  Design this retrieval stage deliberately, preserve useful metadata, and measure its effect on evidence recall and answer quality. [Study: Performing semantic search](https://developers.openai.com/api/docs/guides/retrieval#performing-semantic-search)
* **Hybrid retrieval**
  Design this retrieval stage deliberately, preserve useful metadata, and measure its effect on evidence recall and answer quality. [Study: Practical guide to hybrid retrieval](https://www.elastic.co/what-is/hybrid-search)
* **Query rewriting**
  Structure instructions and context so the model can identify the objective, constraints, examples, and completion criteria unambiguously. [Study: Query rewriting](https://developers.openai.com/api/docs/guides/retrieval#query-rewriting)
* **Reranking**
  Design this retrieval stage deliberately, preserve useful metadata, and measure its effect on evidence recall and answer quality. [Study: Reranking retrieved candidates](https://www.sbert.net/examples/sparse_encoder/applications/retrieve_rerank/README.html)
* **Context assembly**
  Design this retrieval stage deliberately, preserve useful metadata, and measure its effect on evidence recall and answer quality. [Study: Include search results in the response](https://developers.openai.com/api/docs/guides/tools-file-search#include-search-results-in-the-response)
* **Grounded answers**
  Answer from available evidence, attach citations to supported claims, and return an insufficient-evidence result when grounding is weak. [Study: Grounding, citations, and retrieval budgets](https://developers.openai.com/api/docs/guides/prompt-guidance-gpt-5p6#grounding-citations-and-retrieval-budgets)
* **Citations**
  Answer from available evidence, attach citations to supported claims, and return an insufficient-evidence result when grounding is weak. [Study: Citations](https://developers.openai.com/api/docs/guides/citation-formatting#citations)
* **Retrieval evaluation**
  Design this retrieval stage deliberately, preserve useful metadata, and measure its effect on evidence recall and answer quality. [Study: Practical guide to retrieval evaluation](https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/context_precision)

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

* **Image input**
  Prepare the visual input correctly, state the analysis task precisely, and verify extracted details against the source image or document. [Study: Images and vision](https://developers.openai.com/api/docs/guides/images-vision)
* **Multiple images**
  Prepare the visual input correctly, state the analysis task precisely, and verify extracted details against the source image or document. [Study: Analyze multiple images](https://developers.openai.com/api/docs/guides/images-vision#analyze-multiple-images)
* **Image resolution**
  Prepare the visual input correctly, state the analysis task precisely, and verify extracted details against the source image or document. [Study: Specify image input detail level](https://developers.openai.com/api/docs/guides/images-vision#specify-image-input-detail-level)
* **OCR**
  Prepare the visual input correctly, state the analysis task precisely, and verify extracted details against the source image or document. [Study: OCR fundamentals and preprocessing](https://tesseract-ocr.github.io/tessdoc/ImproveQuality.html)
* **Chart analysis**
  Prepare the visual input correctly, state the analysis task precisely, and verify extracted details against the source image or document. [Study: Non-PDF image and chart limitations](https://developers.openai.com/api/docs/guides/file-inputs#non-pdf-image-and-chart-limitations)
* **Screenshot understanding**
  Prepare the visual input correctly, state the analysis task precisely, and verify extracted details against the source image or document. [Study: Image understanding combined with retrieval](https://developers.openai.com/cookbook/examples/multimodal/image_understanding_with_rag)
* **Diagram interpretation**
  Prepare the visual input correctly, state the analysis task precisely, and verify extracted details against the source image or document. [Study: Practical guide to diagram interpretation](https://developers.openai.com/cookbook/examples/multimodal/document_and_multimodal_understanding_tips)
* **PDF-page analysis**
  Prepare the visual input correctly, state the analysis task precisely, and verify extracted details against the source image or document. [Study: PDF detail levels](https://developers.openai.com/api/docs/guides/file-inputs#pdf-detail-levels)
* **Visual question answering**
  Answer from available evidence, attach citations to supported claims, and return an insufficient-evidence result when grounding is weak. [Study: Analyze images](https://developers.openai.com/api/docs/guides/images-vision#analyze-images)
* **Structured visual extraction**
  Prepare the visual input correctly, state the analysis task precisely, and verify extracted details against the source image or document. [Study: Practical guide to structured visual extraction](https://developers.openai.com/cookbook/examples/multimodal/using_gpt4_vision_with_function_calling)

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

* **Text-to-image generation**
  Prepare the visual input correctly, state the analysis task precisely, and verify extracted details against the source image or document. [Study: Image generation](https://developers.openai.com/api/docs/guides/image-generation)
* **Image prompting**
  Structure instructions and context so the model can identify the objective, constraints, examples, and completion criteria unambiguously. [Study: Image generation](https://developers.openai.com/api/docs/guides/tools-image-generation)
* **Composition**
  Prepare the visual input correctly, state the analysis task precisely, and verify extracted details against the source image or document. [Study: Composition, constraints, and text rendering with GPT Image](https://developers.openai.com/api/docs/models/gpt-image-2)
* **Aspect ratio**
  Prepare the visual input correctly, state the analysis task precisely, and verify extracted details against the source image or document. [Study: Size and quality options](https://developers.openai.com/api/docs/guides/image-generation#size-and-quality-options)
* **Text rendering**
  Prepare the visual input correctly, state the analysis task precisely, and verify extracted details against the source image or document. [Study: Limitations](https://developers.openai.com/api/docs/guides/image-generation#limitations)
* **Visual consistency**
  Prepare the visual input correctly, state the analysis task precisely, and verify extracted details against the source image or document. [Study: Multi turn image generation](https://developers.openai.com/api/docs/guides/image-generation#multi-turn-image-generation)
* **Image editing**
  Prepare the visual input correctly, state the analysis task precisely, and verify extracted details against the source image or document. [Study: Image API](https://developers.openai.com/api/docs/guides/image-generation#image-api)
* **Masking**
  Prepare the visual input correctly, state the analysis task precisely, and verify extracted details against the source image or document. [Study: Edit images](https://developers.openai.com/api/docs/guides/image-generation#edit-images)
* **Input fidelity**
  Prepare the visual input correctly, state the analysis task precisely, and verify extracted details against the source image or document. [Study: Input fidelity](https://developers.openai.com/api/docs/guides/image-generation#input-fidelity)
* **Iterative refinement**
  Prepare the visual input correctly, state the analysis task precisely, and verify extracted details against the source image or document. [Study: Practical guide to iterative refinement](https://developers.openai.com/cookbook/examples/generate_images_with_gpt_image)
* **Image evaluation**
  Prepare the visual input correctly, state the analysis task precisely, and verify extracted details against the source image or document. [Study: Image generation evals](https://developers.openai.com/api/docs/guides/image-generation#image-generation-evals)

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

* **Speech-to-text**
  Choose the appropriate audio format and processing mode, handle real-world recording conditions, and evaluate transcript or speech quality. [Study: Audio and speech](https://developers.openai.com/api/docs/guides/audio)
* **Audio transcription**
  Choose the appropriate audio format and processing mode, handle real-world recording conditions, and evaluate transcript or speech quality. [Study: Audio Transcriptions — Create](https://developers.openai.com/api/reference/resources/audio/subresources/transcriptions/methods/create)
* **Text-to-speech**
  Choose the appropriate audio format and processing mode, handle real-world recording conditions, and evaluate transcript or speech quality. [Study: Text to speech](https://developers.openai.com/api/docs/guides/text-to-speech)
* **Audio input**
  Choose the appropriate audio format and processing mode, handle real-world recording conditions, and evaluate transcript or speech quality. [Study: Audio inputs and outputs](https://developers.openai.com/api/docs/guides/realtime-conversations#audio-inputs-and-outputs)
* **Audio output**
  Choose the appropriate audio format and processing mode, handle real-world recording conditions, and evaluate transcript or speech quality. [Study: Supported output formats](https://developers.openai.com/api/docs/guides/text-to-speech#supported-output-formats)
* **Streaming**
  Learn how to consume incremental events, assemble partial output, and handle completion, cancellation, and stream failures. [Study: Streaming transcriptions](https://developers.openai.com/api/docs/guides/speech-to-text#streaming-transcriptions)
* **Noise handling**
  Choose the appropriate audio format and processing mode, handle real-world recording conditions, and evaluate transcript or speech quality. [Study: Handling silence and background noise](https://developers.openai.com/api/docs/guides/realtime-transcription#handling-silence-and-background-noise)
* **Speaker considerations**
  Choose the appropriate audio format and processing mode, handle real-world recording conditions, and evaluate transcript or speech quality. [Study: Speaker diarization](https://developers.openai.com/api/docs/guides/speech-to-text#speaker-diarization)
* **Transcription evaluation**
  Choose the appropriate audio format and processing mode, handle real-world recording conditions, and evaluate transcript or speech quality. [Study: Evaluate transcription quality](https://developers.openai.com/api/docs/guides/transcription#evaluate-transcription-quality)

**Practice**

Create a meeting assistant that transcribes audio, extracts decisions and produces structured action items.

---

### Chapter 13: Realtime API and voice agents

**Topics**

* **Realtime sessions**
  Understand the event and transport lifecycle, manage turns and interruptions, and measure latency under realistic conversation conditions. [Study: Realtime sessions](https://developers.openai.com/api/docs/guides/realtime#realtime-sessions)
* **WebRTC**
  Understand the event and transport lifecycle, manage turns and interruptions, and measure latency under realistic conversation conditions. [Study: Realtime API with WebRTC](https://developers.openai.com/api/docs/guides/realtime-webrtc)
* **WebSocket**
  Understand the event and transport lifecycle, manage turns and interruptions, and measure latency under realistic conversation conditions. [Study: Realtime API with WebSocket](https://developers.openai.com/api/docs/guides/realtime-websocket)
* **Audio buffers**
  Choose the appropriate audio format and processing mode, handle real-world recording conditions, and evaluate transcript or speech quality. [Study: Realtime conversations](https://developers.openai.com/api/docs/guides/realtime-conversations)
* **Voice activity detection**
  Understand the event and transport lifecycle, manage turns and interruptions, and measure latency under realistic conversation conditions. [Study: Voice activity detection (VAD)](https://developers.openai.com/api/docs/guides/realtime-vad)
* **Turn detection**
  Understand the event and transport lifecycle, manage turns and interruptions, and measure latency under realistic conversation conditions. [Study: Turn detection](https://developers.openai.com/api/docs/guides/realtime-vad#turn-detection)
* **Interruptions**
  Understand the event and transport lifecycle, manage turns and interruptions, and measure latency under realistic conversation conditions. [Study: Realtime guide](https://openai.github.io/openai-agents-python/realtime/guide)
* **Realtime tools**
  Define the capability and its input contract, validate every invocation, and enforce permissions or approval before execution. [Study: Realtime with tools](https://developers.openai.com/api/docs/guides/realtime-mcp)
* **Context management**
  Choose where state lives, what must persist between turns, and how to prevent stale, duplicated, or sensitive context. [Study: Managing conversations](https://developers.openai.com/api/docs/guides/realtime-conversations#managing-conversations)
* **Voice-agent latency**
  Measure the baseline, apply the relevant optimization, and compare cost, throughput, tail latency, and task success afterward. [Study: Seven principles](https://developers.openai.com/api/docs/guides/latency-optimization#seven-principles)
* **Voice-agent evaluation**
  Define representative cases, a measurable success criterion, and a repeatable grading method that can detect regressions. [Study: Realtime voice-agent evaluation](https://developers.openai.com/cookbook/examples/realtime_eval_guide)

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

* **Storyboarding**
  Translate the intended scene into precise visual and motion instructions, then evaluate continuity, composition, and generated artifacts. [Study: Storyboards, shot lists, and camera terminology](https://www.studiobinder.com/blog/types-of-camera-shots-sizes-in-film)
* **Scene prompts**
  Structure instructions and context so the model can identify the objective, constraints, examples, and completion criteria unambiguously. [Study: Video generation with Sora](https://developers.openai.com/api/docs/guides/video-generation)
* **Camera directions**
  Translate the intended scene into precise visual and motion instructions, then evaluate continuity, composition, and generated artifacts. [Study: Effective prompting](https://developers.openai.com/api/docs/guides/video-generation#effective-prompting)
* **Motion description**
  Translate the intended scene into precise visual and motion instructions, then evaluate continuity, composition, and generated artifacts. [Study: Generate a video](https://developers.openai.com/api/docs/guides/video-generation#generate-a-video)
* **Temporal consistency**
  Translate the intended scene into precise visual and motion instructions, then evaluate continuity, composition, and generated artifacts. [Study: Use characters for consistency](https://developers.openai.com/api/docs/guides/video-generation#use-characters-for-consistency)
* **Reference assets**
  Translate the intended scene into precise visual and motion instructions, then evaluate continuity, composition, and generated artifacts. [Study: Reference assets reference](https://developers.openai.com/api/reference/resources/videos)
* **Generation lifecycle**
  Translate the intended scene into precise visual and motion instructions, then evaluate continuity, composition, and generated artifacts. [Study: Sora model capabilities and generation constraints](https://developers.openai.com/api/docs/models/sora-2)
* **Video evaluation**
  Translate the intended scene into precise visual and motion instructions, then evaluate continuity, composition, and generated artifacts. [Study: Perceptual video-quality evaluation](https://github.com/Netflix/vmaf)

**Practice**

Generate a short technical product explainer from a storyboard and evaluate visual consistency between scenes.

---

## Phase 5 — Agent engineering

### Chapter 15: Agent fundamentals

**Topics**

* **Agent versus workflow**
  Define ownership, control flow, context boundaries, and stopping behavior so the agent workflow remains bounded and inspectable. [Study: Workflow boundaries matter](https://developers.openai.com/api/docs/guides/agents/guardrails-approvals#workflow-boundaries-matter)
* **Instructions**
  Structure instructions and context so the model can identify the objective, constraints, examples, and completion criteria unambiguously. [Study: Shape instructions, handoffs, and outputs](https://developers.openai.com/api/docs/guides/agents/define-agents#shape-instructions-handoffs-and-outputs)
* **Tools**
  Define the capability and its input contract, validate every invocation, and enforce permissions or approval before execution. [Study: Tools guide](https://openai.github.io/openai-agents-python/tools)
* **State**
  Choose where state lives, what must persist between turns, and how to prevent stale, duplicated, or sensitive context. [Study: Results and state](https://developers.openai.com/api/docs/guides/agents/results)
* **Memory**
  Choose where state lives, what must persist between turns, and how to prevent stale, duplicated, or sensitive context. [Study: Persist memory across runs](https://developers.openai.com/api/docs/guides/agents/sandboxes#persist-memory-across-runs)
* **Planning**
  Define the objective and reasoning budget clearly, then verify that the chosen approach improves results without unnecessary work. [Study: Planning for the context window](https://developers.openai.com/plugins/build/examples#planning-for-the-context-window)
* **Execution loops**
  Define ownership, control flow, context boundaries, and stopping behavior so the agent workflow remains bounded and inspectable. [Study: Agents SDK](https://developers.openai.com/api/docs/guides/agents)
* **Stop conditions**
  Define ownership, control flow, context boundaries, and stopping behavior so the agent workflow remains bounded and inspectable. [Study: Exceptions](https://openai.github.io/openai-agents-python/running_agents/#exceptions)
* **Human approval**
  Define the capability and its input contract, validate every invocation, and enforce permissions or approval before execution. [Study: Human approval before consequential tool calls](https://openai.github.io/openai-agents-python/human_in_the_loop)
* **Tracing**
  Capture the relevant execution events and sensitive-data controls so behavior can be debugged, evaluated, and audited later. [Study: Tracing](https://openai.github.io/openai-agents-python/tracing)
* **Handoffs**
  Define ownership, control flow, context boundaries, and stopping behavior so the agent workflow remains bounded and inspectable. [Study: Handoffs](https://openai.github.io/openai-agents-python/handoffs)

**Practice**

Convert an existing deterministic workflow into a bounded agent and compare both approaches.

OpenAI’s guidance distinguishes a Responses API application—where one model call plus tools and application logic may be sufficient—from systems that need SDK-managed orchestration.

---

### Chapter 16: Agents SDK fundamentals

**Topics**

* **Agent definitions**
  Define ownership, control flow, context boundaries, and stopping behavior so the agent workflow remains bounded and inspectable. [Study: Agent definitions](https://developers.openai.com/api/docs/guides/agents/define-agents)
* **Agent instructions**
  Structure instructions and context so the model can identify the objective, constraints, examples, and completion criteria unambiguously. [Study: Agent instructions guide](https://openai.github.io/openai-agents-python/agents)
* **Agent runner**
  Define ownership, control flow, context boundaries, and stopping behavior so the agent workflow remains bounded and inspectable. [Study: Running agents](https://developers.openai.com/api/docs/guides/agents/running-agents)
* **Results**
  Define ownership, control flow, context boundaries, and stopping behavior so the agent workflow remains bounded and inspectable. [Study: Results guide](https://openai.github.io/openai-agents-python/results)
* **Output types**
  Define a strict machine-readable contract, handle invalid or refused outputs, and validate parsed data before downstream use. [Study: Output types](https://openai.github.io/openai-agents-python/agents/#output-types)
* **Sessions**
  Choose where state lives, what must persist between turns, and how to prevent stale, duplicated, or sensitive context. [Study: Sessions guide](https://openai.github.io/openai-agents-python/sessions)
* **Tools**
  Define the capability and its input contract, validate every invocation, and enforce permissions or approval before execution. [Study: Common Tools](https://openai.github.io/openai-agents-python/tools#common-tools)
* **Model configuration**
  Configure the model and provider settings explicitly, understand which options apply per run, and verify compatibility with required capabilities. [Study: Model configuration guide](https://openai.github.io/openai-agents-python/config)
* **Error handling**
  Identify likely failure modes, choose safe retry or fallback behavior, and verify that recovery does not duplicate consequential work. [Study: Handling errors in function tools](https://openai.github.io/openai-agents-python/tools/#handling-errors-in-function-tools)
* **Tracing**
  Capture the relevant execution events and sensitive-data controls so behavior can be debugged, evaluated, and audited later. [Study: Tracing](https://developers.openai.com/api/docs/guides/agents/integrations-observability#tracing)

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

* **Manager pattern**
  Define ownership, control flow, context boundaries, and stopping behavior so the agent workflow remains bounded and inspectable. [Study: Orchestration and handoffs](https://developers.openai.com/api/docs/guides/agents/orchestration)
* **Specialist agents**
  Define ownership, control flow, context boundaries, and stopping behavior so the agent workflow remains bounded and inspectable. [Study: Add specialists only when the contract changes](https://developers.openai.com/api/docs/guides/agents/orchestration#add-specialists-only-when-the-contract-changes)
* **Handoffs**
  Define ownership, control flow, context boundaries, and stopping behavior so the agent workflow remains bounded and inspectable. [Study: Use handoffs for delegated ownership](https://developers.openai.com/api/docs/guides/agents/orchestration#use-handoffs-for-delegated-ownership)
* **Agent-as-tool**
  Define the capability and its input contract, validate every invocation, and enforce permissions or approval before execution. [Study: Use agents as tools for manager-style workflows](https://developers.openai.com/api/docs/guides/agents/orchestration#use-agents-as-tools-for-manager-style-workflows)
* **Sequential execution**
  Define ownership, control flow, context boundaries, and stopping behavior so the agent workflow remains bounded and inspectable. [Study: Deterministic flows](https://openai.github.io/openai-agents-python/examples/#deterministic-flows)
* **Parallel execution**
  Define ownership, control flow, context boundaries, and stopping behavior so the agent workflow remains bounded and inspectable. [Study: Parallelization](https://openai.github.io/openai-agents-python/examples/#parallelization)
* **Routing**
  Define ownership, control flow, context boundaries, and stopping behavior so the agent workflow remains bounded and inspectable. [Study: Example Gallery](https://openai.github.io/openai-agents-python/examples)
* **Context isolation**
  Define ownership, control flow, context boundaries, and stopping behavior so the agent workflow remains bounded and inspectable. [Study: Context strategies](https://openai.github.io/openai-agents-python/context)
* **Shared state**
  Choose where state lives, what must persist between turns, and how to prevent stale, duplicated, or sensitive context. [Study: Local context](https://openai.github.io/openai-agents-python/context/#local-context)
* **Result synthesis**
  Define ownership, control flow, context boundaries, and stopping behavior so the agent workflow remains bounded and inspectable. [Study: Final output](https://openai.github.io/openai-agents-python/results/#final-output)

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

* **Session state**
  Choose where state lives, what must persist between turns, and how to prevent stale, duplicated, or sensitive context. [Study: Serializable run state for pause, resume, and recovery](https://openai.github.io/openai-agents-python/ref/run_state)
* **Short-term memory**
  Choose where state lives, what must persist between turns, and how to prevent stale, duplicated, or sensitive context. [Study: Core session behavior](https://openai.github.io/openai-agents-python/sessions/#core-session-behavior)
* **Persistent memory**
  Choose where state lives, what must persist between turns, and how to prevent stale, duplicated, or sensitive context. [Study: Memory persistence](https://openai.github.io/openai-agents-python/sessions/#memory-persistence)
* **Context compaction**
  Understand how context and token limits affect quality, latency, and cost, then apply an appropriate budgeting or compaction strategy. [Study: Context compaction guide](https://developers.openai.com/api/docs/guides/compaction)
* **Summarization**
  Preserve the source’s important facts and qualifications while controlling length, structure, and unsupported inference. [Study: Client side compaction](https://developers.openai.com/api/docs/guides/compaction#client-side-compaction)
* **Checkpoints**
  Bound long-running work with saved progress, explicit limits, cancellation support, and a reliable resume or termination path. [Study: Use checkpoints if needed](https://developers.openai.com/api/docs/guides/supervised-fine-tuning#use-checkpoints-if-needed)
* **Resumability**
  Bound long-running work with saved progress, explicit limits, cancellation support, and a reliable resume or termination path. [Study: Long running approvals](https://openai.github.io/openai-agents-python/human_in_the_loop/#long-running-approvals)
* **Execution budgets**
  Bound long-running work with saved progress, explicit limits, cancellation support, and a reliable resume or termination path. [Study: Usage and pricing](https://openai.github.io/openai-agents-python/usage)
* **Maximum iterations**
  Bound long-running work with saved progress, explicit limits, cancellation support, and a reliable resume or termination path. [Study: Max turns](https://openai.github.io/openai-agents-python/running_agents/#max-turns)
* **Loop detection**
  Bound long-running work with saved progress, explicit limits, cancellation support, and a reliable resume or termination path. [Study: Tool use behavior](https://openai.github.io/openai-agents-python/tools/#tool-use-behavior)
* **Cancellation**
  Bound long-running work with saved progress, explicit limits, cancellation support, and a reliable resume or termination path. [Study: Streaming lifecycle and diagnostics](https://openai.github.io/openai-agents-python/results/#streaming-lifecycle-and-diagnostics)
* **Recovery**
  Identify likely failure modes, choose safe retry or fallback behavior, and verify that recovery does not duplicate consequential work. [Study: Errors and recovery](https://openai.github.io/openai-agents-python/running_agents/#errors-and-recovery)

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

* **MCP clients and servers**
  Define the capability and its input contract, validate every invocation, and enforce permissions or approval before execution. [Study: MCP architecture: hosts, clients, and servers](https://modelcontextprotocol.io/docs/learn/architecture)
* **MCP tools**
  Define the capability and its input contract, validate every invocation, and enforce permissions or approval before execution. [Study: MCP tools and discovery](https://modelcontextprotocol.io/specification/2025-06-18/server/tools)
* **MCP resources**
  Define the capability and its input contract, validate every invocation, and enforce permissions or approval before execution. [Study: MCP resources and subscriptions](https://modelcontextprotocol.io/specification/2025-06-18/server/resources)
* **Tool discovery**
  Define the capability and its input contract, validate every invocation, and enforce permissions or approval before execution. [Study: Model Context Protocol](https://openai.github.io/openai-agents-python/mcp)
* **Authentication**
  Choose the appropriate authentication flow, scope access narrowly, and handle authorization failures without exposing credentials. [Study: Authentication](https://developers.openai.com/api/docs/guides/tools-connectors-mcp#authentication)
* **Local versus remote MCP**
  Define the capability and its input contract, validate every invocation, and enforce permissions or approval before execution. [Study: MCP and Connectors](https://developers.openai.com/api/docs/guides/tools-connectors-mcp)
* **Approval controls**
  Define the capability and its input contract, validate every invocation, and enforce permissions or approval before execution. [Study: Approvals](https://developers.openai.com/api/docs/guides/tools-connectors-mcp#approvals)
* **Trust boundaries**
  Identify the threat and trust boundary, apply least-privilege controls, and test that unsafe inputs or actions are blocked safely. [Study: Logging boundaries](https://developers.openai.com/api/docs/guides/secure-mcp-tunnels#logging-boundaries)
* **Auditing**
  Capture the relevant execution events and sensitive-data controls so behavior can be debugged, evaluated, and audited later. [Study: Compliance API and audit events](https://developers.openai.com/codex/enterprise/compliance-api)

**Practice**

Expose a read-only internal architecture repository through an MCP server and connect it to your research agent.

---

### Chapter 20: Computer use and sandbox agents

**Topics**

* **Computer interaction loops**
  Define the execution boundary, verify each observed action or result, and require approval for external or destructive operations. [Study: Option 1: Run the built-in Computer use loop](https://developers.openai.com/api/docs/guides/tools-computer-use#option-1-run-the-built-in-computer-use-loop)
* **Screenshots**
  Prepare the visual input correctly, state the analysis task precisely, and verify extracted details against the source image or document. [Study: Computer use](https://developers.openai.com/api/docs/guides/tools-computer-use)
* **Browser actions**
  Define the execution boundary, verify each observed action or result, and require approval for external or destructive operations. [Study: 3. Run every returned action](https://developers.openai.com/api/docs/guides/tools-computer-use#3-run-every-returned-action)
* **Action verification**
  Define the execution boundary, verify each observed action or result, and require approval for external or destructive operations. [Study: Acknowledge safety checks](https://developers.openai.com/api/docs/guides/tools-computer-use#4-acknowledge-safety-checks)
* **Sandboxed code execution**
  Configure the capability, understand the returned evidence or artifacts, and validate outputs before incorporating them into the final answer. [Study: Sandbox Agents](https://developers.openai.com/api/docs/guides/agents/sandboxes)
* **Filesystem boundaries**
  Define the execution boundary, verify each observed action or result, and require approval for external or destructive operations. [Study: Filesystem access](https://developers.openai.com/codex/sandboxing#filesystem-access)
* **Network restrictions**
  Define the execution boundary, verify each observed action or result, and require approval for external or destructive operations. [Study: Network access](https://developers.openai.com/api/docs/guides/tools-shell#network-access)
* **Credential protection**
  Configure credentials without exposing them in code or logs, and understand the rotation and storage practices required in production. [Study: Credential and secret protection](https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html)
* **Human approval**
  Define the capability and its input contract, validate every invocation, and enforce permissions or approval before execution. [Study: Human in the loop](https://developers.openai.com/api/docs/guides/tools-computer-use#human-in-the-loop)
* **Coding agents**
  Use repository context and tests to produce focused, reviewable changes, then verify behavior before accepting the implementation. [Study: Building an AI-Native Engineering Team](https://developers.openai.com/codex/guides/build-ai-native-engineering-team)

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

* **Eval datasets**
  Define representative cases, a measurable success criterion, and a repeatable grading method that can detect regressions. [Study: Working with evals](https://developers.openai.com/api/docs/guides/evals)
* **Representative cases**
  Define representative cases, a measurable success criterion, and a repeatable grading method that can detect regressions. [Study: Handle edge cases](https://developers.openai.com/api/docs/guides/evaluation-best-practices#handle-edge-cases)
* **Edge cases**
  Define representative cases, a measurable success criterion, and a repeatable grading method that can detect regressions. [Study: Evaluation best practices](https://developers.openai.com/api/docs/guides/evaluation-best-practices)
* **Adversarial cases**
  Define representative cases, a measurable success criterion, and a repeatable grading method that can detect regressions. [Study: Red teaming](https://developers.openai.com/api/docs/guides/red-teaming)
* **Regression tests**
  Define representative cases, a measurable success criterion, and a repeatable grading method that can detect regressions. [Study: Uploading test data](https://developers.openai.com/api/docs/guides/evals#uploading-test-data)
* **Dataset versioning**
  Define representative cases, a measurable success criterion, and a repeatable grading method that can detect regressions. [Study: Getting started with datasets](https://developers.openai.com/api/docs/guides/evaluation-getting-started)
* **Human evaluation**
  Define representative cases, a measurable success criterion, and a repeatable grading method that can detect regressions. [Study: Human evaluation design](https://huggingface.co/docs/evaluate/main/a_quick_tour)
* **Automated graders**
  Define representative cases, a measurable success criterion, and a repeatable grading method that can detect regressions. [Study: Add graders](https://developers.openai.com/api/docs/guides/evaluation-getting-started#add-graders)

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

* **Exact-match grading**
  Define representative cases, a measurable success criterion, and a repeatable grading method that can detect regressions. [Study: Exact-match and regular-expression techniques](https://docs.python.org/3/howto/regex.html)
* **Schema validation**
  Define a strict machine-readable contract, handle invalid or refused outputs, and validate parsed data before downstream use. [Study: JSON Schema validation](https://python-jsonschema.readthedocs.io/en/stable/validate)
* **Regex grading**
  Define representative cases, a measurable success criterion, and a repeatable grading method that can detect regressions. [Study: Python graders](https://developers.openai.com/api/docs/guides/graders#python-graders)
* **Semantic similarity**
  Understand the vector operation behind this pattern, choose an appropriate similarity or indexing method, and evaluate retrieval quality. [Study: Text similarity graders](https://developers.openai.com/api/docs/guides/graders#text-similarity-graders)
* **Model-based grading**
  Define representative cases, a measurable success criterion, and a repeatable grading method that can detect regressions. [Study: Model graders](https://developers.openai.com/api/docs/guides/graders#model-graders)
* **Pairwise comparison**
  Define representative cases, a measurable success criterion, and a repeatable grading method that can detect regressions. [Study: Practical guide to pairwise comparison](https://developers.openai.com/cookbook/examples/evaluation/how_to_eval_abstractive_summarization)
* **Human grading**
  Define representative cases, a measurable success criterion, and a repeatable grading method that can detect regressions. [Study: Human evals](https://developers.openai.com/api/docs/guides/evaluation-best-practices#human-evals)
* **Multi-grader aggregation**
  Define representative cases, a measurable success criterion, and a repeatable grading method that can detect regressions. [Study: Multi-grader aggregation and score calibration](https://scikit-learn.org/stable/modules/calibration.html)

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

* **Tool-selection accuracy**
  Define the capability and its input contract, validate every invocation, and enforce permissions or approval before execution. [Study: Trace spans for tools, handoffs, and agent trajectories](https://openai.github.io/openai-agents-python/ref/tracing)
* **Tool-argument accuracy**
  Define the capability and its input contract, validate every invocation, and enforce permissions or approval before execution. [Study: Evaluate tool calls](https://developers.openai.com/api/docs/guides/agent-evals#evaluate-tool-calls)
* **Agent trajectory**
  Capture the relevant execution events and sensitive-data controls so behavior can be debugged, evaluated, and audited later. [Study: Evaluate agent workflows](https://developers.openai.com/api/docs/guides/agent-evals)
* **Handoff correctness**
  Define ownership, control flow, context boundaries, and stopping behavior so the agent workflow remains bounded and inspectable. [Study: Evaluate handoffs](https://developers.openai.com/api/docs/guides/agent-evals#evaluate-handoffs)
* **Retrieval recall**
  Design this retrieval stage deliberately, preserve useful metadata, and measure its effect on evidence recall and answer quality. [Study: Practical guide to retrieval recall](https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/context_recall)
* **Citation correctness**
  Answer from available evidence, attach citations to supported claims, and return an insufficient-evidence result when grounding is weak. [Study: Validate citations](https://developers.openai.com/api/docs/guides/citation-formatting#validate-citations)
* **Image understanding**
  Prepare the visual input correctly, state the analysis task precisely, and verify extracted details against the source image or document. [Study: Evaluate multimodal outputs](https://developers.openai.com/api/docs/guides/agent-evals#evaluate-multimodal-outputs)
* **Voice-agent quality**
  Define representative cases, a measurable success criterion, and a repeatable grading method that can detect regressions. [Study: Evaluating a realtime agent](https://developers.openai.com/cookbook/examples/realtime_eval_guide#evaluating-a-realtime-agent)
* **Latency and cost**
  Measure the baseline, apply the relevant optimization, and compare cost, throughput, tail latency, and task success afterward. [Study: Track agent-evaluation latency and cost](https://developers.openai.com/api/docs/guides/agent-evals#track-latency-and-cost)
* **Failure recovery**
  Identify likely failure modes, choose safe retry or fallback behavior, and verify that recovery does not duplicate consequential work. [Study: Evaluate failure recovery](https://developers.openai.com/api/docs/guides/agent-evals#evaluate-failure-recovery)

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

* **Moderation**
  Identify the threat and trust boundary, apply least-privilege controls, and test that unsafe inputs or actions are blocked safely. [Study: Moderation](https://developers.openai.com/api/docs/guides/moderation)
* **Prompt injection**
  Identify the threat and trust boundary, apply least-privilege controls, and test that unsafe inputs or actions are blocked safely. [Study: Prompt injection](https://developers.openai.com/api/docs/guides/tools-connectors-mcp#prompt-injection)
* **Indirect prompt injection**
  Identify the threat and trust boundary, apply least-privilege controls, and test that unsafe inputs or actions are blocked safely. [Study: Prompt injections](https://developers.openai.com/api/docs/guides/agent-builder-safety#prompt-injections)
* **Jailbreaks**
  Identify the threat and trust boundary, apply least-privilege controls, and test that unsafe inputs or actions are blocked safely. [Study: Practical guide to jailbreaks](https://genai.owasp.org/llmrisk/llm01-prompt-injection)
* **PII protection**
  Identify the threat and trust boundary, apply least-privilege controls, and test that unsafe inputs or actions are blocked safely. [Study: PII identification and data minimization](https://www.nist.gov/privacy-framework)
* **Secret leakage**
  Configure credentials without exposing them in code or logs, and understand the rotation and storage practices required in production. [Study: Private data leakage](https://developers.openai.com/api/docs/guides/agent-builder-safety#private-data-leakage)
* **Tool allowlists**
  Identify the threat and trust boundary, apply least-privilege controls, and test that unsafe inputs or actions are blocked safely. [Study: Advanced: allowlisted HTTP callouts](https://developers.openai.com/api/docs/guides/secure-mcp-tunnels#advanced-allowlisted-http-callouts)
* **Output validation**
  Define a strict machine-readable contract, handle invalid or refused outputs, and validate parsed data before downstream use. [Study: Use structured outputs to constrain data flow](https://developers.openai.com/api/docs/guides/agent-builder-safety#use-structured-outputs-to-constrain-data-flow)
* **Data exfiltration**
  Identify the threat and trust boundary, apply least-privilege controls, and test that unsafe inputs or actions are blocked safely. [Study: Prompt injection and exfiltration](https://developers.openai.com/api/docs/guides/deep-research#prompt-injection-and-exfiltration)
* **Human approval**
  Define the capability and its input contract, validate every invocation, and enforce permissions or approval before execution. [Study: Keep tool approvals on](https://developers.openai.com/api/docs/guides/agent-builder-safety#keep-tool-approvals-on)
* **Audit logs**
  Capture the relevant execution events and sensitive-data controls so behavior can be debugged, evaluated, and audited later. [Study: Retrieve audit logs](https://developers.openai.com/api/docs/guides/admin-apis#retrieve-audit-logs)
* **Least privilege**
  Identify the threat and trust boundary, apply least-privilege controls, and test that unsafe inputs or actions are blocked safely. [Study: Manage permissions in the OpenAI platform](https://developers.openai.com/api/docs/guides/rbac)

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

* **Prompt caching**
  Structure instructions and context so the model can identify the objective, constraints, examples, and completion criteria unambiguously. [Study: Prompt caching](https://developers.openai.com/api/docs/guides/upgrading-to-gpt-5p6-sol#prompt-caching)
* **Streaming**
  Learn how to consume incremental events, assemble partial output, and handle completion, cancellation, and stream failures. [Study: Streaming guide](https://developers.openai.com/api/docs/guides/structured-outputs#streaming)
* **Batch processing**
  Measure the baseline, apply the relevant optimization, and compare cost, throughput, tail latency, and task success afterward. [Study: Process tokens faster](https://developers.openai.com/api/docs/guides/latency-optimization#process-tokens-faster)
* **Parallel requests**
  Define ownership, control flow, context boundaries, and stopping behavior so the agent workflow remains bounded and inspectable. [Study: Parallel requests and concurrency control](https://developers.openai.com/cookbook/examples/how_to_handle_rate_limits)
* **Rate limits**
  Measure the baseline, apply the relevant optimization, and compare cost, throughput, tail latency, and task success afterward. [Study: Rate limits](https://developers.openai.com/api/docs/guides/rate-limits)
* **Exponential backoff**
  Measure the baseline, apply the relevant optimization, and compare cost, throughput, tail latency, and task success afterward. [Study: Retrying with exponential backoff](https://developers.openai.com/api/docs/guides/rate-limits#retrying-with-exponential-backoff)
* **Concurrency**
  Measure the baseline, apply the relevant optimization, and compare cost, throughput, tail latency, and task success afterward. [Study: Cost and latency](https://developers.openai.com/api/docs/guides/cost-optimization#cost-and-latency)
* **Model routing**
  Compare the available options by capability, quality, latency, cost, and operational constraints before defining a selection policy. [Study: Don't default to an LLM](https://developers.openai.com/api/docs/guides/latency-optimization#dont-default-to-an-llm)
* **Context pruning**
  Understand how context and token limits affect quality, latency, and cost, then apply an appropriate budgeting or compaction strategy. [Study: When to compact](https://developers.openai.com/api/docs/guides/compaction#when-to-compact)
* **Token budgets**
  Understand how context and token limits affect quality, latency, and cost, then apply an appropriate budgeting or compaction strategy. [Study: Spend limits](https://developers.openai.com/api/docs/guides/spend-limits)
* **Load testing**
  Measure the baseline, apply the relevant optimization, and compare cost, throughput, tail latency, and task success afterward. [Study: Load testing methodology](https://grafana.com/docs/k6/latest/testing-guides/load-testing-websites)
* **Cost attribution**
  Measure the baseline, apply the relevant optimization, and compare cost, throughput, tail latency, and task success afterward. [Study: Cost optimization](https://developers.openai.com/api/docs/guides/cost-optimization)

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

* **When to fine-tune**
  Establish a baseline, prepare representative training and validation data, and confirm that customization improves held-out results. [Study: Fine-tune a model](https://developers.openai.com/api/docs/guides/model-optimization#fine-tune-a-model)
* **Dataset creation**
  Establish a baseline, prepare representative training and validation data, and confirm that customization improves held-out results. [Study: Build your dataset](https://developers.openai.com/api/docs/guides/supervised-fine-tuning#build-your-dataset)
* **Training and validation splits**
  Establish a baseline, prepare representative training and validation data, and confirm that customization improves held-out results. [Study: Fine-tuning best practices](https://developers.openai.com/api/docs/guides/fine-tuning-best-practices)
* **Supervised fine-tuning**
  Establish a baseline, prepare representative training and validation data, and confirm that customization improves held-out results. [Study: Supervised fine-tuning](https://developers.openai.com/api/docs/guides/supervised-fine-tuning)
* **Vision fine-tuning**
  Prepare the visual input correctly, state the analysis task precisely, and verify extracted details against the source image or document. [Study: Control image quality](https://developers.openai.com/api/docs/guides/vision-fine-tuning#control-image-quality)
* **Preference optimization**
  Establish a baseline, prepare representative training and validation data, and confirm that customization improves held-out results. [Study: Direct preference optimization](https://developers.openai.com/api/docs/guides/direct-preference-optimization)
* **Reinforcement fine-tuning**
  Establish a baseline, prepare representative training and validation data, and confirm that customization improves held-out results. [Study: Reinforcement fine-tuning](https://developers.openai.com/api/docs/guides/reinforcement-fine-tuning)
* **Distillation**
  Establish a baseline, prepare representative training and validation data, and confirm that customization improves held-out results. [Study: Fine Tuning](https://developers.openai.com/api/reference/resources/fine_tuning)
* **Overfitting**
  Establish a baseline, prepare representative training and validation data, and confirm that customization improves held-out results. [Study: Fine-tuning methods](https://developers.openai.com/api/docs/guides/model-optimization#fine-tuning-methods)
* **Post-training evaluation**
  Define representative cases, a measurable success criterion, and a repeatable grading method that can detect regressions. [Study: Compare to evals](https://developers.openai.com/api/docs/guides/supervised-fine-tuning#compare-to-evals)

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

* **Repository instructions**
  Structure instructions and context so the model can identify the objective, constraints, examples, and completion criteria unambiguously. [Study: Repository instructions with AGENTS.md](https://developers.openai.com/codex/guides/agents-md)
* **Coding-agent prompts**
  Structure instructions and context so the model can identify the objective, constraints, examples, and completion criteria unambiguously. [Study: Keep tool boundaries explicit in coding and terminal agents](https://developers.openai.com/api/docs/guides/latest-model/gpt-5.4#keep-tool-boundaries-explicit-in-coding-and-terminal-agents)
* **Planning**
  Define the objective and reasoning budget clearly, then verify that the chosen approach improves results without unnecessary work. [Study: Maximizing coding performance, from planning to execution](https://developers.openai.com/api/docs/guides/latest-model/gpt-5#maximizing-coding-performance-from-planning-to-execution)
* **Goal definition**
  Define the objective and reasoning budget clearly, then verify that the chosen approach improves results without unnecessary work. [Study: Write a clear task](https://developers.openai.com/codex/prompting#write-a-clear-task)
* **Test-driven changes**
  Use repository context and tests to produce focused, reviewable changes, then verify behavior before accepting the implementation. [Study: Practical guide to test-driven changes](https://docs.pytest.org/en/stable/how-to/assert.html)
* **Iterative repair**
  Use repository context and tests to produce focused, reviewable changes, then verify behavior before accepting the implementation. [Study: Iterate on the result](https://developers.openai.com/codex/prompting#iterate-on-the-result)
* **Code review**
  Use repository context and tests to produce focused, reviewable changes, then verify behavior before accepting the implementation. [Study: Code review](https://developers.openai.com/codex/code-review)
* **Legacy migration**
  Use repository context and tests to produce focused, reviewable changes, then verify behavior before accepting the implementation. [Study: Practical guide to legacy migration](https://martinfowler.com/articles/patterns-legacy-displacement)
* **CI integration**
  Use repository context and tests to produce focused, reviewable changes, then verify behavior before accepting the implementation. [Study: Non-interactive execution in CI](https://developers.openai.com/codex/noninteractive)
* **Sandboxed execution**
  Define the execution boundary, verify each observed action or result, and require approval for external or destructive operations. [Study: Sandbox](https://developers.openai.com/codex/sandboxing)

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

* **Apps SDK architecture**
  Understand how the app’s MCP tools, component UI, bridge APIs, and ChatGPT runtime responsibilities fit together. [Study: Apps SDK architecture and project setup](https://developers.openai.com/apps-sdk)
* **MCP server integration**
  Define the capability and its input contract, validate every invocation, and enforce permissions or approval before execution. [Study: Building the MCP server and defining tools](https://developers.openai.com/apps-sdk/build/mcp-server)
* **Tool definitions**
  Define the capability and its input contract, validate every invocation, and enforce permissions or approval before execution. [Study: Define tools](https://developers.openai.com/apps-sdk/build/mcp-server#define-tools)
* **UI components**
  Understand how the app’s MCP tools, component UI, bridge APIs, and ChatGPT runtime responsibilities fit together. [Study: Building an interactive ChatGPT UI](https://developers.openai.com/apps-sdk/build/chatgpt-ui)
* **Authentication**
  Choose the appropriate authentication flow, scope access narrowly, and handle authorization failures without exposing credentials. [Study: Practical guide to authentication](https://developers.openai.com/apps-sdk/build/auth)
* **ChatGPT components**
  Understand how the app’s MCP tools, component UI, bridge APIs, and ChatGPT runtime responsibilities fit together. [Study: Use components](https://developers.openai.com/apps-sdk/build/chatgpt-ui#use-components)
* **Application state**
  Choose where state lives, what must persist between turns, and how to prevent stale, duplicated, or sensitive context. [Study: Practical guide to application state](https://developers.openai.com/apps-sdk/build/state-management)
* **Deployment**
  Prepare the runtime configuration, security controls, monitoring, and rollback path needed to move from development to production. [Study: Practical guide to deployment](https://developers.openai.com/apps-sdk/deploy)
* **Security and review**
  Identify the threat and trust boundary, apply least-privilege controls, and test that unsafe inputs or actions are blocked safely. [Study: Security reminders](https://developers.openai.com/apps-sdk/deploy#security-reminders)

**Practice**

Build a ChatGPT app that searches your architecture standards and displays structured recommendations in an interactive UI.

---

### Chapter 29: gpt-oss and local AI

**Topics**

* **Open-weight models**
  Understand the model and runtime requirements, choose compatible serving settings, and benchmark quality, safety, memory use, and latency. [Study: gpt-oss-120b model capabilities](https://developers.openai.com/api/docs/models/gpt-oss-120b)
* **Local inference**
  Understand the model and runtime requirements, choose compatible serving settings, and benchmark quality, safety, memory use, and latency. [Study: Local inference with Transformers](https://huggingface.co/docs/transformers/main/model_doc/gpt_oss)
* **Hardware requirements**
  Understand the model and runtime requirements, choose compatible serving settings, and benchmark quality, safety, memory use, and latency. [Study: Hardware requirements](https://huggingface.co/openai/gpt-oss-120b#hardware-requirements)
* **Quantization**
  Understand the model and runtime requirements, choose compatible serving settings, and benchmark quality, safety, memory use, and latency. [Study: Quantization concepts and trade-offs](https://huggingface.co/docs/transformers/quantization/overview)
* **Model serving**
  Understand the model and runtime requirements, choose compatible serving settings, and benchmark quality, safety, memory use, and latency. [Study: Serving models with vLLM](https://docs.vllm.ai/en/latest/serving/openai_compatible_server)
* **Prompt formats**
  Understand the model and runtime requirements, choose compatible serving settings, and benchmark quality, safety, memory use, and latency. [Study: Usage tips](https://huggingface.co/docs/transformers/main/model_doc/gpt_oss#usage-tips)
* **Tool use**
  Define the capability and its input contract, validate every invocation, and enforce permissions or approval before execution. [Study: Make tool use persistent when correctness depends on it](https://developers.openai.com/api/docs/guides/latest-model/gpt-5.4#make-tool-use-persistent-when-correctness-depends-on-it)
* **Fine-tuning**
  Establish a baseline, prepare representative training and validation data, and confirm that customization improves held-out results. [Study: Practical guide to fine-tuning](https://developers.openai.com/cookbook/articles/gpt-oss/fine-tune-transfomers)
* **Safety models**
  Understand the model and runtime requirements, choose compatible serving settings, and benchmark quality, safety, memory use, and latency. [Study: Practical guide to safety models](https://huggingface.co/openai/gpt-oss-safeguard-120b)
* **Hosted/local model routing**
  Compare the available options by capability, quality, latency, cost, and operational constraints before defining a selection policy. [Study: Choose models per agent](https://developers.openai.com/api/docs/guides/agents/models#choose-models-per-agent)

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
