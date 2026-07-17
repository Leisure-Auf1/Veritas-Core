#!/usr/bin/env python3
"""
Veritas-Core Runtime Demo — Engine internals, hooks, events, metrics.

Shows: RuntimeEngine, hooks, observer, event bus, metrics collection.

Run: python examples/runtime_demo.py
"""
from __future__ import annotations


def main():
    print("=" * 60)
    print("  Veritas-Core Runtime Demo")
    print("=" * 60)
    print()

    from veritas.runtime import (
        RuntimeEngine, RuntimeObserver, RuntimeMetrics, RuntimeEventBus,
    )

    bus = RuntimeEventBus()
    metrics = RuntimeMetrics()
    metrics.attach(bus)
    observer = RuntimeObserver(bus=bus)

    engine = RuntimeEngine(session_id="runtime_demo")
    engine.add_hook(observer)

    print("1️⃣  Setup: RuntimeEngine + Observer + Metrics")
    print(f"   Session: {engine.session_id}")
    print()

    engine.run()

    print("2️⃣  Engine executed")
    print(f"   State: {engine._checkpoint.current_state}")
    print()

    summary = metrics.summary()
    print("3️⃣  Metrics Summary:")
    for key, value in summary.items():
        print(f"   {key}: {value}")
    print()

    timeline = engine.timeline()
    print(f"4️⃣  Timeline: {len(timeline)} transitions")
    for t in timeline[:5]:
        print(f"   {t.from_state.value} → {t.to_state.value} [{t.status}]")
    print()

    print("=" * 60)
    print("  ✅ Runtime Demo Complete")
    print("=" * 60)


if __name__ == "__main__":
    main()
