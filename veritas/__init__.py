"""
Veritas Agent Runtime Framework — Public API

Example:
    from veritas import RuntimeClient, RuntimeEngine

    client = RuntimeClient()
    result = client.run(TaskRequest(objective="analyze", agent="evaluator"))
"""

# Runtime Engine (core)
from veritas.runtime import RuntimeEngine, RuntimeContext, AgentState
from veritas.runtime import StateTransition, TransitionTable
from veritas.runtime import RuntimeCheckpoint
from veritas.runtime import RuntimeHook, CompositeHook
from veritas.runtime import RuntimeEvent, RuntimeEventBus
from veritas.runtime import RuntimeObserver, RuntimeMetrics
from veritas.runtime import RuntimeSnapshot, RuntimeBus
from veritas.runtime import RuntimeStore, SessionRecord

# Intelligence Layer
from veritas.runtime import (
    RuntimeAnalyzer, HealthReport,
    FailureDetector, FailureEvent,
    RuntimePolicyEngine,
    RuntimeDecision, DecisionLog,
)

# Recovery
from veritas.runtime.recovery import (
    RecoveryStrategy, RecoveryConfig,
    CheckpointManager, RecoveryManager,
    ProviderFallback,
)

# Lifecycle
from veritas.runtime.lifecycle import (
    AgentLifecycle, LifecycleManager,
    RuntimeSession,
)

# Explainability
from veritas.runtime.explain import (
    DecisionTrace, DecisionReason,
    ExplanationRecorder,
)

# Plugins
from veritas.runtime.plugins import (
    RuntimePlugin, PluginRegistry,
    PluginLoader, PluginHookBridge,
    PluginManager, PluginMetadata,
)

# Distributed
from veritas.runtime.distributed import (
    RuntimeNode, NodeRegistry,
    DistributedEventBus, RemoteExecutionManager,
    DistributedTraceCollector,
)

# SDK (Public Contract Layer)
from veritas.sdk import (
    RuntimeClient,
    TaskRequest, TaskResult, SessionInfo, TaskStatus,
    RuntimeConfig, ConfigLoader,
    VeritasError, ConfigError, RuntimeClientError, TaskExecutionError,
)

# Security
from veritas.security import (
    PermissionMatrix, ToolGateway,
    PromptGuard, AuditLogger,
)

# Memory
from veritas.memory import (
    MemoryManager, StudentMemory,
    ExperienceMemoryStore, ExperienceRecord,
)
from veritas.memory.experience_extractor import ExperienceExtractor

# LLM
from veritas.llm import (
    LLMProvider, LLMResponse,
    MockLLMProvider, create_provider, FallbackChain,
)

# Benchmark
from veritas.benchmark import (
    BenchmarkRunner, FailureInjector,
    BenchmarkMetrics, BenchmarkReporter,
)

__all__ = [
    # Runtime
    "RuntimeEngine", "RuntimeContext", "AgentState",
    "RuntimeHook", "RuntimeEventBus", "RuntimeMetrics",
    # SDK
    "RuntimeClient", "TaskRequest", "TaskResult",
    # Recovery
    "RecoveryManager", "RecoveryStrategy",
    # etc. (see above for full list)
]

__version__ = "7.0.0"
