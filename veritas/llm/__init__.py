"""
Phase 4.7 — LLM Provider Abstraction Layer

Unified LLM interface. All LLM calls flow through LLMProvider.
Supports: OpenAI, DeepSeek, Spark, Mock, Rule + FallbackChain.

Usage:
    from veritas.llm import create_provider
    provider = create_provider("deepseek", fallback_chain=True)
    response = provider.generate("Hello")
"""

from veritas.llm.provider import LLMProvider, LLMResponse
from veritas.llm.mock_provider import MockLLMProvider
from veritas.llm.xunfei_provider import XunfeiSparkProvider
from veritas.llm.openai_provider import OpenAIProvider
from veritas.llm.deepseek_provider import DeepSeekProvider
from veritas.llm.rule_provider import RuleProvider
from veritas.llm.factory import create_provider, FallbackChain, get_provider_info

__all__ = [
    "LLMProvider",
    "LLMResponse",
    "MockLLMProvider",
    "XunfeiSparkProvider",
    "OpenAIProvider",
    "DeepSeekProvider",
    "RuleProvider",
    "FallbackChain",
    "create_provider",
    "get_provider_info",
]
