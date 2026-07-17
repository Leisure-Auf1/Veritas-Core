# Veritas-Core — Agent Runtime Framework

> **Production-grade Agent Infrastructure** | 77 modules | 558 tests | Python 3.10+

*Pluggable, observable, recoverable — the runtime that powers AI agent systems.*

---

## What is Veritas-Core?

Veritas-Core is a **standalone Agent Runtime Framework** extracted from the A3 Multi-Agent research system. It provides the infrastructure layer that any AI agent application needs: state machine execution, plugin system, recovery, lifecycle management, distributed coordination, and more.

```
pip install veritas-core
```

```python
from veritas import RuntimeClient, TaskRequest

client = RuntimeClient()
result = client.run(TaskRequest(objective="analyze", agent="evaluator"))
print(result.status, result.execution_time_ms)
```

---

## Evolution

```
A3-Multi-Agent-System (Research)
    │
    │  12 agents, 1042 tests, monolithic
    │  Phase 1–6: runtime, sdk, recovery, plugins
    │
    ▼ Phase 7.0: Extraction via git filter-branch
    │
Veritas-Core (Framework)        A3 (Application)
    │                               │
    │  Runtime Engine                │  Learning agents
    │  Public SDK                    │  Streamlit UI
    │  Plugin system                 │  FastAPI
    │  Recovery & Lifecycle          │  Multimodal gateway
    │  Distributed runtime           │  Product API v2
    │  Security & Memory             │
    │                               │
    ▼                               ▼
  pip install veritas-core        depends on veritas-core
```

---

## Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    Veritas-Core 7.0.0                        │
│                                                             │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────┐ │
│  │   Runtime   │  │     SDK     │  │      Plugins        │ │
│  │   Engine    │  │  (Public    │  │  (Extensible         │ │
│  │             │  │   API)      │  │   hook system)      │ │
│  │ • State     │  │             │  │                     │ │
│  │   Machine   │  │ • Client    │  │ • Base Plugin       │ │
│  │ • Hooks     │  │ • Contracts │  │ • Registry          │ │
│  │ • Events    │  │ • Config    │  │ • Loader            │ │
│  │ • Observer  │  │ • Adapter   │  │ • Manager           │ │
│  │ • Metrics   │  │ • Errors    │  │                     │ │
│  └──────┬──────┘  └──────┬──────┘  └──────────┬──────────┘ │
│         │                │                     │            │
│  ┌──────┴──────┐  ┌──────┴──────┐  ┌──────────┴──────────┐ │
│  │  Recovery   │  │  Lifecycle  │  │    Distributed      │ │
│  │             │  │             │  │                     │ │
│  │ • Retry     │  │ • Agent OS  │  │ • Node Registry     │ │
│  │ • Rollback  │  │ • Session   │  │ • Event Bus         │ │
│  │ • Fallback  │  │ • Timeline  │  │ • Remote Exec       │ │
│  │ • Repair    │  │ • States    │  │ • Trace Collector   │ │
│  └─────────────┘  └─────────────┘  └─────────────────────┘ │
│                                                             │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────┐ │
│  │  Security   │  │   Memory    │  │     Benchmark       │ │
│  │             │  │             │  │                     │ │
│  │ • Permission│  │ • Student   │  │ • Failure Injector  │ │
│  │ • Gateway   │  │ • Experience│  │ • Scenarios         │ │
│  │ • Guard     │  │ • Manager   │  │ • Metrics           │ │
│  │ • Audit     │  │ • Extractor │  │ • Reporter          │ │
│  └─────────────┘  └─────────────┘  └─────────────────────┘ │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │                    LLM Layer                         │   │
│  │  • LLMProvider ABC  • DeepSeek/OpenAI/Mock/Rule     │   │
│  │  • FallbackChain    • create_provider()             │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │                     CLI (veritas)                     │   │
│  │  veritas run | status | trace | plugins | demo       │   │
│  └─────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
```

---

## Key Capabilities

### Runtime Engine
State machine-driven agent execution with hooks, events, observers, and metrics. Handlers fire on state transitions; policies enable autonomous decisions.

```python
from veritas import RuntimeEngine, RuntimeHook

engine = RuntimeEngine(session_id="demo")
engine.add_hook(MyHook())
engine.run()
```

### Recovery System
Automatic failure recovery with 5 strategies: retry, checkpoint rollback, fallback agent, memory repair, terminate. Configurable per agent.

```python
from veritas import RuntimeEngine, RecoveryManager

engine = RuntimeEngine(session_id="demo", recovery_manager=RecoveryManager())
```

### Plugin System
Extensible plugin architecture. Plugins are hooks — they receive state transitions, errors, and lifecycle events. Error-isolated: one failing plugin doesn't break others.

```python
from veritas import PluginManager, RuntimePlugin

class SecurityPlugin(RuntimePlugin):
    name = "security"
    def on_start(self): ...

mgr = PluginManager()
mgr.install(SecurityPlugin())
```

### Distributed Runtime
Multi-node agent execution with node registry, distributed event bus, remote task execution, and cross-node trace collection.

### SDK (Public Contract Layer)
Clean public API via `RuntimeClient`. Applications never touch RuntimeEngine internals — they use contracts (TaskRequest, TaskResult, SessionInfo).

### Security Layer
Permission matrix, tool gateway, prompt injection guard, and audit logging. All security checks are hooks — pluggable with zero engine changes.

### Memory Layer
Student memory with EMA mastery tracking, experience memory for agent learning, and experience extraction from meta-reflections.

---

## Installation

```bash
# From GitHub (recommended)
pip install git+https://github.com/Leisure-Auf1/Veritas-Core.git@main

# From local
git clone https://github.com/Leisure-Auf1/Veritas-Core.git
cd Veritas-Core
pip install -e .
```

### Requirements
- Python 3.10+
- pyyaml >= 6.0

---

## Quick Start

```python
from veritas import RuntimeEngine, RuntimeObserver, RuntimeMetrics, RuntimeEventBus

# Setup
bus = RuntimeEventBus()
metrics = RuntimeMetrics()
metrics.attach(bus)
observer = RuntimeObserver(bus=bus)

engine = RuntimeEngine(session_id="quickstart")
engine.add_hook(observer)
engine.run()

# Results
print(metrics.summary())
print(observer.events_by_type("evaluation"))
```

More examples in [examples/](examples/).

---

## Testing

```bash
make test       # 558 tests
make test-cov   # With coverage
```

---

## Repository Relationship

| Repository | Role | Tests |
|:-----------|:-----|:-----:|
| **Veritas-Core** | Agent Runtime Framework | 558 |
| [A3-Multi-Agent-System](https://github.com/Leisure-Auf1/A3-Multi-Agent-System) | AI Learning Application (depends on VC) | 1130 |
| [Terence-Agent](https://github.com/Leisure-Auf1/Terence-Agent) | Engineering Governance | — |

---

## License

MIT
